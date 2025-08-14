class Jar:
    def __init__(self, capacity=12):
        self.set_size(0)
        if not (capacity >= 0):
            raise ValueError
        else:
            self._capacity = capacity




    def __str__(self):
        text = ''
        for i in range(self._size):
            text += '🍪'
        return text


    def deposit(self, n):
        if self.get_size() + n <= self.capacity:
            self.set_size(self.get_size() + n)
        else:
            raise ValueError('Too many cookies')


    def withdraw(self, n):
        if self.get_size() >= n:
            self.set_size(self.get_size() - n)
        else:
            raise ValueError('Not enough cookies')

    def set_capacity(self, n):
        if not (n >= 0):
            raise ValueError
        else:
            self._capacity = n

    def set_size(self, n):
        self._size = n

    def get_size(self):
        return(self._size)

    def get_capacity(self):
        return(self._capacity)



    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


