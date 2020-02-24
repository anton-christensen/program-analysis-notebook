from distutils.core import setup

with open('README.rst') as f:
    readme = f.read()

setup(
    name='while_kernel',
    version='0.1',
    packages=['while_kernel'],
    description='While kernel for Jupyter',
    long_description=readme,
    author='Test Horse Development Team',
    author_email='hsaren14@student.aau.dk',
    url='https://github.com/anton-christensen/program-analysis-notebook',
    install_requires=[
        'jupyter_client', 'IPython', 'ipykernel'
    ],
    classifiers=[
        'Intended Audience :: Rene',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
    ],
)
