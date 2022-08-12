import myfood
foodlist=["짜장","짬뽕","우동","탕수육","비빔밥"]

#그만 입력하면 실행중단
#무한루프 while

while True:
    addfood = input("추가음식입력:")
    print(f"당신인 입력한 내용: {addfood}")
    #만약에 입력한 글자가 그만과 같다면 무한반복 멈춤
    if addfood == "그만":
        break
    foodlist.append(addfood)

myfood.print_list(foodlist)