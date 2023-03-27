def replace_ex(string: str, old: str, new: str) -> str:
    """Функция должна заменить в аргументе string включение old на new.
    Пример replace_ex('hello', 'e', 'o') -> 'hollo'
    """
    pass


assert replace_ex('123456', '123456', '000000') == '000000'
assert replace_ex('123456', '7', '000') == '123456'
assert replace_ex('123123123123', '123', 'x') == 'xxxx'
