def _graph(obj):
    if obj is None:
        return repr(obj)
    if hasattr(obj, "__graph__"):
        if callable(obj.__graph__):
            return obj.__graph__()
        else:
            return repr(obj.__graph__)
    else:
        raise AttributeError(f"Object {obj} does not implement __graph__()")

def graph(obj):
    print(_graph(obj))

