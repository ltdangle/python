# 5. Write a function that calculates performance of deposit on bank account.
# The function called simple_interest takes three arguments: the initial amount, the annual interest rate (as a float), and the time in years.
# The function should return the final amount after the simple interest has been applied. Use a for loop to accomplish this.
# Round the answer to the nearest hundredth.
#
# ```python
# def simple_interest(initial_amount, interest_rate, years):
#     # Your code here
#
#
# print(simple_interest(10000, 0.1, 10))
# >>> 25937.42
# ```
def simple_interest(initial_amount: int, interest_rate: float, years: int):
    sum = initial_amount

    if interest_rate < 1:
        interest_rate = 1 + interest_rate

    for i in range(years):
        sum = sum * interest_rate
    return round(sum, 2)


print(simple_interest(10000, 0.1, 10))
