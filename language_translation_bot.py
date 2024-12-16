# -*- coding: utf-8 -*-
import os
from googletrans import Translator, LANGUAGES

def print_banner():
    banner = """
############################################################
#                                                          #
#           LANGUAGE TRANSLATION BOT - PYTHON 2.7         #
#                 Multilingual Translation Tool            #
#                                                          #
############################################################
    """
    print(banner)

def list_languages():
    print("Supported Languages:")
    for code, lang in LANGUAGES.items():
        print("{}: {}".format(code, lang))

def translate_text(text, src_lang, dest_lang):
    translator = Translator()
    try:
        result = translator.translate(text, src=src_lang, dest=dest_lang)
        return result.text
    except Exception as e:
        return "Error during translation: {}".format(str(e))

def main():
    print_banner()
    print("Welcome to the Language Translation Bot!")
    while True:
        print("\nOptions:")
        print("1. Translate Text")
        print("2. Translate Text File (Batch)")
        print("3. List Supported Languages")
        print("4. Exit")
        
        choice = raw_input("Enter your choice (1-4): ").strip()
        if choice == '1':
            text = raw_input("Enter text to translate: ")
            src_lang = raw_input("Enter source language code (or 'auto' to detect): ")
            dest_lang = raw_input("Enter target language code: ")
            result = translate_text(text, src_lang, dest_lang)
            print("\nTranslated Text: {}".format(result))
        elif choice == '2':
            file_path = raw_input("Enter file path for batch translation: ")
            if os.path.exists(file_path):
                with open(file_path, 'r') as file:
                    lines = file.readlines()
                src_lang = raw_input("Enter source language code (or 'auto' to detect): ")
                dest_lang = raw_input("Enter target language code: ")
                print("\nTranslating...")
                for line in lines:
                    translated_line = translate_text(line.strip(), src_lang, dest_lang)
                    print("Original: {}".format(line.strip()))
                    print("Translated: {}\n".format(translated_line))
            else:
                print("File not found: {}".format(file_path))
        elif choice == '3':
            list_languages()
        elif choice == '4':
            print("Thank you for using the Language Translation Bot!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
