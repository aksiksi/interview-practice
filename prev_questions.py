import collections

def str_mask(s, c):
    """
        Given a string of letters, implement method that outputs string of 1's and 0's of the same size corresponding
        to if a selected letter is in that position in the input string.
    """
    if len(s) == 0:
        return s

    mask = ""

    for each in s:
        if each == c:
            mask += '1'
        else:
            mask += '0'

    return mask

# TODO: implement a custom queue
class MultiIterator:
    def __init__(self, *iters):
        self.queue = collections.deque(iters)

    def __iter__(self):
        return self

    def __next__(self):
        it = self.queue.popleft()

        try:
            v = next(it)
            self.queue.append(it) # Put iterator back into queue
            return v
        except StopIteration:
            raise StopIteration

if __name__ == '__main__':
    a = iter(['a1', 'a2', 'a3'])
    b = iter(['b1', 'b2', 'b3'])
    c = iter(['c1', 'c2', 'c3'])
    mi = MultiIterator(a, b, c)

    for e in mi:
        print(e)
