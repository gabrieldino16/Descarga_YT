# 🎬 Descargador de YouTube DinoPRO

Una aplicación con interfaz gráfica para descargar videos o audios desde YouTube en alta calidad, usando `pytubefix` y `moviepy`. Permite elegir la carpeta de destino, seleccionar si querés bajar el **video completo** o solo el **audio en MP3**, y ver el progreso de la descarga.

---

## 🖥️ Captura de pantalla
<img src="https://github.com/tuusuario/tu-repo/raw/main/screenshot.png" width="600">

---

## 🚀 Características

- Interfaz simple y clara hecha con `Tkinter`.
- Descarga de video en `.mp4` o audio en `.mp3`.
- Barra de progreso durante la descarga.
- Selección de carpeta de destino.
- Manejo de errores y feedback visual.
- Multihilo para evitar que se congele la interfaz.

---

## 🔧 Requisitos

- Python 3.10 o superior (⚠️ no se recomienda Python 3.13 aún)
- pip

### Instalación de dependencias

```bash
pip install pytubefix moviepy
