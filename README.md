# Text Editor - System Software Project

A simple yet powerful text editor built using Python and Tkinter. This project was developed as part of a System Software course by a team of students. The text editor includes features like file handling, text formatting, find/replace functionality, and text-to-speech conversion.

![Text Editor Screenshot](screenshot.png) <!-- Add a screenshot if available -->

---

## Features

- **File Operations**: Create, open, save, and save-as text files.
- **Text Formatting**: Change font style and size.
- **Find and Replace**: Search for specific words and replace them.
- **Text-to-Speech**: Convert text content into speech using Google Text-to-Speech (gTTS).
- **Character Count**: Display the number of characters in the document.
- **Customizable UI**: Dark and light themes with a modern look using `customtkinter`.

---

## Installation

### Prerequisites

- Python 3.x
- Required Python libraries: `tkinter`, `gtts`, `Pillow`, `customtkinter`

### Steps

1. Clone the repository:
 ```bash
 git clone https://github.com/Combust10/SimpleTextEditor.git
 cd SimpleTextEditor
 ```
2. Install the required libraries:
```bash
pip install -r requirements.txt
Run the text editor:
```
3. Run the text editor:
```bash
python text_editor.py
```

## Usage

1. **File Menu**:
   - **New**: Create a new file.
   - **Open**: Open an existing text file.
   - **Save**: Save the current file.
   - **Save As**: Save the file with a new name.
   - **Exit**: Close the application.

2. **Format Menu**:
   - **Font Style**: Change the font style (e.g., Times New Roman, Arial).
   - **Font Size**: Adjust the font size (e.g., 8, 10, 12, 14).

3. **Edit Menu**:
   - **Find**: Search for a specific word in the text.
   - **Find and Replace**: Replace a specific word with another.

4. **Text-to-Speech**:
   - Click the speaker icon at the bottom-right corner to convert the text into speech.

5. **Character Count**:
   - The number of characters in the document is displayed at the bottom-left corner.

## Acknowledgments

- Thanks to the `customtkinter` library for providing a modern UI.
