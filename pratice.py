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

# python = "Python is Amazing"

# print(python)
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python", "Java"))

# index = python.index("n")
# print(index)
# index = python.index("n",index + 1)
# print(index)

# print(python.find("n"))
# # print(python.index("Java"))   #Error
# print(python.count("n"))

# # 방법1
# print("나는 %d살 입니다" % 20)
# print("나는 %s을 좋아해요" % "파이썬")
# print("Apple 은 %c로 시작해요" % "A")


# print("나는 %s살 입니다" % 20)
# print("나는 %s을 좋아해요" % "파이썬")
# print("Apple 은 %s로 시작해요" % "A")

# print("나는 %s색과 %s색을 좋아해요" % ("파란","빨간"))

# # 방법2
# print("나는 {}살 입니다".format(20))
# print("나는 {}색과 {}색을 좋아해요".format("파란","빨간"))
# print("나는 {0}색과 {1}색을 좋아해요".format("파란","빨간"))
# print("나는 {1}색과 {0}색을 좋아해요".format("파란","빨간"))

# # 방법3
# print("나는 {age}살이며 {color}색을 좋아해요".format(age = 20, color = "빨간"))
# print("나는 {age}살이며 {color}색을 좋아해요".format(color = "빨간", age = 20))


# # 방법4(v3.6 이상~)
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며 {color}색을 좋아해요")

# print("백문이 불여일견 \n백견이 불여일타")
# print('저는 "나도코딩" 입니다.')
# print("저는 \"나도코딩\" 입니다.")
# print("D:\\Git\\study\\pythonStudy>")

# print("Red Apple\rPine")    #\r : 커서 맨앞으로
# print("Redd\b Apple")      #\b : 한글자 삭제
# print("Red\t Apple")

# '''
# Quiz
# 사이트별 비밀번호 생성
# ex) http://naver.com
# 규칙1 : http:// 제외
# 규칙2 : 처음 만나는 점(.) 이후 부분 제외
# 규칙3 : 남은 글자중 처음 세자리 + 글자 갯수 + 글자내 'e' 갯수 + '!' 로 구성
#                 (nav)               (5)         (1)
# 생상된 비밀번호 : nav51!
# '''
# # my answer
# url = "http://naver.com"
# url = url.replace("http://","")
# url = url.split(".")
# pw = url[0][0:3] + str(len(url[0])) + str(url[0].count("e")) + "!"
# print(pw)

# # answer
# url = "http://naver.com"
# my_str = url.replace("http://","")
# # print(my_str)
# my_str = my_str[:my_str.index(".")]
# # print(my_str)
# pw = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print(f"{url}의 비밀번호는 {pw} 입니다.")

# # 리스트
# subway = [10,20,30]
# print(subway)

# subway = ["유재석","박명수","조세호"]
# print(subway)

# #조세호가 어디에 타고있는가
# print(subway.index("조세호"))

# subway.append("하하")
# print(subway)

# subway.insert(1,"정형돈")
# print(subway)

# print(subway.pop())
# print(subway)

# # 같은 이름이 몇명있는지 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# num_list = [5,2,3,4,1]
# num_list.sort()
# print(num_list)

# # 뒤집기
# num_list.reverse()
# print(num_list)

# num_list.clear()
# print(num_list)

# # 다양한 자료형 함께 사용
# mix_list = ["유재석", 5, True]
# print(mix_list)

# # 리스트 확장
# mix_list.extend(subway)
# print(mix_list)

# # 사전
# # 변수 = {key:value}
# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# # print(cabinet[5])   # Error
# print(cabinet.get(5))   # None
# print(cabinet.get(5, "사용 가능")) 

# print(3 in cabinet)     #True
# print(5 in cabinet)     #False

# cabinet = {"A-3":"유재석", "B-100":"김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# print(cabinet)
# cabinet["A-3"] = "김종국"
# cabinet["C-20"] = "조세호"
# print(cabinet)

# del cabinet["A-3"]
# print(cabinet)

# print(cabinet.keys())
# print(cabinet.values())
# print(cabinet.items())

# cabinet.clear()
# print(cabinet)

# #튜플
# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# # menu.add("생선까스") # Error (add 할수 없음)

# # name = "김종국"
# # age = 20
# # hobby = "코딩"
# # print(name, age, hobby)

# (name, age, hobby) = ("김종국", 10, "코딩") # name, age, hobby = "김종국", 10, "코딩"
# print(name, age, hobby)

# # 집합 (set)
# # 중복 안됨, 순서 없음
# my_set = {1,2,3,3,3}
# print(my_set)

# java = {"유재석","김태호","양세형"}
# python = set(["유재석","박명수"])

# # 교집합
# print(java & python)
# print(java.intersection(python))

# # 합집랍
# print(java | python)
# print(java.union(python))

# # 차집합
# print(java - python)
# print(java.difference(python))

# python.add("김태호")
# print(python)

# java.remove("김태호")
# print(java)


# # 자료구조의 변경
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))

# # 퀴즈 4
# '''
# Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복은 불가
# 조건3 : random 모듈의 shuffle 과 sample 을 활용

