def twoSum(nums, target):
    possibles = {}
    for i, number in enumerate(nums):
        if str(number) in possibles:
                return [possibles[str(number)], i] 
        diff = str(target - number)
        possibles[diff] = i
        
        

nums = [2,7,11,15]
print(twoSum(nums, 9))