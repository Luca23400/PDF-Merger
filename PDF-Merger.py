import tkinter as tk
from tkinter import filedialog
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
    #outPutPath = os.path.join(os.path.expanduser("~"), "Desktop", "MergedPDF.pdf")
    outPutPath = ""
    pdfList = [f"{pdf1}", f"{pdf2}"]
    merge_pdfs(pdfList,outPutPath)
    print(f"Neues PDF wird erstellt aus: {pdf1} und {pdf2}")
    
def merge_pdfs(pdf_list, output_file):
    """
    Merges multiple PDFs into a single PDF file.

    Args:
        pdf_list (list): List of PDF file paths to merge.
        output_file (str): Path of the output merged PDF.
    """
    merger = PdfMerger()

    try:
        for pdf in pdf_list:
            merger.append(pdf)

        # Write the merged PDF to the output file
        merger.write(output_file)
        print(f"PDFs wurden erfolgreich zu '{output_file}' zusammengeführt.")
    except Exception as e:
        print(f"Fehler beim Zusammenfügen der PDFs: {e}")
    finally:
        merger.close()
 
# Hauptfenster erstellen
root = tk.Tk()
root.title("PDF Merger")
root.geometry("450x200")
 
# Label und Eingabefelder
label1 = tk.Label(root, text="existing PDF:")
label1.grid(row=0, column=0, padx=10, pady=5, sticky="w")
 
entry_pdf1 = tk.Entry(root, width=40)
entry_pdf1.grid(row=0, column=1, padx=10, pady=5)
 
button_pdf1 = tk.Button(root, text="...", command=lambda: open_file(entry_pdf1))
button_pdf1.grid(row=0, column=2, padx=5, pady=5)
 
label2 = tk.Label(root, text="add:")
label2.grid(row=1, column=0, padx=10, pady=5, sticky="w")
 
entry_pdf2 = tk.Entry(root, width=40)
entry_pdf2.grid(row=1, column=1, padx=10, pady=5)
 
button_pdf2 = tk.Button(root, text="...", command=lambda: open_file(entry_pdf2))
button_pdf2.grid(row=1, column=2, padx=5, pady=5)
 
# Button zum Erstellen eines neuen PDFs
create_button = tk.Button(root, text="merge", command=create_pdf)
create_button.grid(row=2, column=1, pady=20)
 
# GUI starten
root.mainloop()