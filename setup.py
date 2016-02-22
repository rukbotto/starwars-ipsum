from setuptools import find_packages, setup


def get_readme():
    readme = ''
    try:
        import pypandoc
        readme = pypandoc.convert('README.md', 'rst')
    except (ImportError, IOError):
        with open('README.md', 'r') as file_data:
            readme = file_data.read()
    return readme


setup(
    name='starwars-ipsum',
    version='0.0.2',
    author='Jose Miguel Venegas Mendoza',
    author_email='jvenegas@rukbottoland.com',
    description=('A simple utility that generates placeholder text from Star '
                 'Wars intros.'),
    long_description=get_readme(),
    license='BSD',
    keywords='starwars utilities ipsum',
    url='https://github.com/rukbotto/starwars-ipsum',
    packages=find_packages(),
    package_data={
        'starwars_ipsum': ['*.txt']
    },
    install_requires=['markdown==2.6.5'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities'
    ]
)
