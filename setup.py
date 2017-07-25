from setuptools import setup

setup(
    name='rank-histogram',
    description='Python function that takes model data, obs data, and a boolean mask to generate a rank histogram.',
    version='0.2',
    url='https://github.com/oliverangelil/rankhistogram',
    install_requires=['numpy','scipy'],
    author='Oliver Marc Angelil',
    author_email='molofishy@gmail.com',
    py_modules=['ranky'],
    license='MIT',
    keywords='rank histogram climate ensemble Hamil'
)
