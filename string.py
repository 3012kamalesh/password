import string
import random
lower_len=int(input("enter the lower case"))
upper_len=int(input("enter the upper cae"))
digits_len=int(input("enter the number"))
symbol_len=int(input("enter the symbol"))
password=lower_len+upper_len+digits_len+symbol_len
lower=string.ascii_lowercase
upper=string.ascii_uppercase
number=string.digits
symbol=string.punctuation
string=random.choices(lower,k=lower_len)+random.choices(upper,k=upper_len)+random.choices(number,k=digits_len)+random.choices(symbol,k=symbol_len)
random.shuffle(string)
pwd="".join(string)
print("password is",pwd)




