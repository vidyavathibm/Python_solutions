# a="this is a string"
# b=a.split(" ")
# print(b)
# c='-'.join(a)
# print(c)
#
# c='-'.join(b)
# print(c)
# x=12
# def fun():
#     global x
#     x=2
#     x=x+2
#     print(x)
#
# fun()

# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
#
# print("fact=",fact(-5))
#
# a,b=1,0
# try:
#     c=a/b
#     print (c)
#
# except:
#     print("there is an exception")
#
# finally:
#     print("finally block")


# str1="aba"
#
# if str==str1[::-1]:
#     print('pal')
# str="abc"
# string=""
# for i in str:
#     string=i+string;
#
# print(string)
#
# list1=['a','b','c']
# list1.pop()
# print(list1)
# list1.remove(list1[0])
# print(list1)


# str="abc"
# string=""
# string="".join(reversed(str))
# print(string)

str="abc"
string=""
j=0
for i in range(len(str)-1,0):
    print(len(str))
    string[j]=str[i]
    j=j+1
print(string)

