#!/usr/bin/env python

from setuptools import setup, find_packages


setup(name='arpy',
      version='1.0',
      packages=find_packages(),

      install_requires=['numpy', 'matplotlib', 'scipy'],
      setup_requires=['setuptools_git >= 0.3', ],

      author='Pierre Rouanet',
      author_email='pierre.rouanet@gmail.com',
      description='Simple Hamming Marker Detection using OpenCV',
      url='https://github.com/pierre-rouanet/ARPy',
      license='GNU GENERAL PUBLIC LICENSE Version 3',
      )
