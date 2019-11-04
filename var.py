"""
Just a module with a single global variable and function to increment.
"""


foo = 1

def increment():
    global foo
    foo += 1