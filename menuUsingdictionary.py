menu = {
    1:{"code" : 1, "dish" : "Nasi Ayam", "price" : 5.50},
    2:{"code" : 2, "dish" : "Nasi Minyak", "price" : 6.00},
    3:{"code" : 3, "dish" : "Nasi Tomato", "price" : 8.00}
}

print(menu)

code = input("insert code: ")
dish = input("insert dish: ")
price = float(input("insert price: "))

menu[4] = {"code":code, "dish":dish, "price":price}
print(menu)
