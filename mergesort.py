def swap(l, i, j):
    if i != j:
        l[i], l[j] = l[j], l[i]

def merge(l, start, mid, end):
    p, q = start, mid+1
    temp = [0 for _ in range((end-start)+1)]
    k = 0

    while k <= end-start:
        if p > mid:
            temp[k] = l[q]
            q += 1
        elif q > end:
            temp[k] = l[p]
            p += 1
        elif l[p] > l[q]:
            temp[k] = l[q]
            q += 1
        else:
            temp[k] = l[p]
            p += 1

        k += 1

    l[start:end+1] = temp

def mergesort(l, start, end):
    if start < end:
        mid = (start + end) // 2
        mergesort(l, start, mid)
        mergesort(l, mid+1, end)
        merge(l, start, mid, end)

def main():
    l = [10, 7, 1, 3, 8, 9, 9, 1, 1, 4]
    mergesort(l, 0, 1)
    print(l)

if __name__ == '__main__':
    main()