# 縮排及區塊結構:使用Tab來縮排區分區塊
n= 9
r=1
while n>0:
    r*=n
    n-=1
    print(n)

# 註解符號:#

# 變數宣告與指派:一張標籤便利貼，不需宣告型別，可參考各類型物件
# 建立變數x作為物件9的標籤名稱
x=9
print(x)
# Everything is an Object!

# 刪除變數:del敘述
del x
# print(x)

# 運算式:先乘除後加減，使用括號
3/2
# 1.5(整數相除回傳浮點數)
3//2
# 1(傳回商數整數部分)

# 字串:""or''
# 跳脫字元
string1 = "\t:Tab;\n:換行;\\:正常斜線;\":正常雙引號;':單引號不用跳脫"
string2 = '\t:Tab;\n:換行;\\:正常斜線;\':正常雙引號;":雙引號不用跳脫'
# 跨行字串:""" or '''
string3 = """
aaaaa
bbbbb
''單引不用跳脫
""雙引也不用跳脫
"""
# 使用\定異長字串
string4='www'\
		'xxx'\
		'vvv'
# 使用()定義長字串
longstring=(
	"long"
	"string"
	'practice'
)
print(string1)
print(string2)
print(string3)
print(string4)
print(longstring)

# 數字:整數、浮點數、複數和布林值
# 整數相除得浮點數
# 科學記號2e+2 = 2 * 10的2次方、2e-2= 2 * 10的-2次方
# 內建數值函式:型別轉型、max、min、abs等
x=2.0
print(int(x))
# 進階數值函式:math模組提供
# 進階數值計算:NumPy套件提供(陣列計算)
# 複數:3+2j:用j表示虛部
# 進階複數計算:cmath套件

# 取得輸入:input()回傳字串
name=input("Name?")
print(name)
number=int(input("Number?"))
print(number+1.0)