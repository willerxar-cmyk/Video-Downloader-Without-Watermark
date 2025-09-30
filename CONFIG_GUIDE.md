# 📝 Guia de Configuração

Este guia explica como personalizar o comportamento do Multi-Platform Video Downloader usando o arquivo `config.json`.

## 📁 Arquivos de Configuração

- **`config.json`** - Arquivo de configuração ativo (edite este arquivo)
- **`config.example.json`** - Arquivo de exemplo com todas as opções e comentários

## 🎨 Configuração de Bordas

### Modo: Random (Aleatório)
Adiciona bordas com tamanho aleatório em cada vídeo processado.

```json
{
  "anti_detection": {
    "border": {
      "mode": "random",
      "random_min": 8,
      "random_max": 20,
      "color": "white"
    }
  }
}
```

**Resultado:** Cada vídeo terá uma borda entre 8px e 20px.

---

### Modo: Fixed (Fixo)
Adiciona bordas com tamanho fixo em todos os vídeos.

```json
{
  "anti_detection": {
    "border": {
      "mode": "fixed",
      "fixed_size": 15,
      "color": "white"
    }
  }
}
```

**Resultado:** Todos os vídeos terão borda de 15px.

---

### Modo: None (Sem Borda)
Não adiciona bordas aos vídeos.

```json
{
  "anti_detection": {
    "border": {
      "mode": "none"
    }
  }
}
```

**Resultado:** Vídeos sem bordas.

---

## 🎨 Cores de Borda Disponíveis

Você pode usar qualquer cor suportada pelo FFmpeg:

- `white` - Branco (padrão)
- `black` - Preto
- `red` - Vermelho
- `blue` - Azul
- `green` - Verde
- `yellow` - Amarelo
- `gray` - Cinza
- `#RRGGBB` - Código hexadecimal (ex: `#FF5733`)

**Exemplo com borda preta:**
```json
{
  "anti_detection": {
    "border": {
      "mode": "fixed",
      "fixed_size": 10,
      "color": "black"
    }
  }
}
```

---

## 💡 Filtros de Cor

### Desabilitar Todos os Filtros
```json
{
  "anti_detection": {
    "brightness": {"enabled": false},
    "contrast": {"enabled": false},
    "saturation": {"enabled": false},
    "hue": {"enabled": false}
  }
}
```

### Desabilitar Apenas Alguns Filtros
```json
{
  "anti_detection": {
    "brightness": {"enabled": true},
    "contrast": {"enabled": true},
    "saturation": {"enabled": false},
    "hue": {"enabled": false}
  }
}
```

### Ajustar Intensidade dos Filtros
```json
{
  "anti_detection": {
    "brightness": {
      "enabled": true,
      "random_min": 0.05,
      "random_max": 0.15
    },
    "contrast": {
      "enabled": true,
      "random_min": 1.05,
      "random_max": 1.15
    }
  }
}
```

---

## 🎬 Configurações de Vídeo

### Qualidade Máxima (Processamento Lento)
```json
{
  "video": {
    "codec": "libx264",
    "preset": "veryslow",
    "crf": "18"
  }
}
```

### Qualidade Balanceada (Padrão)
```json
{
  "video": {
    "codec": "libx264",
    "preset": "medium",
    "crf": "23"
  }
}
```

### Processamento Rápido (Qualidade Menor)
```json
{
  "video": {
    "codec": "libx264",
    "preset": "ultrafast",
    "crf": "28"
  }
}
```

### Explicação dos Parâmetros

- **preset:** Velocidade de encoding
  - `ultrafast` - Muito rápido, qualidade menor
  - `fast` - Rápido
  - `medium` - Balanceado (padrão)
  - `slow` - Lento, melhor qualidade
  - `veryslow` - Muito lento, máxima qualidade

- **crf:** Qualidade do vídeo (18-28)
  - `18` - Qualidade máxima (arquivo maior)
  - `23` - Qualidade boa (padrão)
  - `28` - Qualidade aceitável (arquivo menor)

---

## 📂 Configurações de Saída

### Mudar Pasta de Saída
```json
{
  "output": {
    "directory": "meus_videos",
    "remove_metadata": true
  }
}
```

### Desabilitar Remoção de Metadados
```json
{
  "output": {
    "directory": "output",
    "remove_metadata": false
  }
}
```

