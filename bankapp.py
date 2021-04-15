import sys
class customer:
	def __init__(self,name,balance=0.0):
		self.name=name
		self.balance=balance

	def deposit(self,amount):
		#self.balance +=amount
		self.balance=self.balance+amount
		print("balance after deposit is ", self.balance)
		print('ThankYou')
		#sys.exit(0)

	def withdraw(self,amount):
		if amount>self.balance:
			print("balance is low")
		else:
			self.balance=self.balance-amount
			print("please collect your money")
			print("balance after withdraw is ",self.balance)
			#sys.exit(0)

name1=input('enter customer name ')
c=customer(name=name1)
while True:
	print("plz select..\n d/D-deposit\n w/W-withdraw\n")
	option=input('plz enter your option ')
	if option=='d' or option=='D':
		amount1=int(input('enter amount '))
		c.deposit(amount=amount1)
		
		#sys.exit(0)

	elif option=='w' or option=='W':
		amount1=int(input('enter amount'))
		c.withdraw(amount=amount1)
		print('ThankYou')
		#sys.exit(0)

	else:
		print('invalid customer')





