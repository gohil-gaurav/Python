# Python credit card validator program

# Steps
# 1. Remove '-' or ' '
# 2. Add all digits in the odd places from right to left
# 3. Double every second digit from right to left 
#                   (if result is a two-digit number,
#                   add a two digit number together to get a single digit.)
# 4. Sum the total of steps 2 & 3. 
# 5. If sum of divisible by 10, the credit card is valid   

sum_odd_digits = 0
sum_even_digits = 0
total = 0

# Step 1

card_number = input("Enter a credit card #: ")
card_number = card_number.replace("-","")
card_number = card_number.replace(" ","")
card_number = card_number[::-1]

# Step 2

for x in card_number[::2]:
    sum_odd_digits += int(x)

# Step 3

for x in card_number[1::2]:
    x = int(x)*2
    if x >= 10 :
        sum_even_digits += (1 + (x % 10))
    else :
        sum_even_digits += x

# Step 4

total = sum_even_digits + sum_odd_digits

# Step 5

if total % 10 == 0 :
    print("VALID!")

else :
    print("INVALID!")

