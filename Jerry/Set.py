#set:無順序,元素不重複,保持各元素唯一性,元素不可變(list,dict,set不行)
# x={1,2,3,1,2,3,1,2,3}
# print(x)

# 轉換成set
# x=set([1,2,3,1,2,3,3,2,1])
# x=set((2,2,2,2,2,2))
# print(x)

# add():添加元素
# x={1,2,3}
# x.add(4)
# print(x)

# remove():刪除元素
# x={1,2,3}
# x.remove(3)
# print(x)

# 關鍵字in:檢查有無某元素
# x={1,2,3}
# print(3 in x)
# print(4 in x)

# x={1,2,3,4}
# y={3,4,5,6}
#聯集OR
# print(x|y)
# 交集AND
# print(x&y)
# 對稱差XOR
# print(x^y)

# frozenset:不可變更的set
# x={1,2,3,4}
# z=frozenset(x)
# z.add(5)#錯誤:不可變更
# x.add(z)#frozenset可當作set的元素
# print(x)

