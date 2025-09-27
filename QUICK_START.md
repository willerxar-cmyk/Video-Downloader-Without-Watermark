# 🚀 Início Rápido - TikTok Downloader

## ⚡ Instalação Ultra-Rápida

1. **Setup automático completo:**
   ```cmd
   setup_complete.bat
   ```

   Isso instala tudo automaticamente!

## 🎯 Uso Imediato

1. **Execute o sistema:**
   ```cmd
   run_tiktok_downloader.bat
   ```

2. **Digite a URL do TikTok quando solicitado**

3. **Pressione Enter para baixar**

4. **Repita para mais downloads ou digite 'quit' para sair**

## 📁 Onde encontrar os vídeos

Os vídeos são salvos na pasta `output/` com o formato:
```
clean_usuario_titulo_id.mp4
```

## ✅ Verificar se está funcionando

```cmd
python test_system.py
```

## 🔧 Status Atual

- ✅ Python 3.13 - OK
- ✅ Dependências instaladas - OK
- ✅ Sistema funcionando - OK
- ⚠️ FFmpeg não instalado (opcional para remoção de metadados)

## 💡 Dicas

- **Sem ffmpeg:** O download funciona, mas metadados não são removidos
- **Com ffmpeg:** Download + remoção completa de metadados
- **URLs suportadas:** Todos os formatos do TikTok (padrão, vm.tiktok.com, etc.)

## 🆘 Problemas Comuns

**"Invalid TikTok URL"**
- Verifique se a URL está correta
- Teste com URL completa: `https://www.tiktok.com/@user/video/123`

**"ffmpeg not found"**
- Sistema funciona sem ffmpeg
- Para remover metadados, instale o ffmpeg

**Erro de download**
- Verifique conexão com internet
- Vídeo pode estar privado ou removido
