from setuptools import setup, find_packages

version = '0.4'


def description():
    try:
        return open('README.rst').read()
    except:
        return ''

setup(name='pyramid_fanstatic',
      version=version,
      description="pyramid tween for fanstatic",
      long_description=description(),
      classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
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
      entry_points="""
      # -*- Entry points: -*-
      [pyramid.scaffold]
      pyramid_fanstatic=pyramid_fanstatic.scaffolds:PyramidFanstaticTemplate
      """,
      )
