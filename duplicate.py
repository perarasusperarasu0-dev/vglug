<<<<<<< HEAD

def duplicate(a):
    for i in a:
       if a.count(i)>1:
           if i not in dup:
             dup.append(i)
    return dup

orginal_string = input("ENTER A STRING  :")
a = orginal_string
dup = []

duplicate(a)

print("duplicate string",dup)
=======
fruit_name = ["apple", "banana", "cherry","date", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "ugli fruit", "vanilla bean", "watermelon", "xigua", "yellow passion fruit", "zucchini"]
duplicate_fruits = []
for fruit in fruit_name:
    if fruit_name.count(fruit) > 1 and fruit not in duplicate_fruits:
        duplicate_fruits.append(fruit)  
print("Duplicate fruits:", duplicate_fruits)
>>>>>>> 968811033577d69fc8a569cc4007488d4efae655
