#!/bin/bash
# Script de sincronización rápida para el Búnker Digital

echo "🔍 Verificando estado del repositorio..."
git status -s

echo "➕ Agregando cambios..."
git add .

read -p "📝 Mensaje del commit (presiona Enter para usar mensaje por defecto): " msg
if [ -z "$msg" ]; then
    msg="update: actualización de registros y documentos $(date +'%Y-%m-%d %H:%M')"
fi

git commit -m "$msg"

echo "🚀 Subiendo a GitHub..."
git push origin main

echo "✅ ¡Sincronización completada con éxito!"
