

def remainder_crc(data_bits, key_bits, pad_bit):
    key_bits = key_bits.lstrip('0')
    ip_len = len(data_bits)
    padding = pad_bit*(len(key_bits)-1)
    padded_ip_list = list(data_bits+padding)
    while '1' in padded_ip_list[:ip_len]:
        curr_shift = padded_ip_list.index('1')
        for i in range(len(key_bits)):
            padded_ip_list[curr_shift +
                           i] = str(int(key_bits[i] != padded_ip_list[curr_shift+i]))

    return ''.join(padded_ip_list)[ip_len:]


def check_crc(data_bits, key_bits, check_bits):
    key_bits = key_bits.lstrip('0')
    ip_len = len(data_bits)
    padding = check_bits
    padded_ip_list = list(data_bits+padding)
    while '1' in padded_ip_list[:ip_len]:
        curr_shift = padded_ip_list.index('1')
        for i in range(len(key_bits)):
            padded_ip_list[curr_shift +
                           i] = str(int(key_bits[i] != padded_ip_list[curr_shift+i]))

    return('1' not in ''.join(padded_ip_list)[ip_len:])


print(remainder_crc('100100', '1101', '0'))
print(check_crc('100101', '1101', '001'))
