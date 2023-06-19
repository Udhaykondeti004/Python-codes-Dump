def palindrome(n):
    temp = n
    rev = 0
    while(n!=0):
        d = n%10
        rev = rev*10+d
        n = n//10
    if(rev==temp):
        print("Number is Palindrome")
    else:
        print("Number isnt a Palindrome")
    
num = int(input("Enter a number: "))
palindrome(num)
