def main():
    id = list(map(int, input().split()))
    n, a, b = id[0], id[1], id[2]
    print(2 * n * a * b)

if __name__ == '__main__':
    main()