from setuptools import setup, find_packages
import slacksay

setup(name='slacksay',
      version=slacksay.__version__,
      packages=find_packages(exclude=['tests']),
      entry_points='''
          [console_scripts]
          slacksay = slacksay.main:main
      ''',
      install_requires=[
          'click',
          'pyyaml',
          'requests',
      ])
