from setuptools import setup

setup(
    name = 'pypremis',
    version = '1.0.0',
    url = 'https://github.com/uchicago-library/uchicagoldr-premiswork',
    author = "Brian Balsamo <balsamo@uchicago.edu>",
    author_email = "balsamo@uchicago.edu",
    packages = ['pypremis'],
    description = "A set of python classes for working with PREMIS records.",
    keywords = ["uchicago", "repository", "file-level", "processing", "premis",
                "metadata", "preservation"],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Operating System :: Unix",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    install_requires = [])
