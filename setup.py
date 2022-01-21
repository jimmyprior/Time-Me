from setuptools import setup, find_packages


setup(
    name="timeme",
    version="0.0.1",
    author="Jimmy Prior",
    author_email="jimmyprior04@gmail.com",
    description="time your program when you want to. Leave it as comments when you don't.",
    url="https://github.com/jimmyprior/Time-Me",
    packages=find_packages(),
    python_requires=">=3.6",
    entry_points = {
        "console_scripts" : [
            "timeme = timeme.timeme:main"
        ]
    }
)