sfile = input("Enter a file to open: ")
f1 = open(sfile,"r")
data = f1.read().replace(" ","").lower()
vowel = 0
consonant = 0
for i in data:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        vowel = vowel+1
    else:
        consonant = consonant+1
print("Number of vowels are:",vowel)
print("Number of consonants are:",consonant)
f1.close()
