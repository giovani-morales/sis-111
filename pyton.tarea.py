nums = [int(input(f"Enter number {i+1}: ")) for i in range(5)]

if nums == sorted(nums):
    print("Ascending order")
elif nums == sorted(nums, reverse=True):
    print("Descending order")
else:
    print("Random order")


nums = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Enter the number to search for: "))

found = False
for num in nums:
    if num == target:
        found = True
        break

print("Number found" if found else "Number not found")


number = int(input("Enter an integer: "))
even = odd = 0

for digit in str(abs(number)):
    if int(digit) % 2 == 0:
        even += 1
    else:
        odd += 1

print(f"Even digits: {even}, Odd digits: {odd}")


team_a = list(map(int, input("Enter 5 results for Team A: ").split()))
team_b = list(map(int, input("Enter 5 results for Team B: ").split()))

avg_a = sum(team_a) / len(team_a)
avg_b = sum(team_b) / len(team_b)

if avg_a > avg_b:
    print("Team A performed better")
elif avg_b > avg_a:
    print("Team B performed better")
else:
    print("Both teams performed equally")



from itertools import combinations

nums = list(map(int, input("Enter 4 numbers: ").split()))
max_product = max(a * b for a, b in combinations(nums, 2))

print(f"Largest product: {max_product}")


goal = int(input("Enter savings goal: "))
total = 0
day = 0
daily_saving = 5

while total < goal:
    total += daily_saving
    daily_saving += 2
    day += 1

print(f"Goal reached in {day} days")


num = input("Enter an integer: ")
if num == num[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")


    from itertools import combinations

nums = list(map(int, input("Enter 4 numbers: ").split()))
for a, b in combinations(nums, 2):
    print(f"({a}, {b})")


    import math

n = int(input("Enter an integer: "))
if n <= 1:
    print("Not prime")
else:
    is_prime = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            is_prime = False
            break
    print("It is prime" if is_prime else "It is not prime")


    nums = list(map(int, input("Enter numbers separated by space: ").split()))
even_sum = sum(n for n in nums if n % 2 == 0)
print(f"Sum of even numbers: {even_sum}")

