my_list = [0,1,2,3,4,5]
x = int(input('State an number under 5. '))
try:
 x = my_list[x]
 print(x)
except IndexError:
 print("Out of Range")

t = True
while t:
 try:
  y = input ('Write a number for me. ')
  y = float(y)
  t = False
 except ValueError:
  print('I need a numberal please, not ',y)
print(y)