# Multi-Platform Video Downloader

Um microsistema ultra-funcional em Python para download de vídeos do **TikTok, YouTube e Instagram** com a melhor qualidade possível, remoção de metadados e salvamento na pasta output.

## 🚀 Características

- ✅ **Multi-plataforma:** TikTok, YouTube, Instagram
- ✅ **Melhor qualidade:** Download na melhor qualidade disponível (até 1080p)
- ✅ **Sem metadados:** Remoção completa de metadados dos vídeos
- ✅ **Organizado:** Salvamento automático na pasta `output`
- ✅ **Nomes limpos:** Arquivos com nomes organizados e seguros
- ✅ **Validação inteligente:** Detecta e valida URLs automaticamente
- ✅ **Interface amigável:** Modo interativo contínuo
- ✅ **Robusto:** Tratamento avançado de erros


## 📋 Pré-requisitos

- Python 3.7 ou superior
- ffmpeg (para remoção de metadados)

### Instalação do ffmpeg

**Windows:**
1. Baixe o ffmpeg de https://ffmpeg.org/download.html
2. Extraia e adicione ao PATH do sistema

**macOS:**
```bash
brew install ffmpeg
```

**Ubuntu/Debian:**
```bash
sudo apt install ffmpeg
```

**CentOS/RHEL:**
```bash
sudo yum install ffmpeg
```

## 🛠️ Instalação

### Instalação Automática (Recomendada)

Execute o setup completo:
```cmd
setup_complete.bat
```

Este script irá automaticamente:
- Instalar dependências Python
- Instalar FFmpeg via WinGet
- Configurar o sistema
- Testar tudo

### Instalação Manual

1. **Instalar dependências:**
   ```cmd
   install_requirements.bat
   ```

2. **Instalar FFmpeg:**
   ```cmd
   install_ffmpeg.bat
   ```

3. **Testar sistema:**
   ```cmd
   python test_system.py
   ```

## 📖 Como Usar

### Uso Principal (Recomendado)

Execute o sistema interativo:
```cmd
run_tiktok_downloader.bat
```

O sistema irá:
1. **Solicitar URL:** Digite a URL do TikTok
2. **Processar:** Baixar e limpar o vídeo automaticamente
3. **Repetir:** Voltar a pedir nova URL para próximo download
4. **Sair:** Digite 'quit' ou pressione Ctrl+C

### Uso por Linha de Comando

Para download único:
```cmd
python tiktok_downloader.py "https://www.tiktok.com/@usuario/video/123"
```

### Exemplos de URLs Suportadas

**📱 TikTok:**
```
https://www.tiktok.com/@taynaras2martins/video/7524848855460973830
https://vm.tiktok.com/ZMexample
https://vt.tiktok.com/ZSexample
https://m.tiktok.com/v/1234567890
```

**📺 YouTube:**
```
https://www.youtube.com/watch?v=dQw4w9WgXcQ
https://youtu.be/dQw4w9WgXcQ
https://www.youtube.com/shorts/abc123
```

**📷 Instagram:**
```
https://www.instagram.com/p/ABC123
https://www.instagram.com/reel/ABC123
https://www.instagram.com/tv/ABC123
```


### Uso Programático

```python
from tiktok_downloader import TikTokDownloader

# Criar instância do downloader
downloader = TikTokDownloader(output_dir="meus_videos")

# Processar vídeo
url = "https://www.tiktok.com/@usuario/video/1234567890"
resultado = downloader.process_video(url)

if resultado:
    print(f"Vídeo salvo em: {resultado}")
else:
    print("Falha no download")
```

## 📁 Estrutura de Arquivos

```
tiktokcleaner/
├── tiktok_downloader.py      # Script principal (modo interativo)
├── setup_complete.bat        # Setup automático completo
├── install_requirements.bat  # Instalar dependências Python
├── install_ffmpeg.bat        # Instalar FFmpeg
├── run_tiktok_downloader.bat # Executar o sistema
├── test_system.py           # Testar o sistema
├── requirements.txt         # Dependências Python
├── README.md               # Este arquivo
└── output/                 # Pasta onde os vídeos são salvos
```

## 🔧 Dependências

- **yt-dlp**: Downloader de vídeos moderno e atualizado
- **ffmpeg-python**: Interface Python para ffmpeg

## 📝 Formato dos Arquivos Salvos

Os vídeos são salvos com o formato:
```
clean_{uploader}_{titulo}_{id}.mp4
```

Exemplo:
```
clean_usuario_video_incrivel_1234567890.mp4
```

## 🛡️ Características de Segurança

- Validação rigorosa de URLs
- Nomes de arquivo sanitizados
- Remoção completa de metadados
- Tratamento seguro de erros
- Limpeza automática de arquivos temporários

## ⚠️ Limitações

- Funciona apenas com vídeos públicos do TikTok
- Qualidade limitada pela disponibilidade no TikTok
- Requer conexão com internet
- Alguns vídeos podem ter restrições geográficas

## 🐛 Solução de Problemas

### Erro: "ffmpeg is not installed"
- Instale o ffmpeg seguindo as instruções acima
- Verifique se está no PATH do sistema

### Erro: "Invalid TikTok URL"
- Verifique se a URL está correta
- Teste com diferentes formatos de URL do TikTok

### Erro de download
- Verifique sua conexão com internet
- O vídeo pode estar privado ou removido
- Tente novamente após alguns minutos

## 📄 Licença

Este projeto é fornecido "como está" para fins educacionais. Respeite os termos de serviço do TikTok e os direitos autorais dos criadores de conteúdo.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir melhorias
- Enviar pull requests

## 📞 Suporte

Se encontrar problemas, verifique:
1. Se todas as dependências estão instaladas
2. Se o ffmpeg está funcionando
3. Se a URL do TikTok é válida
4. Se há conexão com internet
