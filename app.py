from View.Login import LoginView
LoginView()

#INVOICE DETAIL
# SELECT b.invoice_number, b.phone_number, b.date_time, bd.particular, bd.qty, bd.rate, c.name, c.address
# FROM bills as b
# INNER JOIN customer as c on b.phone_number = c.phone_number
# INNER JOIN bill_details AS bd on b.invoice_number = bd.invoice_number where invoice_number = 2

#INVOICE LIST
# SELECT b.invoice_number, b.phone_number, c.name FROM bills as b INNER JOIN customer as c on b.phone_number = c.phone_number


#SEARCH
# SELECT b.invoice_number, b.phone_number, c.name
# FROM bills as b
# INNER JOIN customer as c on b.phone_number = c.phone_number
# where b.invoice_number = 3 or b.phone_number = ''