"""
https://stepik.org/lesson/41234/step/1?unit=19818

Вы разрабатываете текстовый редактор для программистов и хотите реализовать проверку корректности
расстановки скобок. В коде могут встречаться скобки []{}(). В случае, если скобки расставлены неправильно,
редактор должен также сообщить пользователю первое место, где обнаружена ошибка.

В первую очередь необходимо найти закрывающую скобку, для которой либо нет соответствующей открывающей
(например, скобка "]" в строке “]()”), либо же она закрывает не соответствующую ей открывающую скобку
(пример: "()[}"). Если таких ошибок нет, необходимо найти первую открывающую скобку,
для которой нет соответствующей закрывающей (пример: скобка "(" в строке “{}([]”).

Помимо скобок, исходный код может содержать символы латинского алфавита, цифры и знаки препинания.

Формат входа. Строка s[1...n], состоящая из заглавных и прописных букв латинского алфавита, цифр,
знаков препинания и скобок из множества []{}().

Формат выхода. Если скобки в s расставлены правильно, выведите
строку “Success". В противном случае выведите индекс (используя индексацию с единицы) первой закрывающей скобки, для
которой нет соответствующей открывающей. Если такой нет,
выведите индекс первой открывающей скобки, для которой нет
соответствующей закрывающей.
"""


def brackets(s: str) -> int | None:
    """Решение задачи о проверке корректности расстановки скобок. Сложность O(N)"""
    open_brackets, close_brackets = "([{", ")]}"
    d = dict(zip(open_brackets, close_brackets))
    stack = []

    for i, c in enumerate(s):
        if c in open_brackets:
            stack.append(i)
        elif c in close_brackets:
            if stack and c == d[s[stack[-1]]]:
                stack.pop()
            else:
                return i + 1

    result = (stack.pop() + 1) if stack else None

    return result