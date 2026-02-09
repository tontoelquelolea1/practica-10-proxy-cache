#!/bin/bash
echo "🛠️ Recuperando archivos borrados..."

# Git restaura cualquier archivo que falte o haya sido modificado
git checkout .

echo "✅ Archivos restaurados desde el repositorio local."
ls -l