---

## 🔧 Exemplos de Configurações Completas

### Exemplo 1: Máxima Anti-Detecção
```json
{
  "anti_detection": {
    "enabled": true,
    "border": {
      "mode": "random",
      "random_min": 15,
      "random_max": 30,
      "color": "white"
    },
    "brightness": {
      "enabled": true,
      "random_min": 0.05,
      "random_max": 0.12
    },
    "contrast": {
      "enabled": true,
      "random_min": 1.05,
      "random_max": 1.12
    },
    "saturation": {
      "enabled": true,
      "random_min": 0.95,
      "random_max": 1.08
    },
    "hue": {
      "enabled": true,
      "random_min": -0.05,
      "random_max": 0.05
    }
  }
}
```

### Exemplo 2: Apenas Borda, Sem Filtros
```json
{
  "anti_detection": {
    "enabled": true,
    "border": {
      "mode": "fixed",
      "fixed_size": 20,
      "color": "black"
    },
    "brightness": {"enabled": false},
    "contrast": {"enabled": false},
    "saturation": {"enabled": false},
    "hue": {"enabled": false}
  }
}
```

### Exemplo 3: Sem Anti-Detecção (Apenas Download)
```json
{
  "anti_detection": {
    "enabled": false
  },
  "output": {
    "directory": "downloads",
    "remove_metadata": true
  }
}
```

### Exemplo 4: Processamento Rápido
```json
{
  "anti_detection": {
    "enabled": true,
    "border": {
      "mode": "fixed",
      "fixed_size": 10,
      "color": "white"
    },
    "brightness": {"enabled": false},
    "contrast": {"enabled": false},
    "saturation": {"enabled": false},
    "hue": {"enabled": false}
  },
  "video": {
    "preset": "ultrafast",
    "crf": "28"
  }
}
```

---

## 🚀 Como Usar

1. **Edite o arquivo `config.json`** com suas preferências
2. **Execute o programa normalmente:**
   ```bash
   python main.py
   ```
3. **O sistema carregará automaticamente suas configurações**

---

## ⚠️ Notas Importantes

- Se o arquivo `config.json` não existir, o sistema usará configurações padrão
- Campos com `_` no início (como `_comment`) são ignorados
- Valores inválidos serão substituídos pelos padrões
- Você pode copiar `config.example.json` para `config.json` e editar

---

## 🔄 Restaurar Configurações Padrão

Para restaurar as configurações padrão, delete o arquivo `config.json` ou copie o conteúdo de `config.example.json`.

---

## 💡 Dicas

1. **Para vídeos do TikTok:** Use bordas maiores (15-25px) para melhor evasão
2. **Para vídeos do YouTube:** Bordas menores (8-15px) são suficientes
3. **Para Instagram:** Combine bordas com filtros de cor para melhor resultado
4. **Processamento rápido:** Desabilite filtros de cor e use preset `fast`
5. **Máxima qualidade:** Use preset `veryslow` e crf `18`

---

## 📊 Comparação de Modos

| Modo | Velocidade | Qualidade | Anti-Detecção | Tamanho do Arquivo |
|------|-----------|-----------|---------------|-------------------|
| Sem anti-detecção | ⚡⚡⚡⚡⚡ | ⭐⭐⭐⭐⭐ | ❌ | Pequeno |
| Apenas borda | ⚡⚡⚡⚡ | ⭐⭐⭐⭐ | ⭐⭐ | Médio |
| Borda + Filtros | ⚡⚡⚡ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | Médio |
| Máxima anti-detecção | ⚡⚡ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Grande |

---

## 🆘 Problemas Comuns

### Erro ao carregar config.json
- Verifique se o JSON está válido (use um validador online)
- Certifique-se de que não há vírgulas extras
- Verifique se todas as chaves estão entre aspas duplas

### Vídeo muito grande
- Aumente o valor de `crf` (ex: 25 ou 28)
- Use preset `fast` ou `ultrafast`
- Reduza o tamanho das bordas

### Processamento muito lento
- Use preset `fast` ou `ultrafast`
- Desabilite alguns filtros de cor
- Reduza o tamanho das bordas

---

Para mais informações, consulte `ANTI_DETECTION.md` e `README.md`.

