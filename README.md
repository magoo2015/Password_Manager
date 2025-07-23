# 🔐 Password Vault - Gen Z Style

A modern, stylish password generator and manager built with Python and Tkinter, featuring a Gen Z aesthetic with vibrant colors and emojis.

## ✨ Features

- **🎲 Password Generation**: Create strong, customizable passwords
- **💾 Password Storage**: Save and manage website credentials
- **🔍 Search & Filter**: Quickly find saved passwords
- **🌐 Website Integration**: Open websites directly from the app
- **📋 Copy to Clipboard**: One-click password copying
- **🎨 Gen Z UI**: Modern, vibrant interface with emojis and trendy colors

## 🚀 Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd DesktopPasswordManager
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python password_generator.py
```

## 🎯 Usage

### Generate Tab
- Set password length (8-50 characters)
- Choose character types (uppercase, lowercase, numbers, symbols)
- Click "🎲 Generate Password" to create a new password
- Use "📋 Copy" to copy the password to clipboard

### Saved Tab
- View all saved website credentials
- Search through saved passwords
- Show/hide passwords
- Delete unwanted entries
- Open websites directly

### Add New Tab
- Add new website credentials manually
- Generate passwords for new entries
- Save passwords with website and username

## 🛡️ Security

- Passwords are stored locally in JSON format
- No cloud storage or external services
- Passwords are masked by default in the interface
- All data is stored in `passwords.json`

## 🎨 Design

The application features a Gen Z aesthetic with:
- Dark theme with vibrant accent colors
- Emoji icons throughout the interface
- Modern flat design
- Purple, pink, and cyan color scheme
- Tabbed interface for easy navigation

## 📁 File Structure

```
DesktopPasswordManager/
├── password_generator.py    # Main application
├── passwords.json          # Password storage (created automatically)
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🔧 Customization

You can customize the colors by modifying the `colors` dictionary in the `PasswordGenerator` class:

```python
self.colors = {
    "bg": "#1a1a2e",           # Main background
    "secondary_bg": "#16213e",  # Secondary background
    "accent": "#0f3460",        # Accent color
    "text": "#e94560",          # Text color
    "white": "#ffffff",         # White text
    "purple": "#8b5cf6",        # Purple accent
    "pink": "#ec4899",          # Pink accent
    "cyan": "#06b6d4"           # Cyan accent
}
```

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📄 License

This project is open source and available under the MIT License.