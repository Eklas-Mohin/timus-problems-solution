def main():
    string = input()
    one ='adgjmpsvy.'
    two = 'behknqtwz,'
    ans = 0

    for char in string:
        if char in one or char == ' ':
            ans += 1
        elif char in two:
            ans += 2
        else:
            ans += 3
    
    print(ans)

if __name__ == '__main__':
    main()
