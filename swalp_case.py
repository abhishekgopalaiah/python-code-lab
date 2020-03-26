"""
input :
AbhIShek
output:
aBHisHEK

"""
def swap_case(s):
    swap = []
    for i in s:
        if i.isupper():
            swap.append(i.lower())
        else:
            swap.append(i.upper())

    return ''.join(swap)


if __name__ == '__main__':
    s = "AbhIShek"  # input()
    result = swap_case(s)
    print(result)
