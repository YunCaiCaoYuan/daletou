import math


# 计算AC值
def calc_ac_val(arr):
	ac = []
	for i in range(len(arr)):
		for j in arr[i+1:]:
			ac.append(j - arr[i])
	ac_arr = list(set(ac))		
	return len(ac_arr) - (5 - 1)

# 计算大小比
def big_small_ratio(arr):
	mid = 18
	big = 0
	small = 0
	for i in arr:
		if i > 18 :
			big += 1
		if i < 18 :
			small += 1	
	return [big, small]

# 计算奇偶比
def odd_even_ratio(arr):
	odd = 0
	for i in arr:
		if i % 2 != 0 :
			odd += 1	
	return odd

# 是否质数
def is_prime(num):
	if num == 1 or num == 4:
		return False
	if num == 2 or num == 3:
		return True
	for i in range(2, int(math.sqrt(num))):
		if num % i == 0:
			return False	
	return True 	

# 计算质合比
def prime_full_ratio(num):
	prime = 0
	for i in num:
		if is_prime(i) == True:
			prime += 1
	return prime

def daletou_print(front_list, back_list, filename = None):
	merge_list = front_list + back_list
	print("\n", file = filename)
	print("====== 大乐透预测 ======", file = filename)
	print("== 前区号码:", front_list, file = filename)
	print("== 后区号码:", back_list, file = filename)
	print("== 前区和值:", sum(front_list), file = filename)
	print("== 总和值:", sum(merge_list), file = filename)
	print("== AC值:", calc_ac_val(front_list), file = filename)
	print("== 大小比: %d : %d"%(big_small_ratio(front_list)[0], big_small_ratio(front_list)[1]), file = filename)
	print("== 奇偶比: %d : %d"%(odd_even_ratio(front_list), 5 - odd_even_ratio(front_list)), file = filename)
	print("== 质合比: %d : %d"%(prime_full_ratio(front_list), 5 - prime_full_ratio(front_list)), file = filename)
	print("========================", file = filename)

# 和值范围
# AC值:一组号码组合中任意两个数字的不同正数差值的总数减去“选出数-1”的值
# 大小比:大小比是指乐透型彩票（如双色球，大乐透）红球开奖数字中大数与小数的比值。
# 奇偶比
# 质合比

if __name__ == '__main__':
	front_list = [3,16,27,28,32]
	back_list = []
	daletou_print(front_list, back_list)
