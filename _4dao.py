from _5utils import conn
def checkAadhar(aadhar):
    try:
        cursor = conn.cursor()
        cursor.execute('use bank')
        stmt = 'select * from bank_accounts where aadhar = %s'
        cursor.execute(stmt, (aadhar,))
        records = cursor.fetchall()
        conn.commit()
        if records:
            return True
    except Exception as e:
        print(e)
    return False



def create_acc(name, dob, mobile, aadhar):
    try:
        cursor = conn.cursor()
        cursor.execute('use bank')
        code = '15'
        balance = float(input('Enter amount[Initial account balance is 500] : '))
        acc_number = code + aadhar
        acc = (name,  dob, mobile, aadhar, acc_number, balance)
        stmt = "insert into bank_accounts values(%s, %s, %s, %s, %s, %s)"
        cursor.execute(stmt, acc)
        print(f'New Bank Account is created with Account number {acc_number}')
    except Exception as e:
        print('DAO :: Exception Occurred', e)
    finally:
        conn.commit()

# retrieve
def checkBankAcc(bankAccNum):
    try:
        cursor = conn.cursor()
        cursor.execute('use bank')
        stmt = 'select * from bank_accounts where Acc_number = %s'
        cursor.execute(stmt, (bankAccNum,))
        records = cursor.fetchall()
        conn.commit()
        if records:
            return records
    except Exception as e:
        print(e)
    return False


def updateAmount(bankAccNum, c_balance, r_balance):
    try:
        cursor = conn.cursor()
        cursor.execute('use bank')
        stmt = 'update bank_accounts set balance = %s where Acc_number = %s'
        cursor.execute(stmt, (r_balance, bankAccNum))
        conn.commit()
    except Exception as e:
        print(e)

def deleteAcc(acc):
    # try:
    cursor = conn.cursor()
    cursor.execute('use bank')
    stat = 'delete from bank_accounts where Acc_number = %s'
    acc = (acc,)
    cursor.execute(stat, acc)
    conn.commit()
# except Exception as e:
#     print(e)
    return True

