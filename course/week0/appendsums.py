def appendsums(lst): 
    sum = 0
    for i in range(25):
        sum = lst[len(lst)-1] + lst[len(lst)-2] + lst[len(lst)-3]
        lst.append(sum)
    return lst

sum_three = [0, 1, 2]
appendsums(sum_three)
print(sum_three[10])
print(sum_three)

