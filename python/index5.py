#Logical Operator :evaluate maltiple conditions(or,and ,not)
#         or = at least one cond. must be true
#         and = both cond. must be true
#          not = inverts the cond.

#or statement
temp = -5
is_sunny = False

# if temp >= 28 or temp < 0 or is_sunny:
#     print("It is ok")
# else :
#     print("It's not ok")


#and Statement & Not statement

if temp >=28 and is_sunny:
   print("It is hot 🥵 and sunny ☀️")
elif temp <= 0 and is_sunny:
   print("It is cold 🥶 and sunny ☀️")
elif 0 < temp < 28 and  is_sunny:
   print("It is warm 🥰 and sunny ☀️")
elif temp >=28 and not is_sunny:
   print("It is hot 🥵 and cloudy ☁️")
elif temp <= 0 and not is_sunny:
   print("It is cold 🥶 and cloudy ☁️")
elif 0 < temp < 28 and  is_sunny:
   print("It is warm 🥰 and cloudy ☁️")


