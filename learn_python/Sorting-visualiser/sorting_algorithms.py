import random, time
import pygame

import values as v

status_continue = True

class Algorithm():
    def __init__(self, alg_name):
        self.name = alg_name
        self.array = random.sample(range(v.height), v.height)

    def update(self, a=None, b=None):
        import main
        main.update_screen(self, a, b)
        
    def play(self):
        self.start_time = time.time()
        self.update()
        self.algorithm()
        self.update()
        self.after_info()

    def after_info(self):
        import main
        main.show_info()


class BubbleSort(Algorithm):
    def __init__(self):
        super().__init__("BubbleSort")

    def algorithm(self):
        n = len(self.array) 
        for i in range(n-1): 
            for j in range(0, n-i-1): 
                if self.array[j] > self.array[j+1]: 
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
                if status_continue == False: return None
                self.update(self.array[j], self.array[j-1])


class QuickSort(Algorithm):
    def __init__(self):
        super().__init__("QuickSort")

    def algorithm(self):
        try:
            # Hoare partition scheme
            def _quicksort(low, high):
                if low < high: 
                    p = partition(low, high)
                    _quicksort(low, p)
                    _quicksort(p+1, high)

            def partition(low, high):
                pivot = self.array[low]
                while True:
                    while self.array[low] < pivot:
                        low += 1
                    while self.array[high] > pivot:
                        high -= 1
                    if low >= high:
                        return high
                    self.array[low], self.array[high] = self.array[high], self.array[low]
                    low += 1
                    high -= 1
                    if status_continue == False: return None
                    self.update(self.array[low], self.array[high])
            _quicksort(0, len(self.array)-1)
        except:
            pass


class InsertionSort(Algorithm):
    def __init__(self):
        super().__init__("InsertionSort")

    def algorithm(self):
        for i in range(1, len(self.array)): 
            key = self.array[i] 
            j = i-1
            while j >= 0 and key < self.array[j] : 
                    self.array[j+1] = self.array[j] 
                    j -= 1
            self.array[j+1] = key
            if status_continue == False: return None
            self.update(key, j)

# Don't try this one
class BogoSort(Algorithm):
    def __init__(self):
        super().__init__("BogoSort")

    def algorithm(self):
        def _bogosort():
            random.shuffle(self.array)
            for i, j in enumerate(self.array):
                if i != j:
                    if status_continue == False: return None
                    self.update(i, j)
                    _bogosort()
        _bogosort()


class CocktailSort(Algorithm):
    def __init__(self):
        super().__init__("CocktailSort")

    def algorithm(self):
        for i in range(len(self.array)//2):
            swap = False
            for j in range(1+i, len(self.array)-i):
                if self.array[j] < self.array[j-1]:
                    self.array[j], self.array[j-1] = self.array[j-1], self.array[j]
                    swap = True
                    if status_continue == False: return None
                    self.update(self.array[j], j)
            if not swap: break
            swap = False
            for j in range(len(self.array)-i-1, i, -1):
                if self.array[j] < self.array[j-1]:
                    self.array[j], self.array[j-1] = self.array[j-1], self.array[j]
                    swap = True
                    if status_continue == False: return None
                    self.update(self.array[j], j)
            if not swap: break


class ShellSort(Algorithm):
    def __init__(self):
        super().__init__("ShellSort")

    def algorithm(self):
        n = len(self.array)
        gap = int(n/2)
        while gap > 0: 
            for i in range(gap,n): 
                temp = self.array[i] 
                j = i 
                while  j >= gap and self.array[j-gap] >temp: 
                    self.array[j] = self.array[j-gap] 
                    j -= gap
                if status_continue == False: return None
                self.update(self.array[j], self.array[temp])
                self.array[j] = temp 
            gap /= 2
            gap = int(gap)


class GnomeSort(Algorithm):
    def __init__(self):
        super().__init__("GnomeSort")

    def algorithm(self):
        idx = 0
        while idx < len(self.array):
            if idx == 0:
                idx += 1
            if self.array[idx] >= self.array[idx - 1]:
                idx += 1
            else:
                self.array[idx], self.array[idx-1] = self.array[idx-1], self.array[idx]
                if status_continue == False: return None
                self.update(self.array[idx], self.array[idx-1])
                idx -= 1

class RadixSort(Algorithm):
    def __init__(self):
        super().__init__("RadixSort")

    def algorithm(self):
        def countingSort(exp1): 
            n = len(self.array)
            output = [0] * (n)
            count = [0] * (10)
            for i in range(0, n): 
                index = (self.array[i]/exp1) 
                count[int((index)%10)] += 1
            for i in range(1,10): 
                count[i] += count[i-1]
            i = n-1
            while i>=0: 
                index = (self.array[i]/exp1) 
                output[count[int((index)%10)]-1] = self.array[i] 
                count[int((index)%10)] -= 1
                i -= 1
            i = 0
            for i in range(0,len(self.array)): 
                self.array[i] = output[i]
                if status_continue == False: return None
                self.update(self.array[i])
        def radixsort():
            max1 = max(self.array)
            exp = 1
            while max1/exp > 0: 
                countingSort(exp) 
                exp *= 10
                for i, j in enumerate(self.array):
                    if i != j: break
                    else: return None
        radixsort()
