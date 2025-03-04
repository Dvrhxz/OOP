num = 1
amount = 10
sum_list = []
while amount > 0:
    nums = float(input(f"input number {num}: "))
    sum_list.append(nums)
    amount -= 1
    num +=1

sums = sum(sum_list)
print (f"The sum of all ten numbers is = {sums}")