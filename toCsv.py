


file1 = open("names.csv")
lines1 = file1.readlines()

file2 = open("train-081914.txt")
lines2 = file2.readlines()

for l1, l2 in zip(lines1, lines2):
  print(f"\"{l2.strip()}\"| {l1}")