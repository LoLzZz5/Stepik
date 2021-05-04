#Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и выводит закодированную последовательность на стандартный вывод. Кодирование должно учитывать регистр символов.
import collections
def f(genome):
	result = collections.deque()
	genome += '$'
	last = genome[0]
	counter = 1
	for c in genome[1:]:
		if c == last:
			counter += 1
		else:
			result.append('%s%d' % (last, counter))
			last = c
			counter = 1
	print(''.join(result))

if __name__=='__main__':
	f('aaaabbcaa')#a4b2c1a2
	f('abc')#a1b1c1