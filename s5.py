#Требуется определить, является ли данный год високосным.
def f(a):
	if a%400 == 0:
		print("Високосный")
	elif a%4 == 0 and a%100 != 0:
		print("Високосный")
	else :
		print("Обычный")

if __name__=='__main__':
	f(2100)#Обычный
	f(2000)#Високосный