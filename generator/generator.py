"""
author: @guu8hc
"""

from datetime import datetime

class Generator:
    """
    A base class for generating files.
    """
    def __init__(self, filename):
        """
        constructor
        """
        self.filename = "_out/" + filename
        self.content = ""

    def generate(self):
        """
        generate the file
        """
        print(f"[DEBUG] Generating file: {self.filename}")
        with open(self.filename, 'w', encoding='utf-8') as file:
            file.write(self.content)

    def build_header(self):
        """
        build the header
        """
        self.content += "#!/usr/bin/env python3\n"
        self.content += "# -*- coding: utf-8 -*-\n"
        self.content += "\n"
        self.content += "# Generated by guu8hc\n"
        self.content += f"# Generated time: {datetime.now()}\n"
