#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from linuxd import __version__

from setuptools import setup
from setuptools.command.install import install


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


class CustomInstallCommand(install):
    def run(self):
        install.run(self)


setup(
    name="linuxd",
    version=__version__,
    author="Fernando Celmer",
    author_email="email@fernandocelmer.com",
    description="🐧 Dev Linux Profile",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/linux-profile/linux-dev",
    cmdclass={
        'install': CustomInstallCommand,
    },
    install_requires=[
        'linuxp>=1.0.19'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    include_package_data=True,
    python_requires=">=3.6",
    zip_safe=True,
    fullname='linuxd',
    entry_points={
        'console_scripts': ['linuxd=linux_dev.main:main'],
    },
)
