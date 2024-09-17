from setuptools import setup, find_packages

setup(
    name='django-whiff',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='A Django template tag that combines the functionality of "with" and "if".',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ehamiter/django-whiff',
    author='Eric Hamiter',
    author_email='ehamiter@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 5.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.12',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
