def main():
    n = int(input())
    matrix = [[0] * n] * n
    output = []

    for i in range(n):
        lst = list(map(int, input().split()))
        matrix[i] = lst
    
    for i in range(2 * n - 1):
        if i < n:
            j = i
            k = 0
            while j >= 0:
                output.append(matrix[j][k])
                j = j - 1
                k = k + 1
        else:
            j = n - 1
            k = i - n + 1
            t = k
            while j >= k:
                output.append(matrix[j][t])
                j = j - 1
                t = t + 1

    print(*output)

if __name__ == '__main__':
    main()