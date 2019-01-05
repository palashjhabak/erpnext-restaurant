import frappe
import datetime
import json
import requests
from frappe.data_migration.doctype.data_migration_connector.connectors.base import BaseConnection
from bs4 import BeautifulSoup

class ZomatoConnector(BaseConnection):
	def __init__(self, connector):
		self.connector = connector
		settings = frappe.get_doc('Zomato Sync Settings', None)
		todays_date = datetime.datetime.now()
		end_sync_date = todays_date - datetime.timedelta(days=1)
		end_sync_date = end_sync_date.replace(hour=23, minute=59, second=59)

		last_sync_date_string = settings.last_sync_date

		last_sync_date = datetime.datetime.strptime(last_sync_date_string, '%Y-%m-%d %H:%M:%S')
		last_sync_date = last_sync_date.replace(hour=0, minute=0, second=0)

		self.start_date = last_sync_date.strftime('%Y-%m-%d %H:%M:%S')
		self.end_date = end_sync_date.strftime('%Y-%m-%d %H:%M:%S')

		print self.start_date
		print self.end_date
		url_login = 'https://www.zomato.com/php/asyncLogin.php'
		self.name_field = 'id'
		headers_login = {
			'origin': 'https://www.zomato.com',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'en-US,en;q=0.9',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
			'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'accept': 'application/json, text/javascript, */*; q=0.01',
			'referer': 'https://www.zomato.com/',
			'authority': 'www.zomato.com',
			'x-requested-with': 'XMLHttpRequest',
		}

		data_login = {
			'remeberFlag': 'checked',
			'login': settings.email,
			'password':settings.password
		}

		self.session = requests.Session()
		login_response = self.session.post(url_login,  headers=headers_login, data=data_login)
		print(login_response.text)

	def get(self, remote_objectname, fields=None, filters=None, start=0, page_length=10):
		res_id = filters.get('res_id')
		orders =  self.get_zomato_order(self.start_date, self.end_date, start, page_length, res_id)
		return orders

	def get_zomato_order(self, start_date, end_date, start, page_length, res_id):
		return self.get_orders_for_a_date(res_id, start_date, end_date, start, page_length)

	def insert(self, doctype, doc):
		pass

	def update(self, doctype, doc, migration_id):
		pass

	def delete(self, doctype, migration_id):
		pass

	def get_order_details(self, res_id, order_id):
		header_delivery_order = {
			'Accept': 'application/json, text/javascript, */*; q=0.01',
			'Accept-Encoding': 'gzip, deflate, br',
			'Accept-Language': 'en-US,en;q=0.9',
			'Connection': 'keep-alive',
			'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'Origin': 'https://www.zomato.com',
			'Referer': 'https://www.zomato.com/',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
			'X-Requested-With': 'XMLHttpRequest'
		}

		action = 'orderdetail'
		url_delivery_order = 'https://www.zomato.com/php/delivery_orders_dashboard_handler.php'

		data_delivery = {
			'action': action,
			'tab_id': order_id,
			'res_id': res_id
		}

		response_delivery = self.session.post(url_delivery_order, data=data_delivery, headers=header_delivery_order)

		if response_delivery.status_code != 200:
			return False
		else:
			try:
				response_object = response_delivery.json()
				return response_object["tab"]
			except:
				return False

	def get_orders_for_a_date(self, res_id, start_date, end_date, start, page_length):
		order_ids = []
		orders = []

		order_ids = self.get_delivery_data(res_id, start_date, end_date, start, page_length)

		for i in range(0, len(order_ids)):
			orders.append(self.get_order_details(res_id, order_ids[i]))

		return orders

	def get_delivery_data(self, res_id, start_date, end_date, offset, limit):

		header_delivery_order = {
			'Accept': 'application/json, text/javascript, */*; q=0.01',
			'Accept-Encoding': 'gzip, deflate, br',
			'Accept-Language': 'en-US,en;q=0.9',
			'Connection': 'keep-alive',
			'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'Origin': 'https://www.zomato.com',
			'Referer': 'https://www.zomato.com/',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
			'X-Requested-With': 'XMLHttpRequest'
		}

		action = 'searchOrders'
		url_delivery_order = 'https://www.zomato.com/php/delivery_orders_dashboard_handler.php'

		data_delivery = {
			'start_date': start_date,
			'end_date': end_date,
			'offset': offset,
			'limit': limit,
			'action': action,
			'res_id': res_id
		}

		response_delivery = self.session.post(url_delivery_order, data=data_delivery, headers=header_delivery_order)

		if response_delivery.status_code != 200:
			return False
		else:
			response_text = response_delivery.text
			try:
				response_object = json.loads(response_text)
				response_html = response_object['data']['html']
				if response_html == '':
					return False

				soup = BeautifulSoup(response_html)

				list_of_order_ids = []

				for link in soup.find_all('a'):
					order_id = link.get('data-tab-id')
					list_of_order_ids.append(order_id)

				return list_of_order_ids
			except Exception as e:
				print(e)
				return False

