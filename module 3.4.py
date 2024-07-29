a = []


def single_root_words(root_word, *other_words):
    for i in other_words:
        i = str(i).upper()
        root_word = str(root_word).upper()
        if i.count(root_word) > 0:
            a.append(i)
        if root_word.count(i) > 0:
            a.append(i)
    #        print(i)
    #        print(root_word)
    print(a)


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
