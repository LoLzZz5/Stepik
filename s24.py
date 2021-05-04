#Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... (число повторяется столько раз, чему равно).
def f(n):
	p=str(n)
	suc=[]
	succ=''
	if n == 1:
		print(n)
	elif n==2:
		print('1 2')
	else:
		for i in range(1,n):
		    counter=0
		    while counter!=i:
		        counter+=1
		        st=''
		        st+=str(i)+' '
		        suc.append(st)
		suc=suc[:n]
		for i in suc:
			succ+=i
		print(succ[:len(succ)-1])

if __name__=='__main__':
	f(7)#1 2 2 3 3 3 4