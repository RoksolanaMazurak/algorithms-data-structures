def generate_shift_table(pattern):
    skip_list = {}
    for i in range(0, len(pattern)):
        skip_list[pattern[i]] = max(1, len(pattern) - i - 1)
    return skip_list


def boyer_moore_search(source, pattern):
    bad_char = generate_shift_table(pattern)
    print(bad_char)
    i = len(pattern) - 1
    answer = []
    while i <= len(source) - 1:
        j = 0
        while j < len(pattern) and pattern[len(pattern) - j - 1] == source[i - j]:
            j += 1
        if j == len(pattern):
            answer.append(i - len(pattern) + 1)
            i += 1
            continue
        else:
            shift = bad_char.get(source[i + j], len(pattern))
            if shift == 0:
                shift = len(pattern) - 1

            skips = shift - j

            i += skips
    return answer

#
# txt = "PAAAAAAAAAAAAA"
# pat = "PAAAAAK"
# print(boyer_moore_search(txt, pat))



