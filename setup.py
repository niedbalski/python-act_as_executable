from setuptools import setup, find_packages

dependencies = [ "envoy" ]

setup(
    name="act_as_executable",
    version="1.0",
    packages=find_packages(),
    install_requires=dependencies,
    author="Jorge Niedbalski R.",
    author_email="jnr@pyrosome.org",
    description="A Python wrapper to build CLI wrappers",
    keywords="cli-wrapper, cli, wrapper, wrap cli",
    include_package_data=False,
    license="BSD",
    classifiers=['Intended Audience :: Developers',
                'Operating System :: Unix ']
)
