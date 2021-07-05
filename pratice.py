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

# def std_weight(height, gender):
#     if gender == "남자":
#         return height*height*22
#     else:
#         return height*height*21

# height = 175
# gender = "남자"
# weight = round(std_weight(height / 100, gender),2)

# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))

# 표준 입출력

# print("python", "java", sep = ",", end = "?")
# print("무엇이 더 재미있을까요?")

# import sys
# print("python", "java", file =sys.stdout)
# print("python", "java", file =sys.stderr)

# scores = {"수학":0, "영어":50,"코딩":100}
# for subject, score in scores.items():
#     print(subject.ljust(8), str(score).rjust(4), sep=":")  #왼쪽으로 정렬(8자리의 공간 확보후)

# for num in range(1,21):
#     print("대기번호 : " + str(num).zfill(3))

# answer = input("아무 값이나 입력하세요 : ")
# print(type(answer))
# print("입력하신 값은 " + answer + "입니다")

# 출력 포멧
# print("{0: >10}".format(500))
# print("{0: >10}".format(-500))
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))

# print("{0:_<+10}".format(500))

# print("{0:,}".format(100000000000000))
# print("{0:+,}".format(100000000000000))
# print("{0:+,}".format(-100000000000000))
# print("{0:^<+30,}".format(100000000000000))

# print("{0:f}".format(5/3))
# print("{0:.2f}".format(5/3))

# 파일 입충력
# scor_file = open("score.txt","w",encoding="utf8") #write
# print("수학 : 0",file=scor_file)
# print("영어 : 50",file=scor_file)
# scor_file.close()

# scor_file = open("score.txt","a",encoding="utf8")   # append
# scor_file.write("과학 : 80")
# scor_file.write("\n코딩 : 80")
# scor_file.close()

# scor_file = open("score.txt","r",encoding="utf8")   # read
# print(scor_file.read())
# scor_file.close()

# scor_file = open("score.txt","r",encoding="utf8")   # read
# print(scor_file.readline(),end="") # 한줄 읽고 커서 다음줄
# print(scor_file.readline(),end="")
# print(scor_file.readline(),end="")
# print(scor_file.readline(),end="")
# scor_file.close()

# scor_file = open("score.txt","r",encoding="utf8")   # read
# while True:
#     line = scor_file.readline();
#     if not line:
#         break
#     print(line,end="") 
# scor_file.close()

# score_file = open("score.txt","r",encoding="utf8")
# lines =  score_file.readlines()
# for line in lines:
#     print(line,end="") 
# score_file.close()

# pickle

# import pickle
# profile_file = open("profile.pickle","wb")  # wb의 b는 바이너리
# profile = {"이름": "박명수", "나이":30, "취미":["축구","골프","야구"]}
# print(profile)

# pickle.dump(profile, profile_file)
# profile_file.close()

# profile_file = open("profile.pickle","rb")
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()

# with open("profile.pickle","rb") as profile_file:   # file close 자동으로 함
#     print(pickle.load(profile_file))

# with open("study.txt","w",encoding="utf8") as study_file:
#     study_file.write("파이썬을 공부하고 있어요")

# with open("study.txt","r",encoding="utf8") as study_file:
#     print(study_file.read())

# Quiz 7
'''
Quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
보고서는 항상 아래와 같은 형태로 출력되어야 합니다.
 
- X 주차 주간보고 -
부서 : 
이름 : 
업무 요약 : 

1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.
조건 : 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만듭니다.
'''

# for i in range(1,51):
#     with open(str(i) + "주차.txt", "w",encoding="utf8") as report_file:
#         report_file.write("- {0} 주차 주간보고 -".format(i))
#         report_file.write("\n부서 :")
#         report_file.write("\n이름 :")
#         report_file.write("\n업무 요약 :")

# name = "마린"
# hp = 40
# damage = 5
# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp,damage))

# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35
# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp,tank_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
#         .format(name,location,damage))

# attack(name,"1시",damage)
# attack(tank_name,"12시",tank_damage)

# class Unit:
#     def __init__(self, name, hp, damage):       # 생성자
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp,self.damage))

# # marine1 = Unit("마린",40,5)
# # marine2 = Unit("마린",40,5)
# # tank = Unit("텡크",150,35)

