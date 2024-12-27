class Bank:
    def __init__(self):
        self.__accNo="123456789"
        self.__bankBalc=50000

    def withdraw(self,wAmount):
      self.__bankBalc = self.__bankBalc-wAmount
      print("Current Balance : ",self.__bankBalc)
      
    def deposit(self,dAmount):
      self.__bankBalc = self.__bankBalc+dAmount
      print("Current Balance : ",self.__bankBalc)


bankObj=Bank()
bankObj.deposit(10000)

