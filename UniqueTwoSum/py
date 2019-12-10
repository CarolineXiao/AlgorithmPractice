
def twoSum(nums, target):

    num_dict = {}
    r = 0;
    r_list = list();
        
    for i in range(len(nums)):
        sub = target - nums[i]
        if sub not in num_dict:
            num_dict[nums[i]] = i
        else:
            if sub not in r_list:
                r += 1;
                r_list.append(sub);
                r_list.append(nums[i]);
    return r;

if __name__ == '__main__':
    a = twoSum([1, 1, 2, 45, 46, 46], 47)
    print(a)
    b = twoSum([1, 1], 2)
    print(b)
    c = twoSum([1, 5, 1, 5], 6)
    print(c)
    
# Complexity: O(n)
