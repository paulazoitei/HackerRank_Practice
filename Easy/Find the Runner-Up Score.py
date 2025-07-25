def find_runner_up(lista):
    lista = list(lista)
    scoruri_unice = set(lista)
    scoruri_unice.remove(max(scoruri_unice))
    return max(scoruri_unice)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(find_runner_up(arr))
