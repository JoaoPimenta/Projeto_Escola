# Usar imagem oficial do Python como base
FROM python:3.10-slim

# Definir diretório de trabalho dentro do container
WORKDIR /app

# Copiar e instalar as dependências primeiro (para melhor cache)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expõe a porta que o Flask vai usar
EXPOSE 8000

# Definir variáveis de ambiente para Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8000

# Comando para rodar a aplicação
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]
