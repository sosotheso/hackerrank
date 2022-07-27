def count_substring(string, sub_string):
    sub_len = len(sub_string)
    str_len = len(string)
    count = 0
    for i in range(0, str_len - sub_len + 1):
        if string[i:i + sub_len] == sub_string:
            count = count + 1

    return count

