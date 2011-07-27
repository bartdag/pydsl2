from simpledsl.html import *

# This is a mix of html tags with some python code.
# Simple, but a bit ugly since no indentation is possible.

t.html
t.head
t.title
s("This is the title")
t._title
t._head

t.body
s("This is the body")
t.ul
for i in range(10):
    t.li
    s("This is the item {0}".format(i))
    t._li
t._ul
t._body

t._html
