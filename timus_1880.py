def main():
    n1 = int(input())
    lst1 = list(map(int, input().split()))
    n2 = int(input())
    lst2 = list(map(int, input().split()))
    n3 = int(input())
    lst3 = list(map(int, input().split()))
    eigenvalues = 0

    for i in range(n1):
        if lst1[i] in lst2 and lst1[i] in lst3:
            eigenvalues += 1 

    print(eigenvalues)

if __name__ == '__main__':
    main()