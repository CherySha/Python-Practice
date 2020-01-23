# tuple:內容無法被更改(1,2,3)
# 使用起來像list一樣
# x=('a','b','c')
# 不能賦予值
# x[2]='d'#會錯誤

# 可使用切片、+、* 來取值來建立新的tuple
# print(x[:2])
# print(x+('d','e','f'))
# print(x*3)
# 單一元素要加逗號來跟強制運算式做區分
# print(x+(8+9,))

# 自動打包、解包
# (one,two,three,four)=(1,2,3,4)
# 簡化
# one,two,three,four=1,2,3,4
# print(one)
# print(three)

# 序列型別都能自動解包(list,string)
# v1,v2,v3=[1,2,3]
# print(v1)
# print(v3)
# v1,v2,v3='abc'
# print(v1)
# print(v3)

# 自動打包與解包也用函式的回傳值
# def get_user_info(id):
#     return '09123455', 'Eric','aa@gmail'#回傳時自動打包
# phone,name,email=get_user_info(5)#賦值時自動解包
# print(phone)
# print(name)
# print(email)

# 標有*吸收多餘的元素放入list(無則是空list)
# x=(1,2,3,4)
# a,b,*_=x
# print(a)
# print(b)
# print(_)
# a,b,c,d,*_=x
# print(a)
# print(b)
# print(c)
# print(d)
# print(_)#空list

#list與tuple轉換:產生相同元素的新物件,適用於任何Python序列型別
# x=(1,2,3,4)
# y=list(x)
# y[0]=8
# x=[[5,6],2,3,4]
# y=tuple(x)
# x[0][0]=1
# print(x)
# print(y)
# 也能分解成字元
# x=list('Hello')
# print(x)

# 排序tuple:產生新tuple,因為元素無法更改
# x=(3,4,1,2)
# x=sorted(x)
# print(x)    