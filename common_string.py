def readsequences(file_name):
    file = open(file_name, "r")
    seq = tuple(file.read().splitlines())
    return seq
    print("The first sequence is " + seq[0])
    print("The second sequence is " + seq[1])


def longest_common_string(st1, st2):
    import re
    common = ""
    i = 0
    for x in st1:
        if re.search(x, st2):
            s = x
            while re.search(s, st2):
                if len(s) > len(longest):
                    longest = s
                if i+len(s) == len(s1):
                    break
                s = s1[i:i+len(s)+1]
        i += 1
    return common


longest_common_string(seq[0], seq[1])
