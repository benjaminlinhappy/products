products = []
while True:
	name = input('please input product name: ')
	if name == 'q':
		break
	price = input('please input product price:')
	products.append([name, price])
print(products)

