i = 10
while i >= -10:
    print(i)
    i -= 1

i = 1
while i <= 100:
    print(i)
    i += 2


correct_password = "goa123"
attempts = 3

while attempts > 0:
    user_input = input("Enter password: ")

    if user_input == correct_password:
        print("password is correct")
        break
    else:
        attempts -= 1
        print("Password is incorrect! Try again")
        print("trys left:", attempts)

    if attempts == 0:
        break
