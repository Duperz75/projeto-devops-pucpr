# Imagem base oficial do Python
FROM python:3.10

# Diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do projeto
COPY . .

# Comando para rodar a aplicação
CMD ["python", "app.py"]
