

def importText(fname):
    with (open(fname, 'r',encoding='utf8')) as f:
        return f.read()
