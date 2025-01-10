# Find the second largest number in list... O(n log n):

example_list = [1, 5, 6, 0, 19, -1, -56, 78, 3, 12, 44, 5]

second_largest_num = list(sorted(example_list))[-2]

print(second_largest_num)