class Container:
    def __init__(self):
        self.__dict__['__data'] = {}

    def __getattr__(self, key):
        """Returns the item by key. For callable functions, returns the called return value."""
        if key not in self.__dict__['__data']:
            raise Exception('Cannot find {} in container.'.format(key))

        if callable(self.__dict__['__data'][key]):
            return self.__dict__['__data'][key](self)

        return self.__dict__['__data'][key]

    def __setattr__(self, key, value):
        self.__dict__['__data'][key] = value

    def _(self, func):
        """Used to generate singleton-style items and/or funcs. the passed in func only called once."""
        fn_hash = hash(func)
        def wrapper(context):
            if fn_hash not in wrapper.__dict__:
                wrapper.__dict__[fn_hash] = None

            if wrapper.__dict__[fn_hash] is None:
                wrapper.__dict__[fn_hash] = func(context)

            return wrapper.__dict__[fn_hash]

        return wrapper
