from setuptools import setup, find_packages

version = '0.6'


setup(name='pyramid_fanstatic',
      version=version,
      description="pyramid tween for fanstatic",
      long_description=(
          open('README.rst').read()
          + '\n'
          + open('CHANGES.rst').read()
      ),
      classifiers=[
          "Intended Audience :: Developers",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
          "Framework :: Pylons",
          "Topic :: Internet :: WWW/HTTP :: WSGI",
          "License :: OSI Approved :: MIT License",
      ],
      keywords='pyramid fanstatic js css',
      author='Gael Pasgrimaud',
      author_email='gael@gawel.org',
      url='https://github.com/FormAlchemy/pyramid_fanstatic',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'pyramid',
          'fanstatic',
      ],
      extras_require={
          "test": [
              "js.jquery == 1.9.1",  # We test on specific file names.
              "webtest",
          ],
      },
      entry_points="""
      # -*- Entry points: -*-
      [pyramid.scaffold]
      pyramid_fanstatic=pyramid_fanstatic.scaffolds:PyramidFanstaticTemplate
      """,
      )
