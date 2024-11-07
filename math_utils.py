def find_max_number(num1, num2, num3):
    # you need to write this function

def find_mean(num1, num2, num3):
    return  # You should fill in this line!

def find_mean_std(num1, num2, num3):
    mean = find_mean(num1, num2, num3)
    variance = (num1 - mean) ** 2 + (num2 - mean) ** 2 + (num3 - mean) ** 2
    variance /=  # You should fill in this line!
    return mean, variance ** (0.5)  # std is the root square of the variance