# (출력 예제)
#  -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
#  -- 축하합니다 --
#  '''
# from random import *

# users = range(1,21)
# users = list(users)
# shuffle(users)
# winners = sample(users, 4)

# print("-- 당첨자 발표 --")
# print("치킨 당첨자 : {0}".format(winners[0]))
# print("커피 당첨자 : {0}".format(winners[1:]))
# print("-- 축하합니다 --")
############################################################################################
# 문법
# if
# weather = "비"
# weather = input("오늘날씨는 어때요? ")

# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물이 필요없어요")


# temp = int(input("오늘 기온은 어때요? "))

# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp and temp < 30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지 마세요")

# for
# for num in [0,1,2,3,4]:
# for num in range(5):
#     print("대기번호 : {0}".format(num))

# starbucks = ["아이언맨","토르","그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다".format(customer))

# while
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비되었습니다 {1}번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분 되었습니다.")

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비되었습니다 호출 {1}회".format(customer, index))
#     index += 1


# customer = "토르"
# person = "Unkown"

# while person != customer:
#     print("{0}, 커피가 준비되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요? ")

# absent = [2, 5]
# no_book = [7]
# for student in range(1,11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지 {0}은 교무실로 따라와".format(student))
#         break
#     print("{0}, 책을 읽어봐".format(student))

# 한줄 for

# students = [1,2,3,4,5]
# print(students)

# students = [i + 100 for i in students]
# print(students)

# students = ["Iron man","Thor","Groot"]
# students = [len(i) for i in students]
# print(students)

# students = ["Iron man","Thor","Groot"]
# students = [i.upper() for i in students]
# print(students)

# '''
# Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

# (출력문 예제)
# [O] 1번째 손님 (소요시간 : 15분)
# [  ] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 5분) 
# ...
# [  ] 50번째 손님 (소요시간 : 16분) 

# 총 탑승 승객 : 2 분
# '''
# from random import *
# count = 0
# for customer in range(1,51):
#     time = randrange(5,51)
#     if 5 <= time <= 15:
#         count += 1
#         print("[O] {0}번쨰 손님 (소요시간 : {1}분) ".format(customer, time))
#     else:
#         print("[ ] {0}번쨰 손님 (소요시간 : {1}분) ".format(customer, time))

# print("총 탑승 승객 : {0} 분".format(count))

# # 함수

# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# def deposit(balance, money):
#     print("입금이 확인되었습니다. 잔액은 {0}원 입니다.".format(balance+money))
#     return balance+money

# def withdraw(balance, money):
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance - money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))
#         return balance

# def withdraw_night(balance, money):
#     commission = 100
#     return commission, balance - money - commission

# balance = 0
# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 2000)
# # balance = withdraw(balance, 500)
# commission, balance = withdraw_night(balance, 500)
# print("수수로 {0}원이며, 잔액은 {1}원 입니다.".format(commission,balance))

# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}\t"\
#         .format(name, age, main_lang))

# profile("유재석",20,"python")
# profile("김태호",25,"java")

# 같은 학교, 같은 학년, 같은 반, 같은 수업

# def profile(name, age = 17, main_lang = "python"):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}\t"\
#         .format(name, age, main_lang))

# profile("유재석")
# profile("김태호")

# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}\t"\
#         .format(name, age, main_lang))

# profile("유재석",main_lang="python", age=20)
# profile(main_lang="java", age=25, name="김태호")

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t"\
#         .format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

# profile("유재석",20,"python","java","C","C++","C#")
# profile("김태호",23,"kotlin","swift","","","")
# def profile(name, age, *lang):
#     print("이름 : {0}\t나이 : {1}\t"\
#         .format(name, age), end=" ")
#     for i in lang:
#         print(i, end=" ")
#     print()

# profile("유재석",20,"python","java","C","C++","C#")
# profile("김태호",23,"kotlin","swift")
# profile("김종국",22,"python","java","C","C++","C#", "javascript")

# gun = 10

# def checkpoiunt(soldiers):
#     global gun  # 전역 변수 사용
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
    
# def checkpoiunt_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun

# print("전체 총 : {0}".format(gun))
# # checkpoiunt(2)
# gun = checkpoiunt_ret(gun,2)
# print("남은 총 : {0}".format(gun))

'''
Quiz) 표준 체중을 구하는 프로그램을 작성하시오
* 표준 체중 : 각 개인의 키에 적당한 체중

(성별에 따른 공식)

 남자 : 키(m) * 키(m) * 22
 여자 : 키(m) * 키(m) * 21

조건1 : 표준 체중은 별도의 함수 내에서 계산
        * 함수명 : std_weight 
        * 전달값 : 키(height), 성별(gender)
조건2 : 표준 체중은 소수점 둘째자리까지 표시

(출력 예제)
키 175cm 남자의 표준 체중은 67.38kg 입니다.
'''

def std_weight(height, gender):
    if gender == "남자":
        return height*height*22
    else:
        return height*height*21

height = 175
gender = "남자"
weight = round(std_weight(height / 100, gender),2)

print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))