from setuptools import setup, find_packages

setup(
    name="wmi-query",
    version="0.1.5",
    license="BSD2CLAUSE",
    packages=['wmi_query'],
    keywords="wmi impacket",
    url="https://github.com/kanazux/wmi-query",
    author='Silvio AS a.k.a kanazuchi',
    author_email='alvolivre@live.com',
    scripts=['scripts/wmi-query'],
    description="A simple way to convert wmi data from wmi class objects into defaultdict.",
    install_requires=['impacket', 'pycrypto', 'pyasn1'],
    zip_safe=False
)
