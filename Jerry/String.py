# 也是一種序列型別
# x="Hello World"
#字串不能被修改，只能產生新字串
# print(x[0])
# print(x[-1])
# print(x[1:5])#也可切片

# 取字串長度
# print(len(x))

# y="I"+"am"+"superman"
# y="I" "am" "superman"#可省略+號
# y="GG"*5
# print(y)

# 取消print後面自動換行
# print("abc\n",end="")

# 常用函式:字串名稱.method()
# spilt(separatot,max):將字串切割為字串list
# join(target list):將某字串插入字串list各字串間並連接成新字串
# x="I am superman\t\t .\nand\tyou?"
# print(x.split())#預設以空白字元切割
# y="HelloaaaMyaaaLovelyaaaCuteaaaDog"
# print(y.split("aaa",3))
# li=x.split()
# print("---".join(li))
# print("".join(li))
# print(" ".join(li))

# x="this is a test"
# result='-'.join(x.split())
# print(result)

#轉換成數字
# x=int('3333')
# y=float('123.456')
# x2=int('101',2)#2進位
# x8=int('10000',8)#8進位
# x16=int('ff',16)#16進位
# print(x)
# print(y)
# print(x2)
# print(x8)
# print(x16)

# x="  Hello world\t\t"
# # strip():刪除前後空白
# print(x.strip())
# # lstrip():刪除前空白
# print(x.lstrip())
# # rstrip():刪除後空白
# print(x.rstrip())
# # 刪除所有指定字元(僅頭尾部分)
# print(x.strip(" Hd\t"))

# x="(name,, date),,\n"
# print(x.rstrip("\n,)("))

# 檢查字串特徵
# # isdigit():是否由數字組成
# x="123"
# print(x.isdigit())
# # isalpha():是否由英文字母組成
# print(x.isalpha())
# # islower():是否全部小寫
# y="MM"
# print(y.islower())
# # isupper():是否全部小寫
# print(y.isupper())

# 檢查字串內容
# x="Hello world"
# print("ello" in x)
# print("o w" in x)
# print("hel" in x)

# 搜尋文字索引位置
# find(string,start,end)
# rfind(string,start,end):反過來找
# x="Hello world"
# print(x.find("llo"))
# print(x.find("zzz"))
# print(x.find("o",5,8))
# print(x.rfind("o"))
# # index()
# print(x.index("llo"))
# # print(x.index("zzz"))#exception
# print(x.rindex("o"))
# 另一種更強的搜尋字串方式:re模組:使用regular expression

# 找特定字串出現幾次
# count()
# x="Hello\t"*3
# print(x.count("Hello"))

# 檢查頭尾是否符合特定文字
# startswith()
# endswith()
# x="aaaHellobbb"
# print(x.startswith("aaa"))
# print(x.startswith("c"))
# print(x.endswith("bbb"))
# print(x.endswith("c"))
# # 傳入tuple可搜尋多筆，只要有任一符合就是True
# print(x.endswith(("c","bbb")))

# 字串替換:產生新字串
# x="Hello world"
# y=x.replace("llo","KKK")
# print(y)
# re模組提供更強大的替換方式

# 一次多替換多字串:maketrans()+translate()
# x="AAABBBCCCDDD"
# table=x.maketrans("ABCD","QWER")
# print(x.translate(table))

# 多個修改字串的method:
# # 全部轉換小寫
# x="BSKOE"
# print(x.lower())
# # 全部轉換大寫
# x="jaskl"
# print(x.upper())
# # 第一個字元改大寫
# x="i am superman"
# print(x.capitalize())
# # 字串所有單字第一個字元改大寫
# x="dahyun kim"
# print(x.title())
# # 大改小 小改大
# x="i AM SUPERMAN"
# print(x.swapcase())
# # 指定空格數量替換tab
# x="I\tam\tsuperman"
# print(x)
# print(x.expandtabs(1))

# 對齊:用途未知
# x="Today is a nice day!"
# print(x.ljust(4))
# print(x.rjust(4))
# print(x.center(4))
# # 數字補0
# x="3"
# print(x.zfill(3))

# 修改原本字串的方法:透過轉成list再轉回來達成
# text="Hello, World"
# wordlist=list(text)
# wordlist[6:]=[]
# wordlist.reverse()
# text="".join(wordlist)
# print(text)

# 將物件轉成字串表示
# 適合除錯
x=[1,2,3,4,[5,6]]
print("this list is:"+repr(x))
print(repr(len))#正式字串表示法,給python讀取的
print(str(len))#非正式字串表示法,給人看得