def main():
    n = int(input())
    srr = []
    cnt = 0
    ans = ''

    for i in range(n):
        s = input()
        srr.append(s)

    for string in srr:
        k = srr.count(string)
        if k > cnt:
            cnt = k
            ans = string
    print(ans)

if __name__ == '__main__':
    main()
