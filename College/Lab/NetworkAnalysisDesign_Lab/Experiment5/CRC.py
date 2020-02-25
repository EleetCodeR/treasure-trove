

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


# 1010011101100 000 <--- input right padded by 3 bits
# 1011               <--- divisor
# 01100011101100 000 <--- result (note the first four bits are the XOR with the divisor beneath, the rest of the bits are unchanged)
#  1011              <--- divisor ...
# 00111011101100 000
#   1011
# 00010111101100 000
#    1011
# 00000001101100 000 <--- note that the divisor moves over to align with the next 1 in the dividend (since quotient for that step was zero)
#        1011             (in other words, it doesn't necessarily move one bit per iteration)
# 00000000110100 000
#         1011
# 00000000011000 000
#          1011
# 00000000001110 000
#           1011
# 00000000000101 000
#            101 1
# -----------------
# 00000000000000 100 <--- remainder (3 bits).  Division algorithm stops here as dividend is equal to zero.
