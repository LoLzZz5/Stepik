#Напишите программу, которая получает на вход три целых числа, по одному числу в строке, и выводит на консоль в три строки сначала максимальное, потом минимальное, после чего оставшееся число.
def f(a,b,c):
	if a >= b and a >= c:
		print(a)
		if b >= c:
			print(c,b)
		else:
			print(b,c)
	elif b >= a and b >= c:
		print(b)
		if a >= c:
			print(c,a)
		else:
			print(a,c)
	elif c >= a and c >= b:
		print(c)
		if a >= b:
			print(b,a)
		else:
			print(a,b)

if __name__=='__main__':
	f(8,2,14)#14 2 8
	f(23,23,21)#23 21 23