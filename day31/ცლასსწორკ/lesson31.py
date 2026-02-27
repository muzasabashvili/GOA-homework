
text = "Hello World from Python Programming"


print(text.upper())


print(text.lower())


print(text.capitalize())


print(text.title())



index_o = text.find("o")
print(index_o)


first_o = text.find("o")            
second_o = text.find("o", first_o+1) 
print(second_o)


index_z = text.find("z")
print(index_z)   


index_word = text.find("Python")
print(index_word)


# ------------------------------------
# find() ფუნქცია ეძებს სიმბოლოს ან სიმბოლოების ჯგუფს (substring-ს) string-ში.

