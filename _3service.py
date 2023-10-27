from _4dao import checkAadhar, checkBankAcc


def validateAadhar(aadhar):
    is_exits = checkAadhar(aadhar)
    return is_exits

def findBankAcc(bankAccNum):
    data_found = checkBankAcc(bankAccNum) # list
    if data_found:
        return data_found
    else:
        return f"Sorry, We didn't find bank account with this number '{bankAccNum}'"