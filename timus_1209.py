import math

def main():
    n = int(input())
    ans = ''

    for _ in range(n):
        k = int(input())
        t = k - 1
        x = (-1 + math.sqrt(1 + 8 * t)) // 2
        x = (x * (x + 1)) // 2
        if x == k - 1:
            ans = ans + '1 '
        else:
            ans = ans + '0 '
        
    print(ans.strip())

if __name__ == '__main__':
    main()