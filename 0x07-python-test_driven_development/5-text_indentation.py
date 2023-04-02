#!/usr/bin/python3
"""
This module contains a function that indents texts
"""
def text_indentation(text):
    """
    This function adds two newlines after each ".", "?", or ":" in the given text string.
    
    Args:
        text (str): The text string to be formatted.
        
    Raises:
        TypeError: If the input argument is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    count = 0
    while count < len(text) and text[count] == " ":
        count += 1
    
    while count < len(text):
        print(text[count], end="")
        
        if text[count] == "\n" or text[count] in ".?:":
            if text[count] in ".?:":
                print("\n\n")
            count += 1
            
            while count < len(text) and text[count] == " ":
                count += 1
                
            continue
        
        count += 1
