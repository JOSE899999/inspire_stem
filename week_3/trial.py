import tkinter as tk
from tkinter import messagebox
from pytube import YouTube
import os

def download_video():
    try:
        yt = YouTube(url_entry.get())
        stream = yt.streams.get_highest_resolution()
        download_path = os.path.expanduser("~") + "/Downloads/"
        stream.download(download_path)
        messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("YouTube Video Downloader")

# URL Entry
url_label = tk.Label(root, text="Enter YouTube URL:")
url_label.pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

# Download Button
download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack()

# Run the Tkinter event loop
root.mainloop()
