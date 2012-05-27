from setuptools import setup, find_packages
 
version = '0.1.0'
 
setup(
    name='django-crispy-extensions',
    version=version,
    description="Some extensions to the wonderful crispy forms",
    long_description=open('README.rst').read(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=['forms', 'django', 'crispy', 'formsets'],
    author='Andy Theyers',
    author_email='andy.theyers@isotoma.com',
    url='http://github.com/offmessage/django-crispy-extensions',
    license='Apache',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['Django',
                      'django-crispy-forms',
                      ],
)