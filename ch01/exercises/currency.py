rate = input("What is the current exchange rate for the Euro to Dollar?")
amount = input("What is the amount of currency to exchange?")

therate = int(rate)
theamt = int(amount)

total = int(theamt / therate)
result = int(total - 3)
print(result)