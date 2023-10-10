# 3. Transaction
#  a) Define a global variable called balance and set it to 1000. Write a function called transaction that takes an argument amount and argument _type that can be either deposit or withdrawal.
# b) Inside the function create two inner functions called deposit and withdrawal that take an argument amount.
# c) Inside the deposit function, add the amount to the balance variable and print the new balance.
# d) Inside the withdrawal function, subtract the amount from the balance variable and print the new balance.
# e) Inside the transaction function, check if the _type argument is deposit or withdrawal and call the appropriate function.

balance = 100


def transaction(amount: int, type: str):
    def deposit(amount: int):
        new_balance = balance + amount
        print(f"Balance: {new_balance}")

    def withdrawal(amount: int):
        new_balance = balance - amount
        print(f"Balance: {new_balance}")

    if type == "deposit":
        deposit(amount)
    if type == "withdrawal":
        withdrawal(amount)


transaction(10, "deposit")
transaction(10, "withdrawal")
