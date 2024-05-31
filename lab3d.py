#!/usr/bin/env python3

# Author ID: hshah98

import subprocess

def free_space():
    # Launch the Linux command: df -h | grep '/$' | awk '{print $4}'
    command = "df -h | grep '/$' | awk '{print $4}'"
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    
    # Communicate with the process and retrieve its output
    output, error = p.communicate()

    # Check if there was an error
    if error:
        return f"Error: {error.decode('utf-8').strip()}"

    # Convert the output to a string and strip off newline characters
    return output.decode('utf-8').strip()

if __name__ == '__main__':
    print(free_space())

