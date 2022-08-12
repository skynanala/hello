import random

#화면에 음식리스트 출력하는 기능
def print_list(aa):
    for i, food in enumerate(aa):
        print(f"{i+1}.{food}")



foodlist=["짜장","짬뽕","우동","탕수육","비빔밥"]
food=random.choice(foodlist)
print(food)
#5번을 연속으로 추천해보자 수행문장 반복 
for i in foodlist:
    print(i)
print(".............")
for i in range(5):
    print(i)
print(".........")
for i in range(1,3):
    print(i)
print("----------------")
a=[(1,2),(3,4),(5,6)]
for (fst,second)in a:
    print(fst+second)

for i in range(5):
    print(i+1)

print("종료")   

for i in range(5):
    # print(i+1)
    food=random.choice(foodlist)
    # print(food)
    print(f"{i+1}.{food}")
print("종료")

#화면에 음식리스트를 출력하고 
#리스트중에 먹고 싶은 메뉴가 없으면
#우리가 추가해서 그중에서 추천했으면 좋겠다

for i in foodlist:
    print(f"1.{i}")

for i, food in enumerate(foodlist):
    print(f"{i+1}.{food}")

addfood = input("추가 음식입력:")
print(f"당신이 입력한 내용:{addfood}")

foodlist.append(addfood)

for i, food in enumerate(foodlist):
    print(f"{i+1}.{food}")