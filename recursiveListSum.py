def recurListSum(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] + recurListSum(list[1:])
    
list1 = [1, 3, 5, 6, 8]

print( recurListSum(list1) )
