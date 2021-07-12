firstSem=float(input("Enter 1st Sem Marks:\n"))
secondSem=float(input("Enter 2nd Sem Marks:\n"))
thirdSem=float(input("Enter 3rd Sem Marks:\n"))
fourthSem=float(input("Enter 4th Sem Marks:\n"))
fifthSem=float(input("Enter 5th Sem Marks:\n"))
sixthSem=float(input("Enter 6th Sem Marks:\n"))

totalEarned = sum([((firstSem*22)/10),((secondSem*21.5)/10),((thirdSem*21.5)/10),((fourthSem*24.5)/10),((fifthSem*19)/10),((sixthSem*15)/10)])

totalGPA = 123.5

myGPA = (totalEarned/totalGPA)*10

print("Your CGPA = ",myGPA)



