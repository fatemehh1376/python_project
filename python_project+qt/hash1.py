# defining hash function


def HASH(sth):
    new = str(sth).upper()[2:8]
    return ascii(new)
