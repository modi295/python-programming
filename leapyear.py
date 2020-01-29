x = int(input(" enter  year "))
if x%4==0 and x%100==0 and x%400==0:
    print(" {} is a leap year ".format(x))
else:
     print(" {} is not a leap year ".format(x))
