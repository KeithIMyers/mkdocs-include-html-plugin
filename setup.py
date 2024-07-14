from setuptools import setup, find_packages

setup(
    name='mkdocs-include-html-plugin',
    version='0.1.3',
    description='An MkDocs plugin to include HTML and JS content in each directory',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Keith I Myers',
    author_email='Keith@KMyers.me',
    url='https://github.com/KeithIMyers/mkdocs-include-html-plugin',
    packages=find_packages(),
    install_requires=[
        'mkdocs',
        'beautifulsoup4'
    ],
    entry_points={
        'mkdocs.plugins': [
            'include_html_plugin = include_html_plugin.plugin:IncludeHtmlPlugin',
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Documentation',
    ],
    python_requires='>=3.6',
)
