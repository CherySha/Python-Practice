temperatures=[]
with open('lab_05.txt') as infile:
    for row in infile:
        temperatures.append(float(row.strip()))

# 最高溫度
print(max(temperatures))
# 最低溫度
print(min(temperatures))
# 平均溫度
sum_=sum(temperatures)//len(temperatures)
print(sum_)
# 溫度中位數
temperatures.sort()
print(temperatures[len(temperatures)//2])
# 有多少個不同的值
temperatures_set=set(temperatures)
print(len(temperatures_set))