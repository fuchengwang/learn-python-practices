def countfeq(s):
    l = [i for i in s.split('/') if i not in r'，。！”“']

    words = {}
    for w in l:
        words.setdefault(w, 0)
        words[w] += 1

    return words


if __name__ == "__main__":
    s = input()

    s_dict = countfeq(s)
    print(len(s_dict.keys()))
