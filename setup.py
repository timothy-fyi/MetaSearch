import setuptools

# with open("README.md", "r", encoding="utf-8") as fhand:
#     long_description = fhand.read()

setuptools.setup(
    name="meta-search",
    version="0.0.1",
    author="hot pancakes",
    author_email="itshotpancakes@gmail.com",
    description=("A quick metacritic search tool"),
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    url="",
    project_urls={
        "Bug Tracker": "",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests"],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "metasearch = metasearch.cli:main",
        ]
    }
)