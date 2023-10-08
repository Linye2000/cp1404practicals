numbers = [3, 1, 4, 1, 5, 9, 2]

#What values do the following expressions have?
#numbers[0] = 3
#numbers[-1] = 2
#numbers[3] = 1
#numbers[:-1] = [3, 1, 4, 1, 5, 9]
    #No last number(slice)
#numbers[3:4] = [1]
    #Also slice, and [] mains have left, no right, so no 5th number
#5 in numbers           True
#7 in numbers           False
#"3" in numbers
    #The number 3 exists in the list, but the string "3" does not exist in the list
#numbers + [6, 5, 3]    [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    #Add together

# Change the first element to "ten"
numbers[0] = "ten"

# Change the last element to 1
numbers[-1] = 1

# Print all elements except the first two(slice)
print(numbers[2:])

# Print whether 9 is an element of numbers
print(9 in numbers)
