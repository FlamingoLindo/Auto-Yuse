"""
This module provides a function to get user input via a simple dialog box 
using tkinter and customtkinter libraries.
"""

from tkinter import simpledialog
import customtkinter as tk


def get_user_input(prompt):
    """
    Displays a dialog box to get user input in a tkinter-based application.

    This function creates a hidden tkinter window and opens an input dialog 
    to prompt the user for a response.

    Args:
        prompt (str): The message displayed to the user in the input dialog.

    Returns:
        str: The user input as a string. If the user cancels or closes the dialog, 
             returns None.
    """
    root = tk.CTk()
    root.withdraw()  # Hide the main window
    user_input = simpledialog.askstring("Input", prompt)
    return user_input
