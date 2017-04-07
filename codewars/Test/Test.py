class Test:
    @staticmethod
    def assert_equals(actual, expected):
        result = (actual == expected)
        print("Result from test:", result)
        return result


def reverseWords(str):
    return " ".join(list(reversed(list(str.split(" ")))))

print(reverseWords("Hello world!"))
