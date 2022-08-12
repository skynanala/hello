import random

#화면에 음식리스트 출력하는 기능
def print_list(foodlist):
    for i, food in enumerate(foodlist):
        print(f"{i+1}.{food}")

foodlist=["짜장","짬뽕","우동","탕수육","비빔밥"]

def print_rand_list(foodlist):
    for i in range(5):
        food =random.choice(foodlist)
        print(f"{i+1}.{food}")