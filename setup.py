import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Jetson_MFRC522",
    version="0.0.2",
    author="Fabian Alvarez",
    author_email="support@fabianalvarez.dev",
    description="A library to integrate the MFRC522 RFID readers with the Raspberry Pi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SantaCRC/Jetson-MFRC522",
    packages=setuptools.find_packages(),
    install_requires=[
        'Jetson.GPIO',
        'spidev'
        ],
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: POSIX :: Linux",
        'Topic :: System :: Hardware',
    ],
)
