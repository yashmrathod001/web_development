num = [9,8,7,6,5,4,3,2,1];
min = num[0];
max = num[0];


def swip(num1,num2):
    num1 = num2-num1
    num2 = num2-num1
    num1 = num2 - num1
    print(num1,num2)

swip(10,2)

