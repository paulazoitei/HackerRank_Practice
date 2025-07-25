n=int(input())
lista=[]
for i in range(n):
    a,b=map(str,input().split())
    lista.append([a,b])


for i in lista:
    try:
        print(int(i[0])//int(i[1]))
    except ZeroDivisionError as e:
        print ("Error Code:",e)
    except ValueError as e:
        print("Error Code:",e)
