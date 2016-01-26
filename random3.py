import random
number1=random.randint(1, 10)

number2=random.randint(1, 10)


result = eval(input('what is ' + str(number1) + '+' + str(number2) + '?'))

if result== (number1 + number2):
    print('the answer is right')
else:
    print('the answer is wrong')

