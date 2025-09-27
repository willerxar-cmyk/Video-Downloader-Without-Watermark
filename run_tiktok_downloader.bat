@echo off
REM TikTok Downloader - Script principal de execução
REM Configura o PATH do FFmpeg e executa o downloader

echo.
echo 🎬 Multi-Platform Video Downloader
echo ===================================
echo 📱 Supports: TikTok, YouTube, Instagram
echo.

REM Verificar se Python está disponível
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python não encontrado!
    echo.
    echo Execute primeiro: install_requirements.bat
    echo.
    pause
    exit /b 1
)

REM Verificar se as dependências estão instaladas
python -c "import yt_dlp, ffmpeg" >nul 2>&1
if errorlevel 1 (
    echo ❌ Dependências não instaladas!
    echo.
    echo Execute primeiro: install_requirements.bat
    echo.
    pause
    exit /b 1
)

REM Configurar PATH do FFmpeg (múltiplas tentativas)
set FFMPEG_FOUND=0

REM Tentar encontrar FFmpeg em locais comuns
for /d %%i in ("%LOCALAPPDATA%\Microsoft\WinGet\Packages\Gyan.FFmpeg*") do (
    if exist "%%i\ffmpeg-*\bin\ffmpeg.exe" (
        for /d %%j in ("%%i\ffmpeg-*") do (
            set PATH=%PATH%;%%j\bin
            set FFMPEG_FOUND=1
            echo ✅ FFmpeg configurado: %%j\bin
            goto :ffmpeg_configured
        )
    )
)

REM Verificar se FFmpeg já está no PATH
ffmpeg -version >nul 2>&1
if not errorlevel 1 (
    set FFMPEG_FOUND=1
    echo ✅ FFmpeg já disponível no PATH
)

:ffmpeg_configured
if %FFMPEG_FOUND%==0 (
    echo ⚠️ FFmpeg não encontrado
    echo.
    echo O sistema funcionará, mas sem remoção de metadados
    echo Para instalar o FFmpeg, execute: install_ffmpeg.bat
    echo.
)

echo.
echo 🚀 Iniciando Multi-Platform Downloader...
echo.

REM Executar o downloader
python main.py

echo.
echo 👋 Multi-Platform Downloader finalizado
pause
