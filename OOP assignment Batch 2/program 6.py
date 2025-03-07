nums = []
for i in range(10):
    num = float(input(f"Input number {i + 1}: "))
    nums.append(num)

num1 = nums[0]
for num in nums[1:]:
    num1 -= num

print(f"The first number {nums[0]} minus all the remaining numbers is = {num1}")