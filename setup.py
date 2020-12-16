from setuptools import setup

setup(
    name="manzip",
    version='1.0.0',
    py_modules=['manzip'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        manzip=app:main
    ''',
)