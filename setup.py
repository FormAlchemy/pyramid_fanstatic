from setuptools import setup, find_packages

version = '0.1'

setup(name='pyramid_fanstatic',
      version=version,
      description="pyramid tweens for fanstatic",
      long_description="""\
""",
      classifiers=[],
      keywords='',
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
