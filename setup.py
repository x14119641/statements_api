from setuptools import setup

setup(
    name='statements_api',
    version='0.1.0',
    author='Daniel',
    author_email='x14119641@student.ncierl.ie',
    packages=['app', ],
    license='LICENSE.txt',
    description='POST API Showing Users and Accounts information.',
    long_description=open('README.txt').read(),
    install_requires=[
        "flask",
        "pytest",
        "python-dotenv",
    ],
)
