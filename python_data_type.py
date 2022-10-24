from msilib import _directories
from operator import truediv


x = "python" # 문자형
x = 123
x = "123"
x = [1, 2, 3, 4]
x = {"name":"lee", "age":34} # 키랑 벨류가 있으면 딕션형태
x = True # 대문자로  True, False를 구분한다

# print(type(x))

# 숫자형 데이터
a = 1 + 1
a = 100 -1
a = 12 * 12
a = 3 / 4
# print(a)

# 문자열 데이터
a = " 하루는 성실하게 \n 인생 전체를 되는대로" # \n 줄바꾸기
# print(a)

a = """ 하루는 성실하게 
인생 전체를 되는대로 """ # 따음표 3개 """ 를 하면 문자의 내용이 그대로 들어감

#print(a)

a = """ "Failure is simply the opportunityt to begin again." he says." """
# b = ` "Failure is simply the opportunityt to begin again." he says." `

# print(a)
# print(b)

a = "A"
b = "B"
# print(a*b)
print (a*100)


# 문자열의 길이를 확인 할때

a = "100"

# print(len(a)) # 문자 전체의 길이를 확인 할때

b = "hello python!"

print(b[0]) # indexing  특정 문자 하나만 지정하는것
print(b[0:4]) # slcng 특정 범위를 지정하는것 0 <= c < 5
print(b[6:13]) 
print(b[6:-1]) # -1은 문자 끝까지 가져와 달라는 의미
print(b[:]) # :은 문자 처음부터 끝까지 다 가져와라는 의미

x = "TitanicJames"
# title = (x[:7]
#  director = (x[7:])

# print(title,director)

# a = ["a", "b", "c", "d", "e"]
a = ["a", "b", ["c", "d", "e"]] # [] 대가로 안에 또 대가로 [] 그래서 2번째가 [] 대가로 전체 임

# print(a[1])
# print(a[2])
# print(a[2][1])

t = ("a", "a", "a", "a")

# print(type(t))

x = {"key1":"valuel", "key2":"value2"}
# print(x["key2"]) # 시각화 할때 많이 쓰임

x = set([1,1,1,2]) # set 집합형 중복을 지워준다
print(x)


