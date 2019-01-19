# a=int(input('enter value of a:'))
# b=int(input('enter value of b:'))
# temp=a##giving value of a to temp
# a=b##giving value of b to a
# b=temp##giving value of temp to b
#
# # a,b=b,a
# print(a,b)
#
# a,b=b,a
#

year=int(input("Enter year to be checked:"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("The year is a leap year!")
else:
    print("The year isn't a leap year!")