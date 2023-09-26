n = int(input())


num_digits = len(str(n))


total_signs = 0

for digit in range(10):
    signs_needed = n // 10 * 10
    if digit <= n % 10:
        signs_needed += 1
    total_signs += signs_needed

print(total_signs)