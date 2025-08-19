# Read string
s = input("Enter a string: ")

# Find length manually (without len)
count = 0
for _ in s:
    count += 1

# Check palindrome by comparing characters
is_palindrome = True
i = 0
j = count - 1
while i < j:
    if s[i] != s[j]:
        is_palindrome = False
        break
    i += 1
    j -= 1

# Print result
if is_palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")
