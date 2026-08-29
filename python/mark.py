tamilmark = int(input("Enter your Tamil mark:"))
englishmark = int(input("Enter your English mark:"))
mathsmark = int(input("Enter your Maths mark: "))
biologymark = int(input("Enter your Biology mark:"))
totalmark = tamilmark+englishmark+mathsmark+biologymark
percentage = totalmark

if percentage<=90:
   print("congratilation you are selected for SRM UNIVERSITY💌")
elif percentage>=70 and percentage<=80:
   print("keep waite for next round⏳")
else:
   print("sorry better luck next time😔😔")