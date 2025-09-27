@echo off
echo.
echo 🎬 TikTok Downloader - Instalando FFmpeg
echo ========================================
echo.

REM Verificar se winget está disponível
winget --version >nul 2>&1
if errorlevel 1 (
    echo ❌ WinGet não encontrado!
    echo.
    echo Por favor, instale o FFmpeg manualmente:
    echo 1. Baixe de: https://ffmpeg.org/download.html
    echo 2. Extraia para C:\ffmpeg\
    echo 3. Adicione C:\ffmpeg\bin ao PATH do sistema
    echo.
    pause
    exit /b 1
)

echo ✅ WinGet encontrado
echo.
echo 📥 Instalando FFmpeg via WinGet...
echo.

REM Instalar FFmpeg
winget install ffmpeg

if errorlevel 1 (
    echo.
    echo ❌ Erro ao instalar FFmpeg via WinGet!
    echo.
    echo Tente instalar manualmente:
    echo 1. Baixe de: https://ffmpeg.org/download.html
    echo 2. Extraia para C:\ffmpeg\
    echo 3. Adicione C:\ffmpeg\bin ao PATH do sistema
    echo.
    pause
    exit /b 1
)

echo.
echo ✅ FFmpeg instalado com sucesso!
echo.
echo 🔧 Configurando PATH...

REM Encontrar o caminho do FFmpeg instalado pelo WinGet
set FFMPEG_PATH=
for /d %%i in ("%LOCALAPPDATA%\Microsoft\WinGet\Packages\Gyan.FFmpeg*") do (
    if exist "%%i\ffmpeg-*\bin\ffmpeg.exe" (
        for /d %%j in ("%%i\ffmpeg-*") do (
            set FFMPEG_PATH=%%j\bin
            goto :found
        )
    )
)

:found
if "%FFMPEG_PATH%"=="" (
    echo ⚠️ Caminho do FFmpeg não encontrado automaticamente
    echo.
    echo O FFmpeg foi instalado, mas você pode precisar:
    echo 1. Reiniciar o terminal
    echo 2. Ou usar o script 'run_tiktok_downloader.bat'
    echo.
) else (
    echo ✅ FFmpeg encontrado em: %FFMPEG_PATH%
    echo.
    echo 💡 Para usar o FFmpeg em qualquer terminal, adicione ao PATH do sistema:
    echo %FFMPEG_PATH%
    echo.
)

echo 🎉 Instalação do FFmpeg concluída!
echo.
echo Agora você pode executar 'run_tiktok_downloader.bat' para usar o sistema completo
echo.
pause
