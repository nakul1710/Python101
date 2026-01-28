#Format Specifiers : Value at which values will be replaced

price1 = 3000.14159
price2 = -9870.74
price3 = 1200.89

print(f"price1 : {price1: .2f}")
print(f"price2 : {price2: .2f}")
print(f"price3 : {price3: .2f}")


print(f"price1 : {price1: 10}")
print(f"price2 : {price2: 10}")
print(f"price3 : {price3: 10}")


print(f"price1 : {price1: 010}")
print(f"price2 : {price2: 010}")
print(f"price3 : {price3: 010}")

#Right justify <
print(f"price1 : {price1: <10}")
print(f"price2 : {price2: <10}")
print(f"price3 : {price3: <10}")


#left justify >
print(f"price1 : {price1: >10}")
print(f"price2 : {price2: >10}")
print(f"price3 : {price3: >10}")


#center justify ^
print(f"price1 : {price1: ^10}")
print(f"price3 : {price3: ^10}")
print(f"price2 : {price2: ^10}")


#plus
print(f"price1 : {price1: +}")
print(f"price3 : {price3: +}")
print(f"price2 : {price2: +}")

#Commo seprator
print(f"price1 : {price1: ,}")
print(f"price3 : {price3: ,}")
print(f"price2 : {price2: ,}")

