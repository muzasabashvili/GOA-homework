# 2) append(), insert() და pop() ფუნქციების დანიშნულება

# .append() — ამატებს ელემენტს სიის ბოლოში
# .insert(index, value) — ამატებს ელემენტს სიის კონკრეტულ ინდექსზე
# .pop() — შლის და აბრუნებს სიის ბოლო ელემენტს (ან მითითებულ ინდექსზე მყოფს)


# 3)
numbers = [1, 2, 3, 4, 5]
print(len(numbers))  


# 4) 
nums = []

for i in range(5):
    number = int(input("შეიყვანე რიცხვი: "))
    nums.append(number)

print(nums)


# 5)
colors = ["red", "green", "blue", "yellow", "purple"]
colors.pop()  
print(colors)


# 6) 
animals = ["dog", "cat", "elephant", "lion"]
animals.insert(1, "monkey")
print(animals)


# 7) 
students = []

for i in range(3):
    name = input("შეიყვანე სტუდენტის სახელი: ")
    students.append(name)

students.insert(0, "Teacher")   
students.pop()                  

print(len(students))            
print(students)                 


# 8) custom ფუნქციები
# custom ფუნქცია არის მომხმარებლის მიერ შექმნილი ფუნქცია,
# რომელიც გამოიყენება კოდის გამეორების თავიდან ასაცილებლად.
# ფუნქციის შექმნის ეტაპები:
# 1) def საკვანძო სიტყვა
# 2) ფუნქციის სახელი
# 3) პარამეტრები ()
# 4) კოდის ბლოკი
# პარამეტრი — ფუნქციის აღწერისას გამოყენებული ცვლადი
# არგუმენტი — ფუნქციის გამოძახებისას გადაცემული მნიშვნელობა


# 9) 
def sum_two(a, b):
    return a + b


# 10) 
def check_even(n):
    if n % 2 == 0:
        print("რიცხვი ლუწია")
    else:
        print("რიცხვი კენტია")


# 11) 
def square(n):
    return n * n


# 12) 
def to_upper(text):
    return text.upper()


# 13) 
def full_name(name, surname):
    print(f"ჩემი სახელია {name} და გვარია {surname}")
