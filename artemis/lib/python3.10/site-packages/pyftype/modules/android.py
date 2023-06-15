from pyftype.modules import Type


class Dex(Type):
    """Android Dalvik Executable Format"""

    MIME = "application/vnd.android.dex"
    EXTENSION = "dex"

    def __init__(self):
        super(Dex, self).__init__(mime=Dex.MIME, extension=Dex.EXTENSION)

    def match(self, buf):
        return buf[:4] == b"dex\n"


class DEY(Type):
    """Android Optimized Dalvik EXecutable"""

    MIME = "application/vnd.android.dey"
    EXTENSION = "dey"

    def __init__(self):
        super(DEY, self).__init__(mime=DEY.MIME, extension=DEY.EXTENSION)

    def match(self, buf):
        return buf[:4] == b"dey\n"


class ARSC(Type):
    """Android Resources File"""

    MIME = "application/vnd.android.arsc"
    EXTENSION = "arsc"

    def __init__(self):
        super(ARSC, self).__init__(mime=ARSC.MIME, extension=ARSC.EXTENSION)

    def match(self, buf):
        return buf[:4] == b"\x02\x00\x0c\x00"


class AXML(Type):
    """Android binary XML"""

    MIME = "application/vnd.android.arsc"
    EXTENSION = "axml"

    def __init__(self):
        super(AXML, self).__init__(mime=AXML.MIME, extension=AXML.EXTENSION)

    def match(self, buf):
        return buf[:4] == b"\x03\x00\x08\x00"


class AXMLX(Type):
    """Android binary XML 修改后的"""

    MIME = "application/vnd.android.axml"
    EXTENSION = "axml"

    def __init__(self):
        super(AXMLX, self).__init__(mime=AXMLX.MIME, extension=AXMLX.EXTENSION)

    def match(self, buf):
        return buf[:4] == b"\x00\x00\x08\x00"
