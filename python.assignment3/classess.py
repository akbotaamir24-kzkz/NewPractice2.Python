import os
import csv
import json


class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        print("Checking file...")
        if os.path.exists(self.filename):
            print("File found: students.csv")
            return True
        else:
            print("Error: students.csv not found.")
            return False

    def create_output_folder(self, folder="output"):
        print("\nChecking output folder...")
        if os.path.exists(folder):
            print("Output folder already exists: output/")
        else:
            os.makedirs(folder)
            print("Output folder created: output/")


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


class DataAnalyzer:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        gpas = []
        high = 0

        
        for s in self.students:
            try:
                gpa = float(s["GPA"])
                gpas.append(gpa)

                if gpa > 3.5:
                    high += 1
            except:
                pass

        
        high_gpa_students = list(filter(lambda s: float(s["GPA"]) > 3.8, self.students))

        
        gpa_values = list(map(lambda s: float(s["GPA"]), self.students))

        
        hard_workers = list(filter(lambda s: float(s["study_hours_per_day"]) > 4, self.students))

        self.result = {
            "analysis": "GPA Statistics",
            "total_students": len(self.students),
            "average_gpa": round(sum(gpas) / len(gpas), 2),
            "max_gpa": max(gpas),
            "min_gpa": min(gpas),
            "high_performers": high,

            
            "students_gpa_above_3_8": len(high_gpa_students),
            "first_5_gpa_values": gpa_values[:5],
            "students_studying_above_4_hours": len(hard_workers)
        }

        return self.result

    def print_results(self):
        print("\n-----------------------------")
        print("GPA Analysis")
        print("-----------------------------")
        print("Total students :", self.result["total_students"])
        print("Average GPA :", self.result["average_gpa"])
        print("Highest GPA :", self.result["max_gpa"])
        print("Lowest GPA :", self.result["min_gpa"])
        print("Students GPA>3.5 :", self.result["high_performers"])
        print("-----------------------------")

       
        print("\n-----------------------------")
        print("Lambda / Map / Filter")
        print("-----------------------------")
        print("Students with GPA > 3.8 :", self.result["students_gpa_above_3_8"])
        print("GPA values (first 5) :", self.result["first_5_gpa_values"])
        print("Students studying > 4 hrs :", self.result["students_studying_above_4_hours"])
        print("-----------------------------")

class ResultSaver:
    def __init__(self, result, output_path):
        self.result = result
        self.output_path = output_path

    def save_json(self):
        try:
            with open(self.output_path, "w", encoding="utf-8") as f:
                json.dump(self.result, f, indent=4)

            print("\nResult saved to output/result.json")

        except Exception as e:
            print("Error while saving:", e)