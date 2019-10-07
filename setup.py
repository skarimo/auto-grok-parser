from setuptools import setup

setup(
   name='gphelper',
   version='1.0',
   description='Useful module for quickly parsing logs',
   author='Sherzod K.',
   author_email='sherzod.karimov@datadoghq.com',
   packages=['gphelper'],
   install_requires=['click'],
   entry_points = {
       'console_scripts': [
           'gphelp = gphelper.__main__:main'
       ]
   }
)

