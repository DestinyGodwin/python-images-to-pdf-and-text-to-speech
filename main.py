from tkinter import Tk, Label, Button, filedialog, messagebox
from pdf_utils import extract_text_from_pdf, convert_images_to_pdf
from tts_utils import TextToSpeech

class PDFReaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dynamic PDF Reader and Image to PDF Converter")
        self.tts = TextToSpeech()

        # GUI Components
        self.label = Label(root, text="Select a PDF file to read or convert images to PDF", font=("Arial", 14))
        self.label.pack(pady=10)

        # Buttons
        self.select_pdf_button = Button(
            root, text="Select PDF", command=self.select_pdf_file, font=("Arial", 12), bg="blue", fg="white"
        )
        self.select_pdf_button.pack(pady=10)

        self.convert_images_button = Button(
            root, text="Convert Images to PDF", command=self.convert_images_to_pdf, font=("Arial", 12), bg="purple", fg="white"
        )
        self.convert_images_button.pack(pady=10)

        self.play_button = Button(
            root, text="Play", command=self.resume_reading, font=("Arial", 16, "bold"), bg="green", fg="white", state="disabled"
        )
        self.play_button.pack(pady=10)

        self.pause_button = Button(
            root, text="Pause", command=self.pause_reading, font=("Arial", 16, "bold"), bg="orange", fg="white", state="disabled"
        )
        self.pause_button.pack(pady=10)

        self.exit_button = Button(
            root, text="Exit", command=root.quit, font=("Arial", 12), bg="red", fg="white"
        )
        self.exit_button.pack(pady=10)

    def select_pdf_file(self):
        """Open file dialog and select a PDF file."""
        file_path = filedialog.askopenfilename(
            title="Select a PDF file",
            filetypes=[("PDF Files", "*.pdf")],
        )
        if file_path:
            self.start_reading(file_path)
        else:
            messagebox.showinfo("No File Selected", "Please select a PDF file to proceed.")

    def convert_images_to_pdf(self):
        """Convert selected images to a PDF file."""
        image_paths = filedialog.askopenfilenames(
            title="Select Images", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
        )
        if image_paths:
            output_pdf_path = filedialog.asksaveasfilename(
                title="Save PDF", defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")]
            )
            if output_pdf_path:
                try:
                    convert_images_to_pdf(image_paths, output_pdf_path)
                    messagebox.showinfo("Success", "Images have been successfully converted to PDF!")
                except Exception as e:
                    messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            messagebox.showinfo("No Images Selected", "Please select images to convert.")

    def start_reading(self, file_path):
        """Start reading the PDF file."""
        try:
            text = extract_text_from_pdf(file_path)
            self.tts.read_text(text)
            self.play_button.config(state="normal")
            self.pause_button.config(state="normal")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def pause_reading(self):
        """Pause reading."""
        self.tts.pause()
        print("Reading paused.")

    def resume_reading(self):
        """Resume reading."""
        self.tts.resume()
        print("Reading resumed.")

# Main program
if __name__ == "__main__":
    root = Tk()
    app = PDFReaderApp(root)
    root.mainloop()
