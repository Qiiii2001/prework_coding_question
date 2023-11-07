def is_consecutive(a_list):
    for x in range(len(a_list)-1):
        if abs(a_list[x+1]- a_list[x]) != 1:
            return False
    return True

print(is_consecutive([1,2,4,4,4,5]))
print(is_consecutive([1,2,3,4,5]))
print(is_consecutive([5,4,3,2,1]))
