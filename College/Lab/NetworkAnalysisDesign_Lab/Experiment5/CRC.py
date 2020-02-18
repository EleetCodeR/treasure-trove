

def remainder_crc(data_bits, key_bits, pad_bit):
    key_bits = key_bits.lstrip('0')
    ip_len = len(data_bits)
    padding = pad_bit*(len(key_bits)-1)
    padded_inp_list = list(data_bits+padding)
    while '1' in padded_inp_list[:ip_len]:
        curr_shift = padded_inp_list.index('1')
        for i in range(len(key_bits)):
            padded_inp_list[curr_shift +
                            i] = str(int(key_bits[i] != padded_inp_list[curr_shift+i]))

    return ''.join(padded_inp_list)[ip_len:]


def check_crc(data_bits, key_bits, check_bits):
    key_bits = key_bits.lstrip('0')
    ip_len = len(data_bits)
    padding = check_bits
    padded_inp_list = list(data_bits+padding)
    while '1' in padded_inp_list[:ip_len]:
        curr_shift = padded_inp_list.index('1')
        for i in range(len(key_bits)):
            padded_inp_list[curr_shift +
                            i] = str(int(key_bits[i] != padded_inp_list[curr_shift+i]))

    return('1' not in ''.join(padded_inp_list)[ip_len:])


# print(remainder_crc('100100', '1101', '0'))
# print(check_crc('100101', '1101', '001'))


def crc_Code():
    data = input("\n Enter data: ")
    key = input("\n Enter Key : ")
    remainder = remainder_crc(data, key, '0')
    print("\n Calculated remainder : ", remainder)
    received_data = input("\n Data received at receiver : ")
    print("\n No-Transmission Error : ",
          check_crc(received_data, key, remainder))


crc_Code()
