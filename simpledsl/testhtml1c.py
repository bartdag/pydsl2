from simpledsl.html import *

# Here, we use functions to use control statements.
# The HTML document is still defined in a tuple at.

def HEADER():
    (
    t.head,
        t.title,
        s("This is the title"),
        t._title,
    t._head,
    )


def LIST_ITEMS():
    t.ul
    for i in range(10):
        t.li
        s("This is the item {0}".format(i))
        t._li
    t._ul


def FOOTER():
    t.hr_
    t.p, s("This is the footer"), t._p

(
t.html,
    HEADER(),

    t.body,
    t.p, s("This is the body"), t._p,

    LIST_ITEMS(),
    
    FOOTER(),

    t._body,

t._html,
)
