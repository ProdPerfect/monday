def url_join(base, *args):
    path = '/'.join([str(i) for i in args])
    return f'{base}/{path}'
