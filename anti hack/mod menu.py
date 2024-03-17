import tkinter as tk
import webbrowser
import urllib.request

class ModDownloaderApp:
    def __init__(self, master):
        self.master = master
        master.title("Mod Downloader")

        self.label = tk.Label(master, text="Click the button to download mod files:")
        self.label.pack()

        self.mod1_button = tk.Button(master, text="Download Mod 1", command=self.download_mod1)
        self.mod1_button.pack()

    def download_mod1(self):
        mod_urls = ["https://liquidmenu.pro/", "https://mistermodzz.com/"]
        for url in mod_urls:
            webbrowser.open(url)

root = tk.Tk()
app = ModDownloaderApp(root)
root.mainloop()
