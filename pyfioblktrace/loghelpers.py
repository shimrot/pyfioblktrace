#!/usr/bin/env python3

import sys, pprint

# Global methods and vars defining the application environment
pp = pprint.PrettyPrinter(indent=4, width=100, compact=True)


def eprint(*args, **kvargs):
    print(*args, file=sys.stderr, **kvargs)


def CurFuncName():
    return sys._getframe(1).f_code.co_name


class Lazy(object):
    """
    Use with logging to prevent message string from being expanded unless used.
    Otherwise the arguments may always be expanded, even if not being printed,
    which can have significant performance impacts.

    For example::
        logger.debug(Lazy(lambda: "some {} text {} with expansions".format("stuff", "replace")))

    of course with logger with this simple example you could do this instead::
        logger.debug("some %s text %s with expansions", "stuff", "replace")

    but it doesn't apply when the arguments require more complicated  evaluations
    """
    def __init__(self,func):
        self.func = func
    def __str__(self):
        return self.func()


