#HackerRank
#TextWrap
import textwrap

def wrap(string, max_width):
    if max_width > len(string):
        a = textwrap.TextWrapper(string, max_width)
        a.break_long_words(max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
