#!/usr/bin/env python3
"""
Script de teste para o TikTok Downloader
Verifica se todas as dependências estão funcionando corretamente.
"""

import sys
import subprocess
import tempfile
import os
from pathlib import Path


def test_python_version():
    """Testa a versão do Python."""
    print("🐍 Testando versão do Python...")
    if sys.version_info >= (3, 7):
        print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} - OK")
        return True
    else:
        print(f"❌ Python {sys.version_info.major}.{sys.version_info.minor} - Versão muito antiga")
        return False


def test_imports():
    """Testa se as bibliotecas necessárias podem ser importadas."""
    print("\n📦 Testando importações...")
    
    tests = [
        ("yt_dlp", "yt-dlp"),
        ("ffmpeg", "ffmpeg-python"),
        ("pathlib", "pathlib (built-in)"),
        ("tempfile", "tempfile (built-in)"),
        ("subprocess", "subprocess (built-in)"),
        ("re", "re (built-in)"),
    ]
    
    all_passed = True
    
    for module, description in tests:
        try:
            __import__(module)
            print(f"✅ {description} - OK")
        except ImportError as e:
            print(f"❌ {description} - ERRO: {e}")
            all_passed = False
    
    return all_passed


def test_ffmpeg():
    """Testa se o ffmpeg está disponível."""
    print("\n🎬 Testando ffmpeg...")
    try:
        result = subprocess.run(
            ['ffmpeg', '-version'], 
            capture_output=True, 
            text=True, 
            timeout=10
        )
        if result.returncode == 0:
            # Extrair versão do ffmpeg
            version_line = result.stdout.split('\n')[0]
            print(f"✅ {version_line}")
            return True
        else:
            print(f"❌ ffmpeg retornou código de erro: {result.returncode}")
            return False
    except FileNotFoundError:
        print("❌ ffmpeg não encontrado no PATH")
        print("   Instale o ffmpeg: https://ffmpeg.org/download.html")
        return False
    except subprocess.TimeoutExpired:
        print("❌ ffmpeg não respondeu (timeout)")
        return False
    except Exception as e:
        print(f"❌ Erro ao testar ffmpeg: {e}")
        return False


def test_multiplatform_downloader():
    """Testa se o módulo MultiPlatformDownloader pode ser importado."""
    print("\n📱 Testando MultiPlatformDownloader...")
    try:
        from main import MultiPlatformDownloader
        print("✅ MultiPlatformDownloader importado com sucesso")

        # Testar criação de instância
        with tempfile.TemporaryDirectory() as temp_dir:
            downloader = MultiPlatformDownloader(output_dir=temp_dir)
            print("✅ Instância criada com sucesso")

            # Testar validação de URLs para múltiplas plataformas
            valid_urls = [
                # TikTok
                "https://www.tiktok.com/@user/video/1234567890",
                "https://vm.tiktok.com/ZMexample",
                "https://vt.tiktok.com/ZSexample",
                "https://m.tiktok.com/v/1234567890",
                # YouTube
                "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                "https://youtu.be/dQw4w9WgXcQ",
                "https://www.youtube.com/shorts/abc123",
                # Instagram
                "https://www.instagram.com/p/ABC123",
                "https://www.instagram.com/reel/ABC123",
            ]

            invalid_urls = [
                "https://facebook.com/video/123",
                "https://twitter.com/status/123",
                "not_a_url",
                "",
            ]

            print("✅ Testando validação de URLs...")

            # Testar URLs válidas
            for url in valid_urls:
                if downloader.validate_url(url):
                    platform = downloader.detect_platform(url)
                    print(f"  ✅ {platform}: {url[:50]}... - válida")
                else:
                    print(f"  ❌ {url} - deveria ser válida")

            # Testar URLs inválidas
            for url in invalid_urls:
                if not downloader.validate_url(url):
                    print(f"  ✅ {url} - corretamente rejeitada")
                else:
                    print(f"  ❌ {url} - deveria ser rejeitada")

            # Testar detecção de plataforma
            print("✅ Testando detecção de plataforma...")
            test_platforms = [
                ("https://www.tiktok.com/@user/video/123", "TikTok"),
                ("https://www.youtube.com/watch?v=123", "YouTube"),
                ("https://www.instagram.com/p/123", "Instagram"),
                ("https://shopee.com.br/produto-i.123.456", "Shopee"),
                ("https://unknown.com/video/123", "Unknown"),
            ]

            for url, expected in test_platforms:
                detected = downloader.detect_platform(url)
                if detected == expected:
                    print(f"  ✅ {expected}: {url[:40]}...")
                else:
                    print(f"  ❌ {url}: esperado {expected}, detectado {detected}")

            # Testar detecção específica do Shopee
            print("✅ Testando detecção de URLs Shopee...")
            shopee_urls = [
                "https://shopee.com.br/produto-i.123.456",
                "https://shopee.com.my/product-i.123.456",
                "https://shopee.ph/product-i.123.456",
                "https://shopee.sg/product-i.123.456",
            ]

            for url in shopee_urls:
                if downloader.is_shopee_url(url):
                    print(f"  ✅ Shopee detectado: {url[:50]}...")
                else:
                    print(f"  ❌ Shopee não detectado: {url}")

        return True

    except ImportError as e:
        print(f"❌ Erro ao importar MultiPlatformDownloader: {e}")
        return False
    except Exception as e:
        print(f"❌ Erro ao testar MultiPlatformDownloader: {e}")
        return False


