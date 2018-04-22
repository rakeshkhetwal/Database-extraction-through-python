import mysql.connector
import datetime

asd= mysql.connector.connect(user='root', password='root', database='bank_details')
cursor= asd.cursor()

def New_account():
    cursor.execute("insert into account_details ( account_NO, account_name, Branch_address, IFSC_code, Bank_name, Deposit_Amt, On_date) values( 1002, 'sumit', 'Tilak nagar', 987654,'SBI', 12000, '12/2/2012')")
    asd.commit()
def amount_deposit():
    cursor.execute("insert into trandet( Account_No, Amount, Trans_type, name, mode_type, trans_date, balance) values ( 1002, 2000, 'credit', 'sumit', 'cash', '12/2/2014',14000)")
    
    asd.commit()

def withdrawal():
    cursor.execute("insert into trandet( Account_No, Amount, Trans_type, name, mode_type, trans_date, balance) values ( 1002, 1000, 'debit', 'amit', 'cash', '12/2/2015', 13000)")
    asd.commit()
def viewstatement():
    cursor.execute("select * from trandet")
    for (Account_No, Amount, Trans_type, name, mode_type, trans_date, balance) in cursor:
          print (Account_No, Amount, Trans_type, name, mode_type, trans_date, balance)
          
def accountclose():

    dd = 0

    acno = input('enter ac no ')


    
    cursor.execute("select * from account_details where Account_No = "+acno)
    for (Account_No, Amount, Trans_type, name, mode_type, trans_date, balance) in cursor:

        dd = balance
        
    cursor.execute("select * from trandet where Account_No = "+acno)
    for (Account_No, Amount, Trans_type, name, mode_type, trans_date, balance) in cursor:

        dd = balance
        
        print (Account_No, Amount, Trans_type, name, mode_type, trans_date, balance)

        
ch=8    
while ch!=0:    
    print('1 for new account 2 for amount deposit 3 for withdrawal 4 for view statement 5 for Account close 0 to exit')
    ch= int(input('Select Option'))
    if ch==1:
       New_account()
    if ch==2:
       amount_deposit()
    if ch==3:
        withdrawal()
    if ch==4:
       viewstatement()
    if ch==5:
        accountclose()
cursor.close()
         
