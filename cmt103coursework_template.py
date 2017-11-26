##CMT103 COURSEWORK 2017/18 ###
###############################
##You need to implet the following methods:
##
##Task 1
##readnumbers()  [2 marks]
##isPrime()    [5 marks]
##
##Task 2
##readsequences()  [2 marks]
##longest_common_string() [6 marks]
##
##Task 3
##get_words() [4 marks]
##sort_tuples() [4 marks]
##get_top_10() [7 marks]
################################


###################################################
#Task 1: Check if a Given Number is a Prim Number:#
###################################################
def readnumbers(file_name):
    file = open(file_name, "r")
    st = file.read()
    stt = st.replace(",", "")
    sstt = stt.split()
    numbers = list(map(int, sstt))
    return numbers


def isPrime(num):
    import math
    if num % 2 == 0:
        return False
    elif num % 3 == 0:
        return False
    elif num % 5 == 0:
        return False
    elif num > 1:
        for n in range(2, int(math.sqrt(num)) + 1, 1):
            if (num % n) == 0:
                return False
                break
        else:
            return True

    else:
        return False

############################################
#Task 2: Find the longest common substring #
#       between two strings:               #
############################################
def readsequences(file_name):
    file = open(file_name, "r")
    seq = tuple(file.read().splitlines())
    return seq

def longest_common_string(st1, st2):
    import re
    common = ""
    k = 0
    for i in range(0, len(st1)):
        for j in range(0, len(st2)):
            while (i + k <= len(st1) and j + k <= len(st2) and st1[i:i+k] == st2[j:j+k]):
                if len(common) <= len(st1[i:i+k]):
                    common = st1[i:i+k]
                k += 1
    return common

######################################
#Task 3: Get Top 10 ly-Words:        #
######################################
def get_words(file_name):
    import string
    file = open(file_name, "r")
    text = file.read().lower()
    for c in string.punctuation:
        text = text.replace(c, "")
    wordlist = text.split()
    return wordlist

def get_dic(words):
    unique = set(words)
    lywords = [w for w in unique if w.endswith('ly')]
    counts = []
    for word in lywords:
        counts.append(words.count(word))
    com = zip(lywords, counts)
    dic = dict(com)
    return dic

def get_top_10(dic):
    lytuple = dic.items()
    srt = sorted(lytuple, key=lambda lyw: lyw[1])
    srt = srt[::-1]
    srt = srt[0:10]
    return srt



####### THE CODE BELOW IS FOR TESTING###################
############### DO NOT  CHANGE #########################


import sys
if __name__ == '__main__':
    #Take care of the console inputs
    if len(sys.argv)<=1:
        sys.argv = ['', "numbers.txt", "sequences.txt", "sense_and_sensitivity.txt"]


    stars = '*'*40
    print(stars)
    print("Testing Task 1 --- Is It a Prime?")
    print(stars)

    #Task 1-a
    try:
        nums = readnumbers(sys.argv[1])
        if not nums:
            print("readnumbers() returns None.")
        else:
            print("Numbers: ", nums)
            print()
    except Exception as e:
        print("Error (readnumbers()): ", e)

    #Task 1-b
    try:
        if not nums: #Task 1-a has not been implemented
            print("isPrime() skipped....")
        else:
            for num in nums:
                result = isPrime(num)
                if result==None:
                    print("isPrime() returns None.")
                    break
                print("{} : {}".format(num, "Prime" if result else "Not Prime"))

    except Exception as e:
        print("Error (isPrime()):", e)

    #testing task 2
    print("\n\n"+stars)
    print("Testing Task 2 --- Longest Common Substring")
    print(stars)

    #Task 2-a
    try:
        tup = readsequences(sys.argv[2])
        if not tup:
            print("readsequences() returns None.")
        else:
            st1, st2 = tup
            print("The first string: {}".format(st1))
            print("The second string: {}".format(st2))
    except Exception as e:
        print("Error (readsequences()):", e)

    #Task 2-b
    try:
        if not tup: #Task 2-a has not been implemented
            print("longest_common_string() skipped...")
        else:
            commonst= longest_common_string(st1, st2)
            if not commonst:
                print("longest_common_string()  returns None.")
            else:
                print("The longest common substring is {} of size {}.".format(commonst,len(commonst)))
    except Exception as e:
        print("Error (longest_common_string()):", e)

    print("\n\n"+stars)
    print("Testing Task 3 --- Top LY Words")
    print(stars)

    #Task 3-a
    try:
        words = get_words(sys.argv[3])
        if not words:
            print("get_words()  returns None.")
        else:
            print("+ {} has a total of {} words.".format(sys.argv[3], len(words)))
    except Exception as e:
        print("Error (get_words()):", e)

    #Task 3-b
    try:
        if not words: #Task 3-a has not been implemented
            print("get_dic() skipped....")
        else:
            dic = get_dic(words)
            if not dic:
                print("get_dic()  returns None.")
            else:
                print("+ There are {} ly-words in the file.\n+ '{}' and '{}' have {}, {} occurrences respectively.\n".format(len(dic), 'only', 'hardly', dic['only'], dic['hardly']))
    except Exception as e:
        print("Error (get_dic()):", e)

    #Task 3-c
    try:
        if not words or not dic: #Task 3-a has not been implemented
            print("get_top_10() skipped....")
        else:
            results = get_top_10(dic)
            if not results:
                print("get_top_10() returns None.")
            else:
                print("+ Top 10 ly-Words in {}:".format(sys.argv[3]))
                for word, n in results:
                    print(" "*5+"{:<20} {:<}".format(word, n))
    except Exception as e:
        print("Error (get_top_10()):", e)
