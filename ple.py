import sys
import requests
import tkinter as tk
from tkinter import messagebox

class LibraryExplorer:
    def __init__(self, root):
        self.root = root
        self.root.title("PyLibrary Explorer")
        self.root.geometry("500x400")

        self.search_label = tk.Label(root, text="Search for a Python library by name:")
        self.search_label.pack(pady=10)

        self.search_input = tk.Entry(root, width=40)
        self.search_input.pack(pady=10)

        self.search_button = tk.Button(root, text="Search", command=self.search_library)
        self.search_button.pack(pady=5)

        self.result_list = tk.Listbox(root, width=60, height=10)
        self.result_list.pack(pady=10)

        self.version_button = tk.Button(root, text="Get Available Versions", command=self.get_versions)
        self.version_button.pack(pady=5)

    def search_library(self):
        library_name = self.search_input.get().strip()
        if not library_name:
            messagebox.showwarning("Input Error", "Please enter a library name to search.")
            return

        response = requests.get(f"https://pypi.org/pypi/{library_name}/json")
        if response.status_code == 200:
            data = response.json()
            latest_version = data.get("info", {}).get("version", "Unknown")
            self.result_list.delete(0, tk.END)
            self.result_list.insert(tk.END, f"Library '{library_name}' is available on PyPI.")
            self.result_list.insert(tk.END, f"Latest version: {latest_version}")
        else:
            self.result_list.delete(0, tk.END)
            self.result_list.insert(tk.END, f"Library '{library_name}' was not found on PyPI.")

    def get_versions(self):
        library_name = self.search_input.get().strip()
        if not library_name:
            messagebox.showwarning("Input Error", "Please enter a library name to check versions.")
            return

        response = requests.get(f"https://pypi.org/pypi/{library_name}/json")
        if response.status_code == 200:
            data = response.json()
            releases = data.get("releases", {})
            versions = sorted(releases.keys(), reverse=True)

            if versions:
                self.result_list.delete(0, tk.END)
                self.result_list.insert(tk.END, f"Available versions for '{library_name}':")
                for version in versions:
                    self.result_list.insert(tk.END, version)
            else:
                self.result_list.delete(0, tk.END)
                self.result_list.insert(tk.END, f"No versions found for '{library_name}'.")
        else:
            self.result_list.delete(0, tk.END)
            self.result_list.insert(tk.END, f"Library '{library_name}' was not found on PyPI.")

if __name__ == "__main__":
    root = tk.Tk()
    explorer = LibraryExplorer(root)
    root.mainloop()
