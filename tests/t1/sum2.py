# copy the code from sum1.py into this file, THEN:
# change your program so it keeps reading numbers until it gets a -1, then prints the sum of all numbers read
y = 0
i = 0
print('So give me as many seperate numbers as you want and I will add them')
print('Give me a -1 to stop me.')
while i < 10:
    num = input("Give me a number: ")
    num = int(num)
    if num == -1:
        print('Ok I will stop')
        i = 2324546768
    else:
     y = y + num
tr = str(y)
print ('Here is the total of all your digits: ' + tr)