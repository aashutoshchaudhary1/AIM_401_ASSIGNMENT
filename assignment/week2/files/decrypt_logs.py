"""
Lesson 2 Individual Assignment
Caesar Shift Log Decryption Utility

This script reads an encrypted server log (raw_logs.txt), decrypts each
line using a left Caesar shift of 3, writes every decrypted line to
decrypted_master.txt, and additionally writes any line containing the
keyword "BREACH" to security_alerts.txt.

Constraints followed:
- No lists, dictionaries, or sets
- No custom functions (no 'def')
- No external libraries (only built-ins: open, ord, chr, str methods)
"""

import os

SHIFT = 3

# Resolve file paths relative to script location to avoid FileNotFoundError
script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, "raw_logs.txt")
master_path = os.path.join(script_dir, "decrypted_master.txt")
alert_path = os.path.join(script_dir, "security_alerts.txt")

# Task 1: Open the input file for reading and both output files for writing
input_file = open(input_path, "r")
master_file = open(master_path, "w")
alert_file = open(alert_path, "w")

line_count = 0

# Task 2: Iterate through each line of the input file
for line in input_file:
    decrypted_line = ""

    # Iterate through each character in the line and apply a left shift of 3
    for char in line:
        if char == "\n":
            # Preserve newline characters without shifting
            decrypted_line = decrypted_line + char
        elif char == " ":
            # Preserve spaces without shifting
            decrypted_line = decrypted_line + char
        elif char >= "A" and char <= "Z":
            # Uppercase letters, with wrap-around at the alphabet boundary
            shifted_code = ord(char) - SHIFT
            if shifted_code < ord("A"):
                shifted_code = shifted_code + 26
            decrypted_line = decrypted_line + chr(shifted_code)
        elif char >= "a" and char <= "z":
            # Lowercase letters, with wrap-around at the alphabet boundary
            shifted_code = ord(char) - SHIFT
            if shifted_code < ord("a"):
                shifted_code = shifted_code + 26
            decrypted_line = decrypted_line + chr(shifted_code)
        else:
            # Punctuation, digits, colons, etc. are left unchanged
            decrypted_line = decrypted_line + char

    # Task 3: Strip leading/trailing whitespace from the decrypted string
    decrypted_line = decrypted_line.strip()

    # Write every decrypted line into the master log file
    master_file.write(decrypted_line + "\n")

    # Convert to uppercase and check for the "BREACH" keyword
    upper_check = decrypted_line.upper()
    if "BREACH" in upper_check:
        alert_file.write(decrypted_line + "\n")

    line_count = line_count + 1

# Close all file handles
input_file.close()
master_file.close()
alert_file.close()

print("Decryption complete.")
print("Lines processed:", line_count)
print("Decrypted log written to decrypted_master.txt")
print("Security alerts written to security_alerts.txt")
