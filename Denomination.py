# a//b is floor division
amount= int(input("Enter the amount: "))
amount= amount-100
twok= amount//2000
amount= amount - twok*2000
fiv= amount//500
amount= amount - fiv*500
hun= amount//100 + 1

print("\nDenominations are: \nTwo Thousands: ",twok)
print("Five hundreds: ",fiv)
print("Hundreds: ",hun)
print("Total no. of denominations: ",twok+fiv+hun)