import greetings
greetings.greet("Alice")

from greetings import greet
greet("Bob")

from greetings import greet as say_hello
say_hello("Charlie")

import greetings as g
g.greet("Diana")


from greetings import *
greet("Eve")
