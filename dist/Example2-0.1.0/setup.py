# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['example2']

package_data = \
{'': ['*']}

install_requires = \
['numpy==1.20.0',
 'pandas==1.2.0',
 'parquet>=1.3.1,<2.0.0',
 'pyarrow>=6.0.0,<7.0.0',
 'requests>=2.26.0,<3.0.0']

setup_kwargs = {
    'name': 'example2',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
