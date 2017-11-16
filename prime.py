import math
file = open("numbers.txt", "r")
st = file.read()
stt = st.replace(",", "")
sstt = stt.split()
numbers = list(map(int, sstt))
print(numbers)

for i in numbers:
    if i % 2 == 0:
        print(i,"is not a prime number")
    elif i % 3 == 0:
        print(i,"is not a prime number")
    elif i % 5 == 0:
        print(i,"is not a prime number")
    elif i > 1:
        for n in range(2,int(math.sqrt(i)) + 1,1):
            if (i%n) == 0:
                print(i,"is not a prime number")
                break
        else:
            print(i,"is a prime number")

    else:
        print(i,"is not a prime number")
