def amortization_amount(principal, interestRate, period):
    x = (1 + interestRate) ** period
    return principal * (interestRate * x) / (x - 1)


def amortization_schedule(principal, interestRate, period):
    amortization_amount = amortization_amount(principal, interestRate, period)
    number = 1
    balance = principal
    while number <= period:
        interest = balance * interestRate
        principal = amortization_amount - interest
        balance = balance - principal
        yield number, amortization_amount, interest, principal, balance if balance > 0 else 0
        number += 1