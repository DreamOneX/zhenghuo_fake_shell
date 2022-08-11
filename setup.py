import setuptools

setuptools.setup(
    name="zhenghuofakeshell",
    description="专业整活shell",
    version="1.1.4",
    author="DreamOneX",
    author_email="me@dreamonex.eu.org",
    maintainer="DreamOneX",
    maintainer_email="DreamOneX",
    url="https://github.com/DreamOneX/zhenghuo_fake_shell",
    download_url="https://github.com/DreamOneX/zhenghuo_fake_shell",
    license="WTFPL",
    packages=setuptools.find_packages("src"),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': ['zhenghuofakeshell = zhenghuofakeshell:run']
    })
