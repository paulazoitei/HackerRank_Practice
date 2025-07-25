if __name__ == '__main__':
    commands=[]
    lista=[]
    N = int(input())
    for _ in range(N):
        a=str(input())
        lista.append(a)
    for i in lista:
        parts = i.split()
        operation = parts[0]
        if operation == "insert":
            parts = i.split()
            index = int(parts[1])
            value = int(parts[2])
            commands.insert(index, value)
        elif operation=="print":
            print(commands)
        elif operation == "remove":
            parts = i.split()
            index = int(parts[1])
            commands.remove(index)
        elif operation == "append":
            parts = i.split()
            index = int(parts[1])
            commands.append(index)
        elif operation == "sort" :
            commands.sort()
        elif operation == "pop" :
            commands.pop()
        elif operation == "reverse" :
            commands.reverse()
