calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string=""):
    global calls
    calls += 1
    tuple_ = len(string), string.upper(), string.lower()
    return tuple_


def is_contains(string="", list_to_search=[]):
    global calls
    calls += 1
    for i in list_to_search:
        new_list_ = i.upper()
    if string.upper() in new_list_:
        return True
    else:
        return False


print(string_info("Привет"))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
