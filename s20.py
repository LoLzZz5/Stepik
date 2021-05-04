#Напишите программу, на вход которой подается одна строка с целыми числами. Программа должна вывести сумму этих чисел.
def f(text):
	lst=text.split()
	lst=[int(item) for item in lst]
	print(sum(lst))

if __name__=='__main__':
	f('4 -1 9 3')#15