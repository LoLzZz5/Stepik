#Из передачи “Здоровье” Аня узнала, что рекомендуется спать хотя бы A часов в сутки, но пересыпать тоже вредно и не стоит спать более B часов.
#Сейчас Аня спит H часов в сутки. Если режим сна Ани удовлетворяет рекомендациям передачи “Здоровье”, выведите “Это нормально”.
#Если Аня спит менее A часов, выведите “Недосып”, если же более B часов, то выведите “Пересып”.
def f(a,b,h):
	if h >= a and h <= b:
		print("Это нормально")
	elif h >= a and h >= b:
		print("Пересып")
	else:
		print("Недосып")

if __name__=='__main__':
	f(6,10,8)#Это нормально
	f(7,9,10)#Пересып
	f(7,9,2)#Недосып