try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Fastapi demo',
    'author': 'Girish Mallula',
    'url': 'http://localhost:8080/docs',
    'download_url': 'Download link',
    'author_email': 'chandramgc@gmail.com',
    'version': '0.1.0',
    'install_requires': ['unittest'], #dependencies
    'packages': ['FASTAPI'],
    'scripts': [],
    'name': 'Customers'
}

setup(**config)