# # # b=False
# # # if(b):
# # #     print("참")
# # # else:
# # #     print("거짓")
# # # # *=  곱한후 대입
# # # # /=  나눈후 대입
# # # %= 값을 나눗셈 한 후에 나머지를대입
# # a=10
# # b=3
# # c=1.5
# # result= a+b
# # print(result)
# # result1=a-b
# # print(result1)
# # result2=a/b
# # print(result2)
# # result3=a%b
# # print(result3)
# # b*=2
# # print(b)
# # a*=c
# # print(a)

# 논리연산자
# and (비트 연산자)&& 둘중하나라도 다르면 False
# or (비트연산자)|| 둘중 하나라도 맞으면 True
# not (비트연산자)~
# ~False =True 
# ~True=False
# print("100==100 :",100==100)
# print("100!=100 :",100!=100)
# c = 10
# d = 4
# print(c==10,c==d,c!=4,d>=0)
# str1 ="Hello"
# str2= "Jongyu"
# result = str1+str2
# print(result)
# str3 ='Hayoon\'s'
# num =3 
# print(str3*3)
# print(chr(65))
# print(ord("A"))

# str1 = "apple"
# 문자열   문자 
# 변수이름[인덱스 번호]
# print(str1[0],str1[1],str1[2],str1[3],str1[4])
# a="hello python"
# b=a[4]+a[5]+a[7]
# print(a[0],a[5],a[9])
# print(b)

# city="Seoul"
# today=2
# day='화요일'
# temp=25
# # 문자열 형식 코드
# # %s 문자열
# # %d 정수
# # %f 실수
# # %c 문자 1개
# print("%s의 %d일 기온은 %d 입니다.", %(city,today,temp))
# format 형식 
name = 'Song'
# age=29
# height=180
# print()
# len
# join
# upper
# lower
# replace
# split
# find = index 
# count
# print("ㅗ".join(name))
# print(name.find("o"))
# str1="For sale: Baby shoes Never worn"
# print(str1.count('e'))
# print(str1.find('e'))
# print(str1.upper())
# print(str1.lower())
# print(str1.replace('e','b'))
# print(str1.split(" "))
# print(str1.strip())

# 입력받은 문자의 길이가 10 이상이면 OK 
# 미만이면 다시 입력해주세요 
# a= input("입력 해 주셈 :")
# if(len(a.replace(""))>10) :
#     print("OK")
# else:
#     print("다시 입력하세요 ")
