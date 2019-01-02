# -*- coding: utf-8 -*-
# Copyright (c) 2018, Techlift and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _, throw

class Booking(Document):
	def validate(self):
		self.set_booking_title()

	def set_booking_title(self):
		self.custom_title = " ".join(filter(None, [self.booking_type, str(self.min_people), 'People']))

	def after_insert(self):
		from frappe.core.doctype.sms_settings.sms_settings import send_sms
		try:
			name = self.customer
			min_people = self.min_people
			date = self.date
			booking_type = self.booking_type
			message = 'Hi, {0}. Your booking for {1} at Cafe 1730, Kharadi on {2} is confirmed for minimum {3} people'.format(name, booking_type, date, min_people)
			contact = frappe.get_doc('Contact', name)
			send_sms([contact.phone, contact.mobile_no], message, 'ALERTS')
		except:
			pass

def set_booking_event_day():
	frappe.db.sql("""update tabBooking set event_day = 'Today' where date = CURDATE()""")
