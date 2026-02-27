# 1) შექმენით სახელების სია (minimum 5 elements), მომხმარებელს input ფუნქციის მეშვეობით შემოატანინეთ სახელი და ჩაამატეთ მომხმარებლის შემოტანილი მნიშვნელობა სიის ბოლოში. გამოიყენეთ შესაბამისი ფუნქცია.

# 2) insert ფუნქციის მეშვეობით ჩაამატეთ 3-ე index-ზე ახალი სახელი "Tarieli"

# 3) pop ფუნქციის მეშვეობით სიაში წაშალეთ მე-4-ე index-ზე მყოფი მნიშვნელობა სიიდან

# 4) remove ფუნქციის მეშვეობით წაშალეთ 1 ნებისმიერი სახელი თქვენი წინასწარ გამზადებული სიიდან.

# 5) მომხმარებელს შემოატანინეთ სახელი და შეამოწმეთ თუ რომელ index-ზე დგას ელემენტი თუა სიაში რა თქმა უნდა, თუ არაა სიაში მაშინ დაუბეჭდეთ რომ "not index in list"

saxelebi=["Giorgi", "Nino", "Luka", "Ana", "Saba"]


axali_saxeli = input("შეიყვანეთ სახელი: ")
saxelebi.append(axali_saxeli)
print(saxelebi)
  

saxelebi.insert(3, "Tarieli")
print(saxelebi)


saxelebi.pop(4)
print(saxelebi)


saxelebi.remove("Ana")
print(saxelebi)



saziebo_saxeli= input("შეიყვანეთ სახელი რომელსაც ეძებთ: ")

if saziebo_saxeli in saxelebi:
    print(saxelebi.index(saziebo_saxeli))  
else:
    print("ცხრილში არ არის")


