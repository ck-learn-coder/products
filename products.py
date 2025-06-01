# 二維度清單
products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')

	np = [] #二維度清單
	np.append(name)
	np.append(price)

	np=[name, price] #這樣寫也可以
	products.append(np)
	#products.append([name, price]) 這樣寫也可以
print(products)

products[0][0]
print('------------')

for p in products:
	print(p[0], '的價格是: ', p[1])