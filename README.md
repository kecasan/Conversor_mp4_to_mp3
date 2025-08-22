### 🎵 Conversor de Vídeo para MP3 (Python + FFmpeg)

Um script simples em Python para converter vídeos (.mp4, .mkv, etc.) em arquivos de áudio .mp3 com qualidade até 320kbps.

Ideal para extrair músicas, diálogos ou trilhas sonoras de filmes.

-----

### 🚀 Requisitos

  - **Python 3.8+**
  - **FFmpeg** instalado e disponível no sistema
  - **Bibliotecas Python**:

<!-- end list -->

```bash
pip install ffmpeg-python
# ou, se preferir,
pip install moviepy
```

-----

### ⚙️ Instalação do FFmpeg (Windows)

1.  Baixe a versão oficial do FFmpeg em: [👉 FFmpeg builds (gyan.dev)](https://www.gyan.dev/ffmpeg/builds/)
2.  Escolha o `Release full build` (arquivo .zip).
3.  Extraia em `C:\ffmpeg\`.
4.  Adicione o caminho `C:\ffmpeg\bin` ao **PATH** do Windows:
      - Menu iniciar → "Variáveis de ambiente"
      - Editar variável `Path` → Novo → `C:\ffmpeg\bin`
5.  Teste no terminal:

<!-- end list -->

```bash
ffmpeg -version
```

Se aparecer a versão → instalação concluída ✅

> **🔹 Dica rápida:** se não quiser configurar o PATH, basta colocar o `ffmpeg.exe` na mesma pasta do `main.py`.

-----

### ▶️ Como usar

1.  Coloque o vídeo (.mp4, .mkv, etc.) na mesma pasta do `main.py`.
2.  Execute:

<!-- end list -->

```bash
python main.py
```

O `.mp3` será gerado na mesma pasta.

-----

### 🛠️ Possíveis Erros e Soluções

**❌ `module 'ffmpeg' has no attribute 'input'`**
Você instalou o pacote errado (`ffmpeg` em vez de `ffmpeg-python`).

✅ **Solução:**

```bash
pip uninstall ffmpeg
pip install ffmpeg-python
```

**❌ `[WinError 2] O sistema não pode encontrar o arquivo especificado`**
O Python não achou o `ffmpeg.exe`.

✅ **Soluções:**

  - Instalar o FFmpeg e adicionar ao PATH (passo a passo acima).
  - OU colocar o `ffmpeg.exe` na mesma pasta do `main.py`.

**⚠️ Erros de qualidade do áudio**
Se o MP3 sair com qualidade baixa, defina o bitrate manualmente no script:

```python
.output("saida.mp3", audio_bitrate="320k")
```

Valores recomendados: `128k` (leve), `192k` (boa qualidade), `320k` (máxima).

-----

### 📌 Notas

  - Funciona em Windows, Linux e MacOS (desde que o FFmpeg esteja instalado).
  - Para lotes de arquivos, basta adaptar o script para percorrer todos os vídeos da pasta.
  - Alternativamente, pode-se usar `moviepy`:

<!-- end list -->

```python
from moviepy.editor import VideoFileClip

video = VideoFileClip("video.mp4")
video.audio.write_audiofile("saida.mp3", bitrate="320k")
```
