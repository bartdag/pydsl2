from collections import deque

class Tags:
    def __init__(self):
        self.stack = deque()

    def __getattr__(self, name):
        new_name = name.lower()
        if name.startswith('_'):
            self.stack.append('</{0}>\n'.format(new_name[1:]))
        elif name.endswith('_'):
            self.stack.append('\n<{0}/>'.format(new_name[:-1]))
        else:
            self.stack.append('\n<{0}>'.format(new_name))
        return Tag(new_name, self.stack)


class Tag:
    def __init__(self, name, stack):
        self.name = name
        self.stack = stack

    def __call__(self, *args, **kargs):
        # Prevent goofs!
        if self.name.startswith('_') or self.name.endswith('_'):
            return

        self.stack.pop()
        tag = '<{0} '.format(self.name)
        for key in kargs:
            tag += '{0}="{1}" '.format(key, kargs[key])
        tag = tag[:-1] + '>'
        self.stack.append(tag)

t = Tags()

def s(val):
    t.stack.append(val)

def finish():
    for item in t.stack:
        print(item, end="")
