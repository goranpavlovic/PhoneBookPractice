from setuptools import setup, find_packages


README = """

"""


setup(
    name='phonebook',
    description='Phone Book',
    long_description=README,
    version='0.0.1',
    url='',
    license='',
    install_requires=[
        "Flask==1.1.2",
        "spectree==0.3.6",
        "psycopg2==2.8.6"
    ]
)
