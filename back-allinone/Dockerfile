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
RUN pip install -r requirements.txt

# Exposez le port sur lequel Gunicorn va écouter
EXPOSE 5000

# Commande pour démarrer l'application avec Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app", "--log-file", "gunicorn.log"]
