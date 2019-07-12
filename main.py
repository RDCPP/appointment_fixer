import random

start = int(input("약속 잡기 시작 시간 : "))
end = int(input("약속 잡기 마침 시간 : "))
while start >= end :
    print("ㅡㅡ 시작 시간이 마침 시간보다 빨라야지 디질래")
    start = int(input("약속 잡기 시작 시간 : "))
    end = int(input("약속 잡기 마침 시간 : "))

half = input("몇 시 반을 하고 싶으면 y 아니면 n : ")
while not (half == "n" or half == "y") :
    half = input("몇 시 반을 하고 싶으면 y 아니면 n : ")

if half != 'y':
    time = str(random.randint(start,end))
    print("약속은 " + time + "시!")

else :
    time = str(random.randint(start,end))
    half_time = str(0)
    if int(time) < end :
        half_time = str(random.choice([0,30]))
    print("약속은 " + time + "시 " + half_time + "분!")