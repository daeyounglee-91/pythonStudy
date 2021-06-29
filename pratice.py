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

sentence = '나는 소년입니다'
print(sentence)

sentence2 = "파이썬은 쉬워요"
print(sentence2)


sentence3 = """ 
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)