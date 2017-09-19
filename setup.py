from setuptools import setup, find_packages

setup(
    name="py-wmi-query",
    version="0.1",
    license="BSD2CLAUSE",
    packages=find_packages(),
    keywords="wmi impacket",
    url="https://github.com/kanazux/py-wmi-query",
    author='Silvio AS a.k.a kanazuchi',
    author_email='contato@kanazuchi.com',
    scripts=['scripts/wmi-query'],
    description="A simple way to convert wmi data from wmi class objects into defaultdict.",
    install_requires=['impacket'],
)
