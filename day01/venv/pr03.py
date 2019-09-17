# for i in range(10,0,-1):
#     print (i)
# a=int(input("range"))
# b=int(input("range"))


# # a=input("range")
# b = int(input("range"))
# #
# # for i in range(a,b):
# #     print (i)
# sume,sumo=0,0
# for i in range(0,b):
#     if i%2==0:
#         sume+=i
#     else:
#         sumo+=i
# print(sume)
# print(sumo)
#
#
# #
# # for i in range(a,b):
# #     print (i)
#
# for i in range(0,int(input("range"))):
#     print(i);
# #
string = 'WELCOME'
# print(string[-1])
# string[2]='A'
# print(string[2])
#
# for i in string[::-1]:
#      print(i);

# cnt=0;
# for i in string:
#     cnt=cnt+1
# print(cnt)


# cnt=0;
# for i in string:
#     if i=='E':
#         cnt=cnt+1
# print(cnt)


# cnt=0;
# temp=""
# for i in string:
#         temp=temp+i
#         cnt=cnt+1
#         if cnt==3:
#             print(temp)
#
#
# print(string[:3])
# print(string[3:])
#
# name=['A','C','C']
# list1=[]
#

# for i in range(0,10,2):
#     list1.append(i)
# print(list1)
#
# list1=[i for i in range(0,10,2)]
# print(list1)
# #
# name = ['A', 'C', 'C',1,2,3,4]
# cnti=0
# cnts=0
# for i in name:
#     print(type(i))
#     if type(i) is int:
#         cnti=cnti+1
#     else:
#         cnts=cnts+1
# print(cnti,cnts)
#

#
# name = ['A1', 'C', 'CC','1', 1, 2, 3, 4, 6]
# cnti = 0
# cnts = 0
# for i in name:
#     if ord(str(i)) >= 65 and ord(str(i)) <= 90:
#         cnti = cnti + 1
#     else:
#         cnts = cnts + 1
# print(cnti, cnts)
#
# print(isdigit(5))

name = ['A', 'C', 'C','1', 1, 2, 3, 4, 6]
cnti = 0
cnts = 0
for i in name:
    if ord(str(i)) >= 65 and ord(str(i)) <= 90:
        cnti = cnti + 1
    else:
        cnts = cnts + 1
print(cnti, cnts)

