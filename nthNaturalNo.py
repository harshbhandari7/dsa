N=int(input())
nth=""
while(N):
    nth=str(N%9)+nth
    N=N//9
print(int(nth))