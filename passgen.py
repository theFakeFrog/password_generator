import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*)(_-+=`~.,></?;:"

while 1:
    pass_len = int(input("how long :"))
    pass_count = int(input("how many do you want :"))
    for x in range(0,pass_count):
        passw = ""
        for x in range(0,pass_len):
            pass_char = random.choice(chars)
            passw = passw + pass_char
        print("", passw)
