#!/bin/bash

# Navegar al directorio del búnker
cd "$(dirname "$0")"

echo "=========================================="
echo "   🚀 BÚNKER DIGITAL - GESTIÓN TOTAL"
echo "=========================================="

# Ejecutar el tracker de postulaciones
python3 tracker.py

# Ejecutar la sincronización automática al salir
echo ""
echo "🔄 Iniciando sincronización automática con GitHub..."
./sync.sh
