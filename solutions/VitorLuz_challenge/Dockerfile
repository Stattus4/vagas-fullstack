# imagem Python
FROM python:3.9-slim

# Diretório de trabalho dentro do contêiner
WORKDIR /Stattus4_desafio_vitor

# Copiar o arquivo de requisitos e instala as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código para o diretório de trabalho
COPY . .

# Comando para rodar os testes de unidade
CMD ["pytest", "-v"]
