class Bank:
    loan=True
    Tbal=100000
    Tloan=0
    account={}
    admin={}
    
    

class User(Bank):
    def __init__(self, name, email, address):
        super().__init__()
        self.name=name
        self.email=email
        self.address=address
        self.balance=0
        self.tr=[]
        self.loanc=0
    


    def deposit(self, amount):
        self.balance+=amount #hhdhhdh
        print(f'Amount {amount} is deposited')
        self.tr.append(f'Deposited amount {amount}.')
        b.Tbal+=amount

    def withdraw(self, amount):
        if amount>b.Tbal:
            print('Sorry! Our bank is bankrupt.')
        else:
            if amount>self.balance:
                print(f'Withdrawal amount exceeded {self.balance}.')
            else:
                self.balance-=amount
                print(f'Current balance {self.balance}')
                b.Tbal-=amount
                self.tr.append(f'Withdrawal amount {amount}.')
        
    def check_balance(self):
        print(f'Current balance {self.balance}.')

    def check_history(self):
        for i in self.tr:
            print(i)

    def loan_req(self):
        if self.loan<2 and b.loan==True:
            self.balance+=5000
            print('Loan added 5000 in account.')
            self.tr.append(f'Added loan 5000.')
            b.Tloan+=5000
        else:
            print('Loan limit exited.')



    def transfer(self, ac2, amount):
        if self.balance<amount:
            print('Not enough balance.')
        else:
            b.account[ac2].deposit(amount)
            self.withdraw(amount)
            self.tr.append(f'Transfered amount {amount}.')


class Admin(Bank):
    def __init__(self, name, email, address):
        super().__init__()
        self.name=name
        self.email=email
        self.address=address

    def delete_user(self, acno):
        if acno in b.account:
            del b.account[acno]
            print('Account deleted.')
        else:
            print('Account not valid.')

    def see_aclist(self):
        for i, k in b.account.items():
            print(f'{i} {k.name} {k.email} {k.address}')

    def bank_balance(self):
        print(f'Total bank balance {b.Tbal}.')

    def loan_amount(self):
        print(f'Total loan amount {b.Tloan}.')

    def change_loan(self):
        if b.loan==True:
            b.loan=False
            print('Loan is off')
        else:
            b.loan=True
            print('Loan is on')

x=3
z=300
al=None
bl=None
b=Bank()
p1=User('Alif', 'alif@', 'Dhaka')
p2=User('Balif', 'balif@', 'Sylhet')
acno=len(p1.email)+x
User.account[acno]=p1
acno=len(p2.email)+x
User.account[acno]=p2
# p1.check_balance()
# p1.deposit(3000)
# p1.loan_req()
# p1.check_balance()
# p1.withdraw(200)
# print('-----')


# p1.transfer(6,3000)
# p1.check_history()
# print('ddd')
# p1.check_balance()
# p2.check_balance()


# print('----------')
a1=Admin('Admin 1', 'admin1@gmail.com', 'Chittagong')
accno=len(a1.email)+z
b.admin[accno]=a1
# a1.see_aclist()
# a1.bank_balance()
# a1.loan_amount()
# a1.change_loan()
x+=1
z+=1




while True:
    print('''1. User.
2. Admin.
3.Terminate. ''')
    ch=int(input('Enter choice: '))
    if ch==1:
        while True:
            print('''1. Create account.
2. Login.
3. Previous Page.''')
            ch2=int(input('Enter your request. '))
            if ch2==1:
                name=input('Enter Name: ')
                email=input('Enter Email: ')
                address=input('Enter address: ')
                person=User(name, email, address)
                acno=len(email)+x
                b.account[acno]=person
                bl=b.account[acno]
                x+=1
                while True:
                    print('''3. Deposit.
4. Withdraw
5. Check Balance.
6. Request for loan.
7. Transfer money.
8. Previous Page. ''')  
                    aa=int(input('Enter choice: '))
                    if aa==3:
                        ab=int(input('Enter a valid deposit amount: '))
                        bl.deposit(ab)
                    if aa==4:
                        ab=int(input('Enter a valid withdraw amount: '))
                        bl.withdraw(ab)
                    if aa==5:
                        bl.check_balance()
                    if aa==6:
                        bl.loan_req()
                    if aa==7:
                        # ac1=int(input('Enter sender account: '))
                        ac2=int(input('Enter recepient account: '))
                        amount=int(input('Enter amount: '))
                        bl.transfer(ac2, amount)
                    if aa==8:
                        break

            elif ch2==2:
                print('id   name')
                for i,k in b.account.items():
                    print(f'{i}   {k.name}')
                id=int(input('Enter User id: '))
                bl=b.account[id]
                while True:
                    print('''3. Deposit.
4. Withdraw
5. Check Balance.
6. Request for loan.
7. Transfer money.
8. Previous Page. ''') 
                    aa=int(input('Enter choice: '))
                    if aa==3:
                        ab=int(input('Enter a valid deposit amount: '))
                        bl.deposit(ab)
                    if aa==4:
                        ab=int(input('Enter a valid withdraw amount: '))
                        bl.withdraw(ab)
                    if aa==5:
                        bl.check_balance()
                    if aa==6:
                        bl.loan_req()
                    if aa==7:
                        # ac1=int(input('Enter sender account: '))
                        ac2=int(input('Enter recepient account: '))
                        amount=int(input('Enter amount: '))
                        bl.transfer(ac2, amount)
                    if aa==8:
                        break
                             


            elif ch2==3:
                break



    elif ch==2:
        while True:
            print('''1. Create account.
2. Login.
3. Previous Page''')
            ca=int(input('Enter choice: '))
            if ca==1:
                name=input('Enter Name: ')
                email=input('Enter Email: ')
                address=input('Enter address: ')
                person=Admin(name, email, address)
                acno=len(email)+z
                b.admin[acno]=person
                z+=1
                al=b.admin[acno]
                while True:
                    aa=int(input('Enter choice: '))
                    print('''3. Delete account.
4. See user account list.
5. Total balance of bank.
6. Total loan amouunt.
7. Change loan feature.
8. Previous Page.''')
                    if aa==3:
                        acno=int(input('Enter account no to delete account: '))
                        al.delete_user(acno)

                    elif aa==4:
                        print('All user list: ')
                        al.see_aclist()
                    elif aa==5:
                        al.bank_balance()
                    elif aa==6:
                        al.loan_amount()
                    elif aa==7:
                        al.change_loan()
                    elif aa==8:
                        break
            elif ca==2:
                    print('id   name')
                    for i, k in b.admin.items():
                        print(f'{i}   {k.name}')
                    id=int(input('Enter id: '))
                    al=b.admin[id]
                    while True:
                        print('''3. Delete account.
4. See user account list.
5. Total balance of bank.
6. Total loan amouunt.
7. Change loan feature.
8. Previous Page.''')
                        aa=int(input('Enter choice: '))
                        if aa==3:
                            acno=int(input('Enter account no to delete account: '))
                            al.delete_user(acno)
                        elif aa==4:
                            print('All user list: ')
                            al.see_aclist()
                        elif aa==5:
                            al.bank_balance()
                        elif aa==6:
                            al.loan_amount()
                        elif aa==7:
                            al.change_loan()
                        elif aa==8:
                            break
            elif ca==3:
                break



    else:
        print('Terminated.')
        break



    




    


    