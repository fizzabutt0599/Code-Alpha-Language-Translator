import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES
import pyttsx3

# Initialize translator and TTS engine
translator = Translator()
engine = pyttsx3.init()

# Translate function
def translate_text():
    try:
        src_lang = source_lang_combo.get()
        dest_lang = target_lang_combo.get()
        text = input_text.get("1.0", tk.END).strip()

        if not text:
            messagebox.showwarning("Input Error", "Please enter text to translate!")
            return

        # Get language codes
        src_code = [code for code, lang in LANGUAGES.items() if lang == src_lang][0]
        dest_code = [code for code, lang in LANGUAGES.items() if lang == dest_lang][0]

        translated = translator.translate(text, src=src_code, dest=dest_code)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated.text)

    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

# Copy to clipboard
def copy_text():
    translated_text = output_text.get("1.0", tk.END).strip()
    if translated_text:
        root.clipboard_clear()
        root.clipboard_append(translated_text)
        messagebox.showinfo("Copied", "Translated text copied to clipboard!")

from gtts import gTTS
import os
from playsound import playsound

# Speak translated text
from gtts import gTTS
import os
from playsound import playsound

# Speak translated text
from gtts import gTTS
import os
from playsound import playsound

def speak_text():
    text = output_text.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("No Text", "Please translate some text first!")
        return

    try:
        # Get the target language code
        dest_lang = target_lang_combo.get()
        dest_code = [code for code, lang in LANGUAGES.items() if lang == dest_lang][0]

        # Generate speech
        tts = gTTS(text=text, lang=dest_code)
        filename = "temp_audio.mp3"
        tts.save(filename)
        playsound(filename)
        os.remove(filename)
    except Exception as e:
        messagebox.showerror("Error", f"Speech failed: {str(e)}")



# GUI window
root = tk.Tk()
root.title("Language Translation Tool")
root.geometry("650x450")
root.config(bg="lightblue")

# Language options
languages = list(LANGUAGES.values())

# Input text
tk.Label(root, text="Enter Text:", bg="lightblue", font=("Arial", 12,"bold")).pack(pady=5)
input_text = tk.Text(root, height=5, width=70)
input_text.pack(pady=5)

# Source and target language dropdowns
frame = tk.Frame(root, bg="lightblue")
frame.pack(pady=5)

tk.Label(frame, text="From:", bg="lightblue").grid(row=0, column=0, padx=5)
source_lang_combo = ttk.Combobox(frame, values=languages, width=20)
source_lang_combo.set("english")
source_lang_combo.grid(row=0, column=1)

tk.Label(frame, text="To:", bg="lightblue").grid(row=0, column=2, padx=5)
target_lang_combo = ttk.Combobox(frame, values=languages, width=20)
target_lang_combo.set("urdu")
target_lang_combo.grid(row=0, column=3)

# Buttons
btn_frame = tk.Frame(root, bg="lightblue")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Translate", command=translate_text, bg="green", fg="white", font=("Arial", 12, )).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Copy", command=copy_text, bg="blue", fg="white", font=("Arial", 12)).grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="Speak", command=speak_text, bg="orange", fg="white", font=("Arial", 12)).grid(row=0, column=2, padx=10)

# Output text
tk.Label(root, text="Translated Text:", bg="lightblue", font=("Arial", 12,"bold")).pack(pady=5)
output_text = tk.Text(root, height=5, width=70)
output_text.pack(pady=5)

# Run GUI
root.mainloop()
