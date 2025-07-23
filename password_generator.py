import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json
import random
import string
import os
from datetime import datetime
import webbrowser

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("✨ Password Vault ✨")
        self.root.geometry("800x600")
        self.root.configure(bg="#1a1a2e")
        
        # Gen Z colors
        self.colors = {
            "bg": "#1a1a2e",
            "secondary_bg": "#16213e",
            "accent": "#0f3460",
            "text": "#e94560",
            "white": "#ffffff",
            "purple": "#8b5cf6",
            "pink": "#ec4899",
            "cyan": "#06b6d4"
        }
        
        # Data storage - Use user's documents folder instead of OneDrive
        import os
        documents_path = os.path.expanduser("~/Documents")
        self.data_file = os.path.join(documents_path, "password_vault.json")
        self.passwords_data = self.load_data()
        
        self.setup_ui()
        
    def load_data(self):
        """Load existing password data from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except:
                return {"websites": []}
        return {"websites": []}
    
    def save_data(self):
        """Save password data to JSON file"""
        try:
            # Ensure the directory exists
            os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
            with open(self.data_file, 'w') as f:
                json.dump(self.passwords_data, f, indent=2)
        except Exception as e:
            messagebox.showerror("Error", f"Could not save data: {str(e)}\n\nTry running the app as administrator or check OneDrive settings.")
    
    def setup_ui(self):
        """Setup the main UI with Gen Z styling"""
        # Main container
        main_frame = tk.Frame(self.root, bg=self.colors["bg"])
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Title
        title_label = tk.Label(
            main_frame,
            text="🔐 Password Vault 🔐",
            font=("Arial", 24, "bold"),
            fg=self.colors["text"],
            bg=self.colors["bg"]
        )
        title_label.pack(pady=(0, 20))
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill="both", expand=True)
        
        # Style the notebook
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TNotebook', background=self.colors["bg"])
        self.style.configure('TNotebook.Tab', background=self.colors["secondary_bg"], foreground=self.colors["white"])
        self.style.map('TNotebook.Tab', background=[('selected', self.colors["purple"])])
        
        # Create tabs
        self.create_generator_tab()
        self.create_saved_tab()
        self.create_add_tab()
        
    def create_generator_tab(self):
        """Create the password generator tab"""
        generator_frame = tk.Frame(self.notebook, bg=self.colors["bg"])
        self.notebook.add(generator_frame, text="🎲 Generate")
        
        # Generator container
        gen_container = tk.Frame(generator_frame, bg=self.colors["secondary_bg"], relief="raised", bd=2)
        gen_container.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Length selection
        length_frame = tk.Frame(gen_container, bg=self.colors["secondary_bg"])
        length_frame.pack(fill="x", padx=20, pady=10)
        
        tk.Label(
            length_frame,
            text="Password Length:",
            font=("Arial", 12, "bold"),
            fg=self.colors["white"],
            bg=self.colors["secondary_bg"]
        ).pack(side="left")
        
        self.length_var = tk.IntVar(value=16)
        length_spinbox = tk.Spinbox(
            length_frame,
            from_=8,
            to=50,
            textvariable=self.length_var,
            font=("Arial", 12),
            bg=self.colors["accent"],
            fg=self.colors["white"],
            selectbackground=self.colors["purple"]
        )
        length_spinbox.pack(side="right", padx=(10, 0))
        
        # Character options
        options_frame = tk.Frame(gen_container, bg=self.colors["secondary_bg"])
        options_frame.pack(fill="x", padx=20, pady=10)
        
        self.use_uppercase = tk.BooleanVar(value=True)
        self.use_lowercase = tk.BooleanVar(value=True)
        self.use_numbers = tk.BooleanVar(value=True)
        self.use_symbols = tk.BooleanVar(value=True)
        
        tk.Checkbutton(
            options_frame,
            text="ABC (Uppercase)",
            variable=self.use_uppercase,
            font=("Arial", 10),
            fg=self.colors["white"],
            bg=self.colors["secondary_bg"],
            selectcolor=self.colors["purple"],
            activebackground=self.colors["secondary_bg"],
            activeforeground=self.colors["white"]
        ).pack(anchor="w")
        
        tk.Checkbutton(
            options_frame,
            text="abc (Lowercase)",
            variable=self.use_lowercase,
            font=("Arial", 10),
            fg=self.colors["white"],
            bg=self.colors["secondary_bg"],
            selectcolor=self.colors["purple"],
            activebackground=self.colors["secondary_bg"],
            activeforeground=self.colors["white"]
        ).pack(anchor="w")
        
        tk.Checkbutton(
            options_frame,
            text="123 (Numbers)",
            variable=self.use_numbers,
            font=("Arial", 10),
            fg=self.colors["white"],
            bg=self.colors["secondary_bg"],
            selectcolor=self.colors["purple"],
            activebackground=self.colors["secondary_bg"],
            activeforeground=self.colors["white"]
        ).pack(anchor="w")
        
        tk.Checkbutton(
            options_frame,
            text="!@# (Symbols)",
            variable=self.use_symbols,
            font=("Arial", 10),
            fg=self.colors["white"],
            bg=self.colors["secondary_bg"],
            selectcolor=self.colors["purple"],
            activebackground=self.colors["secondary_bg"],
            activeforeground=self.colors["white"]
        ).pack(anchor="w")
        
        # Generate button
        generate_btn = tk.Button(
            gen_container,
            text="🎲 Generate Password",
            command=self.generate_password,
            font=("Arial", 14, "bold"),
            bg=self.colors["purple"],
            fg=self.colors["white"],
            relief="flat",
            padx=20,
            pady=10,
            cursor="hand2"
        )
        generate_btn.pack(pady=20)
        
        # Password display
        self.password_var = tk.StringVar()
        password_entry = tk.Entry(
            gen_container,
            textvariable=self.password_var,
            font=("Courier", 16),
            bg=self.colors["accent"],
            fg=self.colors["white"],
            relief="flat",
            justify="center"
        )
        password_entry.pack(fill="x", padx=20, pady=10)
        
        # Copy button
        copy_btn = tk.Button(
            gen_container,
            text="📋 Copy",
            command=self.copy_password,
            font=("Arial", 12),
            bg=self.colors["cyan"],
            fg=self.colors["white"],
            relief="flat",
            padx=15,
            pady=5,
            cursor="hand2"
        )
        copy_btn.pack(pady=10)
        
    def create_saved_tab(self):
        """Create the saved passwords tab"""
        saved_frame = tk.Frame(self.notebook, bg=self.colors["bg"])
        self.notebook.add(saved_frame, text="💾 Saved")
        
        # Search frame
        search_frame = tk.Frame(saved_frame, bg=self.colors["secondary_bg"])
        search_frame.pack(fill="x", padx=20, pady=10)
        
        tk.Label(
            search_frame,
            text="🔍 Search:",
            font=("Arial", 12),
            fg=self.colors["white"],
            bg=self.colors["secondary_bg"]
        ).pack(side="left")
        
        self.search_var = tk.StringVar()
        self.search_var.trace("w", self.filter_passwords)
        search_entry = tk.Entry(
            search_frame,
            textvariable=self.search_var,
            font=("Arial", 12),
            bg=self.colors["accent"],
            fg=self.colors["white"],
            relief="flat"
        )
        search_entry.pack(side="right", fill="x", expand=True, padx=(10, 0))
        
        # Treeview for passwords
        tree_frame = tk.Frame(saved_frame, bg=self.colors["bg"])
        tree_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        columns = ("Website", "Username", "Password", "Date Added")
        self.tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=15)
        
        # Configure columns
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)
        
        # Style the treeview
        self.style.configure("Treeview", 
                       background=self.colors["accent"],
                       foreground=self.colors["white"],
                       fieldbackground=self.colors["accent"])
        self.style.configure("Treeview.Heading", 
                       background=self.colors["purple"],
                       foreground=self.colors["white"])
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Buttons frame
        btn_frame = tk.Frame(saved_frame, bg=self.colors["bg"])
        btn_frame.pack(fill="x", padx=20, pady=10)
        
        tk.Button(
            btn_frame,
            text="👁️ Show Password",
            command=self.show_password,
            font=("Arial", 10),
            bg=self.colors["cyan"],
            fg=self.colors["white"],
            relief="flat",
            padx=10,
            pady=5,
            cursor="hand2"
        ).pack(side="left", padx=(0, 10))
        
        tk.Button(
            btn_frame,
            text="🗑️ Delete",
            command=self.delete_password,
            font=("Arial", 10),
            bg=self.colors["text"],
            fg=self.colors["white"],
            relief="flat",
            padx=10,
            pady=5,
            cursor="hand2"
        ).pack(side="left", padx=(0, 10))
        
        tk.Button(
            btn_frame,
            text="🌐 Open Website",
            command=self.open_website,
            font=("Arial", 10),
            bg=self.colors["purple"],
            fg=self.colors["white"],
            relief="flat",
            padx=10,
            pady=5,
            cursor="hand2"
        ).pack(side="left")
        
        # Load saved passwords
        self.load_saved_passwords()
        
    def create_add_tab(self):
        """Create the add new password tab"""
        add_frame = tk.Frame(self.notebook, bg=self.colors["bg"])
        self.notebook.add(add_frame, text="➕ Add New")
        
        # Form container
        form_container = tk.Frame(add_frame, bg=self.colors["secondary_bg"], relief="raised", bd=2)
        form_container.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Website
        tk.Label(
            form_container,
            text="🌐 Website:",
            font=("Arial", 12, "bold"),
            fg=self.colors["white"],
            bg=self.colors["secondary_bg"]
        ).pack(anchor="w", padx=20, pady=(20, 5))
        
        self.website_var = tk.StringVar()
        website_entry = tk.Entry(
            form_container,
            textvariable=self.website_var,
            font=("Arial", 12),
            bg=self.colors["accent"],
            fg=self.colors["white"],
            relief="flat"
        )
        website_entry.pack(fill="x", padx=20, pady=(0, 15))
        
        # Username
        tk.Label(
            form_container,
            text="👤 Username:",
            font=("Arial", 12, "bold"),
            fg=self.colors["white"],
            bg=self.colors["secondary_bg"]
        ).pack(anchor="w", padx=20, pady=(0, 5))
        
        self.username_var = tk.StringVar()
        username_entry = tk.Entry(
            form_container,
            textvariable=self.username_var,
            font=("Arial", 12),
            bg=self.colors["accent"],
            fg=self.colors["white"],
            relief="flat"
        )
        username_entry.pack(fill="x", padx=20, pady=(0, 15))
        
        # Password
        tk.Label(
            form_container,
            text="🔐 Password:",
            font=("Arial", 12, "bold"),
            fg=self.colors["white"],
            bg=self.colors["secondary_bg"]
        ).pack(anchor="w", padx=20, pady=(0, 5))
        
        self.new_password_var = tk.StringVar()
        password_entry = tk.Entry(
            form_container,
            textvariable=self.new_password_var,
            font=("Arial", 12),
            bg=self.colors["accent"],
            fg=self.colors["white"],
            relief="flat",
            show="*"
        )
        password_entry.pack(fill="x", padx=20, pady=(0, 15))
        
        # Show/hide password
        self.show_password_var = tk.BooleanVar()
        tk.Checkbutton(
            form_container,
            text="👁️ Show Password",
            variable=self.show_password_var,
            command=self.toggle_password_visibility,
            font=("Arial", 10),
            fg=self.colors["white"],
            bg=self.colors["secondary_bg"],
            selectcolor=self.colors["purple"],
            activebackground=self.colors["secondary_bg"],
            activeforeground=self.colors["white"]
        ).pack(anchor="w", padx=20, pady=(0, 20))
        
        # Generate password button
        tk.Button(
            form_container,
            text="🎲 Generate Password",
            command=self.generate_for_form,
            font=("Arial", 12),
            bg=self.colors["purple"],
            fg=self.colors["white"],
            relief="flat",
            padx=15,
            pady=8,
            cursor="hand2"
        ).pack(pady=(0, 20))
        
        # Save button
        save_btn = tk.Button(
            form_container,
            text="💾 Save Password",
            command=self.save_new_password,
            font=("Arial", 14, "bold"),
            bg=self.colors["text"],
            fg=self.colors["white"],
            relief="flat",
            padx=20,
            pady=10,
            cursor="hand2"
        )
        save_btn.pack(pady=20)
        
    def generate_password(self):
        """Generate a random password based on selected options"""
        length = self.length_var.get()
        chars = ""
        
        if self.use_uppercase.get():
            chars += string.ascii_uppercase
        if self.use_lowercase.get():
            chars += string.ascii_lowercase
        if self.use_numbers.get():
            chars += string.digits
        if self.use_symbols.get():
            chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
        
        if not chars:
            messagebox.showwarning("Warning", "Please select at least one character type!")
            return
        
        password = ''.join(random.choice(chars) for _ in range(length))
        self.password_var.set(password)
        
    def copy_password(self):
        """Copy password to clipboard"""
        password = self.password_var.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo("Success", "Password copied to clipboard! 📋")
        else:
            messagebox.showwarning("Warning", "No password to copy!")
    
    def load_saved_passwords(self):
        """Load saved passwords into the treeview"""
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for entry in self.passwords_data["websites"]:
            self.tree.insert("", "end", values=(
                entry["website"],
                entry["username"],
                "•" * len(entry["password"]),
                entry["date_added"]
            ))
    
    def filter_passwords(self, *args):
        """Filter passwords based on search term"""
        search_term = self.search_var.get().lower()
        
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for entry in self.passwords_data["websites"]:
            if (search_term in entry["website"].lower() or 
                search_term in entry["username"].lower()):
                self.tree.insert("", "end", values=(
                    entry["website"],
                    entry["username"],
                    "•" * len(entry["password"]),
                    entry["date_added"]
                ))
    
    def show_password(self):
        """Show the selected password"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a password to view!")
            return
        
        item = self.tree.item(selection[0])
        website = item["values"][0]
        username = item["values"][1]
        
        # Find the actual password
        for entry in self.passwords_data["websites"]:
            if entry["website"] == website and entry["username"] == username:
                messagebox.showinfo("Password", f"Password: {entry['password']}")
                break
    
    def delete_password(self):
        """Delete the selected password"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a password to delete!")
            return
        
        if messagebox.askyesno("Confirm", "Are you sure you want to delete this password?"):
            item = self.tree.item(selection[0])
            website = item["values"][0]
            username = item["values"][1]
            
            # Remove from data
            self.passwords_data["websites"] = [
                entry for entry in self.passwords_data["websites"]
                if not (entry["website"] == website and entry["username"] == username)
            ]
            
            self.save_data()
            self.load_saved_passwords()
            messagebox.showinfo("Success", "Password deleted! 🗑️")
    
    def open_website(self):
        """Open the selected website"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a website to open!")
            return
        
        item = self.tree.item(selection[0])
        website = item["values"][0]
        
        # Add https if not present
        if not website.startswith(('http://', 'https://')):
            website = 'https://' + website
        
        try:
            webbrowser.open(website)
        except:
            messagebox.showerror("Error", "Could not open website!")
    
    def toggle_password_visibility(self):
        """Toggle password visibility in the add form"""
        # This would need to be implemented with a custom Entry widget
        # For simplicity, we'll just show a message
        if self.show_password_var.get():
            messagebox.showinfo("Info", "Password visibility toggle would be implemented here!")
    
    def generate_for_form(self):
        """Generate password for the add form"""
        # Use default settings for form generation
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        password = ''.join(random.choice(chars) for _ in range(16))
        self.new_password_var.set(password)
    
    def save_new_password(self):
        """Save a new password entry"""
        website = self.website_var.get().strip()
        username = self.username_var.get().strip()
        password = self.new_password_var.get().strip()
        
        if not all([website, username, password]):
            messagebox.showwarning("Warning", "Please fill in all fields!")
            return
        
        # Check if entry already exists
        for entry in self.passwords_data["websites"]:
            if entry["website"] == website and entry["username"] == username:
                messagebox.showwarning("Warning", "This website/username combination already exists!")
                return
        
        # Add new entry
        new_entry = {
            "website": website,
            "username": username,
            "password": password,
            "date_added": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        
        self.passwords_data["websites"].append(new_entry)
        self.save_data()
        
        # Clear form
        self.website_var.set("")
        self.username_var.set("")
        self.new_password_var.set("")
        
        # Refresh saved passwords
        self.load_saved_passwords()
        
        # Switch to saved tab
        self.notebook.select(1)
        
        messagebox.showinfo("Success", "Password saved successfully! 💾")

def main():
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main() 