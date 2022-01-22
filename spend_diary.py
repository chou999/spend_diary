import os #operating system

products = []
# 讀取檔案
if os.path.isfile('products.csv'): #檢查檔案在不在
	print('yeah!! 找到檔案了！')
	with open('spend_diary.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue #跳過這一迴依然在迴圈裡（類似７加８減裡的pass)
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
else:
	print('找不到檔案．．．')

# 讓使用者輸入
while True:
	name = input('請輸入商品名稱： ')
	if name == 'q':
		break
	price = input('請輸入商品價格： ')
	price = int(price)
	products.append([name, price])
print(products)

# 印出所有購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])

# 寫入檔案
with open('spend_diary.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')