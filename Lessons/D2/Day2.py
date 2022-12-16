name = "lasha"

print(len(name)) #len(length) - სიგრძე.

my_sentence = """ჩემი დაბადების დღეა 
19 სექტებმერი"""   # მრავალ სტრიქონიანი წინადადებების დროს გამოიყენება სამი ბრწალი

print(my_sentence)

if 10>5:
    print("hello")
    # TAB-ის საშუალებით მოვახდუნეთ ინდენტაცია

full_name = "lasha gurguliani"
print(len(full_name))

# position = index სინონიმებია

print(full_name[8])

print("g" not in full_name)

print(full_name[2:9]) # დიაპაზონი დან-მდე
print(full_name[2:9:2]) # start:finish:step
print(full_name[:6])
print(full_name[6:])
print(full_name[-1])
print(full_name[-1]+"abc")
print(full_name[-1:-6:-1])
print(full_name.upper())
print(full_name.lower())

name2 = "  lasha  "

print(name2.strip()) #ზედმეტ სპფეისებს აშორებს

print(name2.replace(" ", "#"))
print(name2.replace("a", "x"))