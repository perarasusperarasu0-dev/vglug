def letter_count(a):             

    letter = 0
    for i in a:
         if a.isalpha():
            letter+=1
    return letter


a = input("ENTER A STRING")
tot_lrtter = letter_count(a)

print("TOTAL LETTERS OF THE STRING",tot_lrtter)


