def main():
    n = int(input())
    n = (n * (n + 1)) // 2

    if n % 2 == 0:
        print('black')
    else:
        print('grimy')
    
if __name__ == '__main__':
    main()
