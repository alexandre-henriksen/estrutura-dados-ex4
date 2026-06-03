from pathlib import Path

# Diretório base do projeto
BASE_DIR = Path(__file__).resolve().parent

# Pasta de dados
DATA_DIR = BASE_DIR / "data"

# Caminhos específicos
CAMINHO_MOCHILA01 = DATA_DIR / "mochila01.txt"
CAMINHO_MOCHILA02 = DATA_DIR / "mochila02.txt"
CAMINHO_MOCHILA1000 = DATA_DIR / "mochila1000"
CAMINHO_MOCHILA2500 = DATA_DIR / "mochila2500"
CAMINHO_MOCHILA5000 = DATA_DIR / "mochila5000"

# Demais pastas
OUTPUT_DIR = BASE_DIR / "output"