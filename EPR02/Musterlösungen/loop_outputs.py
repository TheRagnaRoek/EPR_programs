"""Script containing code for Task 2-01 Code Analysis"""

input("Press <return> to start code outputs...")

print("*" * 20)
print("Output: Code Piece a) \n")

for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, 4):
            print(f"{i} * {j} * {k} = {i * j * k}")

print("*" * 20)
input("Press <return> to continue with b)...")

print("*" * 20)
print("Output: Code Piece b) \n")

count = 3
while count > 0:
    for i in range(count):
        print( "Countdown:" , count, "-", i)
    count -= 1

print("*" * 20)
input("Press <return> to continue with c)...")

print("*" * 20)
print("Output: Code Piece c) \n")

counter = 1
while counter <= 5:
    counter += 1
    print(counter)

print("*" * 20)
input("Press <return> to continue with d)...")

print("*" * 20)
print("Output: Code Piece d) \n")

counter = 1
while counter <= 5:
    print(counter)
    counter += 1

print("*" * 20)
input("Press <return> to finish...")