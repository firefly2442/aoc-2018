from setuptools import setup, find_packages

setup(
    name='jimpoulakos-aoc2018',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_required=[
        'Click==7.0',
        'colorama==0.4.1',
    ],
    entry_points={
        'console_scripts': [
            'aoc=app.executor:cli',
        ],
    },
)
