def first_non_repeating_letter(s):
    S = s.upper()
    for i, j in enumerate(S):
        if S.count(j) == 1:
            return s[i]
    return ''


def first_non_repeating_letter2(s):
    return s[s.upper().index(''.join([x if s.upper().count(x) == 1 else '' for x in s.upper()])[0])]
