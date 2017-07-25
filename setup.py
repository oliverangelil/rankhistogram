from setuptools import setup

setup(
    name='rankhistogram',
    description='Python function that takes model data, obs data, and a boolean mask to generate a rank histogram.',
    version='0.1',
    url='https://github.com/oliverangelil/rankhistogram',
    install_requires=['numpy','scipy'],
    author='Oliver Marc Angélil',
    author_email='molofishy@gmail.com',
    py_modules=['ranky'],
    license='MIT',
    keywords='rank histogram climate ensemble Hamil'
)
