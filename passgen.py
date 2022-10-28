import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*)(_-+=`~.,></?;:|"

while 1:
    passcrack_len = int(input("how long :"))
    passcrack_count = int(input("how many do you want :"))
    for x in range(0,passcrack_count):
        passcrack = ""
        for x in range(0,passcrack_len):
            passcrack_char = random.choice(chars)
            passcrack       = passcrack + passcrack_char
        print("", passcrack)
