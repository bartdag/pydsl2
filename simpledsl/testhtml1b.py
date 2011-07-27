from simpledsl.html import *

# Using the tuple syntax, we can indent as much as we want as long as we
# use commas between tags.
# Biggest limitation: we cannot embed control structures like if and for.

(
t.html,
    t.head,
        t.title,
        s("This is the title"),
        t._title,
    t._head,

    t.body,
    s("This is the body"),
    t.ul,
        t.li,
        s("This is the only item."),
        t._li,
    t._ul,
    t._body,

t._html,
)
