@echo off
echo.
echo 🔧 TikTok Downloader - Instalando Dependências
echo ===============================================
echo.

REM Verificar se Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python não encontrado!
    echo.
    echo Por favor, instale o Python primeiro:
    echo https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

echo ✅ Python encontrado
python --version

echo.
echo 📦 Instalando dependências Python...
echo.

REM Instalar dependências
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo ❌ Erro ao instalar dependências!
    echo.
    pause
    exit /b 1
)

echo.
echo ✅ Dependências instaladas com sucesso!
echo.
echo 📁 Criando pasta output...
if not exist "output" mkdir output
echo ✅ Pasta output criada

echo.
echo 🎉 Instalação concluída!
echo.
echo Próximos passos:
echo 1. Execute 'install_ffmpeg.bat' para instalar o FFmpeg
echo 2. Execute 'run_tiktok_downloader.bat' para usar o sistema
echo.
pause
