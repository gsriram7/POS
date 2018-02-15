def split_word_from_tag(token):
    splits = str(token).rsplit("/", 1)
    return (splits[0], splits[1])