from setuptools import setup, find_packages

setup(
    name='MyPackageName_2',
    version='1.0.0',
    url='https://github.com/mypackage.git',
    author='Author Name',
    author_email='author@gmail.com',
    description='Description of the package',
    packages=find_packages(),
    install_requires=[
        'requests >= 2.24.0',
        'MyPackageName_1 @ git+git://github.com/eugenyProchan/setup_lesson_1@master#egg=my_package_first',
    ]
)
