#Keyword Argument = an argument preceded by an identifier
                  # helps with readability
                  # Order of argument does't matter
                  # 1. Positional  2.Default  3.Keyword  4.arbitary


def hello(greeting,title,first,last):
    print(f"{greeting} {title}{first} {last}")




hello("Hello",title="Mr.", first="Spongebob", last="squarepants")



def get_phone(country,area,first,last):
        return f"{country}-{area}-{first}-{last}"

phone_no = get_phone(country=1,area=51,first=29889,last=78929)
print(phone_no)

