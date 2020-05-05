try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
config = {
    'description': 'Alien Invasion',
    'author': 'sicou2',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'sicou2@gmail.com',
    'version': '0.1',
    'install_requires': ['pytest', 'pygame'],
    'packages': ['alien_invasion'],
    'scripts': ['alien_invasion/alien_invasion'],
    'name': 'alien_invastion_game',
    }
    
setup(**config)