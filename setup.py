from setuptools import setup, find_packages

setup(
    name="wmi_query",
    version="0.1",
    packages=find_packages(),
    author='Silvio AS a.k.a kanazuchi',
    author_email='contato@kanazuchi.com',
    scripts=['scripts/wmi_query_cmd'],
    description="A simple way to convert wmi data from wmic into dict objects.",
)
