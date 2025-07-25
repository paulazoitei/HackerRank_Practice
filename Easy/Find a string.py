def count_substring(string, sub_string):
    lista = []
    a = len(sub_string)
    for i in range(0, len(string)):
        if len(string[i:a]) == len(sub_string):
            lista.append(string[i:a])
            a += 1
    return lista.count(sub_string)


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)