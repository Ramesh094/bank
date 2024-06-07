import random
import json
from _3service import validateAadhar, findBankAcc
from _4dao import create_acc, updateAmount, deleteAcc
from _sms import client
from random import *
# this is for testing
otp = randint(100000, 999999)
def createAccount(name, dob, mobile, aadhar):
    data = validateAadhar(aadhar)
    if data:
        print('Your aadhar is already linked with an other bank account.')
    else:
        create_acc(name,  dob, mobile, aadhar)

# retrieve
def getDetails(bankAccNum):
    data = findBankAcc(bankAccNum)
    if data:
        print(f'Account Number :: {data[0][4]}\nName :: {data[0][0]}\nDOB :: {data[0][1]}\nMobile :: {data[0][2]}\nAadhar :: {data[0][3]}\nCurrent Balance :: {data[0][5]}')
    else:
        print(data)

# withdraw
def is_valid(bankAccNum):
    acc_info = findBankAcc(bankAccNum)
    return acc_info

def withdraw(bankAccNum, w_amount, c_balance, operation, mobile_num=0, ac_mobile=0):
    if operation == 'w':
        if w_amount >= 100:
            if w_amount <= c_balance:
                mobile_num = f'+91{mobile_num}'
                if mobile_num == ac_mobile:
                    message = client.messages.create(
                        to=mobile_num,  # Recipient's phone number
                        from_='+12563056741',  # Your Twilio phone number
                        body=f"Baroda Bank One Time Password to withdraw money- {otp}, Please don't share it with anyone"
                    )
                    e_otp = input('Please enter OTP : ')
                    if e_otp == str(otp):
                        r_balance = c_balance - w_amount
                        updateAmount(bankAccNum, c_balance, r_balance)
                        print('Please collect the money, Have a nice day')
                    else:
                        print('Incorrect OTP...')
                else:
                    print('You Entered mobile is not link with provided bank account')
            else:
                print('Sorry, Insufficient Funds...')
        else:
            print('Minimum withdrawal amount is 100')
    else:
        d_amount = w_amount
        if d_amount >= 100:
            r_balance = c_balance + d_amount
            updateAmount(bankAccNum, c_balance, r_balance)
            print('Amount deposited successfully')
        else:
            print('Depositing amount starts from 100')

def deleteAccount(bankAccNum):
    info = deleteAcc(bankAccNum)
    return info


