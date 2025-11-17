#Consider int val=0xCAFE; Write expressions using bitwise operators that do the following:
# 1. test if at least three of last four bits (LSB) are on
# 2. reverse the byte order (i.e., produce val=0xFECA)
# 3. rotate four bits (i.e., produce val=0xECAF)

#solution
# 0x is a prefix that indicates hexadecimal (base 16)
# c=12, a=10, f=15, e=14 
# (12*16^3)+(10*16^2)+(15*16^1)+(14*16^0)=  49152+2560+240+14=51966   decimal= 1100 1010 1111 1110

val = 0xCAFE
# print(val)  #output = 51966
nibble = val & 0xF  #(0xF = 15 = 1111(in decimal))  
condition = bin(nibble).count("1") >=3
# print(condition) 
if (condition==1):
    print("at least three of last four bits are ON")
else :
    print("OFF")

#high byte = CA,  low byte = FE
reverse = ((val & 0xFF) << 8) | ((val>>8) & 0xFF)
print(hex(reverse).upper())

rotate = ((val >> 4) | ((val & 0xF) << 12)) & 0xFFFF
print(hex(rotate).upper())