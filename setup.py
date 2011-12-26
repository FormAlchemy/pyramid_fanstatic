from setuptools import setup, find_packages

version = '0.1'


def description():
    try:
        return open('README.rst').read()
    except:
        return ''

setup(name='pyramid_fanstatic',
      version=version,
      description="pyramid tween for fanstatic",
      long_description=description(),
      classifiers=[],
      keywords='pyramid fanstatic js css',
      author='Gael Pasgrimaud',
      author_email='gael@gawel.org',
      url='',
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
      """,
      )
