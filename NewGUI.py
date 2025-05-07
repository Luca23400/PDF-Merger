import tkinter as tk
from tkinter import filedialog, ttk
from PyPDF2 import PdfMerger
import os

def open_file(entry_widget):
    file_path = filedialog.askopenfilename(filetypes=[("PDF Dateien", "*.pdf")])
    if file_path:
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, file_path)

def create_pdf():
    pdf1 = entry_pdf1.get()
    pdf2 = entry_pdf2.get()
    outPutPath = "C:\\Users\\lucab\\OneDrive\\Desktop\\mergedPDF.pdf"
    pdfList = [f"{pdf1}", f"{pdf2}"]
    merge_pdfs(pdfList, outPutPath)
    print(f"Neues PDF wird erstellt aus: {pdf1} und {pdf2}")

def merge_pdfs(pdf_list, output_file):
    merger = PdfMerger()
    try:
        for pdf in pdf_list:
            merger.append(pdf)
        merger.write(output_file)
        print(f"PDFs wurden erfolgreich zu '{output_file}' zusammengeführt.")
    except Exception as e:
        print(f"Fehler beim Zusammenfügen der PDFs: {e}")
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