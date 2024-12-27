def main():
    n = int(input())
    ans = 200

    for _ in range(n):
        string = input().strip()
        if '+one' in string:
            ans += 200
        else:
            ans += 100

    if ans == 1300:
        ans += 100

    print(ans)
    
if __name__ == '__main__':
    main()