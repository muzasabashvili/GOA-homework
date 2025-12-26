# 1) შეიყვანოს რიცხვი — თუ >50: გამრავლდეს 5-ზე, სხვანაირად: კვადრატში
num = int(input("Enter a number: "))

if num > 50:
    print(num * 5)
else:
    print(num ** 2)

# 2) შეიყვანოს პაროლი — თუ "goa123": სწორია, თუ არა: არასწორია
password = input("Enter password: ")

if password == "goa123":
    print("Password is correct!")
else:
    print("Incorrect password!")


# 3) შეიყვანოს რიცხვი — დაბეჭდე 1-დან მასამდე ყველა რიცხვის ჯამი
n = int(input("Enter a number: "))

total = 0
for i in range(1, n + 1):
    total += i

print(total)