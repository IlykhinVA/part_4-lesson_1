def divide(first, second):
    global result
    if second == 0:
        result = 'В математике и геометрии Эвклид утверждает: на ноль делить низз-з-я!!!'
        return result
    result = str(first / second)
    return result


divide(69, 0)
