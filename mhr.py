#mhr.py
age = int (input("Please Enter Your Age: "))
mhr = 220-age
minRate = int (mhr * 0.6)
maxRate = int (mhr * 0.7)
print("Minimum heart rate for Zone 2 = ", minRate)
print("Maximum heart rate for Zone 2 = ", maxRate)
