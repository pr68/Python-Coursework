file = open("sequences.txt", "r")
seq = tuple(file.read().splitlines())
print("The first sequence is " + seq[0])
print("The second sequence is " + seq[1])
