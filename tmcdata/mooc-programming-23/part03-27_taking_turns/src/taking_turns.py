num = int(input("Please type in a number: "))
i = 1
nums = []

while i <= num:
    nums.append(i)
    i += 1

j = 0
k = -1
limit = num // 2

if num % 2 == 0: #par
    while j <= limit and k >= -limit:
        print (nums[j])
        print (nums[k])
        j += 1
        k -= 1

elif num % 2 != 0: #impar
    while j <= limit and k >= -limit:
        #print(f"j {j}")
        print (nums[j])
        #print(f"k {k}")
        print (nums[k])
        j += 1
        k -= 1
    print(nums[j])