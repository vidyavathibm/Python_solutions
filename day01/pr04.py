# list1=['a','c','e',121,123,3.23]
# for i in list1:
#     print(i)
# list1.insert(2,'K');
#
# list1.insert('c','K');
# # print(list1)
# dict1={}
# # list1=['Five',5,'Six',6,'Seven',7,'Seven',7,'Nine',9]
# # for i in range(0,len(list1)):
# #     for j in range(0, len(list1),2):
# #         key=list1[i]
# #         dict[key]=list1[j]
# # print(dict)
#
# list1=[]
# list2=[]
# list=['Five',5,'Six',6,'Seven',7,'Seven',7,'Seven',8,'Nine',9]
#
# for i in range(0,len(list),2):
#     dict1[list[i]]=list[i+1]
# print(dict1)

# for i in list[::2]:
#     list1.append(i)
# print(list1)
# for i in list[1::2]:
#     list2.append(i)
# print(list2)
# for i in range(len(list1)):
#     for j in range(len(list2)):
#         if i==j:
#             if list1[i] not in dict:
#                 dict[list1[i]]=list2[j]
#             else:
#                 li=[dict[list1[i]],list2[j]]
#                 dict[list1[i]]=li
# print(dict)
#
# for i in range(len(list)):
#     if i%2==0:
#         list1.append(list[i])
#     else:
#         list2.append(list[i])
# print(list1,list2)
# #
# for i in range(len(list1)):
#     for j in range(len(list2)):
#         if i==j:
#             if list1[i] not in dict:
#                 dict[list1[i]]=list2[j]
#             else:
#                 li=[dict[list1[i]],list2[j]]
#                 dict[list1[i]]=li
# print(dict)

#
# for i in range(len(list1)):
#             if list1[i] not in dict:
#                 dict[list1[i]]=list2[i]
#             else:
#                 li=[dict[list1[i]],list2[i]]
#                 dict[list1[i]]=li
# print(dict)

#extracting digits
# string2=''
# string='di2727hjfa3890'
# for i in string:
#     if i.isdigit():
#         string2=string2+str(i)
# print(string2)

#sum of digits of a string
# string2=0
# string='di2727hjfa3890'
# for i in string:
#     if i.isdigit():
#         string2=string2+int(i)
# print(string2)
sum=0
string2=""
string='di2727hjfa3890'
# for i in string:
#     if i.isdigit():
#         string2=string2+str(i)
# print(string2)
#
# for i in range(0,len(string)-1):
#    # if type(string(i))!=type(string(i+1)):
#         if string[i].isdigit():
#             if string[i+1].isdigit():
#                 string2=string2+string[i]
#                # sum = sum + int(i)
#             else:
#                 string2 = string2 + string[i]
#                 sum = sum + int(string2)
#                # string2 = ""
# print(sum)
# a="dad"
# b="add"
# print(sorted(a))
# cnt=0
# string="were eyes were blazing bright."
# list=string.split(" ")
# print(len(list))

list2=[]
dict1={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'minus':'-','plus':'+','divide':'/'}
list1=['five plus three','seven minus two','two plus eight minus five','eight divide four']
for i in range(1,len(list1)):
    l=list1[i].split(" ")
    for w in l:
      print(w)
      if w in dict1:
          list2[i]=dict1[w]
          print(list2[i])

