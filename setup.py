import os
from setuptools import setup, find_packages


def read_file(filename):
    basepath = os.path.dirname(os.path.dirname(__file__))
    filepath = os.path.join(basepath, filename)
    if os.path.exists(filepath):
        return open(filepath).read()
    else:
        return ''


setup(
    name='norilog',
    version='1.0.0',
    description='The NoriLog web application.',
    long_description=read_file('README.rst'),
    author='ramnext',
    author_email='ramnextevolutions@gmail.com',
<<<<<<< HEAD
    url='https://github.com/ramnext/python-pp3rd/',
=======
    url='https://github.com/ramnext/python-pp-3rd/',
>>>>>>> dff945518c618546af0522c6e9da6c9d4694ecd8
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Flask',
        'License :: OSI Approved :: BSD License',
        'Programing Language :: Python',
        'Programing Language :: Python :: 3.7',
    ],
    packages=find_packages(),
    include_package_data=True,
    keywords=['web', 'norilog'],
    license='BSD License',
    install_requires=[
        'Flask',
    ],
    entry_points="""
        [console_scripts]
        norilog = norilog:main
    """,
)
