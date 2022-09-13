
# Print the pattern
j = [ ]
for i in range(1,6):
    j.append(str("*"))
    print(" ".join(j))
for i in range(1,6):
    j.remove(str("*"))
    print(" ".join(j))