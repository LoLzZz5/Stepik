#Напишите программу, которая считывает список чисел lst из первой строки и число x из второй строки, которая выводит все позиции, на которых встречается число xx в переданном списке lst.
def f():
	lst=str(input())
	lst1=lst.split()
	lst1=[int(item)for item in lst1]
	suc=''
	num=int(input())
	for i in range(len(lst1)):
		if lst1[i]==num:
			suc+=str(i)+' '
	if len(suc)>0:
		print(suc[0:len(suc)])
	else:
		print('Отсутствует')

if __name__=='__main__':
	f()