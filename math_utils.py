def find_max_number(num1, num2, num3):
    # Complete this line to find the maximum number

def find_mean(num1, num2, num3):
    return # Fill in this line to calculate the mean

def find_mean_std(num1, num2, num3):
    mean = find_mean(num1, num2, num3)
    variance = (num1 - mean)**2 + (num2 - mean)**2 + (num3 - mean)**2
    variance /= # Complete this line to calculate variance
    return mean, variance**0.5  # Standard deviation is the square root of variance

