try:
    import pathlib
except ImportError:
    pass


def get_signature_bytes(path, length):
    """
    从文件中读取前262个字节。
    """
    with open(path, "rb") as fp:
        if length is None:
            return bytearray(fp.read())
        return bytearray(fp.read(length))

def signature(array, length):
    """
    截取字节数组的前262字节。
    """
    if length is None:
        return array
    else:
        size = len(array)
        index = length if size > length else size
        return array[:index]
        


def get_bytes(obj, length=None):
    """
    判断输入类型，并读取前262个字节，返回一个字节数组
    """
    kind = type(obj)

    if kind is bytearray:
        return signature(obj, length)

    if kind is str:
        return get_signature_bytes(obj, length)

    if kind is bytes:
        return signature(obj, length)

    if kind is memoryview:
        return bytearray((signature(obj, length).tolist()))

    if isinstance(obj, pathlib.PurePath):
        return get_signature_bytes(obj, length)

    raise TypeError("Unsupported type as file input: %s" % kind)
