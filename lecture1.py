print("Percentage of sick among the tested (0~100): ", end="")
str1 = input()
num1 = int(str1)
print("Test sensitivity (0~100): ", end="")
str2 = input()
num2 = int(str2)
print("Test sensitivity (0~100): ", end="")
str3 = input()
num3 = int(str3)

a=(num1/100)*(num2/100)
b=((100-num1)/100)*((100-num3)/100)
c=a/(a+b)
final_c = c*100
print(f'Among those that tested positive,{final_c:6.2f}% are true positive.')

