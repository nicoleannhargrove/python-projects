
message = input("Enter a message: ")

print("Lowercase:", message.lower())
print("Uppdercase:", message.upper())
print("Capitalize:", message.capitalize())
print("Title:", message.title())

words = message.split()
print("Words: ", words)

sorted_words = sorted(words)
print("Alphabetic First Word: ", sorted_words[0])
print("Alphabetic Lasst Word: ", sorted_words[-1])

