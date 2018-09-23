import math
import daletou

# 组合
def combine(arr, n, out, res):
	if n == 0:
		out.append(res)
		return
	if len(arr) == n:
		out.append(res + arr)
		return
	for i in range(len(arr)):
		temp = res[0:]
		temp.append(arr[i])
		combine(arr[i + 1:], n - 1, out, temp)
	pass

if __name__ == '__main__':
	# 前区复式
	pri_front_list = [8,13,20,22,23,30,34,35]
	back_list = [3,9]
	out_front_list = []
	combine(pri_front_list, 5, out_front_list, []),
	satisfy_list = []


	for i in range(len(out_front_list)):
		front_back = out_front_list[i] + back_list
		## 和值
		if sum(front_back) >= 120 and sum(front_back) <= 129: 
			odd_even = daletou.odd_even_ratio(out_front_list[i])
			big_small = daletou.big_small_ratio(out_front_list[i])[0]
			## 奇偶比 大小比
			if odd_even == 4 or odd_even == 3 or big_small == 2 or big_small == 1: 
				satisfy_list.append(out_front_list[i])
		pass

	doc = open('daletou.txt', 'w')
	print("组合总数:%d"%len(satisfy_list), file = doc)
	for i in range(len(satisfy_list)):
		daletou.daletou_print(satisfy_list[i], back_list, doc)
		doc.close
		pass