def max_num_in_list(a_list):
    max = 0
    for item in a_list:
        if max<item:
            max = item
    return max

print(max_num_in_list([1,2,3,4,5,6,10]))
