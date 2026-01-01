# 🔐 Secure Password Generator

A command-line password generator written in Python. Create strong, customizable passwords with options for uppercase letters, digits, and special characters.

## Features

- Generate passwords of any length (minimum 1 character)
- Toggle inclusion of:
  - Uppercase letters (`A-Z`)
  - Digits (`0-9`)
  - Special symbols (`!@#$%`, etc.)
- Ensures **at least one character from each selected category** is included
- Input validation with helpful prompts
- Graceful handling of keyboard interrupts (`Ctrl+C`) and EOF
- Defaults to secure settings (12 characters, all character types enabled)
