import random

lower = "qwertyuiopasdfghjklzxcvbnm"

upper = "QWERTYUIOPASDFGHJKLZXCVBNM"

number = "1234567890"

symbol = "-/:;()&@.,?![]{}#%^*+=_\|~<>$"

all = lower + upper + number + symbol

length = 12

password = "".join(random.sample(all,length))

print(password)