# Usa una imagen base con Miniconda (más ligera que Anaconda)
FROM continuumio/anaconda3

# Instala dependencias del sistema (git + herramientas de compilación)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git \
        build-essential \       
        gcc \                   
        g++ \                   
        python3-dev \           
        && \
    rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo
WORKDIR /app

# Configura el shell para que conda funcione inmediatamente
SHELL ["/bin/bash", "--login", "-c"]

# Inicializa Conda para el usuario root
RUN conda init bash

# Comando por defecto: shell interactiva con Conda disponible
CMD ["/bin/bash", "--login"]
