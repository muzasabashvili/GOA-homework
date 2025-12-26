balance = int(input("შემოიტანე ბალანსი: "))

if balance >= 1500:
    print("შეგიძლია იყიდო: ლეპტოპი")
elif balance >= 1000:
    print("შეგიძლია იყიდო: ტელეფონი")
elif balance >= 100:
    print("შეგიძლია იყიდო: ფეხსაცმელი")
elif balance >= 50:
    print("შეგიძლია იყიდო: პერანგი")
elif balance >= 5:
    print("შეგიძლია იყიდო: რვეული")
else:
    print("ვერცერთ ჩამოთვლილ პროდუქტს ვერ ყიდულობ")



num = int(input("შემოიტანე რიცხვი: "))

if num > 0:
    print("რიცხვი დადებითია")
elif num < 0:
    print("რიცხვი უარყოფითია")
else:
    print("რიცხვი ნულია")
