# -*- coding: utf-8 -*-
# Copyright (c) 2018, Techlift and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _, throw

class Booking(Document):
	pass

def set_booking_event_day():
	frappe.db.sql("""update tabBooking set event_day = 'Today' where date = CURDATE()""")
