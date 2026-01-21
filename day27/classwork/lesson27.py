car_brands = ["kia","Nisan","BMW","Porche","Mercedes","Honda","Lamorgini","Subaru","Bugati","Alfa Romeo"]

print(car_brands [5] )

print(car_brands [1:6])

print(car_brands[-1])

print(car_brands [1::2])

print(car_brands [3:9:3])

first_five = car_brands[:5]
reversed_list = first_five[::-1]
print(reversed_list)

copied_cars=car_brands[:]
copied_cars=[8]="tesla"

print(car_brands)
print(copied_cars)