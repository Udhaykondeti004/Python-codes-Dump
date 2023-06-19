str = input("Enter a string: ")
result = str.lower()
result1 = result.replace(" ","")

vowel = 0
consonant = 0
for i in result1:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        vowel = vowel+1
    else:
        consonant = consonant+1
print("Number of vowels",vowel)
