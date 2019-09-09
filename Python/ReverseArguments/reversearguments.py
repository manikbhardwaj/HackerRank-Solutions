from functools import wraps


def reversed_args(f):
    @wraps(f)
    def g(*args):
        return f(*args[::-1])

    return g


int_func_map = {
    'pow': pow,
    'cmp': cmp,
}

string_func_map = {
    'join_with': lambda separator, *args: separator.join(args),
    'capitalize_first_and_join': lambda first, *args: ''.join([first.upper()] + list(args)),
}

queries = int(raw_input())
for _ in range(queries):
    line = raw_input().split()
    func_name, args = line[0], line[1:]
    if func_name in int_func_map:
        args = map(int, args)
        print
        reversed_args(int_func_map[func_name])(*args)
    else:
        print
        reversed_args(string_func_map[func_name])(*args)
