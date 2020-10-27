def add_explanation(line):
    return line + '!'

update_line = add_explanation
print(update_line("Hello World"))


def beautify(text):
    return text + '!!!'

def make_line(func, words):
    return "Hello " + func(words)
print(make_line(beautify, "world"))
#আর্গুমেন্ট বা চাহিদা
