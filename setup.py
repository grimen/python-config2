
# =========================================
#       IMPORTS
# --------------------------------------

import os
import glob
import setuptools

# DISABLED/BUG: this line fails when `pip install config2` but works `pip install .`
# from config2 import __version__


# =========================================
#       FUNCTIONS
# --------------------------------------

def find_data_files(data_file_patterns = [], root_path = None):
    root_path = root_path or os.path.abspath(os.path.dirname(__file__))
    data_file_dirs = []

    for root, dirs, files in os.walk(root_path):
        data_file_dirs.append(root)

    data_files = []

    for data_file_dir in data_file_dirs:
        files = []

        for data_file_pattern in data_file_patterns:
            files += glob.glob(os.path.join(data_file_dir, data_file_pattern))

        if not files:
            continue

        target = os.path.join(root_path, data_file_dir)

        data_files.append((target, files))

    return data_files

def get_readme():
    root_path = os.path.abspath(os.path.dirname(__file__))
    readme_file_path = os.path.join(root_path, 'README.md')

    with open(readme_file_path) as file:
        readme = file.read()

    return readme

def get_requirements():
    root_path = os.path.abspath(os.path.dirname(__file__))
    requirements_file_path = os.path.join(root_path, 'requirements.txt')

    with open(requirements_file_path) as file:
        requirements = [requirement.strip() for requirement in file.readlines()]
        requirements = filter(lambda requirement: len(requirement), requirements)
        requirements = list(requirements)

    return requirements


# =========================================
#       MAIN
# --------------------------------------

readme = get_readme()
requirements = get_requirements()
packages = setuptools.find_packages()
data_files = find_data_files(['*.*'], os.path.join('config2', 'tests', '__fixtures__'))

config = {
    'name': 'config2',
    'version': '0.3.0',
    'description': (
        'Python application configuration - highly inspired by `node-config`.'
    ),
    'keywords': [
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
    'author': 'Jonas Grimfelt',
    'author_email': 'grimen@gmail.com',
    'url': 'https://github.com/grimen/python-config2',
    'download_url': 'https://github.com/grimen/python-config2',
    'project_urls': {
        'repository': 'https://github.com/grimen/python-config2',
        'bugs': 'https://github.com/grimen/python-config2/issues',
    },
    'license': 'MIT',

    'long_description': readme,
    'long_description_content_type': 'text/markdown',

    'classifiers': [
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

    'packages': packages,
    'package_dir': {
        'config2': 'config2',
    },
    'package_data': {
        '': [
            'MIT-LICENSE',
            'README.md',
        ],
        'config2': [
            '*.*',
        ],
    },
    'data_files': data_files,
    'include_package_data': True,
    'zip_safe': True,

    'install_requires': requirements,
    'setup_requires': ['setuptools_git >= 1.2'],
}

setuptools.setup(**config)
