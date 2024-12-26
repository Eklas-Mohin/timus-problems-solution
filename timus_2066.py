def main():
    a = int(input())
    b = int(input())
    c = int(input())
    nums = [a, b, c]
    nums.sort()

    ans = nums[0] - nums[1] - nums[2]
    ans = min(ans, nums[0] - nums[1] * nums[2])

    print(ans)
    
if __name__ == '__main__':
    main()