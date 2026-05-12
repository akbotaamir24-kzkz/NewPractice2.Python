import os


class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        print("Checking file...")

        if os.path.exists(self.filename):
            print(f"File found: {self.filename}")
            return True

        else:
            print(f"Error: {self.filename} not found.")
            return False

    def create_output_folder(self, folder="output"):
        print("\nChecking output folder...")

        if os.path.exists(folder):
            print("Output folder already exists: output/")

        else:
            os.makedirs(folder)
            print("Output folder created: output/")