#Task
#The provided code stub reads an integer, n, from STDIN. For all non-negative integers i<n, print i^2.

if __name__ == '__main__':
    n = int(input())
    i = 0
    while(i < n):
        print(i**2)
        i+=1
