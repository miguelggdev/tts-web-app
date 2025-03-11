#!/bin/bash

# Actualiza los paquetes del sistema en Render
apt-get update && apt-get install -y libffi-dev libssl-dev libselinux1

# Instala las dependencias del proyecto
pip install -r requirements.txt
