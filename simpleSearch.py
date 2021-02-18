# 단순탐색
# 그냥 포문돌려서 이프문으로 비교하는거... 별거없음...

arr = [arr+1 for arr in range(100000)]

def simpleSearch(arr,number):

    for idx in range(0,len(arr)):
        if number is arr[idx]:
            return "몇번째냐면",idx,"번째"
    return -1

print(simpleSearch(arr,15))