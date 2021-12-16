def partition(nums, low, high):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1
        j -= 1
        while nums[j] > pivot:
            j -= 1
        if i >= j:
            return j
        nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)
    return nums


def convert_in_list():
    with open("words_list.txt", "r") as f:
        a_list = []
        b_list = []
        for item in f:
            item = item.split("\n", 1)[0]
            a_list.append(item)
            b_list.append(len(item))

    print(f"{a_list}\n")
#    print(b_list)
    return a_list, b_list

a, b = convert_in_list()
b = quick_sort(b)
#print(b)
c = []
for q in b:
    for i in a:
        if len(i) == q:
            if i in c:
                None
            else:
                c.append(i)
print(c)
