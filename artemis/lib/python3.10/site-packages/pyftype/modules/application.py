from pyftype.modules import Type


class Wasm(Type):
    """Implements the Wasm image type matcher."""

    MIME = "application/wasm"
    EXTENSION = "wasm"

    def __init__(self):
        super(Wasm, self).__init__(mime=Wasm.MIME, extension=Wasm.EXTENSION)

    def match(self, buf):
        return buf[:8] == b"\x00\x61\x73\x6d\x01\x00\x00\x00"


class ELF(Type):
    """Executable and Linkable Format"""

    MIME = "application/vnd.linux.executable"
    EXTENSION = "elf"

    def __init__(self):
        super(ELF, self).__init__(mime=ELF.MIME, extension=ELF.EXTENSION)

    def match(self, buf):
        return buf[:4] == b"\x7f\x45\x4c\x46"


class EXE(Type):
    """Executable and Linkable Format"""

    MIME = "application/vnd.microsoft.portable-executable"
    EXTENSION = "exe/dll"

    def __init__(self):
        super(EXE, self).__init__(mime=EXE.MIME, extension=EXE.EXTENSION)

    def match(self, buf):
        return buf[:2] == b"MZ"


class PKCS7(Type):
    """PKCS #7 Certificate File"""

    MIME = "application/x-pkcs7"
    EXTENSION = "p7b"

    def __init__(self):
        super(PKCS7, self).__init__(mime=PKCS7.MIME, extension=PKCS7.EXTENSION)

    def match(self, buf):
        return buf[:2] == b"\x30\x82"


class Sqlite(Type):
    """Sqlite Formate"""

    MIME = "application/x-sqlite3"
    EXTENSION = "sqlite"

    def __init__(self):
        super(Sqlite, self).__init__(mime=Sqlite.MIME, extension=Sqlite.EXTENSION)

    def match(self, buf):
        return (
            buf[:16]
            == b"\x53\x51\x4c\x69\x74\x65\x20\x66\x6f\x72\x6d\x61\x74\x20\x33\x00"
        )
