#Keyword Argument = an argument preceded by an identifier
                  # helps with readability
                  # Order of argument does't matter
                  # 1. Positional  2.Default  3.Keyword  4.arbitary





from typing import Type


def hello(greeting,title,first,last):
    print(f"{greeting} {title}{first} {last}")




hello("Hello",title="Mr.", first="Spongebob", last="squarepants")



def get_phone(country,area,first,last):
        return f"{country}-{area}-{first}-{last}"

phone_no = get_phone(country=1,area=51,first=29889,last=78929)
print(phone_no)


#Args = allows you to pass multiple non-key arguments
#Kwargs = allow you to pass multiple keyword-arguments
#        * unpacking operator
#        1. Positional 2.Default  3.Keyword  4.Arbitary


def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3, 4))




def display_name(*args):
    for arg in args :
        print(arg, end=" ")
    

display_name("Dr.","spongbob","Harold","sqarepants")


# **kwars

def print_address(**kwargs):
    pass
    print(type(kwargs))
    for key,value in kwargs.items():
         print(f"{key}: {value}")


print_address(street="123 Fake st.",
              city="Detroit",
              state="MI",
              zip="404-303"
             )





def shipping_label(*args, **Kwargs):
    for arg in args :
        print(arg, end=" ")
    print()
    for value in Kwargs.value():
        print(value , end=" ")



shipping_label("Dr","Spoongbob","sqarepants","II",
                street="123 Fake st.",
                city="Detroit",
                apt="#105",
                state="MI",
                zip="404-303"
                )

