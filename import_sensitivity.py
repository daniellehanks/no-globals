import sys


def clear_imports():
    # Don't ever do this in real code!
    sys.modules.pop("var", None)
    sys.modules.pop("evil_modifier_one", None)
    sys.modules.pop("evil_modifier_two", None)


def straight_import():
    print("straight")
    import var

    print(f"Foo before increment: {var.foo}")
    var.increment()
    print(f"Foo after increment: {var.foo}")
    clear_imports()


def from_import():
    print("from")
    from var import foo
    from var import increment

    print(f"Foo before increment: {foo}")
    increment()
    print(f"Foo after increment: {foo}")
    clear_imports()


def import_order_one():
    print("import order one")
    import var
    import evil_modifier_one
    import evil_modifier_two
    print(f"Foo: {var.foo}")
    clear_imports()


def import_order_two():
    print("import order two")
    import var
    import evil_modifier_two
    import evil_modifier_one
    print(f"Foo: {var.foo}")
    clear_imports()
