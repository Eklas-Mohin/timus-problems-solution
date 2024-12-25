def main():
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    print(a[0] - c[0], a[1] - b[1])

if __name__ == '__main__':
    main()