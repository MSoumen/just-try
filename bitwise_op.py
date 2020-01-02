a=10
b=9
# 1's compliment
print(bin(a))
print(bin(~a))
print(~a)
print()

# Bit-Wise AND
print(bin(a))
print(bin(b))
print(bin(a & b))
print(a & b)
print()

# Bit-wise OR
print(bin(a))
print(bin(b))
print(bin(a | b))
print(a | b)
print()

# Bit-wise X-OR
print(bin(10))
print(bin(11))
print(bin(10 ^ 11))
print(10 ^ 11)
print()

# Left-shift operator
print(bin(a))
print(bin(a << 3))
print(a << 3) # here leftShift works as "Number << no_of_bit_will_shifted"
print()

# Right_shift operator
print(bin(a))
print(bin(a >> 3))
print(a >> 3) # here Right_Shift works as "Number << no_of_bit_will_shifted"
print()
