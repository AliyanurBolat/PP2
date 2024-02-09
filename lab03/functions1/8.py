def spy_game(nums):
    zero1 = False
    zero2 = False
    for num in nums:
        if num == 0:
            if not zero1:
                zero1 = True
            elif zero1 and not zero2:
                zero2 = True
        elif num == 7:
            if zero1 and zero2:
                return True
    return False
# Test cases
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))
