def main():
    n = int(input())
    ans = (n * (n + 1)) // 2
    if n <= 0:
        ans = 1 + ((-n * (n - 1)) // 2)
    print(ans)

if __name__ == '__main__':
    main()