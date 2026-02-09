#!/bin/bash
# Script de recuperacion ante borrado accidental de archivos

# Restaura todos los archivos del repositorio al ultimo estado guardado en Git
git checkout .

echo "Archivos restaurados correctamente desde el repositorio local"