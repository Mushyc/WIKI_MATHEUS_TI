@echo off
title Iniciar Wiki Matheus TI
color 0B
echo.
echo ====================================
echo   INICIANDO WIKI PESSOAL
echo   Framework: VitePress
echo ====================================
echo.

if not exist node_modules (
    echo [!] Dependencias nao encontradas. Instalando...
    npm install
)

echo [OK] Servidor iniciando...
npm run dev
pause
