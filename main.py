import sys
import math

with open("number.txt",'r') as f:
    num = f.read()

text = ""

whole = num.split('.')[0]
fract = num.split('.')[1]
fract_digits = len(fract)

group_size = 5
groups_per_line = 10

whole_str = f"{whole}. "

# print(str(fract))
# print(fract_digits)

text += f"     | {' '*len(whole_str)}"
for i in range(groups_per_line):
    s = str(i*group_size+1)
    text += f"{s} "
    text += " "*(5-len(s))

text += "\n"
text += "-----+---"
for i in range(groups_per_line):
    text += "------"

text += "\n"

text += f"   0 | "
text += whole_str


for i in range(fract_digits):
    text += fract[i]
    if (i+1)%group_size==0:
        text += " "
    if (i+1)%(groups_per_line*group_size)==0:
        text += "\n"
        text += f"{(i+1):4} | "
        text += " "*len(whole_str)

print (text)
