# # dict:字典
# ages={"Mary":13,"John":14,"Tom":20}
# print(ages["Mary"])
# print(ages["John"])
# print(ages["Tom"])
# ages["Jim"]=24
# print(ages)

# x=[]
# y={}
# y[0]="Hello"#dict會自動儲存新的key:value配對關係
# y[1]="Goodbye"
# # x[0]='Hello'#list的索引不存在不能賦予值
# print(y[0])
# print(y[1]+", Friend.")
# y["two"]="two"
# y["two"]=2
# y["pi"]=3.14
# print(y["two"]*y["pi"])

# x={}
# name1=input("First one?")
# age1=input("Age?")
# x[name1]=age1
# name2=input("Second one?")
# age2=input("Age?")
# x[name2]=age2
# name3=input("Third one?")
# age3=input("Age?")
# x[name3]=age3
# select=input("Find whose age?")
# print(x[select])

# x={"red":"紅色","blue":"藍色","yellow":"黃色"}
# # 查組數
# print(len(x))
# # 查key組
# print(list(x.keys()))
# # 查value組
# print(list(x.values()))
# # 查所有組(回傳每組為一個tuple)
# print(list(x.items()))
# # del:刪除項目
# del x["blue"]
# print(x)
# # in:檢查項目是否存在
# print("red" in x)
# print("blue" in x)
# # get:找值若無則回傳第二參數值(若無則回傳None)
# print(x.get("red","Not found"))
# print(x.get("blue","Not found"))
# print(x.get("blue"))
# # setdefault:類似get,但會新增key:value(value為第二參數值)
# print(x.setdefault("blue","Not Found"))
# print(x)

# x={"red":"紅色","blue":"藍色","yellow":"黃色"}
# # 淺層複製
# y=x.copy()
# # 使用copy.deepcopy來深層複製
# print(y)
# # update():用其他dict來更新共有key的值;並新增新key:value
# y={"blue":"藍","yellow":"黃","pink":"粉紅"}
# x.update(y)
# print(x)

# x={'a':1,"b":2,"c":3,"d":4}
# y={'a':6,'e':5,'f':6}
# del x['d']
# z= x.setdefault('g',7)
# x.update(y)
# print(x)

# 使用在稀疏矩陣很有效!使用矩陣進行大量運算還是使用Numpy較佳。
# 紀錄矩陣行列值
# x={}
# x[(0,0)]="Y"
# x[(0,1)]="M"
# x[(1,0)]="C"
# x[(1,1)]="A"

# # 可用於快取
# sole_cache={}
# def sole(m,n,t):
#     if(m,n,t) in sole_cache:
#         return sole_cache[(m,n,t)]#將快取裡計算完的值直接傳回
#     else:
#         #計算...
#         result=m*n*t
#         sole_cache[(m,n,t)]=result
#         return result
# print(sole(1,2,3))#算完加到快取dict
# print(sole(1,2,3))#直接讀快取
