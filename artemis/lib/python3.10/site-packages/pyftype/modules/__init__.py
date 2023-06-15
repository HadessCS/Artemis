class Type(object):
    """
    类型匹配类
    """

    def __init__(self, mime, extension):
        self.__mime = mime
        self.__extension = extension

    @property
    def mime(self):
        return self.__mime

    @property
    def extension(self):
        return self.__extension

    @property
    def is_extension(self, extension):
        return self.__extension is extension

    @property
    def is_mime(self, mime):
        return self.__mime is mime

    def match(self, buf):
        raise NotImplementedError


class Data(Type):
    """数据类型，不可读"""

    MIME = "application/data"
    EXTENSION = "data"

    def __init__(self):
        super(Data, self).__init__(mime=Data.MIME, extension=Data.EXTENSION)


class Text(Type):
    """文本类型"""

    MIME = "application/txt"
    EXTENSION = "txt"

    def __init__(self):
        super(Text, self).__init__(mime=Text.MIME, extension=Text.EXTENSION)


class APK(Type):
    """文本类型"""

    MIME = "application/vnd.android.package-archive"
    EXTENSION = "apk"

    def __init__(self):
        super(APK, self).__init__(mime=APK.MIME, extension=APK.EXTENSION)
