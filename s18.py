#Напишите программу, которая вычисляет процентное содержание символов G (гуанин) и C (цитозин) в введенной строке (программа не должна зависеть от регистра вводимых символов).
def f(s):
	s = s.lower()
	print(((s.count("c")+s.count("g"))/len(s))*100)

if __name__=='__main__':
	f('acggtgttat')#40.0