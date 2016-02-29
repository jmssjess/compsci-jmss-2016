# write a program that reads in 10 numbers, then prints the sum of those
x = 0
y = 0
print('So give me 10 seperate numbers and I will add them together')
while x < 10:
    num = input("Give me a number: ")
    num = int(num)
    y = y + num
    x = x + 1
tr = str(y)
print ('here is the total of all your digits, ' + tr)
