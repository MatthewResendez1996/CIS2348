#Matthew Resendez
#1431242
def selection_sort_descend_trace(number):
    for i in range(len(number)-1):
        ind = i
        for j in range(i + 1, len(number)):
            if number[ind] < number[j]:
                ind = j
        number[i], number[ind] = number[ind], number[i]
        for x in number:
            print(x,end=" ")
        print()
    return number

if __name__ == "__main__":
    numbers = [int(x) for x in input("").split()]
    selection_sort_descend_trace(numbers)
