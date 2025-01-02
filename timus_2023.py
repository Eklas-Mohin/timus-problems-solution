def main():
    n = int(input())
    cnt, cp, ans = 0, 1, 0
    
    for i in range(n):
        s = input()
        if s[0] == 'A' or s[0] == 'P' or s[0] == 'R' or s[0] == 'O':
            ans = ans + abs(cp - 1)
            cp = 1
        elif s[0] == 'B' or s[0] == 'M' or s[0] == 'S':
            ans = ans + abs(cp - 2)
            cp = 2
        else:
            ans = ans + abs(cp - 3)
            cp = 3

    print(ans)

if __name__ == '__main__':
    main()