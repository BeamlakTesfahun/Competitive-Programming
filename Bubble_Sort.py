def countSwaps(a):
    # Write your code here
    tSwaps = 0
    for i in range(0,len(a)-1):
        nSwaps = 0
        for j in range (0,len(a)-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                nSwaps += 1
                tSwaps += 1
        if nSwaps == 0:
            break
    print('Array is sorted in {} swaps.'.format(tSwaps))
    print('First Element: {}'.format(a[0]))
    print('Last Element: {}'.format(a[len(a)-1]))
if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    countSwaps(a)
