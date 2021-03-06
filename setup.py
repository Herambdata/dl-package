from setuptools import setup, find_packages

with open('README.txt') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name="traversal",
    version="0.4",
    description="A python package to handle all traversal problems",
    long_description_content_type="text/markdown",
    long_description=README,
    license="MIT",
    packages=find_packages(),
    author="Heramb Mishra",
    author_email="heramb1008@gmail.com",
    include_package_data=True
)

install_requires=[
        "numpy>=1.18.5",
        "pandas>=1.0.5",
        "scikit-learn>=0.23.1",      
]

if __name__=='__main__':
    setup(**setup_args,install_requires=install_requires)