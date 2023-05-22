import re
import string

from unidecode import unidecode


class Sanitizer:

    VERSION_REMOVER = re.compile(r"(v[0-9][0-9.]*)$")

    @staticmethod
    def sanitise_model_name(name):
        """Ensure we store model names in ascii"""
        # We just remove exotic unicode characters
        return unidecode(name)

    @staticmethod
    def sanitise_filename(filename):
        """Don't allow crazy filenames, there are a lot"""
        # First remove exotic unicode characters
        filename = unidecode(filename)
        # Now exploit characters
        valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
        return "".join(c for c in filename if c in valid_chars)

    @staticmethod
    def remove_version(string):
        return Sanitizer.VERSION_REMOVER.sub(r"", string)
