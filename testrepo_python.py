class Product(object):
	price = 0
	count = 0
	vat = 0

	def __init__(self, price, count, vat):
		self.price = price
		self.count = count
		self.vat = vat

	def price_with_vat(self):
		return self.price * self.count * self.vat

robot = Product(price=900, count=2, vat=1.25)
book =Product(price=100, count=1, vat=1.08)

products= [robot, book]

total_price = 0
for product in products:
	total_price+=product.price_with_vat()

print total_price








