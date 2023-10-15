import setuptools

setuptools.setup(
    name="meta-search",
    version="0.0.1",
    author="hot pancakes",
    author_email="itshotpancakes@gmail.com",
    description=("A quick metacritic search tool"),
    url="",
    project_urls={
        "Bug Tracker": "",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests", "regex"],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "meta = metasearch.cli:main",
        ]
    }
)