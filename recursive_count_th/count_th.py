'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    # TBC
    count = 0
    if "th" in word:
        count += 1
        count += count_th(word.replace('th', 'ooo', 1))
        return count 
    else:
        return count


print(count_th(""))
