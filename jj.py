import os
with open('names.txt') as f1, open("numbers.txt") as ff1:
 with open('nnames.txt', 'w') as f2, open("nnumbers.txt", "w") as ff2:
  for line1 in f1:
   if line1.strip():
    f2.write(line1)
  for line2 in ff1:
   if line2.strip():
    ff2.write(line2)
os.rename("nnames.txt", "names.txt") ; os.rename("nnumbers.txt", "numbers.txt")
