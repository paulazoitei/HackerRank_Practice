if __name__ == '__main__':
    s = input()
    alfanum=False
    alfa=False
    digit=False
    lower=False
    upper=False

    for i in s:
        if i.isalnum():
            alfanum=True
        if i.isalpha():
            alfa=True
        if i.isdigit():
            digit=True
        if i.islower():
            lower=True
        if i.isupper():
            upper=True
    print(alfanum)
    print(alfa)
    print(digit)
    print(lower)
    print(upper)


