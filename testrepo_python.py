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

products = [Product(price=900, count=2, vat=1.25), Product(price=100, count=1, vat=1.08)]

print products[1].price






