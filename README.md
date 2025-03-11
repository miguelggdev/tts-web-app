# 🗣️ Text-to-Speech Web App 🎵  

Este proyecto es una aplicación web construida con **Flask** que permite convertir texto en audio utilizando el modelo **Kokoro-82M**.  

La aplicación proporciona una interfaz web amigable donde los usuarios pueden ingresar texto, generar el audio y descargarlo en formato `.wav`.  

---

## 🚀 **Características**  
✅ Conversión de texto a voz en varios idiomas.  
✅ Interfaz moderna y responsiva con Bootstrap.  
✅ Archivos de audio almacenados en `static/audio/` sin sobrescribirse.  
✅ Botón de descarga que permite bajar el archivo generado.  
✅ Fondos con animación de colores para un diseño atractivo.  

---

## 🛠️ **Requisitos Previos**  

Antes de comenzar, asegúrate de tener instalado lo siguiente en **Linux Fedora 40** (o cualquier sistema basado en Linux):  

### 📌 **1. Instalar Python 3 y pip**  
```bash
sudo dnf install python3 python3-pip -y
```

### 📌 **2. Instalar dependencias del sistema**
Algunas bibliotecas como espeak-ng son necesarias para Kokoro. Instálalas con:
```bash
sudo dnf install espeak-ng -y
```
### 📌 ** Instalar Git **
```bash
sudo dnf install git -y

```
📥 Clonar el Repositorio

Ejecuta el siguiente comando en la terminal:
```bash
git clone https://github.com/miguelggdev/tts-web-app.git
cd tts-web-app
```

### 📌 ** Instalar dependencias del proyecto**
```bash
pip install -r requirements.txt
```

### 🚀 ** Ejecutar la Aplicación ** 
Después de instalar todo, inicia la aplicación con:

```bash
flask run
```
Por defecto, Flask ejecutará la aplicación en:
🔗 http://127.0.0.1:5000/

Si deseas ejecutarla en modo depuración, usa:
```bash
FLASK_ENV=development flask run
```
### 🎤 **  Uso de la Aplicación** 

1️⃣ Abre el navegador y accede a http://127.0.0.1:5000/.
2️⃣ Ingresa un texto en el campo de entrada.
3️⃣ Haz clic en "Generar Audio".
4️⃣ Descarga el archivo generado con el botón "Descargar Audio".


###  📂 ** Estructura del Proyecto** 
tts-web-app/
│── static/               # Archivos estáticos (CSS, JS, audios)
│   ├── audio/            # Aquí se guardan los archivos generados
│   ├── css/              # Hojas de estilo CSS
│── templates/            # Archivos HTML (Frontend)
│   ├── index.html        # Página principal
│   ├── result.html       # Página de descarga
│── venv/                 # Entorno virtual (se crea después de activar venv)
│── app.py                # Código principal de la aplicación Flask
│── requirements.txt      # Lista de dependencias de Python
│── README.md             # Este archivo 😃



