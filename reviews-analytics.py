# 讀取檔案

data = []
count = 0
with open('reviews.txt', 'r') as f: # 當離開with架構 自動close
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0: # 每1000筆印一次
			print(len(data))
print('檔案讀取完了,共有',len(data),'筆留言')

word_count = {}
for d in data:
	words = d.split(' ')
	for word in words:
		if word in word_count:
			word_count[word] += 1
		else:
			word_count[word] = 1 # 新增新的key進字典
for word in word_count:
	if word_count[word] > 100:
		print(word, word_count[word])

while True:
	word = input('請問你想查什麼字: ')
	if word == 'q':
		print('結束')
		break
	if word in word_count:
		print(word, '出現過', word_count[word], '次')
	else:
		print('沒有這個字')


# sum_reviews = 0
# for d in data:
# 	sum_reviews += len(d)
# print('平均留言長度為: ', sum_reviews/len(data))

# new = []
# for d in data:
# 	if len(d) < 100:
# 		new.append(d)
# print('一共有', len(new), '筆留言長度小於100')