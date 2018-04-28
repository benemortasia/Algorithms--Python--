#!/usr/bin/env python2


# Takes some string s that looks like "abccbaabccba"
# returns the number of pieces that can be equally cut.
# returns 1 if the string can't be totally cut
# returns 0 if the string is empty or non-alphabetic
def Answer(s):
    s = s.strip()

    # edge cases
    if not s or not s.isalpha():
        return 0

    str1 = ''

    # str1 will build like this:
    # 'a', 'ab', 'abc', 'abcc', 'abccb', etc
    # and attempt to fully replace the original string
    for c in s:
        str1 += c
        if s.replace(str1, '') == '':
            return len(s) / len(str1)

    # something weird happened.. return 0
    return 0


print Answer('abccbaabccba')
print Answer('aaaaaaaaaaaa')
print Answer('              ')
print Answer('    abcabcabcabcabc     ')
print Answer('abbaabbaabbaabba')
print Answer('3462')
print Answer('aaabbaaabbaaabb')
print Answer('abcdefedcbaabcdedefdefbbabcabcabcedcba')
