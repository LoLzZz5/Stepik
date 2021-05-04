#Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения, которые встречаются в нём более одного раза.
def f(s):
	x=s.split()
	x=[int(item)for item in x]
	x.sort()
	counter=0
	u=''
	succ=[]
	ex=''
	for i in range(len(x)):
		for j in range(i+1,len(x)):
			if x[i]==x[j]:
				u+=str(x[i])+' '
	suc=u.split()
	for i in suc:
		if i not in succ:
			succ.append(i)
	for i in succ:
		ex+=str(i)+' '
	print(ex[:len(ex)-1])

if __name__=='__main__':
	f('4 8 0 3 4 2 0 3')#0 3 4
	f('10')#
	f('1 1 2 2 3 3')#1 2 3
	f('1 1 1 1 1 2 2 2')#1 2