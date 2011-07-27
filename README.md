PyDSL 2
=======

PyDSL is a collection of DSLs and DSL processors written in Python 3. My goal
is to see how far I can go on the DSL route without having to write my own
parser.

Why the 2? Because there is another PyDSL on github and I did not want the two
projects to be confused.


Contents
--------

Each directory in this project contains a set of DSLs that are limited by the
same set of constraints. For example, the *simpledsl* directory contains small
DSLs that can be embedded in any Python code.

Each directory contains a readme file that explains the dsls and the common
set of constraints.


SimpleDSL
---------

This collection of DSLs shows how far I could go with plain Python. There is
no regex, no text transformation, no pre-processing. This is pure, parsable,
Python code that does not look too much like Python!


Security Concerns
-----------------

Most DSLs proposed in PyDSL 2 can be abused by an attacker or a careless user
(infinite loop anyone?) and should not be used where security is a concern.
They are fine though for a development team or client-side scripting.


License
-------

This software is released under the BDS license. Please see the LICENSE file
for more information.
