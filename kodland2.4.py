hjy = []
import random

import time
import sys
kelime = random.randint(1,100)
for i in range(5):
    
    hjy.append(int(input("Sayı:")))
    
    if kelime in hjy:
        print("sayıyı buldunuz!!!")
        print("Kazandın!!!")
        time.sleep(15)
        sys.exit()
        
    else:
        print("sayıyı bulamadınız")
print("kaybettiniz sayı:",kelime)
time.sleep(15)
sys.exit()
