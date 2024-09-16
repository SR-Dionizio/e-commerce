# Use a imagem base oficial do Python
FROM python:3.11-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Copia o requirements.txt para o container
COPY requirements.txt .

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante dos arquivos da aplicação para o container
COPY . .

# Copia o arquivo .env para o container
COPY .env .env

# Define o PYTHONPATH para garantir que as bibliotecas locais sejam encontradas
ENV PYTHONPATH=/app

# Expõe a porta que será utilizada pela aplicação
EXPOSE 8080

# Comando para rodar a aplicação
CMD ["python", "application.py"]
