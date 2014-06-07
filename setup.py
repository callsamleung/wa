from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='wa',
      version=version,
      description="wa is a flask-based web site develop solution.",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='flask, plugins',
      author='laiyonghao',
      author_email='mail@laiyonghao.com',
      url='https://github.com/laiyonghao/wa',
      license='mit',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'Flask',
          'Flask-Cache',
          'Flask-CDN',

          'abu.admin',
          'versiontools',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )