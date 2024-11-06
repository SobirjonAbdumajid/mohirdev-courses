def toliq_ism(ism, familiya, otasi=''):
    if otasi:
        return f'{ism} {familiya} {otasi}'.title()
    else:
        return f'{ism} {familiya}'.title()
