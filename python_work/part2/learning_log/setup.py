try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Learning Log',
    'author': 'sicou2',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'sicou2@gmail.com',
    'version': '0.1',
    'install_requires': ['pytest'],
    'packages': ['learning_log'],
    'scripts': [],
    'name': 'learning_log_project',
}

setup(**config)
