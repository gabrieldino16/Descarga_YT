import tkinter as tk
from tkinter import filedialog, messagebox
from pytubefix import YouTube
from moviepy.editor import AudioFileClip
import threading
import os
from tkinter import ttk
import re

def descargar_video():
    url = url_entry.get()
    tipo = tipo_var.get()
    carpeta_destino = carpeta_var.get()

    if not url or not carpeta_destino:
        messagebox.showwarning("Faltan datos", "Por favor completa la URL y selecciona la carpeta de destino.")
        return

    def descargar():
        try:
            boton_descargar.config(state="disabled", text="Descargando...")
            yt = YouTube(url, on_progress_callback=update_progress)

            if tipo == "Audio":
                stream = yt.streams.get_audio_only()
            else:
                stream = yt.streams.get_highest_resolution()

            if stream is None:
                messagebox.showerror("Error", "No se encontró un stream adecuado.")
                return

            # Limpiar nombre de archivo
            titulo = re.sub(r'[\\/*?:"<>|]', "", yt.title).replace(" ", "_")
            archivo_temp = os.path.join(carpeta_destino, f"{titulo}.mp4")
            archivo_final = os.path.join(carpeta_destino, f"{titulo}.mp3" if tipo == "Audio" else f"{titulo}.mp4")

            # Preparar la barra de progreso
            progress_bar['value'] = 0
            progress_bar['maximum'] = stream.filesize

            # Descargar el archivo
            stream.download(output_path=carpeta_destino, filename=f"{titulo}.mp4")

            # Convertir si es audio
            if tipo == "Audio":
                audioclip = AudioFileClip(archivo_temp)
                audioclip.write_audiofile(archivo_final)
                audioclip.close()
                os.remove(archivo_temp)

            messagebox.showinfo("Éxito", f"{tipo} descargado correctamente:\n{archivo_final}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo descargar el video:\n{e}")
        finally:
            boton_descargar.config(state="normal", text="Descargar")

    threading.Thread(target=descargar).start()

def update_progress(stream, chunk, bytes_remaining):
    downloaded = stream.filesize - bytes_remaining
    progress_bar['value'] = downloaded
    ventana.update_idletasks()

def seleccionar_carpeta():
    carpeta = filedialog.askdirectory()
    if carpeta:
        carpeta_var.set(carpeta)
        label_carpeta.config(text=carpeta)

# Interfaz
ventana = tk.Tk()
ventana.title("Descargador de YouTube DinoPRO")
ventana.geometry("600x400")
ventana.configure(bg="#EAEAEA")

# Estilos
fuente_titulo = ("Segoe UI", 16, "bold")
fuente_normal = ("Segoe UI", 12)
fuente_boton = ("Segoe UI", 12, "bold")
color_boton = "#007BFF"
color_boton_hover = "#45a049"

# Título
tk.Label(ventana, text="Descargador de YouTube DinoPRO", font=fuente_titulo, bg="#EAEAEA", fg="#2a2a2a").pack(pady=10)

# Frame URL
frame_url = tk.Frame(ventana, bg="#EAEAEA")
frame_url.pack(pady=5)
tk.Label(frame_url, text="URL del video:", font=fuente_normal, bg="#EAEAEA").pack(side="left", padx=5)
url_entry = tk.Entry(frame_url, width=40, font=fuente_normal, bd=2, relief="solid")
url_entry.pack(side="left")

# Frame tipo
frame_tipo = tk.Frame(ventana, bg="#EAEAEA")
frame_tipo.pack(pady=10)
tk.Label(frame_tipo, text="Tipo de descarga:", font=fuente_normal, bg="#EAEAEA").pack(side="left", padx=5)
tipo_var = tk.StringVar(value="Video")
tk.Radiobutton(frame_tipo, text="Video", variable=tipo_var, value="Video", bg="#EAEAEA", font=fuente_normal).pack(side="left")
tk.Radiobutton(frame_tipo, text="Audio", variable=tipo_var, value="Audio", bg="#EAEAEA", font=fuente_normal).pack(side="left")

# Selección de carpeta
carpeta_var = tk.StringVar()
tk.Button(ventana, text="Seleccionar carpeta de destino", font=fuente_normal, command=seleccionar_carpeta, relief="raised", bd=3, bg=color_boton, fg="white").pack(pady=10)
label_carpeta = tk.Label(ventana, text="No se ha seleccionado carpeta", font=fuente_normal, bg="#EAEAEA", fg="#555")
label_carpeta.pack(pady=5)

# Barra de progreso
progress_bar = ttk.Progressbar(ventana, orient="horizontal", length=400, mode="determinate")
progress_bar.pack(pady=10)

# Botón de descarga
boton_descargar = tk.Button(ventana, text="Descargar", font=fuente_boton, command=descargar_video, relief="raised", bd=3, bg=color_boton, fg="white")
boton_descargar.pack(pady=20)

# Efecto hover
def on_enter(e): boton_descargar.config(bg=color_boton_hover)
def on_leave(e): boton_descargar.config(bg=color_boton)
boton_descargar.bind("<Enter>", on_enter)
boton_descargar.bind("<Leave>", on_leave)

ventana.mainloop()
