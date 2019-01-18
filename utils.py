def import_by_string(name: str) -> any:
    components = name.rsplit('.', 1)
    from_name = components[0]
    class_name = components[1]
    mod = __import__(from_name, globals(), locals(), [class_name])

    return getattr(mod, class_name)
