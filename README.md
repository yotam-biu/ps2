# PS2: Simple Statistics

This assignment introduces basic statistics through Python functions. You will create and test three functions for finding the maximum number, calculating the mean, and calculating the standard deviation of three given numbers.

## Files

- **`simple_statistic.ipynb`**: The main notebook for the assignment. It contains instructions, code cells to fill in, and tests for each function.
- **`math_utils.py`**: A module to store your completed functions after testing in the notebook. You will copy each function from the notebook into this file once they work correctly.

## Instructions

1. **Open `simple_statistic.ipynb`** in Google Colab or Jupyter Notebook.

2. Follow the instructions for each part of the assignment:
    - **Part 1: Find the Maximum Number**  
      Create a function `find_max_number` that takes three numbers as input and returns the maximum value.
    - **Part 2: Mean Calculation**  
      Create a function `find_mean` that takes three numbers as input and returns the mean. Remember to use \( n = 3 \) in the formula.
    - **Part 3: Standard Deviation Calculation**  
      Create a function `find_mean_std` that calculates both the mean and standard deviation of three numbers. Use `find_mean` from Part 2 to calculate the mean.

3. **Testing Functions**:  
   For each function, test it using the provided example values to ensure accuracy.

4. **Copy Functions to `math_utils.py`**:  
   Once each function works as expected, copy it into `math_utils.py` in the same format.

5. **GitHub Submission**:  
   - Make sure all code is working.
   - Push your changes to GitHub. Verify that `math_utils.py` contains your functions and that all code passes the provided tests.

## Formulas Used

- **Mean**:  
  \[
  \bar{x} = \frac{x_1 + x_2 + \ldots + x_n}{n}
  \]
  where \( n = 3 \) in this assignment.

- **Standard Deviation**:  
  \[
  \sigma = \sqrt{\frac{(x_1 - \bar{x})^2 + (x_2 - \bar{x})^2 + \ldots + (x_n - \bar{x})^2}{n}}
  \]

## Requirements

- Basic understanding of Python functions
- Knowledge of arithmetic operations and simple statistics
- GitHub account to submit the completed assignment

## License

This repository is for educational purposes and is part of the PS2 statistics assignment in [GitHub Classroom](https://classroom.github.com/).
