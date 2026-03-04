# HOW TO CALCULATE EXECUTION TIME IN Python

import time

start_time = time.perf_counter()

for i in range(100000):
    print("NAkul")

end_time = time.perf_counter()

elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time} seconds")

