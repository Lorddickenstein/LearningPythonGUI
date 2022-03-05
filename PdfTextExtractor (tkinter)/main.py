import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

# Create the user interface
root = tk.Tk()
root.title('PDF Text Extractor')
root.iconbitmap('images/logo.ico')

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

# LOGO
logo = Image.open('images/logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# INSTRUCTIONS
instructions_txt = 'Select a pdf file to extract all of the text'
instructions = tk.Label(root, text=instructions_txt, font='Raleway')
instructions.grid(columnspan=3, column=0, row=1)

# Open pdf file on button click
def open_file():
    browse_txt.set('Loading...')
    file = askopenfile(parent=root, mode='rb', title='Choose a file', filetypes=[('Pdf file', '*.pdf')])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()
        
        # TEXT BOX
        text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_configure('center', justify='center')
        text_box.tag_add('center', 1.0, 'end')
        text_box.grid(column=1, row=3)

    browse_txt.set('Browse')


# BROWSE BUTTON
browse_txt = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_txt, font='Raleway', bg='#20bebe', fg='white', heigh=2, width=15,
                       command=lambda: open_file())
browse_txt.set('Browse')
browse_btn.grid(column=1, row=2)

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

root.mainloop()