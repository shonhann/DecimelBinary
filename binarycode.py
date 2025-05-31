def decimal_to_binary(decimal, bit_width):
    binary = bin(decimal)
    binary = binary[2:]
    if len(binary) < bit_width:
        binary = binary.zfill(bit_width)
    return binary

def apply_two_complement(binary, bit_width):
    inverted = ''.join('1' if bit == '0' else '0' for bit in binary)
    inverted_decimal = int(inverted, 2) + 1
    result_binary = decimal_to_binary(inverted_decimal, bit_width)
    return result_binary


decimal = int(input("Enter a decimal number: "))

binary = decimal_to_binary(decimal, 4)
print("Positive binary representation:", binary)

negative_binary = apply_two_complement(binary, 4)
print(" two's complement:", negative_binary)
