import random

#화면에 음식리스트 출력하는 기능
def print_list(aa):
    #문자열
    str = ""  #빈값
    for i, food in enumerate(aa):
        # print(f"{i+1}.{food}")
        str += f"{i+1}.{food}" #str=str+f"{i+1}.{food}" 이라는 의미
    print(str)    
    
foodlist=["짜장","짬뽕","우동","탕수육","비빔밥"]

def print_rand_list(aa):
    for i in range(5):
        food =random.choice(aa)
        print(f"{i+1}.{food}")


print_list(foodlist)
print_rand_list(foodlist)