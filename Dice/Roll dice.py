import random
number = (1, 2)
rollednumber = []
for i in range(2):
    rollednumber.append(random.randint(1, 6))
print (rollednumber)

a = rollednumber[0]+ rollednumber[1]
if a == 12 :
    print ("you get a second chance")
else:
    print("you do not get a second chance")