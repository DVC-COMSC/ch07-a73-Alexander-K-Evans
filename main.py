

numbers = [5, 20, 30, 35, 50]

insval = int(input('Enter the insertion value: '))
for i in range(len(numbers)):
    if insval < numbers[i]:
        numbers.insert(i, insval)
        break
if len(numbers) == 5:
    numbers.insert(5, insval)
    

print (numbers)
