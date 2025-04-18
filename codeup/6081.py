
hex_input = input().strip()


decimal_value = int(hex_input, 16)

for i in range(1, 16):
    result = decimal_value * i

    print(f"{hex_input}*{hex(i)[2:].upper()}={hex(result)[2:].upper()}")
