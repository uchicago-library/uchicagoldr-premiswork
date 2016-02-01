from distutils.core import setup

setup(
    name = 'pypremis',
    version = '1.0.0',
    author = "Brian Balsamo",
    author_email = ["balsamo@uchicago.edu","tdanstrom@uchicago.edu"],
    packages = ['pypremis'],
    description = "A set of python classes for working with PREMIS records.",
    keywords = ["uchicago","repository","file-level","processing"],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Operating System :: Unix",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    install_requires = [])
