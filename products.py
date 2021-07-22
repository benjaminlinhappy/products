#讀取檔案
products = []
with open('products.csv', 'r') as f:
	for line in f:
		if 'product,price' in line:
			continue
		name, price = line.strip().split(',')
		products.append([name, price])
print(products)	

#讓使用者輸入
while True:
	name = input('please input product name: ')
	if name == 'q':
		break
	price = int(input('please input product price:'))
	products.append([name, price])
print(products)

#印出購買紀錄
for p in products:
	print('the price of', p[0], 'is', p[1])

#寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('product,price\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')