import csv


class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        try:
            print("\nLoading data...")

            with open(self.filename, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    self.students.append(row)

            print("Data loaded successfully:", len(self.students), "students")

        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")

        return self.students

    def preview(self, n=5):
        print("\nFirst", n, "rows:")
        print("-----------------------------")

        for s in self.students[:n]:
            print(
                s["student_id"], "|",
                s["age"], "|",
                s["gender"], "|",
                s["country"], "| GPA:",
                s["GPA"]
            )

        print("-----------------------------")