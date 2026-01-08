
def get_max_recursive (numbers) :
    if len(numbers) == 0 :
        return None
    elif len(numbers) == 1 :
        return numbers[0]
    else :
        return max(numbers[0], get_max_recursive(numbers[1:]))
    

print(get_max_recursive([7, 9, 10, 9999, 0]))