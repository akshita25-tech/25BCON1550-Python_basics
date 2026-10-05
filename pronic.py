num = int(input("Enter a number: "))

flag = False

for i in range(1, num):
    if i * (i + 1) == num:
        flag = True
        break

if flag:
    print("Pronic number")
else:
    print("Not a pronic number")