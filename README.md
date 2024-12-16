
# Language Translation Bot  

**Language Translation Bot** is an automated multilingual translation tool built with Python 2.7. Designed to translate text quickly, it supports hundreds of languages and features both interactive and batch modes for processing multiple texts at once.  

## 📜 Features  
1. **Multilingual Translation**:  
   - Supports over 100 languages.  
   - Automatically detects the source language.  

2. **Interactive Mode**:  
   - Input text directly through the terminal for translation.  

3. **Batch Mode**:  
   - Process text files containing multiple lines of text for bulk translation.  

4. **Language List**:  
   - Display all supported languages and their respective codes.  

## 🔧 Installation  
### Prerequisites  
Ensure **Python 2.7** is installed on your system.  

### Installation Steps  
1. Clone this repository:  
   ```bash
   git clone https://github.com/Jenderal92/language-translation-bot.git
   cd language-translation-bot
   ```  

2. Install the required library:  
   ```bash
   pip install googletrans==2.4.0
   ```  

## 🚀 Usage  
1. Run the program via terminal:  
   ```bash
   python language_translation_bot.py
   ```  

2. Choose from the available options:  
   - **Option 1**: Input text directly for translation.  
   - **Option 2**: Input a text file name to translate multiple lines at once.  
   - **Option 3**: Display a list of supported languages.  
   - **Option 4**: Exit the program.  

### Example Usage  
#### Interactive Mode  
```bash
Enter text to translate: Hello, how are you?  
Enter source language code (or 'auto' to detect): auto  
Enter target language code: id  

Translated Text: Halo, apa kabar?  
```  

#### Batch Mode  
Provide the name of the text file for translation:  
```text
example.txt  
```

Contents of `example.txt`:  
```text
Hello, how are you?  
I am learning Python.  
This is a translation tool.  
```  

Generated Output:  
```text
Original: Hello, how are you?  
Translated: Halo, apa kabar?  

Original: I am learning Python.  
Translated: Saya sedang belajar Python.  

Original: This is a translation tool.  
Translated: Ini adalah alat penerjemahan.  
```  
