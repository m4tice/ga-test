"""
author: @guu8hc
"""

from generator.generator import Generator

if __name__ == "__main__":
    generator = Generator("test.py")
    generator.build_header()
    generator.generate()
    print("File generated successfully.")
