import string
import random
print("Welcome to the password generator!")


length = int(input("\nEnter password length:"))


lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbol = string.punctuation

all = lower + upper + num + symbol

temp = random.sample(all,length)



password = "".join(temp)



print(password)






