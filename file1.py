# Problem Statement
# -----------------
# A Four digit number is guessed and some clues about the number are give below
# 9285 ------ one number is correct wrong placed
# 1937 ------ two number is correct wrong placed
# 5201 ------ one number is correct and well placed
# 6507 ------ nothing correct
# 8524 ------ two numbers are correct and wrong placed
# Guess the number

# Answer 3841

def check1(nums, lst):
    # check if any number is correct and all other number is false
    for i in range(len(lst)):
        current_element = lst[i]
        if lst[i] == nums[i]:
            return False
        if current_element in nums and any(lst[j] in nums for j in range(len(lst)) if j != i):
            return False
    return True


def check2(nums, lst):
    # check if any two number is correct and other two number is false
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i] in nums and lst[j] in nums and all(lst[k] not in nums for k in range(len(lst)) if k != i and k != j):
                if lst[i] == nums[i] or lst[j] == nums[j]:
                    return False
                return True
    return False

def check3(nums, lst):
    # check if any number is correct and all other number is false and also check the position of correct digit matches the place
    for i in range(len(lst)):
        if nums[i] == lst[i]:
            for j in range(len(lst)):
                if j != i and lst[j] in nums:
                    return False
            return True
    return False

for i in range(1000, 10000):
    a = i
    first = a % 10
    a = a//10
    second = a % 10
    a = a//10
    third = a % 10
    a = a//10
    fourth = a % 10
    nums = [fourth, third, second, first]

    # Eliminating 6,5,0,7
    falseflag = False
    for j in nums:
        if j in [6, 5, 0, 7]:
            falseflag = True
            break
    if (falseflag == True):
        continue

    if check3(nums, [5, 2, 0, 1]) and check2(nums, [1, 9, 3, 7]) and check2(nums, [8, 5, 2, 4]) and check1(nums, [9, 2, 8, 5]):
        print("Guessed Value:",i)
