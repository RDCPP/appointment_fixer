import random

start = int(input("약속 잡기 시작 시간 : "))
end = int(input("약속 잡기 마침 시간 : "))
half = input("몇 시 반을 하고 싶으면 y 아니면 나머지 : ")

if half != 'y':
    print("약속은" + str(random.randint(start,end+1)) + "시!")

else :
    half_choicer = [0,30]
    print("약속은 " + str(random.randint(start,end+1)) + "시 " + str(random.choice(half_choicer)) + "분!")