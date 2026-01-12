from setuptools import setup, find_packages, __version__

with open("readme.md", "r", encoding='UTF-8') as fh:
    long_description = fh.read()

setup(
    name='pydatakrx',
    version=__version__,
    description='KRX data scraping',
    url='https://github.com/rinechran/pykrx/',
    author='Brayden Jo, Jonghun Yoo',
    author_email=('rinechran@gmail.com, '
                  'brayden.jo@outlook.com, '
                  'jonghun.yoo@outlook.com, '
                  'pystock@outlook.com'),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['requests', 'pandas', 'datetime', 'numpy', 'xlrd',
                      'deprecated', 'multipledispatch', 'matplotlib'],
    license='MIT',
    packages=find_packages(include=['pydatakrx', 'pydatakrx.*', 'pydatakrx.stock.*']),
    package_data={
        'pydatakrx': ['*.ttf'],
    },
    python_requires='>=3',
    zip_safe=False
)
