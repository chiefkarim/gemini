#!/bin/bash

# Vérifie si l'environnement virtuel est activé
if [ -z "$VIRTUAL_ENV" ]; then
  echo "Activation de l'environnement virtuel..."
  source .venv/bin/activate
else
  echo "L'environnement virtuel est déjà activé."
fi

# Lance l'application uvicorn
uvicorn routes.app:app --reload
