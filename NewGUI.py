import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from PyPDF2 import PdfMerger
import os

def get_desktop_path():
    """Returns the path to the user's desktop using Windows environment variables"""
    try:
        # Versuche zuerst den OneDrive Desktop
        onedrive_desktop = os.path.join(os.environ['USERPROFILE'], 'OneDrive', 'Desktop')
        if os.path.exists(onedrive_desktop):
            return onedrive_desktop
        
        # Fallback auf normalen Desktop
        normal_desktop = os.path.join(os.environ['USERPROFILE'], 'Desktop')
        if os.path.exists(normal_desktop):
            return normal_desktop
            
        raise Exception("Desktop-Ordner konnte nicht gefunden werden")
    except Exception as e:
        messagebox.showerror("Fehler", f"Fehler beim Ermitteln des Desktop-Pfads: {str(e)}")
        return None

def open_file(entry_widget):
    try:
        file_path = filedialog.askopenfilename(filetypes=[("PDF Dateien", "*.pdf")])
        if file_path:
            entry_widget.delete(0, tk.END)
            entry_widget.insert(0, file_path)
    except Exception as e:
        messagebox.showerror("Fehler", f"Fehler beim Öffnen der Datei: {str(e)}")

def create_pdf():
    try:
        pdf1 = entry_pdf1.get()
        pdf2 = entry_pdf2.get()
        
        if not pdf1 or not pdf2:
            messagebox.showerror("Fehler", "Bitte wählen Sie beide PDF-Dateien aus.")
            return
            
        desktop_path = get_desktop_path()
        if not desktop_path:
            return
            
        outPutPath = os.path.join(desktop_path, "MergedPDF.pdf")
        pdfList = [pdf1, pdf2]
        merge_pdfs(pdfList, outPutPath)
        messagebox.showinfo("Erfolg", f"PDFs wurden erfolgreich zusammengeführt!\nGespeichert unter: {outPutPath}")
    except Exception as e:
        messagebox.showerror("Fehler", f"Fehler beim Zusammenführen der PDFs: {str(e)}")

def merge_pdfs(pdf_list, output_file):
    merger = PdfMerger()
    try:
        for pdf in pdf_list:
            if not os.path.exists(pdf):
                raise FileNotFoundError(f"Die Datei {pdf} wurde nicht gefunden.")
            merger.append(pdf)

        merger.write(output_file)
        print(f"PDFs wurden erfolgreich zu '{output_file}' zusammengeführt.")
    except FileNotFoundError as e:
        messagebox.showerror("Fehler", str(e))
    except Exception as e:
        messagebox.showerror("Fehler", f"Fehler beim Zusammenführen der PDFs: {str(e)}")
    finally:
        merger.close()

# Hauptfenster erstellen
root = tk.Tk()
root.title("PDF Merger")
root.geometry("900x380")
root.configure(bg="#f0f0f0")

# Style konfigurieren
style = ttk.Style()
style.theme_use('clam')
style.configure('TButton', padding=6, relief="flat", background="#2196F3", foreground="white")
style.configure('Browse.TButton', padding=6, relief="flat", background="#2196F3", foreground="white", width=18)
style.configure('TLabel', background="#f0f0f0", font=('Segoe UI', 11))
style.configure('TEntry', padding=5, font=('Segoe UI', 10))

# Frame für bessere Organisation
main_frame = ttk.Frame(root, padding="40")
main_frame.pack(fill=tk.BOTH, expand=True)

# Label und Eingabefelder
label1 = ttk.Label(main_frame, text="Bestehende PDF-Datei:")
label1.grid(row=0, column=0, padx=25, pady=15, sticky="w")

entry_pdf1 = ttk.Entry(main_frame, width=55)
entry_pdf1.grid(row=0, column=1, padx=25, pady=15)

button_pdf1 = ttk.Button(main_frame, text="Durchsuchen", command=lambda: open_file(entry_pdf1), style='Browse.TButton')
button_pdf1.grid(row=0, column=2, padx=25, pady=15)

label2 = ttk.Label(main_frame, text="PDF hinzufügen:")
label2.grid(row=1, column=0, padx=25, pady=15, sticky="w")

entry_pdf2 = ttk.Entry(main_frame, width=55)
entry_pdf2.grid(row=1, column=1, padx=25, pady=15)

button_pdf2 = ttk.Button(main_frame, text="Durchsuchen", command=lambda: open_file(entry_pdf2), style='Browse.TButton')
button_pdf2.grid(row=1, column=2, padx=25, pady=15)

# Button zum Erstellen eines neuen PDFs
create_button = ttk.Button(main_frame, text="PDFs zusammenführen", command=create_pdf, style='TButton')
create_button.grid(row=2, column=0, columnspan=3, pady=25)

# GUI starten
root.mainloop()