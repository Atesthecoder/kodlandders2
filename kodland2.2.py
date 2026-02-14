import random
print("şifre oluştrucu")
ff = int(input("Kaç karakterli olsun?"))
ss = "+-/*!&$#'?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
parola = ""
for i in range(ff):
    parola += random.choice(ss)
print("oluştrulan şifre:",parola)