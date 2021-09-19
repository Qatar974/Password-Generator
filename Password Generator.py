import random
import string
def GetPassword(data):
    x = 16
    password = "" 
    while len(password)!= x :
        value = random.choice(data)
        password += value
    return password

data ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*()=.,?0123456789'
for i in range(1000):
        print(GetPassword(data))
        

