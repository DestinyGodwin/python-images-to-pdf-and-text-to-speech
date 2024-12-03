from tkinter import Label, Button, Scale, HORIZONTAL, filedialog, messagebox
from pdf_utils import extract_text_from_pdf
from tts_utils import init_tts, speak_text

class PDFReaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Reader with Adjustable Speech Rate")
        self.tts_engine = init_tts()
        self.speech_rate = 200

        self.label = Label(root, text="Select a PDF file to read", font=("Arial", 14))
        self.label.pack(pady=10)

        self.rate_label = Label(root, text="Adjust Speech Rate:", font=("Arial", 12))
        self.rate_label.pack()

        self.rate_slider = Scale(root, from_=100, to=300, orient=HORIZONTAL, length=300, command=self.update_rate)
        self.rate_slider.set(self.speech_rate)
        self.rate_slider.pack()

        self.select_button = Button(root, text="Select PDF", command=self.select_file, font=("Arial", 12), bg="blue", fg="white")
        self.select_button.pack(pady=10)

        self.exit_button = Button(root, text="Exit", command=root.quit, font=("Arial", 12), bg="red", fg="white")
        self.exit_button.pack(pady=10)

    def update_rate(self, value):
        """Update the speech rate based on the slider."""
        self.speech_rate = int(value)
        self.tts_engine.setProperty('rate', self.speech_rate)

    def select_file(self):
        file_path = filedialog.askopenfilename(
            title="Select a PDF file",
            filetypes=[("PDF Files", "*.pdf")],
        )
        if file_path:
            try:
                text = extract_text_from_pdf(file_path)
                speak_text(self.tts_engine, text)
                messagebox.showinfo("Success", "PDF reading completed successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            messagebox.showinfo("No File Selected", "Please select a PDF file to proceed.")
