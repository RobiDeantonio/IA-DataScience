def is_palindrome(string: str) -> bool:
    string = string.replace(' ', '').lower()
    return string == string[::-1]


def run():
    print(is_palindrome(1000))



if __name__ == '__main__':
    run()


## Execute mypy 01\ Static_typing.py --check-untyped-defs