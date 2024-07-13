import random

chars="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
length=0
geninput=int(input("length?"))
password=""

for i in range (0, geninput):
	password+=random.choice(chars)

print(password)
