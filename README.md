# BankAccount

Two accounts - Basic & Premium account
Basic account includes name, account number, balance, card number and card expiry.  
the account number is the number of accounts created, the card number is 16 digit randomly generated and the card expiry is 3 years from today's date. 
The Premium account includes everything the basic account has however with additional features including overdraft facility and overdrat balance. 

Deposit function: 
Deposits the stated amount into the account, and adjusts the balance appropriately.
Deposits must be a positive amount.

Withdraw Function:
Withdraws the stated amount from the account, prints a message of “<Name> has withdrew £<amount>. New balance is £<amount>”.
If an invalid amount is requested, then the following message should be printed, and the method should then terminate: “Can not withdraw £<amount>”

getAvailableBalance Function:
Returns the total balance that is available in the account and takes into account any overdraft that is available.

getBalance Function:
returns the balance of the account if the account is in an overdraft it will return a negative value.

printBalance Function:
Prints the balance of the account. If an overdraft is available it is printed along with how much overdraft is remaining.

getName Function:
Returns the name of the account holder 

getAcNum Function:
Returns the account number

issueNewCard Function:
Creates a new card number and the expiry is 3 years to the month from today.

closeAccount Function:
Returns any balance (via the withdraw method) and returns True.
If the customer is in debt to the bank it returns False and prints message “Can not close account due to customer being overdrawn by £<amount>”

setOverdraftLimit Function:
Sets the overdraft limit to the stated amount
 
  
