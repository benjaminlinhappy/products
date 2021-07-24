import os # operating system

#讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			if 'product,price' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	return products

#讓使用者輸入
def user_input(products):
	while True:
		name = input('please input product name: ')
		if name == 'q':
			break
		price = input('please input product price:')
		products.append([name, price])
	print(products)
	return products

#印出購買紀錄
def print_products(products):
	for p in products:
		print('the price of', p[0], 'is', p[1])

#寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as f:
		f.write('product,price\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')

def main():
	products = []
	filename = 'products.csv'
	if os.path.isfile(filename):#檢查檔案是否存在
		products = read_file(filename)
		print('file found')
		print(products)
	else:
		print('file not found')
	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()