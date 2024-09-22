def divide(first, second):
    global result
    if second == 0:
        result = 'Однако, Лобачевский и Эйнштейн предполагают, что на ноль делить мона-а!!!'
        return result
    result = str(first / second)
    return result


divide(69, 0)
