with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="validação_de_dados",
    version="0.0.1",
    author="Nicholas Wallace Souza Santos",
    author_email="wallacenicholas84@gmail.com",
    description="Validar dados simples",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NWallacess/Aprendizado-Python/tree/main/Dio/NTT%20DATA%20-%20Engenharia%20de%20Dados%20com%20Python"
    python_requires='>=3.11',
)