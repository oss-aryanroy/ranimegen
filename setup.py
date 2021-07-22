from setuptools import setup, find_packages

# See note below for more information about classifiers
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Education",
    "Operating System :: POSIX :: Linux",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: MacOS",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
]

setup(
    name="ranimegen",
    version="0.1.0",
    description="A python lib to generate random anime and its information",
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    url="https://github.com/Harukomaze/ranimegen",
    author="Harukomaze",
    author_email="sdpqwer0@gmail.com",
    license="MIT",  # note the American spelling
    classifiers=classifiers,
    keywords="discord random-anime anime ranime random-anime-generator anime-generator",  # used when people are searching for a module, keywords separated with a space
    packages=find_packages(),
    install_requires=[
        "aiohttp", "bs4"
    ],  # a list of other Python modules which this module depends on.  For example RPi.GPIO
    include_package_data=True
)
