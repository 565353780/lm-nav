# from distutils.core import setup, find_packages
from setuptools import setup, find_packages


setup(
    name="lm-nav",
    version="1.0",
    description="Source code for the LMNav.",
    author="Błażej Osiński & Dhruv Shah",
    packages=['lm_nav'],
    install_requires=[
        "networkx",
        "h5py",
        "matplotlib",
        "numpy",
        "pillow",
        "pyyaml",
        "utm",
        "openai",
        "jupyter",
        "opencv-python",
        "ftfy",
        "regex",
        "tqdm",
        "clip @ git+https://github.com/openai/CLIP.git",
        "spacy",
        "gdown",
    ],
    package_data={'': ['base.css.html', 'bgraph.js']},
    include_package_data=True,
    extras_require={'dev': ['pytest']},
)
