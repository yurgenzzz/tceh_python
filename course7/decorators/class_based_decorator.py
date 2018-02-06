#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functools


class MyDecorator(object):
    def __init__(self, argument):
        self.arg = argument

    def __call__(self, fn):
        @functools.wraps(fn)
        def decorated(*args, **kwargs):
            print('In my decorator before call, with arg {}'.format(self.arg))
            fn(*args, **kwargs)
            print('In my decorator after call, with arg {}'.format(self.arg))
        return decorated


class Foo(object):
    @MyDecorator("in Foo class!")
    def bar(self):
        print('in bar!')


@MyDecorator('some other func!')
def some_other_function():
    print('in some other function!')

Foo().bar()
some_other_function()

