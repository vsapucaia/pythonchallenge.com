input = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
output = ""

for c in input:
    if ord(c) < 97 or ord(c) > 122:
        output += c
    elif ord(c)+2 < 123:
        output += chr(ord(c)+2)
    elif ord(c)+2 == 123:
        output += chr(97)
    elif ord(c) + 2 == 124:
        output += chr(98)

print(output)
print("fim")