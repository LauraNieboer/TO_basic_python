
# Print the pattern

pattern='*'

for number in range(8):
    #print(number)
    if len(pattern) < 9:
        print(pattern)
        pattern=pattern+' *'

print(pattern)

#mangler halvdelen
