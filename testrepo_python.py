class Product(object):
	price = 0
	count = 0
	vat = 0

robot = Product()
robot.price = 900
robot.count = 2
robot.vat	= 1.25

book = Product()
book.price = 100
book.count = 1
book.vat =1.06


print robot.price*robot.count*robot.vat+book.price*book.count*book.vat

robot_price = 900
robot_count = 2
robot_vat = 1.25
book_price = 100
book_count = 1
book_vat = 1.06

