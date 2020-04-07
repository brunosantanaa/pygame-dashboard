from setuptools import find_packages
from distutils.core import setup
 
setup(name='pygame-dashboard',
      version='0.1',
      url='https://github.com/brunosantanaa/pygame-dashboard',
      license='MIT',
      author='Bruno Santana',
      author_email='bruno.sant.a@gmail.com',
      description='Simples elements of Dashboard from PyGame',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      zip_safe=False)