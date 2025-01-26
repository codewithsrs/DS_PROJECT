import setuptools

with open("README.md","r", encoding = "utf-8") as f:
    long_description = f.read()

__version__ = "1.0.0"

REPO_NAME = "DS_PROJECT"
AUTHOR_USER_NAME = "codewithsrs"
SRC_REPO = "classifier"
AUTHOR_EMAIL = "smr6784@gmail.com"


setuptools.setup(name = SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Package for image classification",
    long_description=long_description,
    long_description_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir = {"":"src"},
    packages = setuptools.find_packages(where = "src")
)
    