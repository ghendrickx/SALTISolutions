from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='SALTISolutions',
    version='0.1',
    author='Gijs G. Hendrickx',
    author_email='G.G.Hendrickx@tudelft.nl',
    description='',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=[
        'neural_network', 'neural_network.application', 'neural_network.machine_learning',
        'utils',
    ],
    license='Apache-2.0',
    keywords=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7'
)
