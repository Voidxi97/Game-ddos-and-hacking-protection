import tkinter as tk
import webbrowser
import os
import subprocess

def test_game_protection():
    # Check if OpenVPN and Malwarebytes are installed
    openvpn_installed = os.path.exists("C:\\Program Files\\OpenVPN\\bin\\openvpn.exe")
    malwarebytes_installed = os.path.exists("C:\\Program Files\\Malwarebytes\\Anti-Malware\\mbam.exe")

    # Determine the security status based on application installations
    if openvpn_installed and malwarebytes_installed:
        status = "Secure"
    elif openvpn_installed or malwarebytes_installed:
        status = "Poor Security"
    else:
        status = "Not Secure"

    # Display the security status
    print("Game Protection Status:", status)

def run_security_test():
    # Command to run the security test
    command = "your_security_test_command_here"

    # Execute the command in the terminal
    subprocess.Popen(command, shell=True)

def open_application_or_website(path_to_exe, website_url):
    if os.path.exists(path_to_exe):
        os.startfile(path_to_exe)
    else:
        webbrowser.open(website_url)

def open_openvpn():
    open_application_or_website(
        "C:\\Program Files\\OpenVPN\\bin\\openvpn.exe",
        "https://openvpn.net/"
    )

def open_malwarebytes():
    open_application_or_website(
        "C:\\Program Files\\Malwarebytes\\Anti-Malware\\mbam.exe",
        "https://www.malwarebytes.com/"
    )

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Game Protection Tester")

    # Add a label
    label = tk.Label(root, text="Click the button to test game protection or open applications (if installed):")
    label.pack(pady=10)

    # Add a button to trigger the test
    test_button = tk.Button(root, text="Test Game Protection", command=test_game_protection)
    test_button.pack(pady=5)

    # Add a button to run security test
    security_test_button = tk.Button(root, text="Run Security Test", command=run_security_test)
    security_test_button.pack(pady=5)

    # Add a button to open OpenVPN application or website
    openvpn_button = tk.Button(root, text="Open OpenVPN", command=open_openvpn)
    openvpn_button.pack(pady=5)

    # Add a button to open Malwarebytes application or website
    malwarebytes_button = tk.Button(root, text="Open Malwarebytes", command=open_malwarebytes)
    malwarebytes_button.pack(pady=5)

    # Add a quit button
    quit_button = tk.Button(root, text="Quit", command=root.destroy)
    quit_button.pack(pady=5)

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    main()
