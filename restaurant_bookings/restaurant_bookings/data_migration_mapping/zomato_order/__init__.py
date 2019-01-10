from math import sin, cos, sqrt, atan2, radians
import frappe
import datetime

def lat_long_distance(lat1, lat2, long1, long2):
	R = 6373.0

	lat1 = radians(lat1)
	lon1 = radians(long1)
	lat2 = radians(lat2)
	lon2 = radians(long2)

	dlon = lon2 - lon1
	dlat = lat2 - lat1

	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))

	distance = R * c

	return distance

def pre_process(zomato_order):
	res_lat = float(zomato_order['restaurant']['location']['latitude'])
	res_long = float(zomato_order['restaurant']['location']['longitude'])
	order_lat = float(zomato_order['deliveryAddressObj']['latitude'])
	order_long = float(zomato_order['deliveryAddressObj']['longitude'])

	distance_in_km = lat_long_distance(res_lat, order_lat, res_long, order_long)

	subzone_name = ''
	try:
		subzone_name = zomato_order['deliveryAddressObj']['subzone_name']
	except:
		subzone_name = ''

	date_timestamp = int(zomato_order['createdAt'])
	order_date = datetime.datetime.fromtimestamp(date_timestamp).strftime('%Y-%m-%d')
	order_time = datetime.datetime.fromtimestamp(date_timestamp).strftime('%H:%M:%S')
	return_object =  {
		'res_id': zomato_order['restaurant']['id'],
		'id': zomato_order['id'],
		'full_name': zomato_order['creator']['name'],
		'phone': zomato_order['userPhone'],
		'totalCost': zomato_order['order']['totalCost'],
		'payment_method': zomato_order['paymentMethod'],
		'is_phone_verified': zomato_order['isPhoneVerified'],
		'latitude': zomato_order['deliveryAddressObj']['latitude'],
		'longitude': zomato_order['deliveryAddressObj']['longitude'],
		'address': zomato_order['deliveryAddressObj']['address'],
		'subzone_name': subzone_name,
		'email': zomato_order['creator']['email'],
		'deliveryboy_name': zomato_order['deliveryBoyName'],
		'deliveryboy_phone': zomato_order['deliveryBoyPhone'],
		'instagram': zomato_order['creator']['instagramId'],
		'twitter': zomato_order['creator']['twitterId'],
		'followers': zomato_order['creator']['noOfFollowers'],
		'profile_image': zomato_order['creator']['profileImage']['large'],
		'customer_number_of_orders': zomato_order['creator']['successfulOnlineOrderCount'],
		'date': order_date,
		'time': order_time,
		'delivery_time': zomato_order['deliveryTime'],
		'distance_in_km': distance_in_km,
		'platform_user_id': zomato_order['creator']['id']
	}

	return return_object

def post_process(zomato_order):
	return