# # wraith1 = Unit("레이스",80,5)
# # print("유닛 이름 : {0}, 공격력 {1}".format(wraith1.name,wraith1.damage))

# # wraith2 = Unit("빼맛은 레이스",80,5)
# # wraith2.clocking = True

# # if wraith2.clocking == True:
# #     print("{0} 은 현재 클로킹 상태입니다.".format(wraith2.name))

    
# class AttackUnit:
#     def __init__(self, name, hp, damage):       # 생성자
#         self.name = name
#         self.hp = hp
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
#             .format(self.name,location,self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name,self.hp))

#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# firebat1 = AttackUnit("파이어 뱃", 50, 16)
# firebat1.attack("5시")
# firebat1.damaged(25)
# firebat1.damaged(25)

# 상속

# class Unit:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp

    
# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self,name,hp)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
#             .format(self.name,location,self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name,self.hp))

#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# firebat1 = AttackUnit("파이어 뱃", 50, 16)
# firebat1.attack("5시")
# firebat1.damaged(25)
# firebat1.damaged(25)

# 다중 상속

# from random import *

# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print("{0} 유닛이 생성되었습니다".format(name))

#     def move(self, location):
#         print("[지상유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
#             .format(self.name,location,self.speed))
    
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name,self.hp))

#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))
 
# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self,name,hp,speed)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
#             .format(self.name,location,self.damage))

# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 오로 닐이깁ㄴ;디. [속도 {2}]"\
#             .format(self.name,location,self.flying_speed))

# class FlyableAttackUnit(AttackUnit,Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0,damage)
#         Flyable.__init__(self,flying_speed)

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 오로 날아갑니다. [속도 {2}]"\
#             .format(self.name,location,self.flying_speed))
            
#     def move(self, location):
#         print("[공중유닛 이동]")
#         self.fly(self.name, location)

# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self, "마린",40,1,5)

#     def stimpack(self):
#         if self.hp > 10:
#             self.hp -= 10
#             print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
#         else:
#             print("{0} : 체력이 부족하여 스팀팩을 사용할수 없습니다.".format(self.name))

# class Tank(AttackUnit):
#     seize_developed = False
#     def __init__(self):
#         AttackUnit.__init__(self, "탱크",150,1,35)
#         self.seize_mode = False

#     def set_seize_mode(self):
#         if Tank.seize_developed == False:
#             return
        
#         if self.seize_mode == False:
#             print("{0} : 시즈모드로 전환 합니다.".format(self.name))
#             self.damage *= 2
#             self.seize_mode = True
#         else:
#             print("{0} : 시즈모드를 헤제 합니다.".format(self.name))
#             self.damage /= 2
#             self.seize_mode = False

# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self,"탱크",80,20,5)
#         self.clocked = False

#     def clocking(self):
#         if self.clocked == True:
#             print("{0} : 클로킹 모드를 헤제 합니다.".format(self.name))
#             self.clocked = False
#         else:
#             print("{0} : 클로킹 모드 설정합니다.".format(self.name))
#             self.clocked = True

# # vulture = AttackUnit("벌쳐",80,10,20)
# # battlecruiser = FlyableAttackUnit("배틀크루져",500,25,3)

# # vulture.move("11시")
# # battlecruiser.fly(battlecruiser.name, "9시")
# # battlecruiser.move("7시")
# # # valkyrie.fly(valkyrie.name, "3시")

# # class BuildingUnit(Unit):
# #     def __init__(self, name, hp, location):
# #         # Unit.__init__(self,name,hp,0)
# #         super().__init__(name,hp,0)
# #         self.location = location

# # supply_depot = BuildingUnit("서플라이 디폿", 500, "7시 ")

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     print("player : gg")
#     print("[player] 님이 게임에서 퇴장하였습니다.")

# game_start()

# m1 = Marine()
# m2 = Marine()
# m3 = Marine()

# t1 = Tank()

# w1 = Wraith()

# attack_units = []
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# attack_units.append(t1)
# attack_units.append(w1)

# for unit in attack_units:
#     unit.move("1시")

# Tank.seize_developed = True
# print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# for unit in attack_units:
#     if isinstance(unit,Marine) == True:
#         unit.stimpack()
#     elif isinstance(unit,Tank) == True:
#         unit.set_seize_mode()
#     elif isinstance(unit,Wraith) == True:
#         unit.clocking()

