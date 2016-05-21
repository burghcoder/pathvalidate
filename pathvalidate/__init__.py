# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <gogogo.vm@gmail.com>
"""

import re

import dataproperty


__INVALID_PATH_CHARS = '\:*?"<>|'


def validate_filename(filename):
    """
    :param str filename: Filename to validate.
    :raises ValueError:
        If the ``filename`` is empty or includes invalid char(s):
        (``\``, ``:``, ``*``, ``?``, ``"``, ``<``, ``>``, ``|``).
    """

    if dataproperty.is_empty_string(filename):
        raise ValueError("null path")

    match = re.search("[%s]" % (
        re.escape(__INVALID_PATH_CHARS)), filename)
    if match is not None:
        raise ValueError(
            "invalid char found in the file path: '%s'" % (
                re.escape(match.group())))


def sanitize_filename(filename, replacement_text=""):
    """
    Replace invalid chars for a file path within the ``filename`` with
    the ``replacement_text``.

    :param str filename: Filename to validate.
    :param str replacement_text: Replacement text.
    :return: A replacement string.
    :rtype: str
    """

    filename = filename.strip()
    re_replace = re.compile("[%s]" % re.escape(__INVALID_PATH_CHARS))

    return re_replace.sub(replacement_text, filename)


def replace_symbol(filename, replacement_text=""):
    fname = sanitize_filename(filename, replacement_text)
    if fname is None:
        return None

    re_replace = re.compile("[%s]" % re.escape(" ,.%()/"))

    return re_replace.sub(replacement_text, fname)
