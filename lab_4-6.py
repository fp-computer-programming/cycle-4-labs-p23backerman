print('Write down an animal')
animal = input()
print('Write down a dish')
dish = input()
a = dish[0:1]
b = animal[0:1]
if a is b:
    print('the beast can carry the dish')
else:
    print('The beast can not carry the dish')