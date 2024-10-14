def char_stuffing(data, flag=['STX', 'ETX'], esc='DLE'):
    stuffed = ''
    i = 0
    while i < len(data):
        if data[i:i+3] in flag or data[i:i+3] == esc:
            stuffed += esc
            stuffed += data[i:i+3]
            i += 3
        else:
            stuffed += data[i]
            i += 1
    return stuffed

def char_destuffing(stuffed, flag=['STX', 'ETX'], esc='DLE'):
    res = ''
    i = 0
    while i < len(stuffed):
        if stuffed[i:i+3] == esc:
            i += 3
            res += stuffed[i:i+3]
            i += 3
        else:
            res += stuffed[i]
            i += 1
    return res

def bit_stuffing(data):
    stuffed = ''
    count = 0
    for bit in data:
        if bit == '1':
            stuffed += bit
            count += 1
            if count == 5:
                stuffed += '0'
                count = 0
        else:
            count = 0
            stuffed += bit
    return stuffed

def bit_destuffing(data):
    destuffed = ''
    count = 0
    i = 0
    while i < len(data):
        bit = data[i]
        if bit == '1':
            count += 1
            if count == 5:
                if i + 1 < len(data) and data[i + 1] == '0':
                    i += 1
                count = 0
        else:
            count = 0
        destuffed += bit
        i += 1
    return destuffed

if __name__ == "__main__":
    message_chars = input("Enter your message (Special characters - DLE, STX, ETX):")
    stuffed_chars = char_stuffing(message_chars)
    print("Character Stuffed Message:", stuffed_chars)
    destuffed_chars = char_destuffing(stuffed_chars)
    print("Character Destuffed Message:", destuffed_chars)

    message_bits = input("Enter your message (Binary):")
    stuffed_bits = bit_stuffing(message_bits)
    print("Bit Stuffed Message:", stuffed_bits)
    destuffed_bits = bit_destuffing(stuffed_bits)
    print("Bit Destuffed Message:", destuffed_bits)
