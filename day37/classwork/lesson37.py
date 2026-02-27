gela=[1,2,3,4,5,6]

def my_len(iterable):
    count = 0
    for i in iterable:
        count += 1
    return count

print(my_len(gela))



for i in range(5):
    print(i)



def len_clone(colection):
    if str != type(colection) != list:
        return "Error: Invalid arguments(function takes only str or list)"

    result = 0

    for _ in colection:
        result += 1
    return result

print(len_clone(True))



def find_clone(text, symbol, start_index = 0):
    for i in range(start_index, len(text)):
        if text[i] == symbol:
            return i
    return -1

print(find_clone("abcdabcd", "a", 5))