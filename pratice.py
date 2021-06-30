# https://www.youtube.com/watch?v=kWiCuklohdY&ab_channel=%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9
# print(5)
# print(-10)
# print(3.14)
# print(1000)
# print(5 + 3)
# print(2 * 8)
# print(3*(3+1))

# print('풍선')
# print("나비")
# print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
# print("ㅋ"*9)

# # 참 / 거짓
# print(5 > 10)
# print(5 < 10)
# print(True)
# print(False)
# print(not True)
# print(not False)
# print(not (5 > 10))

# #애완동물을 소개해주세요
# name = "연탄이"
# animal = "강아지"
# age = 4
# hobby = "산책"
# is_adult = age >=3

# print("우리집" + animal + "의 이름은 " + name + "에요")
# #print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
# print(name , "는 " ,age, "살이며, " , hobby , "을 아주 좋아해요")
# print(name + "는 어른일까요? " + str(is_adult))

# '''
# 이러면 여러줄의
# 주석을 할수있음
# '''
# station = "사당"
# print(station,"행 열차가 들어오고 있습니다.")

# station = "신도림"
# print(station,"행 열차가 들어오고 있습니다.")

# station = "인천공항"
# print(station,"행 열차가 들어오고 있습니다.")


# #연산자

# print(1+1)
# print(3-2)
# print(5*2)
# print(6/3)

# print(2**3) #2^3
# print(5%3)
# print(10%3)
# print(5//3) #몫구하기

# print(5//3) #몫구하기


# print(abs(-5))  #5
# print(pow(4,2))  #16
# print(max(5,12))  #12
# print(min(5,12))  #5
# print(round(3.14))  #3(반올림)

# from math import *
# print(floor(4.99)) #내림
# print(ceil(4.99)) #올림
# print(sqrt(16)) #루트

# from random import *

# print(random()) #0.0 ~ 1.0 사이에 임의의 값 생성
# print(int(random()*10)) #int casting
# print(randrange(1,46)) # 1~46미만의 임의의 값 생성
# print(randint(1,45)) # 1~45이하의 임의의 값 생성



#예제
# from random import *
# print("오프라인 스터디 모임 날짜는 매월" , randint(4,28),"일로 선정되었습니다.")

# sentence = '나는 소년입니다'
# print(sentence)

# sentence2 = "파이썬은 쉬워요"
# print(sentence2)


# sentence3 = """ 
# 나는 소년이고,
# 파이썬은 쉬워요
# """
# print(sentence3)

python = "Python is Amazing"

print(python)
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n",index + 1)
print(index)

print(python.find("n"))
# print(python.index("Java"))   #Error
print(python.count("n"))

# 방법1
print("나는 %d살 입니다" % 20)
print("나는 %s을 좋아해요" % "파이썬")
print("Apple 은 %c로 시작해요" % "A")


print("나는 %s살 입니다" % 20)
print("나는 %s을 좋아해요" % "파이썬")
print("Apple 은 %s로 시작해요" % "A")

print("나는 %s색과 %s색을 좋아해요" % ("파란","빨간"))

# 방법2
print("나는 {}살 입니다".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파란","빨간"))
print("나는 {0}색과 {1}색을 좋아해요".format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아해요".format("파란","빨간"))

# 방법3
print("나는 {age}살이며 {color}색을 좋아해요".format(age = 20, color = "빨간"))
print("나는 {age}살이며 {color}색을 좋아해요".format(color = "빨간", age = 20))


# 방법4(v3.6 이상~)
age = 20
color = "빨간"
print(f"나는 {age}살이며 {color}색을 좋아해요")

print("백문이 불여일견 \n백견이 불여일타")
print('저는 "나도코딩" 입니다.')
print("저는 \"나도코딩\" 입니다.")
print("D:\\Git\\study\\pythonStudy>")

print("Red Apple\rPine")    #\r : 커서 맨앞으로
print("Redd\b Apple")      #\b : 한글자 삭제
print("Red\t Apple")

'''
Quiz
사이트별 비밀번호 생성
ex) http://naver.com
규칙1 : http:// 제외
규칙2 : 처음 만나는 점(.) 이후 부분 제외
규칙3 : 남은 글자중 처음 세자리 + 글자 갯수 + 글자내 'e' 갯수 + '!' 로 구성
                (nav)               (5)         (1)
생상된 비밀번호 : nav51!
'''
# my answer
url = "http://naver.com"
url = url.replace("http://","")
url = url.split(".")
pw = url[0][0:3] + str(len(url[0])) + str(url[0].count("e")) + "!"
print(pw)

# answer
url = "http://naver.com"
my_str = url.replace("http://","")
# print(my_str)
my_str = my_str[:my_str.index(".")]
# print(my_str)
pw = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print(f"{url}의 비밀번호는 {pw} 입니다.")