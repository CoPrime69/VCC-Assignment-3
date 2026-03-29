import time

print("Stress script started")

counter = 0

while True:
    x = 0
    for i in range(10000000):
        x += i

    counter += 1
    print(f"Running iteration : {counter}")