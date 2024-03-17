import tkinter as tk
import subprocess

class KaliLinuxTerminal(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Kali Linux Terminal")

        self.terminal_output = tk.Text(self, height=20, width=80)
        self.terminal_output.pack(fill=tk.BOTH, expand=True)

        self.command_entry = tk.Entry(self, width=80)
        self.command_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.run_button = tk.Button(self, text="Run", command=self.execute_command)
        self.run_button.pack(side=tk.RIGHT)

    def execute_command(self):
        command = self.command_entry.get()
        output = subprocess.getoutput(command)
        self.terminal_output.insert(tk.END, f"$ {command}\n{output}\n\n")
        self.command_entry.delete(0, tk.END)

def main():
    app = KaliLinuxTerminal()
    app.mainloop()

if __name__ == "__main__":
    main()
