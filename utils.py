def split_word_from_tag(token):
    if (token[-1] == '/'):
        tag = '/'
        word = token[:-2]
        return (word, tag)

    else:
        splits = token.split('/')
        tag = splits[-1]
        len_of_tag = len(tag) + 1
        word = token[:(-len_of_tag)]
        return (word, tag)