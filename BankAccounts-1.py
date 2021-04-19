
import random #imports the random Library in order to get random card number
import datetime #imports the datetime Library in order to get date for card expiry date

class BasicAccount:
    """
    Basic Account is a bank account. Has name, Account Number, Balance,Card Number, Card Expiry.
    """
    numAccounts=0
    def __init__(self,theName, theBalance):
        self.name = theName
        BasicAccount.numAccounts +=1
        self.acNum= BasicAccount.numAccounts
        self.balance = float(theBalance)
        self.cardNum = ''
        self.cardExp= ()

    #__str__ returns the account holder name and the balance of the account
    def __str__(self):
        return '\nName:{self.name}\nOpening Balance:£{self.balance}\n'.format(self=self)
     

    def deposit(self, amount):
        """
        Deposits the amount given and updates the balance

        Parameters:
            amount: float - the amount that needs to be deposited
        Returns: 
            Nothing
        """
        try:
            if amount >0:
                self.balance+ amount
            else:
                raise ValueError #raises error when a negative value is inputted 
        except ValueError:
            self.balance+abs(amount) #assumes typing error, excepts value error and deposits the absolute value 
            

    def withdraw(self,amount):
        """
        Withdraws the amount (if the avalible balance is more than the amount) and updates the balance, if this isnt possible the balance isnt updated  
        Parameters:
         amount: float- the amount given that needs to be withdrew
        Returns:
            float- adjusted or unadjusted balance
        """
        newBalance= self.getAvailableBalance()
        if newBalance < amount:
            print(self.name,'can not withdraw £',amount)
            return self.balance
        if amount==0:
            print('Balance: £',self.balance)
        else:
            self.balance = self.balance-amount # deducts the amount inputted
            print("\n{self.name} has withdrew £".format(self=self),amount ,"New balance is £", self.balance,"\n")
            return self.balance

    def getAvailableBalance(self):
        """
        Finds the Balance that is avalible in the account

        Parameters:
            Nothing
        Returns: 
            float - Avalible balance
        """
        return self.balance

    def getBalance(self):
        """
        Finds the total Balance that is avalible in the account
        
        Parameters:
            Nothing
        Returns: 
            float - Total balance not taking overdraft into account
        """
        return self.balance
    
    
    def printBalance(self):
        """
        Prints total Balance of the account

        Parameters:
            Nothing
        Returns: 
            Nothing
        """
        print("\n{self.name}'s balance: £{self.balance}\n".format(self=self))

    
    def getName(self):
        """
        finds the name of account holder

        Parameters:
            Nothing
        Returns: 
            string - Name
        """
        return '\nAccount holder name: {self.name}\n'.format(self=self)

    
    def getAcNum(self):
        """
        finds the account number of the account holder

        Parameters:
            Nothing
        Returns: 
            string - Account number
        """
        return "{self.name}'s account number: {self.acNum}\n".format(self=self)
    
 
    def cardNumber(self):
        """
        Creates a 16 digit card number

        Parameters:
            Nothing
        Returns: 
            string - Card Number
        """
        for _ in range(0,16):
            self.cardNum+=str(random.randint(1,9)) #creates random 16 digit card number
        return self.cardNum
    
    def expiry(self):
        """
        Issues a new expriry date 3 years from the date it is requested 

        Parameters:
            Nothing
        Returns: 
            tuple - New expriry date
        """
        todayDate= datetime.date.today() # todays date
        todayYear= todayDate.year
        self.cardExp=(todayDate.month,(todayYear + 3)) #adds 3 years 
        return self.cardExp
    
    def issueNewCard(self):
        """
        Prints a new card number from the cardNumber method and returns the new exiry date from the method expiry

        Parameters:
            Nothing
        Returns: 
            Nothing
        """
        self.cardNumber()
        self.expiry()
        print('\nNew card number: {self.cardNum}'.format(self=self))
        print('New card expiry date: {self.cardExp}\n'.format(self=self))

    def closeAccount(self):  
        """
        closes the account if the account is not in debt to the bank and withdraws the remaining balance

        Parameters:
            Nothing
        Returns: 
            boolean - True or False 
        """
        self.withdraw(0)
        print("Withdrawing {self.name}'s remaining Balance...\n".format(self=self))
        self.withdraw(self.balance)
        print("Close account accepted?")
        return True
        
class PremiumAccount(BasicAccount):
    """
    Premium Account is a bank account. Has name, Account Number, Balance,Card Number, Card Expiry, Overdraft .
    """
    def __init__(self,theName, theBalance, theOverdraftLimit):
        super().__init__(theName, theBalance)
        self.overdraft = True
        self.overdraftLimit = float(theOverdraftLimit)
    
    #__str__ returns the name and overdraft information when the object is printed
    def __str__(self):
        return 'Name:{self.name}\nOpeining Balance:£ {self.balance} \nOverdraft Limit:£{self.overdraftLimit}\n'.format(self=self)
    
    
    def setOverdraftLimit(self,newLimit):
        """
        Sets the overdraft limit to the stated amount if overdraft is True

        Parameters:
            amount: float- inputted amount
        Returns: 
            float - adjusted overdraft avalible
            string- if Overdraft facility is not avalible to the account
        """
        if self.overdraft == True:
            if isinstance(newLimit,float)==False:
                newLimit=float(newLimit)
                self.overdraftLimit = newLimit
            return self.overdraftLimit
        else:
            raise TypeError('\nOverdraft Facility is not available\n')

    def getAvailableBalance(self):
        """
        Finds the total Balance that is avalible in the account and takes into account any overdraft avalible

        Parameters:
            Nothing
        Returns: 
            float - Avalible balance taking overdraft into account
        """
        newBalance = self.balance + self.overdraftLimit
        return newBalance

    def printBalance(self):
        """
        Prints total Balance of the account, the overdraft limit and the amount of overdraft remaining

        Parameters:
            Nothing
        Returns: 
            Nothing
        """
        print("{self.name}'s balances:\nAvailable Balance: £ {self.balance}".format(self=self))
        print("Overdraft avalible: {self.overdraft}\nAvailable Overdraft: £ {self.overdraftLimit}".format(self=self))
        print("Total Balance: £", self.balance+self.overdraftLimit,"\n")
    
    def closeAccount(self):
        """
        closes the account if the account is not in debt to the bank

        Parameters:
            Nothing
        Returns: 
            Boolean - True or False 
        """
        self.withdraw(0)
        if self.balance > 0:
            print("Withdrawing {self.name}'s remaining Balance...".format(self=self))
            self.withdraw(self.balance)
            print("Close account Accepted?")
            return True
        else:
            print("\nCan not close account due to {self.name} being overdrawn by £".format(self=self),abs(self.balance))
            print("\nClose account Accepted?")
            return False
