from datetime import datetime
import decimal


def import_by_string(name: str) -> any:
    components = name.rsplit('.', 1)
    from_name = components[0]
    class_name = components[1]
    mod = __import__(from_name, globals(), locals(), [class_name])

    return getattr(mod, class_name)


def compact_result(data: list) -> list:
    buf = []

    for item in data:
        item = dict(item)
        keys = item.keys()
        for key in keys:
            if type(item[key]) is datetime:
                item[key] = str(item[key])
            elif type(item[key]) is decimal.Decimal:
                item[key] = float(item[key])

        buf.append(item)

    return buf
