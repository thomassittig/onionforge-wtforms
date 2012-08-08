import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = ["wtforms",
            "jhi_tools"
    ]

setup(name='onionforge_wtforms',
      version='0.0',
      description='extensions for wtforms',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web tools',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='onionforge_wtforms',
      install_requires = requires,
      entry_points = """\
      [paste.app_factory]
      """,
      )

