def main():
    a = list(map(int, input().split()))
    a[0] = a[0] * 2
    print(max(2, (a[0] + a[1] - 1) // a[1])) 

if __name__ == '__main__':
    main()