# Dockerfile backend

# Utilisez une image Debian comme base
FROM python:3.8-slim-buster

# Installez les dépendances nécessaires, y compris les bibliothèques systemd
RUN apt-get update && \
   apt-get install -y gcc libc-dev

RUN apt-get install -y libsystemd-dev libmariadb-dev pkg-config

# Définissez le répertoire de travail
WORKDIR /app

# Copiez les fichiers nécessaires dans le conteneur
COPY . .

# Installez Gunicorn et les dépendances nécessaires
RUN pip install gunicorn
RUN pip install --no-cache-dir -r requirements.txt

# Commande pour démarrer l'application Flask
CMD ["gunicorn", "-c", "gunicorn_config.py", "app:app"]
