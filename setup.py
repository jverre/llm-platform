from setuptools import setup, find_packages

required_packages = [
]

setup(
    name="llm-platform",
    version="0.0.1",
    author="Jacques Verré",
    author_email="jverre@gmail.com",
    description="LLM serving platform",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    keywords="LLM serving logging api gateway",
    license="Apache 2.0 License",
    url="https://github.com/jverre/llm-platform",
    package_dir={"": "src"},
    packages=find_packages("src"),
    install_requires=required_packages,
    include_package_data=True,
    zip_safe=False,
    entry_points={"console_scripts": ["llm-platform=llm_platform.cli:cli"]},
    python_requires=">=3.8.0"
)