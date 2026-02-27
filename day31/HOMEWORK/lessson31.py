# .upper()
# აბრუნებს ახალ სტრინგს, სადაც ყველა ასო არის დიდ ასოდ (uppercase)
text = "hello"
print(text.upper())        # HELLO
print("Python".upper())    # PYTHON
print("saBa".upper())      # SABA


# .lower()
# აბრუნებს ახალ სტრინგს, სადაც ყველა ასო არის პატარა ასოდ (lowercase)
text = "HELLO"
print(text.lower())        # hello
print("PyThOn".lower())    # python
print("TBILISI".lower())   # tbilisi


# .capitalize()
# სტრინგის მხოლოდ პირველი ასო გადაჰყავს დიდზე, დანარჩენები ხდება პატარა
text = "hello world"
print(text.capitalize())   # Hello world
print("pYTHON".capitalize()) # Python
print("java".capitalize()) # Java


# .title()
# თითოეული სიტყვის პირველ ასოს გადაჰყავს დიდზე
text = "hello world"
print(text.title())        # Hello World
print("python is fun".title()) # Python Is Fun
print("i love coding".title()) # I Love Coding


# .find()
# ეძებს სიმბოლოს ან სიტყვას სტრინგში
# აბრუნებს პირველივე ნაპოვნი ელემენტის ინდექსს
# თუ ვერ იპოვა — აბრუნებს -1
text = "hello world"
print(text.find("o"))      # 4
print(text.find("world"))  # 6
print(text.find("x"))      # -1


# Dot notation (წერტილოვანი ნოტაცია)
# გამოიყენება ობიექტის მეთოდების გამოსაძახებლად
# სინტაქსი: object.method()
text = "hello"
print(text.upper())        # HELLO
print(text.lower())        # hello