#the varables
loanamount = 0
interestrate = 0
loandurationinyears = 0
monthlypayment = 0
numberofpayment = 0

#collect input from users
loanamount = input("How much would you borrow? ")
interestrate = input("What is your interest rate? ")
loandurationinyears = input("How many years would it take you to pay off the loan? ")

#since payment is ones per month, number of payment would be number of year for the loan *12
numberofpayment = loandurationinyears*12

#calculate mounthly payment with this formular
monthlypayment = loanamount * interestrate * (1+ interestrate) * numberofpayment / ((1+ interestrate) * numberofpayment -1)

#user result
print("your monthly payment would be $%.2f" % monthlypayment)