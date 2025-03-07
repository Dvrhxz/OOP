x = int(input("input 1st number: "))
y = int(input("input 2nd number: "))

start = min(x, y) + 1
end = max(x, y)

print(f"Numbers between {x} and {y}: ")
for num in range(start, end):
    print(num)