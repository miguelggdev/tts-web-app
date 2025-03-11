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

### 📌 **2. Instalar dependencias del sistema**
Algunas bibliotecas como espeak-ng son necesarias para Kokoro. Instálalas con:
```bash
sudo dnf install espeak-ng -y

