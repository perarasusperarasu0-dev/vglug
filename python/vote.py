# nested if statment
number = int(input("Enter the value"))
if number%3==0 or number%5==0:
    if number%3==0 and number%5==0:
        print("fungun")
    elif number%3==0:
        print("fun")
    else:
        print("gun")
else:
    print("not div by 3 and 5")