def test_output_directory():
    """Testa se a pasta output pode ser criada."""
    print("\n📁 Testando criação de diretório...")
    try:
        output_dir = Path("output")
        output_dir.mkdir(exist_ok=True)
        
        if output_dir.exists() and output_dir.is_dir():
            print(f"✅ Diretório 'output' criado: {output_dir.absolute()}")
            return True
        else:
            print("❌ Falha ao criar diretório 'output'")
            return False
    except Exception as e:
        print(f"❌ Erro ao criar diretório: {e}")
        return False


def test_file_permissions():
    """Testa permissões de escrita."""
    print("\n🔐 Testando permissões de escrita...")
    try:
        test_file = Path("output") / "test_write.txt"
        test_file.write_text("teste")
        
        if test_file.exists():
            test_file.unlink()  # Remove o arquivo de teste
            print("✅ Permissões de escrita - OK")
            return True
        else:
            print("❌ Falha ao escrever arquivo de teste")
            return False
    except Exception as e:
        print(f"❌ Erro de permissão: {e}")
        return False


def main():
    """Função principal de teste."""
    print("🧪 TESTE DO SISTEMA MULTI-PLATFORM DOWNLOADER (TikTok, YouTube, Instagram, Shopee)")
    print("=" * 50)

    tests = [
        ("Versão do Python", test_python_version),
        ("Importações", test_imports),
        ("FFmpeg", test_ffmpeg),
        ("MultiPlatformDownloader", test_multiplatform_downloader),
        ("Diretório Output", test_output_directory),
        ("Permissões", test_file_permissions),
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ Erro inesperado em {test_name}: {e}")
            results.append((test_name, False))
    
    # Resumo dos resultados
    print("\n" + "=" * 50)
    print("📊 RESUMO DOS TESTES")
    print("=" * 50)
    
    passed = 0
    failed = 0
    
    for test_name, result in results:
        if result:
            print(f"✅ {test_name}")
            passed += 1
        else:
            print(f"❌ {test_name}")
            failed += 1
    
    print(f"\n📈 Resultados: {passed} passou(m), {failed} falhou(ram)")
    
    if failed == 0:
        print("\n🎉 TODOS OS TESTES PASSARAM!")
        print("O sistema está pronto para uso.")
        print("\nPara usar:")
        print("  python tiktok_downloader.py <url_do_tiktok>")
    else:
        print(f"\n⚠️ {failed} teste(s) falharam.")
        print("Verifique os erros acima antes de usar o sistema.")
        
        if any("ffmpeg" in name for name, result in results if not result):
            print("\n💡 Dica: Se apenas o ffmpeg falhou, o download ainda funcionará,")
            print("   mas os metadados não serão removidos.")
    
    return failed == 0


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
