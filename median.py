"""Median calculator."""
while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

# Sort the list of numbers
numbers.sort()

# Calculate the median
n = len(numbers)
if n % 2 == 0:
    # If the list has an even number of elements, the median is the average of the middle two elements
    median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2
else:
    # If the list has an odd number of elements, the median is the middle element
    median = numbers[n // 2]

print("Median:", median)
