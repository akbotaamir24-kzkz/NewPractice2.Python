class DataAnalyzer:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        print("Not implemented - use child class")

    def print_results(self):
        for key, value in self.result.items():
            print(f"{key}: {value}")

    def __str__(self):
        return f"DataAnalyzer: base class, {len(self.students)} students"


class GpaAnalyzer(DataAnalyzer):
    def __init__(self, students):
        super().__init__(students)

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

        high_gpa_students = list(
            filter(lambda s: float(s["GPA"]) > 3.8, self.students)
        )

        gpa_values = list(
            map(lambda s: float(s["GPA"]), self.students)
        )

        hard_workers = list(
            filter(lambda s: float(s["study_hours_per_day"]) > 4, self.students)
        )

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

    def print_results(self):
        print("\n==========================")
        print("GPA ANALYSIS REPORT")
        print("==========================")

        super().print_results()

        print("==========================")

    def __str__(self):
        return f"GpaAnalyzer: GPA Statistics, {len(self.students)} students"