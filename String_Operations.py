str = "srm university college 123  "
print(str)

print(str.upper())
print(str.lower())
print(str.swapcase())
print(str.title())
print(str.capitalize())

print(str.isdigit())
print(str.isalpha())
print(str.isalnum())

print(str.isspace())
print(str.lstrip())
print(str.rstrip())
print(str.strip())

print(str.replace("university","college"))
print(str.split('-'))

result = "@".join(str.split('-'))
print(result)

print(str.find("s"))
print(str.find("s",2,12))

print(str.rfind("e"))

print(str.startswith('srm'))
print(str.count("e"))


