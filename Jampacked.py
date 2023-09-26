n, k, b = map(int, input().split())


boxes = (n + k - 1) // k


jars_in_least_filled_box = (n + boxes - 1) // boxes

print(jars_in_least_filled_box)