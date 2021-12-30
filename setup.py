from setuptools import setup, find_packages

setup(
    name='Hospital application',
    version='1.0',
    author='Vihor Dmytro',
    author_email='vdude112358@gmail.com',
    description='Web library to work with hospital departments and employees',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask == 2.0.2',
        'Flask_Login == 0.5.0',
        'Flask_Migrate == 3.1.0',
        'Flask_RESTful == 0.3.9',
        'Flask_SQLAlchemy == 2.5.1',
        'Flask_WTF == 1.0.0',
        'SQLAlchemy == 1.4.27',
        'Werkzeug == 2.0.2',
        'WTForms == 3.0.0',
    ]
)
