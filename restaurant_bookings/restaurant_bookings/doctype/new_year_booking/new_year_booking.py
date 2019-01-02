# -*- coding: utf-8 -*-
# Copyright (c) 2018, Techlift and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class NewYearBooking(Document):
	pass

	def after_insert(self):
		from frappe.core.doctype.sms_settings.sms_settings import send_sms

		if self.book_done_by == 'Backend':
			booking = self
			recepient = [booking.email]
			subject = "Cafe 1730, New Year Booking Confirmation"
			message = "Thanks for Booking"
			message_sms = ""
			booking_for = booking.booking_for
			name = booking.name1
			phone = booking.mobile
			people = booking.people
			kids = booking.kids
			couple = booking.couple
			male_stag = booking.male_stag
			female_stag = booking.female_stag
			booking_code = booking.name
			total = booking.total_amount
			total_advance = booking.total_advance

			subject = 'Cafe 1730, {0} Confirmation'.format(booking_for)
			if booking_for == "New Year 2019 Party on 31st December":
				message = """<p>Hi {0},</p><p>Thanks for Booking {1} at Cafe 1730, Kharadi. Details of your booking is as follows.</p> Name: {2}<br>Phone: {3}<br>Number of Couple: {4}<br>Number of Female Stag: {5}<br>Number of Male Stag: {6}<br>Number of Kids: {7}<br>Total Amount: {8}<br>Advance Received: {9}<p>Your booking code is {10}, please show this to the staff when you reach at the Cafe.</p><p>Thanks,<br>Team Cafe 1730<br>7410000195.</p>""".format(name, booking_for, name, phone, couple, female_stag, male_stag, kids, total, total_advance, booking_code)
				message_sms = """Hi {0}\n\nThanks for Booking {1} at Cafe 1730, Kharadi.\n\nDetails of your booking is as follows.\n\nName: {2}\nPhone: {3}\nNumber of Couple: {4}\nNumber of Female Stag: {5}\nNumber of Male Stag: {6}\nNumber of Kids: {7}\nTotal Amount: {8}\nAdvance Received: {9}\n\nYour booking code is {10}\n\nPlease show this to the staff when you reach at the Cafe.\n\nThanks,\nTeam Cafe 1730,\n+91-7410000195.""".format(name, booking_for, name, phone, couple, female_stag, male_stag, kids, total, total_advance, booking_code)

			else:
				message = """<p>Hi {0},</p><p>Thanks for Booking {1} at Cafe 1730, Kharadi. Details of your booking is as follows.</p> Name: {2}<br>Phone: {3}<br>Number of People: {4}<br>Total Amount: {5}<br>Advance Received: {6}<p>Your booking code is {7}, please show this to the staff when you reach at the Cafe.</p><p>Thanks,<br>Team Cafe 1730<br>7410000195.</p>""".format(name, booking_for, name, phone, people, total, total_advance,  booking_code)
				message_sms = """Hi {0},\n\nThanks for Booking {1} at Cafe 1730, Kharadi.\n\nDetails of your booking is as follows.\n\nName: {2}\nPhone: {3}\nNumber of People: {4}\nTotal Amount: {5}\nAdvance Received: {6}\n\nYour booking code is {7}\n\nPlease show this to the staff when you reach at the Cafe.\n\nThanks,\nTeam Cafe 1730,\n+91-7410000195.""".format(name, booking_for, name, phone, people, total, total_advance,  booking_code)

			frappe.sendmail(recipients=recepient, subject=subject, message=message) 
			try:
				send_sms([phone], message_sms, 'ALERTS')
			except:
				pass

