Hi {{frappe.db.get_value("Contact", doc.customer, "first_name")}} {{frappe.db.get_value("Contact", doc.customer, "last_name")}}, <br><br>

Thanks for your interest in Cafe 1730. <br><br>

Your booking "{{doc.custom_title}}" is confirmed and details of the same are attached in this Email. Should you have any other query, please feel free to contact the manager at +91-8087071730.<br><br>

Thanks,<br>
Team Cafe-1730<br>
http://cafe1730.com
