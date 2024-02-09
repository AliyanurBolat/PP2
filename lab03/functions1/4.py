#4
def prime(nums):
    if nums < 2:
        return False
    for i in range(2, nums):
        if nums % i == 0:
            return False
    return True

def filter(num):
    return[nums for nums in num if prime(nums)]

a = input()
a_list = [int(nums)for nums in a.split()]

primeNum = filter(a_list)
print(primeNum)