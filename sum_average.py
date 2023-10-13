# Python program to find the sum and average of the list of numbers

def sum_average(num_list):

# variable to store the sum
    sum = 0

# Finding the sum
    for i in num_list:
        sum += i

# calculate the average
    avg = sum/len(num_list)

    return sum, avg


num_list = [4, 5, 1, 2, 9, 7, 10, 8]

sum, average =sum_average(num_list)

print("sum of numbers is",sum)
print("average of numbers is", average)
