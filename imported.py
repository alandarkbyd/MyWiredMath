import math                             
i2 = -1
cr = pow(3, (1/3))
# inp = input("The number")
#The comment Keywords
'''
Notes:
In the __init__ method it's creating the variables and in the other
methods it's just assigning or updateing the value of a perticular variable

'''


class SecondOne():
	def dSF(self):
		cose = int(abs(object1.s ** i2))
		tan = int(abs(object1.t ** i2))
		return cose - tan

class FirstOne():
	x = 3734
	cc = 34
	ct = 34
	ta = 4
	co = 9
	si = 2

	def __init__(self,x):
		# self.x = 9
		self.s = math.cos(x) * math.tan(x)
		self.a = 1 - self.x
		self.aa = self.x + self.a
		self.t = math.sin(self.x)/math.cos(self.x)
		# print(self.aa)
		# self.co =  pow(self.cc, 2)
		# self.si = pow(self.s, 2)
		# self.ta = pow(self.ct, 2)
		
		# self.co =  pow(self.cc, 2)
		# self.bacco = 1 - self.co
		# self.acco = int(self.bacco + self.co)
		
		# self.si = pow(self.s, 2)
		# self.bacsi = 1 - self.si
		# self.acsi = int(self.bacsi + self.si)
	
	def afterOne(self):
		# x = None
		# c = math.sin(self.x)/math.cos(self.x)
		c = math.sin(self.x)/math.cos(self.x)
		t = math.sin(self.x)/math.cos(self.x)
		self.cc = c
		self.ct = t

	# def theSqurel(self):
	def theCo(self):
		# self.afterOne()
		co =  pow(self.cc, 2)
		bacco = 1 - co
		acco = int(bacco + co)
		return acco

	def theSi(self):
		si = pow(self.s, 2)
		bacsi = 1 - si	
		acsi = int(bacsi + si)
		return acsi
	
	def theTan(self):
		self.ta = pow(self.ct, 2)
		bactan = 1 - ta
		actan = int(bactan + ta)
		return actan
	
	# def sumAll(self):
		self.theTan()
		self.ta = self.si + self.co
		return self.ta
	
	def sumAll(self):
			
			self.ta = self.acco + self.acsi
			return self.ta - 1
		

# class SecondOne():
# 	def dSF(self):
# 		cose = int(abs(object1.s ** i2))
# 		tan = int(abs(object1.t ** i2))
# 		return cose - tan


class ThirdOne():
	def dSF(self):
		mcom = complex(3462342356342376523 +(round(math.sqrt(2))) -3462342356342376523)
		mtcr = mcom.real
		return int(mtcr)

list1 = []
# def theClasObjs():
	# object1 = FirstOne(5)
	# object2 = ThirdOne()
	# object3 = SecondOne()
	# return object1, object2, object3
# print(object3.dSF())
# print(object2.dSF())
# print(object1.aa)
# object1.afterOne()
# ff = object1.theCo()
# fd = object1.theSi()
# df = object1.sumAll()
# print(df)
# print(ff)
# print(fd)
# print(object1.cc)
# theClasObjs()

object1 = FirstOne(5)
object3 = ThirdOne()
object2 = SecondOne()

def outterSum():
	sine = object1.theSi()
	cosine = object1.theCo()
	tangent = sine + cosine - 1
	return tangent
OS = outterSum()
b = ThirdOne().dSF()
c = SecondOne().dSF()

s3 = outterSum() + b + c
def checkingLast(inp,out):
	global list1
	for i in range(inp):
		list1 += '1'
	# print(list1)
	# for inpl in list1:
		# print(list1[i], end="")
		# print(list1[i] + '+ ', end="")


# the main output
	# if s3 == round(pow(cr, 3)):
	# 	print("\nSo it is proved that {} + {} + {} = {}".format(b,c,OS, s3))
	# else:
	# 	print("Apology, it was my bad!")
	# if inp == (OS * inp):
	if inp == out:
		# print(f"So it is proved that {('+ 1' * inp) + ' ='}", inp)
		print(f"{'+'.join('1'*inp)} = {inp}")
		print("Your given statement is True")
	else:
		print("Sorry, I couldn't prove your statement. Forgive me!")

	# print(('+ 1' * inp) + ' =')
	# print(OS * inp)

