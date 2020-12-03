phone=input("Phone:")
words= {
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five"
}
for ch in phone:
    print(words[ch])


output=""
for ch in phone:
   output+= words.get(ch,"!") + " "
print(output)
