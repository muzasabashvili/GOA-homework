total = 0
for i in range(5):
    num = int(input("შეიყვანე რიცხვი: "))
    total += num

print("ჯამი:", total)

if total % 2 == 0:
    print("რიცხვი ლუწია")
else:
    print("რიცხვი კენტია")



while True:
    num = int(input("შეიყვანე რიცხვი: "))
    if num % 5 == 0 and num % 7 == 0:
        print(num)
        break
