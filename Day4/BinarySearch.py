class BinarySearch(list):
    """BinarySearch class
    """
    def __init__(self, a, b):
        super().__init__()

        for i in range(1, a+1):
            self.append(i * b)

        self.length = a

    def search(self, num):
        first = 0
        last = len(self) - 1
        num_index = 0
        found = False
        counter = 0

        if num == self[first]:
            num_index = first
            found = True
        elif num == self[last]:
            num_index = last
            found = True

        if num not in self:
            found = True
            num_index = -1

        while first <= last and not found:
            mid = (first + last) // 2
            if self[mid] == num:
                found = True
                num_index = mid
            else:
                counter += 1
                if num < self[mid]:
                    last = mid - 1
                else:
                    first = mid + 1

        return {'count': counter, 'index': num_index}