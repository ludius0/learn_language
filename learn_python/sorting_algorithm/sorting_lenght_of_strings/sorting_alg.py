def convert_in_list():
    with open("words_list.txt", "r") as f:
        a_list = []
        for item in f:
            item = item.split("\n", 1)[0]
            a_list.append(item)

    print(f"{a_list}\n")
    return a_list

a = convert_in_list()
a.sort(key = len)
print(a)
