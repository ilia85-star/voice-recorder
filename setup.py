import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="voice-recorder",
    version="0.0.1",
    author="ilia85-star",
    author_email="ilia.mahjour.shafiei@outlook.com",
    description="Record your voice!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ilia85-star/voice-recorder",
    project_urls={
        "Bug Tracker": "https://github.com/ilia85-star/voice-recorder/issues",
    },
    entry_points={
        "console_scripts": ["recorder = voice-recorder.voice-recorder:main"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
    'librec>=0.0.1',
    'pyaudio>=0.2.0',
    'audio.wave>=4.0.0'
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
)
