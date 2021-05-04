#Напишите программу, на вход которой даются четыре числа a, b, c и d, каждое в своей строке.
#Программа должна вывести фрагмент таблицы умножения для всех чисел отрезка [a; b][a;b] на все числа отрезка [c;d][c;d].
def f(a,b,c,d):
	print("",end = "\t")
	for i in range (c,d+1):
		print(i,end = "\t")
	print("")
	for i in range(a,b+1):
		print(i,end="\t")
		for t in range(c,d+1):
			print(i*t, end="\t")
	print(end="\n")

if __name__=='__main__':
	f(7,10,5,6)
	f(5,5,6,6)
	f(1,3,2,4)