from simpledsl.html2 import *

(
t.html,
    t.head,
        t.title, s('This is the title'), t._title,
    t._head,

    t.body,

        t.p,
            s('This a link you should look at: '),
            t.a(href="http://www.google.com", title="Search Engine"),
                s('google search'),
            t._a,
        t._p,
        t.br_(unknown="impossible"),
    t._body,
t._html,
)

finish()
