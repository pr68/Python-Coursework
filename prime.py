import math


def readnumbers(filename):
    file = open(filename, "r")
    st = file.read()
    stt = st.replace(",", "")
    sstt = stt.split()
    numbers = list(map(int, sstt))
    return numbers


def isprime(filename):
    for i in readnumbers(filename):
        if i % 2 == 0:
            return False
        elif i % 3 == 0:
            return False
        elif i % 5 == 0:
            return False
        elif i > 1:
            for n in range(2, int(math.sqrt(i)) + 1, 1):
                if (i % n) == 0:
                    return False
                    break
            else:
                return True

        else:
            return False


isprime("numbers.txt")
