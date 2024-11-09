def find_max_number(num1, num2, num3):

    return max(num1, num2, num3)
    
    # pass  # Replace 'pass' with code

def find_mean(num1, num2, num3):

    return (num1 + num2 + num3)/3
    
    # pass  # Replace 'pass' with code

def find_mean_std(num1, num2, num3):
    mean = find_mean(num1, num2, num3)

    variance = (num1 - mean)**2 + (num2 - mean)**2 + (num3 - mean)**2
    variance /= 3 # Complete this line to calculate variance
    return mean, variance**0.5  # Standard deviation is the square root of variance
    
    #pass  # Replace 'pass' with code

