# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <tsuyoshi.hombashi@gmail.com>
"""

from __future__ import unicode_literals

import io
import os.path
import sys

import setuptools

MODULE_NAME = "pathvalidate"
REPOSITORY_URL = "https://github.com/thombashi/{:s}".format(MODULE_NAME)
REQUIREMENT_DIR = "requirements"
ENCODING = "utf8"

pkg_info = {}


def need_pytest():
    return set(["pytest", "test", "ptr"]).intersection(sys.argv)


with open(os.path.join(MODULE_NAME, "__version__.py")) as f:
    exec(f.read(), pkg_info)

with io.open("README.rst", encoding=ENCODING) as fp:
    long_description = fp.read()

with io.open(os.path.join("docs", "pages", "introduction", "summary.txt"), encoding=ENCODING) as f:
    summary = f.read().strip()

with open(os.path.join(REQUIREMENT_DIR, "requirements.txt")) as f:
    install_requires = [line.strip() for line in f if line.strip()]

with open(os.path.join(REQUIREMENT_DIR, "test_requirements.txt")) as f:
    tests_require = [line.strip() for line in f if line.strip()]

with open(os.path.join(REQUIREMENT_DIR, "docs_requirements.txt")) as f:
    DOCS_REQUIRES = [line.strip() for line in f if line.strip()]

setuptools.setup(
    name=MODULE_NAME,
    version=pkg_info["__version__"],
    url=REPOSITORY_URL,

    author=pkg_info["__author__"],
    author_email=pkg_info["__email__"],
    description=summary,
    keywords=[
        "path", "validation", "validator", "sanitize", "file",
        "Excel", "JavaScript", "LTSV", "SQLite",
    ],
    license=pkg_info["__license__"],
    long_description=long_description,
    include_package_data=True,
    install_requires=install_requires,
    packages=setuptools.find_packages(exclude=["test*"]),
    project_urls={
        "Documentation": "http://{typepy}.rtfd.io/",
        "Tracker": "{:s}/issues".format(REPOSITORY_URL),
    },

    setup_requires=["pytest-runner"] if need_pytest() else [],
    tests_require=tests_require,
    extras_require={
        "build": "wheel",
        "docs": DOCS_REQUIRES,
        "release": "releasecmd>=0.0.7",
    },

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ])
