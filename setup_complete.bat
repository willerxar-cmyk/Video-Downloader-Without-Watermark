@echo off
echo.
echo 🚀 TikTok Downloader - Setup Completo
echo =====================================
echo.
echo Este script irá:
echo 1. Instalar dependências Python
echo 2. Instalar FFmpeg
echo 3. Configurar o sistema
echo.
set /p confirm="Continuar? (S/N): "
if /i not "%confirm%"=="S" (
    echo.
    echo ❌ Setup cancelado
    pause
    exit /b 0
)

echo.
echo 📋 Iniciando setup completo...
echo.

REM Passo 1: Instalar dependências
echo ==========================================
echo 📦 PASSO 1/3: Instalando dependências...
echo ==========================================
call install_requirements.bat
if errorlevel 1 (
    echo.
    echo ❌ Falha na instalação das dependências
    pause
    exit /b 1
)

echo.
echo ==========================================
echo 🎬 PASSO 2/3: Instalando FFmpeg...
echo ==========================================
call install_ffmpeg.bat
if errorlevel 1 (
    echo.
    echo ⚠️ FFmpeg pode não ter sido instalado corretamente
    echo O sistema funcionará, mas sem remoção de metadados
)

echo.
echo ==========================================
echo ✅ PASSO 3/3: Testando sistema...
echo ==========================================

REM Configurar PATH temporário para teste
for /d %%i in ("%LOCALAPPDATA%\Microsoft\WinGet\Packages\Gyan.FFmpeg*") do (
    if exist "%%i\ffmpeg-*\bin\ffmpeg.exe" (
        for /d %%j in ("%%i\ffmpeg-*") do (
            set PATH=%PATH%;%%j\bin
            goto :test_system
        )
    )
)

:test_system
python test_system.py

echo.
echo ==========================================
echo 🎉 SETUP COMPLETO!
echo ==========================================
echo.
echo ✅ Sistema instalado e configurado
echo.
echo 📖 Como usar:
echo   1. Execute: run_tiktok_downloader.bat
echo   2. Digite a URL do TikTok
echo   3. Pressione Enter para baixar
echo.
echo 📁 Os vídeos serão salvos na pasta 'output'
echo.
echo 💡 Dicas:
echo   - Digite 'quit' para sair
echo   - Use Ctrl+C para interromper
echo.
pause
