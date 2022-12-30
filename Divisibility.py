def divisibility(x , y):
    if x % y == 0:
        return True
    else:
        return False


num = int(input('Input a number: '))
num2 = int(input('Input the second number: '))

if divisibility(num , num2):
    print('Your number is divisible.')
else:
    print('Your number is not divisible.')