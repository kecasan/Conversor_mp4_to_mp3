"""
Video to MP3 Converter
======================

Converte vídeos (.mp4, .mkv, etc.) em arquivos de áudio .mp3 usando Python + FFmpeg.

Requisitos:
- Python 3.8+
- FFmpeg instalado e disponível no PATH ou na mesma pasta do script
- Biblioteca Python: ffmpeg-python (pip install ffmpeg-python)

Uso:
1. Coloque os vídeos na mesma pasta do main.py
2. Execute: python main.py
3. Os arquivos .mp3 serão gerados na mesma pasta
"""

import os
import ffmpeg

def video_to_mp3(input_file):
    """Converte um vídeo em MP3 com qualidade 320kbps"""
    base, _ = os.path.splitext(input_file)
    output_file = base + ".mp3"

    try:
        (
            ffmpeg
            .input(input_file)
            .output(output_file, audio_bitrate="320k")  # Qualidade máxima MP3
            .run()
        )
        print(f"✅ Áudio extraído com sucesso: {output_file}")
    except FileNotFoundError:
        print("❌ Erro: FFmpeg não encontrado. Confira se está instalado e no PATH.")
    except Exception as e:
        print("❌ Erro durante a conversão:", e)

def main():
    # Lista todos os arquivos de vídeo na pasta
    video_extensions = [".mp4", ".mkv", ".mov", ".avi", ".webm"]
    videos = [f for f in os.listdir() if os.path.splitext(f)[1].lower() in video_extensions]

    if not videos:
        print("⚠️ Nenhum vídeo encontrado na pasta.")
        return

    print(f"🎬 Encontrados {len(videos)} vídeo(s). Iniciando conversão...")
    for video in videos:
        print(f"Converting: {video}")
        video_to_mp3(video)

    print("✅ Conversão finalizada!")

if __name__ == "__main__":
    main()
