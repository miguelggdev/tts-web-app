from flask import Flask, request, render_template, send_file
from kokoro import KPipeline
import soundfile as sf
import os

app = Flask(__name__)

pipeline = KPipeline(lang_code='a')  # Inglés Americano
audio_file = "output.wav"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/synthesize', methods=['POST'])
def synthesize():
    text = request.form['text']
    if not text:
        return "Error: Debes ingresar un texto", 400
    
    generator = pipeline(text, voice='af_heart', speed=1, split_pattern=r'\n+')
    for i, (gs, ps, audio) in enumerate(generator):
        sf.write(audio_file, audio, 24000)  # Guarda el archivo de audio
        break  # Solo tomamos el primer resultado
    
    return render_template('download.html', audio_file=audio_file)

@app.route('/download')
def download():
    return send_file(audio_file, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
