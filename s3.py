#Катя узнала, что ей для сна надо X минут. В отличие от Коли, Катя ложится спать после полуночи в H часов и M минут.
#Помогите Кате определить, на какое время ей поставить будильник, чтобы он прозвенел ровно через X минут после того, как она ляжет спать.
def f(x,h,m):
	print((x+(h*60+m))//60,(x+(h*60+m))%60)

if __name__=='__main__':
	f(480,1,2)
	f(475,1,55)