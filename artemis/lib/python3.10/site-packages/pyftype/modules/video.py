from pyftype.modules import Type, isobmff


class Mp4(isobmff._IsoBmff):
    """
    Implements the MP4 video type matcher.
    """

    MIME = "video/mp4"
    EXTENSION = "mp4"

    def __init__(self):
        super(Mp4, self).__init__(mime=Mp4.MIME, extension=Mp4.EXTENSION)

    def match(self, buf):
        if not self._is_isobmff(buf):
            return False

        major_brand, minor_version, compatible_brands = self._get_ftyp(buf)
        for brand in compatible_brands:
            if brand in ["mp41", "mp42", "isom"]:
                return True
        return major_brand in ["mp41", "mp42", "isom"]


class M4v(Type):
    """
    Implements the M4V video type matcher.
    """

    MIME = "video/x-m4v"
    EXTENSION = "m4v"

    def __init__(self):
        super(M4v, self).__init__(mime=M4v.MIME, extension=M4v.EXTENSION)

    def match(self, buf):
        return (
            len(buf) > 10
            and buf[:11] == b'\x00\x00\x00\x1c\x66\x74\x79\x70\x4d\x34\x56'
        )


class Mkv(Type):
    """
    Implements the MKV video type matcher.
    """

    MIME = "video/x-matroska"
    EXTENSION = "mkv"

    def __init__(self):
        super(Mkv, self).__init__(mime=Mkv.MIME, extension=Mkv.EXTENSION)

    def match(self, buf):
        return (
            len(buf) > 15
            and buf[:16] == b'\x1a\x45\xdf\xa3\x93\x42\x82\x88\x6d\x61\x74\x72\x6f\x73\x6b\x61'
        ) or (
            len(buf) > 38
            and buf[31:39] == b'\x6d\x61\x74\x72\x6f\x73\x6b\x61'
        )


class Webm(Type):
    """
    Implements the WebM video type matcher.
    """

    MIME = "video/webm"
    EXTENSION = "webm"

    def __init__(self):
        super(Webm, self).__init__(mime=Webm.MIME, extension=Webm.EXTENSION)

    def match(self, buf):
        return (
            len(buf) > 3
            and buf[:4] == b'\x1a\x45\xdf\xa3'
        )


class Mov(isobmff._IsoBmff):
    """
    Implements the MOV video type matcher.
    """

    MIME = "video/quicktime"
    EXTENSION = "mov"

    def __init__(self):
        super(Mov, self).__init__(mime=Mov.MIME, extension=Mov.EXTENSION)

    def match(self, buf):
        if not self._is_isobmff(buf):
            return False

        major_brand, minor_version, compatible_brands = self._get_ftyp(buf)
        return major_brand == "qt  "


class Avi(Type):
    """
    Implements the AVI video type matcher.
    """

    MIME = "video/x-msvideo"
    EXTENSION = "avi"

    def __init__(self):
        super(Avi, self).__init__(mime=Avi.MIME, extension=Avi.EXTENSION)

    def match(self, buf):
        return (
            len(buf) > 11
            and buf[:4] == b'\x52\x49\x46\x46'
            and buf[8:12] == b'\x41\x56\x49\x20'
        )


class Wmv(Type):
    """
    Implements the WMV video type matcher.
    """

    MIME = "video/x-ms-wmv"
    EXTENSION = "wmv"

    def __init__(self):
        super(Wmv, self).__init__(mime=Wmv.MIME, extension=Wmv.EXTENSION)

    def match(self, buf):
        return (
            len(buf) > 9
            and buf[0:10] == b'\x30\x26\xb2\x75\x8e\x66\xcf\x11\xa6\xd9'
        )


class Flv(Type):
    """
    Implements the FLV video type matcher.
    """

    MIME = "video/x-flv"
    EXTENSION = "flv"

    def __init__(self):
        super(Flv, self).__init__(mime=Flv.MIME, extension=Flv.EXTENSION)

    def match(self, buf):
        return (
            len(buf) > 3
            and buf[0:4] == b'\x46\x4c\x56\x01'
        )


class Mpeg(Type):
    """
    Implements the MPEG video type matcher.
    """

    MIME = "video/mpeg"
    EXTENSION = "mpg"

    def __init__(self):
        super(Mpeg, self).__init__(mime=Mpeg.MIME, extension=Mpeg.EXTENSION)

    def match(self, buf):
        return (
            len(buf) > 3
            and buf[:3] == b'\x00\x00\01'
            and buf[3] >= 0xB0
            and buf[3] <= 0xBF
        )


class M3gp(Type):
    """Implements the 3gp image type matcher."""

    MIME = "video/3gpp"
    EXTENSION = "3gp"

    def __init__(self):
        super(M3gp, self).__init__(mime=M3gp.MIME, extension=M3gp.EXTENSION)

    def match(self, buf):
        return buf[:7] == b'\x66\x74\x79\x70\x33\x67\x70'
