
import setuptools

# DISABLED/BUG: this line fails when `pip install attributedict` but works `pip install .`
# from attributedict import __version__

setuptools.setup(
    name = 'config2',
    version = '0.1.1',
    description = (
        'Python application configuration - highly inspired by `node-config`.'
    ),
    long_description = open('README.md').read(),
    long_description_content_type = 'text/markdown',
    keywords = [
        'config',
        'configuration',
        'configurations',
        'settings',
        'env',
        'environment',
        'environments',
        'application',
        'node-config',
        'python-config',
    ],
    author = 'Jonas Grimfelt',
    author_email = 'grimen@gmail.com',
    url = 'https://github.com/grimen/python-config2',
    download_url = 'https://github.com/grimen/python-config2',
    project_urls = {
        'repository': 'https://github.com/grimen/python-config2',
        'bugs': 'https://github.com/grimen/python-config2/issues',
    },
    packages = setuptools.find_packages(),
    package_dir = {
        'config2': 'config2'
    },
    package_data = {
        '': [
            'MIT-LICENSE',
            'README.md',
        ],
        'config2': [
            '*.*',
        ]
    },
    py_modules = ['config2'],
    license = 'MIT',
    classifiers = [
        'Topic :: Software Development :: Libraries',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    zip_safe = True,
)
