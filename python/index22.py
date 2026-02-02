# Default arguments = A default value for certain parameters 
#                    default is used when that argument is 
#                    omitted make youe function more flexible


import time

def count(start,end):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("Done!")


count(0,10)