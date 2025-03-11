from flask import Flask, request, render_template, send_file, redirect, url_for
from kokoro import KPipeline
import soundfile as sf
import os
import uuid

app = Flask(__name__)

# Inicializa el modelo de texto a voz
pipeline = KPipeline(lang_code='a')  # Inglés Americano

# Directorio para almacenar audios
AUDIO_DIR = "static/audio"
os.makedirs(AUDIO_DIR, exist_ok=True)  # Crea la carpeta si no existe

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/synthesize', methods=['POST'])
def synthesize():
    text = request.form['text']
    if not text:
        return "Error: Debes ingresar un texto", 400

    # Generar un nombre de archivo único
    filename = f"audio_{uuid.uuid4().hex}.wav"
    audio_path = os.path.join(AUDIO_DIR, filename)

    # Generar el audio con Kokoro
    generator = pipeline(text, voice='af_heart', speed=1, split_pattern=r'\n+')
    for i, (gs, ps, audio) in enumerate(generator):
        sf.write(audio_path, audio, 24000)  # Guarda el archivo de audio
        break  # Solo tomamos el primer resultado

    return render_template('download.html', audio_file=filename)

@app.route('/download/<filename>')
def download(filename):
    audio_path = os.path.join(AUDIO_DIR, filename)
    return send_file(audio_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
