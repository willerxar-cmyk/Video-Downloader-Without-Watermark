# 🎬 Como Usar o Multi-Platform Video Downloader

## 🚀 Primeira Vez (Setup)

Execute apenas uma vez:
```cmd
setup_complete.bat
```

Este comando irá:
- ✅ Instalar todas as dependências Python
- ✅ Instalar o FFmpeg automaticamente
- ✅ Configurar tudo para você
- ✅ Testar se está funcionando

## 📱 Uso Diário

Para baixar vídeos do TikTok:

1. **Execute:**
   ```cmd
   run_tiktok_downloader.bat
   ```

2. **Digite a URL quando solicitado:**
   ```
   URL: https://www.tiktok.com/@usuario/video/123456
   ```

3. **Pressione Enter e aguarde o download**

4. **Para baixar outro vídeo, digite nova URL**

5. **Para sair, digite:** `quit`

## 📁 Onde Encontrar os Vídeos

Os vídeos baixados ficam na pasta `output/` com nomes limpos:
```
output/clean_usuario_titulo_id.mp4
```

## 🔧 Scripts Disponíveis

| Script | Função |
|--------|--------|
| `setup_complete.bat` | Setup completo (execute apenas uma vez) |
| `run_tiktok_downloader.bat` | Executar o downloader (uso diário) |
| `install_requirements.bat` | Instalar apenas dependências Python |
| `install_ffmpeg.bat` | Instalar apenas FFmpeg |
| `test_system.py` | Testar se tudo está funcionando |

## 💡 Dicas

- ✅ **URLs suportadas:** Todos os formatos do TikTok
- ✅ **Qualidade:** Sempre a melhor disponível
- ✅ **Metadados:** Removidos automaticamente (com FFmpeg)
- ✅ **Uso contínuo:** Baixe vários vídeos em sequência
- ✅ **Interrupção:** Use Ctrl+C ou digite 'quit'

## 🆘 Problemas?

**"Python não encontrado"**
- Instale o Python: https://www.python.org/downloads/

**"Dependências não instaladas"**
- Execute: `install_requirements.bat`

**"FFmpeg não encontrado"**
- Execute: `install_ffmpeg.bat`
- Ou use sem FFmpeg (funciona, mas não remove metadados)

**"URL inválida"**
- Verifique se é uma URL do TikTok
- Teste com URL completa

**Outros problemas**
- Execute: `python test_system.py`
- Verifique se todos os testes passam
