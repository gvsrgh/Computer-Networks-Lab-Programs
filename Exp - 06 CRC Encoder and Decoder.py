def getXor(partXor, div):
    remainder = ""
    if partXor[0] == '0':
        print(partXor)
        print('0'*len(div))
        print('------------------------')
        return partXor[1:]
    print(partXor)
    print(div)
    for i in range(1, len(div)):
        if partXor[i] == div[i]:
            remainder += '0'
        else:
            remainder +='1'
    print('------------------------')
    return remainder

def encoder(div, data):
    dividend = data + ("0")*(len(div)-1)
    starter = 0
    borrower = len(div)
    partXor = dividend[starter: borrower]
    for _ in range(len(dividend) - len(div) + 1):
        remainder = getXor(partXor, div)
        if borrower >= len(dividend):
            break
        remainder += dividend[borrower]
        starter += 1
        borrower += 1
        partXor = remainder
    return getXor(partXor, div)    

def decoder(div, data, divUtil):
    dividend = data + divUtil
    starter = 0
    borrower = len(div)
    partXor = dividend[starter: borrower]
    for _ in range(len(dividend) - len(div) + 1):
        remainder = getXor(partXor, div)
        if borrower >= len(dividend):
            break
        remainder += dividend[borrower]
        starter += 1
        borrower += 1
        partXor = remainder
    return getXor(partXor, div)    
    

if __name__ == "__main__":
    dataset = input("Enter the data to be transmitted: ")
    divisor = input("Enter the Polynomial divisor for CRC: ")
    print('Encoder Process Started:')
    print('------------------------')
    dividendUtil1 = encoder(divisor, dataset)
    print("Final remainder (from encoder): ", end = "")
    print(dividendUtil1)
    print('------------------------')
    print('Decoder Process Started:')
    print('------------------------')
    dividendUtil2 = decoder(divisor, dataset, dividendUtil1)
    print("Final remainder (from decoder): ", end = "")
    print(dividendUtil2)
    print('------------------------')
    print('Decoder Process with error data')
    print('------------------------')
    error = dividendUtil1[1:] + '1'
    dividendUtil3 = decoder(divisor, dataset, error)
    print("Final remainder (from error decoder): ", end = "")
    print(dividendUtil3)
