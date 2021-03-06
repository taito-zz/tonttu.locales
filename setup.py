from setuptools import find_packages
from setuptools import setup


setup(
    name='tonttu.locales',
    version='0.1',
    description="Overrides default translations of Plone for ABITA site.",
    long_description=open("README.rst").read(),
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7"],
    keywords='',
    author='Taito Horiuchi',
    author_email='taito.horiuchi@abita.fi',
    url='https://github.com/taito/tonttu.locales',
    license='None-free',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['tonttu'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Products.CMFPlone',
        'setuptools'],
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """)
