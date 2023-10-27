from _2con import createAccount, getDetails, is_valid, withdraw, deleteAccount

while True:
    print('Welcome to "Bank of Durga"')
    print('Select the operation from below options by entering first letter of the option')
    print('Create a bank account\nRetrieve the bank account\nWithdrawal money from bank account\nDeposit money to bank account\nClose the bank account')
    operation = input('Enter Your mode of operation: ').strip()
    operation = operation.lower()
    # acc_no = int(input('Enter Your bank account Number: '))
    if operation == 'c':
        name = input('Enter Your Name : ')
        mobile = input('Enter Your Mobile Number : ')
        DOB = input('Enter Your Date Of Birth : ')
        Aadhar = input('Enter Your Aadhar number : ')
        if all([name, DOB, mobile, Aadhar]):
            if len(mobile) == 10 and len(Aadhar) == 12:
                createAccount(name,  DOB, mobile, Aadhar)
            else:
                print('Please enter Valid Aadhar and mobile number')
        else:
            print('All the above fields are required and should not be empty.')
        break
    elif operation == 'r':
        bankAccNum = input('Enter Bank Account number to get your Banking details: ')
        if len(bankAccNum) == 14:
            getDetails(bankAccNum)
        else:
            print('Please enter valid Bank account number, That should be 14 digit length: ')
        break
    elif operation == 'w':
        bankAccNum = input('Enter Bank Account number to Withdraw : ')
        if len(bankAccNum) == 14:
            acc_info = is_valid(bankAccNum)
            if isinstance(acc_info, list):
                mobile_num = input('Enter Your mobile number linked with bank account: ')
                w_amount = float(input('Enter withdrawal amount : '))
                c_balance = float(acc_info[0][5])
                ac_mobile = f'+91{acc_info[0][2]}'
                withdraw(bankAccNum, w_amount, c_balance, operation, mobile_num, ac_mobile)
            else:
                print(acc_info)
        else:
            print('Please enter valid Bank account number, That should be 14 digit length: ')
        break
    elif operation == 'd':
        bankAccNum = input('Enter Bank Account number to Deposit : ')
        if len(bankAccNum) == 14:
            acc_info = is_valid(bankAccNum)
            if isinstance(acc_info, list):
                d_amount = float(input('Enter Depositing amount : '))
                c_balance = float(acc_info[0][5])
                withdraw(bankAccNum, d_amount, c_balance, operation)
            else:
                print(acc_info)
        else:
            print('Please enter valid Bank account number, That should be 14 digit length: ')
        break
    elif operation == 'cl':
        bankAccNum = input('Enter Bank Account number to Close the bank account: ')
        if len(bankAccNum) == 14:
            acc_info = is_valid(bankAccNum)
            if isinstance(acc_info, list):
                res = deleteAccount(bankAccNum)
                if res:
                    print('Your account closed successfully, Welcome back again')
                else:
                    print('Account not closed')
            else:
                print(acc_info)
        else:
            print('Please enter valid Bank account number, That should be 14 digit length: ')
        break
    else:
        print('Please select the mentioned operations only')
