def main():
    inp = list(map(int, input().split()))
    x = inp[0] * inp[1]

    if x % 2:
        print('[second]=:]')
    else:
        print('[:=[first]')

if __name__ == '__main__':
    main()