__title__ = 'wikipy'
__author__ = 'Colby Brown'

"""
Extracts articles from Wikipedia and uses natural language processing to
provide a quick summary, directly to the command line.
"""
from setuptools import find_packages, setup

dependencies = [
    'click',
    'wikipedia',
    'feedparser',
]

setup(
    name='wikipy',
    version='0.0.1',
    url='https://github.com/cbrown132/WikiPy',
    license='MIT',
    author='Colby Brown',
    author_email='colby.brown@dal.ca',
    description='Extracts articles from Wikipedia and uses natural language processing'
                'to provide a quick summary, directly to the command line.',
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'wikipy = wikipy.wikipy:main',
        ],
    },
    classifiers=[
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
