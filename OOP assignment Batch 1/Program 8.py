num = 1
amount = 10
odd_list = []
even_list = []
while amount > 0:
    nums = float(input(f"input number {num}: "))

    if nums %2 == 1:
        odd_list.append(nums)
    else:
        even_list.append(nums)

    amount -= 1
    num +=1

odds = len(odd_list)
print(f"There were {odds} odd numbers from the inputs")