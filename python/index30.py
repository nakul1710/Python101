#Variable scope = Where a variables is visible and accessible
# Scope Resolution = (LEGB) Local -> Enclosed  -> Global -> Built-in

def fun1():
    x = 1
    print(x)


def fun2():
    x = 2
    print(x)


fun1()
fun2()