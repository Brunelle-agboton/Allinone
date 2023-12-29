# Utilisation d'une image Python officielle comme base
FROM python:3.8

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de dépendances et installer les packages
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code de l'application dans le conteneur
COPY . .

# Exposer le port sur lequel Gunicorn va s'exécuter
EXPOSE 5000

# Commande pour lancer l'application Flask avec Gunicorn
CMD ["gunicorn", "-w", "4", "app:app", "--bind", "0.0.0.0:5000"]