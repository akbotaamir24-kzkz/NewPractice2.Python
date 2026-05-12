from analytics import (
    FileManager,
    DataLoader,
    DataAnalyzer,
    GpaAnalyzer,
    ResultSaver,
    Report
)

fm = FileManager('students.csv')

if not fm.check_file():
    print('Stopping program.')
    exit()

fm.create_output_folder()

dl = DataLoader('students.csv')
dl.load()
dl.preview()

print("\nRunning analysers...")
print("--------------------------")

analysers = [
    GpaAnalyzer(dl.students)
]

for analyser in analysers:
    print(analyser)
    analyser.analyse()
    analyser.print_results()

print("\nCreating report...")
print("--------------------------")

gpa = GpaAnalyzer(dl.students)

saver = ResultSaver(gpa.result, 'output/result.json')

report = Report(gpa, saver)

report.generate()