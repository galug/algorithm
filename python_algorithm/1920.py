import sys

n= int(sys.stdin.readline())
# set를 이용시 O(1) 으로 탐색 가능 
fl = set(map(int,sys.stdin.readline().split()))
k  = int(sys.stdin.readline())
sl = list(map(int,sys.stdin.readline().split()))
# binary_search 를 통해서 찾을 수 있는 줄 알았음
def binary_search(l:[],k:int) -> ():
    low = 0
    high = len(l)-1
    while low<=high:
        mid = (low+high)//2
        if l[mid] ==k:
            print(1)
            return
        elif l[mid] > k:
            high = mid-1
        else:
            low = mid+1
    print(0)

for ele in sl:
    if ele in fl:
        print(1)
    else:
        print(0)