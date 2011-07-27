def s(val):
    print(val, end="")


class tag:
    def __getattr__(self, name):
        if name.startswith('_'):
            print('</{0}>'.format(name[1:].lower()))
        elif name.endswith('_'):
            print('\n<{0}/>'.format(name[:-1].lower()), end="")
        else:
            print('\n<{0}>'.format(name.lower()), end="")
        return None

t = tag()
 
