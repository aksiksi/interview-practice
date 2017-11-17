# Practice on sorting algorithms
import random

def swap(l, i, j):
    if i != j:
        l[i], l[j] = l[j], l[i]

def part(l, lo, hi):
    pivot = l[hi]
    i = lo

    for j in range(lo, hi):
        if l[j] < pivot:
            swap(l, i, j)
            i += 1

    if l[hi] < l[i]:
        swap(l, i, hi)

    return i

def quicksort(l, lo, hi):
    if lo < hi:
        p = part(l, lo, hi)
        quicksort(l, lo, p-1)
        quicksort(l, p+1, hi)

def main():
    # Test quicksort 1000 times
    count = 0

    for _ in range(1000):
        l = [random.randrange(1, 1000) for _ in range(random.randrange(10, 100))]
        pre_sorted = list(sorted(l))
        quicksort(l, 0, len(l)-1)

        if l == pre_sorted:
            count += 1

    print("Correct {0}/1000 times.".format(count))

if __name__ == '__main__':
    main()
    