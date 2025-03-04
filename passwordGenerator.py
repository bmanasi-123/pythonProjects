import random
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '@', '^', '*']

print("Welcome to PyPassword Generator")
l = int(input("length of your password: "))
n = int(input("How many numeric chars you want in it: "))
s = int(input("How many symbols you want in it: "))
c = l-(n+s)

password=[]
for i in range(0, c):
    password.append(letters[random.randint(0, 26)])
for i in range(0, n):
    password.append(numbers[random.randrange(0, 9)])
for i in range(0, s):
    password.append(symbols[random.randrange(0, 8)])

print('Your Easy password is: '+''.join(password))
random.shuffle(password)
# print(password)
print('Your Hard password is: '+''.join(password))
