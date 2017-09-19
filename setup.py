from setuptools import setup, find_packages

setup(
    name="wmi-query",
    version="0.1.1",
    license="BSD",
    packages=find_packages(),
    keywords="wmi wmic",
    url="https://github.com/kanazux/wmi_query",
    author='Silvio AS a.k.a kanazuchi',
    author_email='contato@kanazuchi.com',
    scripts=['scripts/wmi_query'],
    description="A simple way to convert wmi data from wmic into dict objects.",
    install_requires=['impacket'],
)
