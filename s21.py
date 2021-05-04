#Напишите программу, на вход которой подаётся список чисел одной строкой. Программа должна для каждого элемента этого списка вывести сумму двух его соседей. 
#Для элементов списка, являющихся крайними, одним из соседей считается элемент, находящий на противоположном конце этого списка. 
#Например, если на вход подаётся список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7".
def f(s):
	succ=''
	x=s.split()
	x=[int(item) for item in x]
	result=[]
	if len(x)==1 or len(x)==0:
		for i in x:
			succ+=str(i)
		print(succ)
	else:
		for i in range(len(x)):
			if i==0:
				result.append(x[i+1]+x[len(x)-1])
			elif i ==len(x)-1:
				result.append(x[i-1]+x[0])
			else:
				result.append(x[i-1]+x[i+1])
		for i in result:
			succ+=str(i)+' '
		print(succ[0:len(succ)-1])

if __name__=='__main__':
	f('1 3 5 6 10')#13 6 9 15 7
	f('10')#10