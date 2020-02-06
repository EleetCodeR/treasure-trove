# PRIMITIVE TYPES.

# BOOT CAMP:

# Shifting and Masking


def count_bits(x=int):
    num_bits = 0
    while x:
        num_bits += x & 1
        # x = x >> 1
        x >>= 1
    return num_bits


x = 10
print(f"Number of bits in {x} is {count_bits(x)} ")

# 1


def parity(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result