# for unit in attack_units:
#     unit.attack("1시")
    
# for unit in attack_units:
#     unit.damaged(randint(5,21))

# game_over()

'''
Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

(출력 예제)
총 3대의 매물이 있습니다.
강남 아파트 매매 10억 2010년
마포 오피스텔 전세 5억 2007년
송파 빌라 월세 500/50 2000년

[코드]
class House:
    # 매물 초기화 : 위치, 건물 종류, 매물 종류, 가격, 준공년도
    def __init__(self, location, house_type, deal_type, price, completion_year):
        pass

    # 매물 정보 표시
    def show_detail(self):
        pass
'''

# class House:
#     # 매물 초기화 : 위치, 건물 종류, 매물 종류, 가격, 준공년도
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year

#     # 매물 정보 표시
#     def show_detail(self):
#         print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

# houses = []

# houses.append(House("강남", "아파트", "매매", "10억", "2010년"))
# houses.append(House("마포", "오피스텔", "전세", "5억", "2007년"))
# houses.append(House("송파", "빌라", "월세", "500/50", "2000년"))

# print("총 {0}대의 매물이 있습니다.".format(str(len(houses))))

# for house in houses:
#     house.show_detail()


# 예외 처리
# try:
#     print("나누기 전용 계산기입니다")
#     num1 = int(input("첫번째 숫자를 입력하세요 : "))
#     num2 = int(input("두번째 숫자를 입력하세요 : "))
#     print("{0} / {1} = {2}".format(num1,num2,int(num1/num2)))
# except ValueError:
#     print("에러 발생")
# except ZeroDivisionError as err:
#     print(err)
# except:
#     print("알수없는 애러 발생")

# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg
    
#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리수 나누기 전용 계산기입니다")
#     num1 = int(input("첫번째 숫자를 입력하세요 : "))
#     num2 = int(input("두번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
#     print("{0} / {1} = {2}".format(num1,num2,int(num1/num2)))
# except ValueError:
#     print("에러 발생")
# except BigNumberError as err:
#     print("에러 발생 한자리수만 입력하세요")
#     print(err)
# finally:
#     print("계산기를 이용해 주셔서 감사합니다")

'''
Quiz) 동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다.
대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다.
시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오.

조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError 로 처리
        출력 메세지 : "잘못된 값을 입력하였습니다."

조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
        치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
        출력 메세지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."

[코드]
chicken = 10 # 남은 치킨 수
waiting = 1 # 홀 안에는 현재 만석. 대기번호 1부터 시작

while(True):
    print("[남은 치킨 : {0}]".format(chicken))
    order = int(input("치킨 몇 마리 주문하시겠습니까?"))
    if order > chicken: # 남은 치킨보다 주문량이 많을 때
        print("재료가 부족합니다.")
    else:
        print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".format(waiting, order))
        waiting += 1 # 대기번호 증가
        chicken -= order # 주문 수 만큼 남은 치킨 감소
'''

# class SoldOutError(Exception):
#     def __init__(self):
#         pass

#     def __str__(self):
#         return "재고가 소진되어 더 이상 주문을 받지 않습니다"
        
# chicken = 10 # 남은 치킨 수
# waiting = 1 # 홀 안에는 현재 만석. 대기번호 1부터 시작

# while(True):
#     try:
#         print("[남은 치킨 : {0}]".format(chicken))
#         order = int(input("치킨 몇 마리 주문하시겠습니까?"))
#         if order < 1:
#             raise ValueError
#         if order > chicken: # 남은 치킨보다 주문량이 많을 때
#             print("재료가 부족합니다.")
#         else:
#             print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".format(waiting, order))
#             waiting += 1 # 대기번호 증가
#             chicken -= order # 주문 수 만큼 남은 치킨 감소
#         if chicken <= 0:
#             raise SoldOutError()
#     except ValueError:
#         print("잘못된 값을 입력하였습니다.")
#     except SoldOutError as msg:
#         print(msg)
#         break

# 모듈
# import theater_module
# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.price_soldier(6)

# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(6)

# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(6)

# from theater_module import price, price_morning
# price(3)
# price_morning(4)

# from theater_module import price_soldier as ps
# ps(3)

