num = [255, 16, 0, -42]

hex_ditits = '0123456789ABCDEF'
for i in num:
    if i == 0:
        hex_str ='0'
    else:
        neg = i < 0
        if neg:
            i = -i
    hex_str = ''
    while i > 0:
        r = i % 16
        hex_str = hex_ditits[r] + hex_str
        i //= 16
    if neg:
        hex_str = '-' + hex_str
print(hex_str)