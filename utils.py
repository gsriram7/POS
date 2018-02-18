def split_word_from_tag(token):
    splits = str(token).rsplit("/", 1)
    return (splits[0], splits[1])


def get_or_default(dict, keys, default):
    res = default
    d = dict
    try:
        for k in keys:
            res = d[k]
            d = d[k]
    except KeyError:
        return default
    return res
