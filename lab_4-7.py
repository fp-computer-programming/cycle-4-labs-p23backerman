#asks the user to give us 5 numbers
print('give us the first number')
a = int(input())
print('give us the second number')
b = int(input())
print('give us the third number')
c = int(input())
print('give us the foruth number')
d = int(input())
print('give us the fifth number')
e = int(input())
#puts 
f = '{0}{1}{2}{3}{4}'.format(a, b, c, d, e)
print(f)

if a > b and a > c and a > d and a > e:
    print("{0} is the greatest number".format(a)) 
    Greatest = a
if a < b and a < c and a < d and a < e:
    print("{0} is the lowest number".format(a)) 
    Lowest = a
if b < a and b < c and b < d and b < e:
    print('{0} is the lowest number'.format(b))
    Lowest = b
if b > a and b > c and b > d and b > e:
    print("{0} is the greatest number".format(b))
    Greatest = b

if c > a and c > b and c > d and c > e:
    print("{0} is the greatest number".format(c)) 
    Greatest = c
if c < a and c < b and c < d and c < e:
    print('{0} is the lowest number'.format(c))
    Lowest = c
if d > a and d > b and d > c and d > e:
    print("{0} is the greatest number".format(d)) 
    Lowest = d
if d < a and d < b and d < c and d < e:
    print('{0} is the lowest number'.format(d))
    Greatest = d
if e< a and e < b and e < c and e < d:
    print('{0} is the lowest number'.format(e))
    Lowest = e
if e> a and e > b and e > c and e > d:
    print("{0} is the greatest number".format(e)) 
    Greatest = e

Product = int(Greatest) * int(Lowest) 
print("{0} is the product of the greatest and lowest number".format(Product))