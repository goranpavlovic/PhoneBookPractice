from setuptools import setup, find_packages


_readme = ""
with open("README.md", "r") as f:
    _readme = f.read()


setup(
    name='phonebook',
    description='Phone Book',
    long_description=_readme,
    version='0.0.1',
    url='',
    license='',
    install_requires=[
        "Flask==1.1.2",
        "spectree==0.3.6",
        "psycopg2==2.8.6",
        "yoyo-migrations==7.2.1",
        "pytest-flask==1.1.0",
        "pydantic==1.8"
    ]
)
