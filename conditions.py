# CS104
# First name Last name
# conditions.py
temp = input("Please enter the current temperature:")
x = int(temp)
if x > 90:
    print ("Wear Shorts")
elif x > 70:
    print ("Short sleeves are fine")
elif x > 50:
    print ("Wear a jacket")
elif x > 32:
    print ("Wear a heavy coat")
else:
    print("Stay Inside")
    
