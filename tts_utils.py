import pyttsx3
import threading

class TextToSpeech:
    def __init__(self, rate=200):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', rate)
        self.rate = rate
        self.is_paused = False
        self.is_reading = False
        self.text = ""
        self.thread = None

    def set_rate(self, rate):
        """Update the speech rate dynamically."""
        self.rate = rate
        self.engine.setProperty('rate', self.rate)

    def read_text(self, text):
        """Read text aloud with pause/resume functionality."""
        self.text = text
        self.is_paused = False
        self.is_reading = True
        self.thread = threading.Thread(target=self._read_thread)
        self.thread.start()

    def _read_thread(self):
        """Internal method to handle reading in a separate thread."""
        for line in self.text.splitlines():
            while self.is_paused:
                continue  # Wait while paused
            if not self.is_reading:
                break  # Stop if interrupted
            self.engine.say(line)
            self.engine.runAndWait()

    def pause(self):
        """Pause reading."""
        if self.is_reading:
            self.is_paused = True

    def resume(self):
        """Resume reading."""
        if self.is_reading and self.is_paused:
            self.is_paused = False

    def stop(self):
        """Stop reading entirely."""
        self.is_reading = False
        self.engine.stop()
