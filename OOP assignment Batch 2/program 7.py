even_list = []
odd_list = []


for i in range(10):
    num = float(input(f"input number {i + 1}: "))

    if num %2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

evens = len(even_list)

print(f"The amount of even numbers is = {evens}")