# METHOD 1

palindromes = []
for x in range(999,100,-1):
    for y in range(999,100,-1):
        product = x * y
        if (str(product) == str(product)[::-1]):
            palindromes.append(product)  
solution = max(palindromes)
print("\n Method 1 \n The largest palindrome made from the product of two 3-digit numbers is " + str(solution))

#________________________________________________________________________________________________________#

# METHOD 2

solution = 1
for x in range(999,100,-1):
    for y in range(999,100,-1):
        product = x * y
        if (str(product) == str(product)[::-1]):
            if (product > solution):
                solution = product                    
print("\n Method 2 \n The largest palindrome made from the product of two 3-digit numbers is " + str(solution))
        

