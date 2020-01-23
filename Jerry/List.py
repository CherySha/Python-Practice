# list:可包含不同型別物件，並會自動調整大小
x=[2,'two',[1,2,3]]

# len():取得list元素個數
# print(len(x))

# 索引
# print(x[0])
# print(x[-2])

# 切片
y=["first","second","third","fourth"]
# print(y[0:3])
# print(y[3:0])
# print(y[:3])#從頭
# print(y[3:])#到尾
z=y[:]#複製一整個list
z[0]="zzz"
# print(z[0])
# print(y[0])
# print(y[int(len(y)/2):])

# 更改元素
# y[1:3]=["one","two","three"]
# y[1:3]=["one"]

# append():將物件加到尾端
# y.append("four")
# extend():將陣列加到尾端
# y.extend(["new1","new2"])
# insert():將物件加入至指定索引(支援負索引)
# y.insert(1,"New Object")
# y.insert(-1,"New Object")
# del:刪除元素
# del y[1]
# del y[:2]
# remove():刪除第一個找到的內容相同之元素
# y.remove("third")
# reverse():反轉排序
y.reverse()

# test=[3,6,7,1,2,10,5]
# test[:0]=test[-3:]
# del test[-3:]

# sort():排序
# test.sort()
# test.sort(reverse=True)

# 自訂排序:
# def compare_num_of_chars(string1): 
#     return len(string1)
# word_list=["Python","is","better","than","C"]
# word_list.sort()
# print(word_list)
# word_list.sort(key=compare_num_of_chars)
# print(word_list)

# sorted():回傳新的排序好的list
# list1=[1,4,10,5]
# list2=sorted(list1)
# list3=sorted(list1,reverse=True)
# print(list1)
# print(list2)
# print(list3)

# def compare_second_of_list(input_list):
#     return input_list[1]
# list1=[2,1,3]
# list2=[2,0,3]
# list3=[2,5,3]
# list4=[list1,list2,list3]
# list4.sort(key=compare_second_of_list)
# print(list4)

# in:測試是否存在
# print(3 in [1,3,4,5])
# print(3 not in [1,3,4,5])

# +:串聯list
# z=[1,3,5]+[7,9]
# print(z)

# *:複製倍數;常用在初始化事前調整好大小
# z=[None]*4
# x=[3,1]*3
# print(z)
# print(x)

# min():找出list內最小的
# print(min([1,2,3,4,5]))
# max():找出list內最大的
# print(max([1,2,3,4,5]))

# index():找出索引值
# x=["Zero","One","Two","Three"]
# print(x.index("One"))

# count():找出在list裡出現幾次
# x=[1,2,2,3,3,3,4,4,4,4]
# print(x.count(1))
# print(x.count(2))
# print(x.count(3))
# print(x.count(4))

# x=len([[1,2]]*3)
# print(x)

# 複製list:x[:];x+[];x*1
# deepcopy():有第二層list時候需要，連第二層的list也複製一份新的，而不是參考原本的
# original=[[0],1]
# shallow=original[:]
# shallow[0][0]=4
# print(original)
# print(shallow)
# import copy
# deep=copy.deepcopy(original)
# deep[0][0]=5
# print(original)
# print(deep)

# x=[[1,2,3],[4,5,6],[7,8,9]]
# import copy
# y=copy.deepcopy(x)
# y[0][1]=9
# print(x)
# print(y)