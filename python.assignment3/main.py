from classess import FileManager, DataLoader, DataAnalyzer, ResultSaver


def main():
    fm = FileManager("students.csv")

    if not fm.check_file():
        print("Stopping program.")
        exit()

    fm.create_output_folder()

    dl = DataLoader("students.csv")
    dl.load()
    dl.preview()

    analyzer = DataAnalyzer(dl.students)
    analyzer.analyse()
    analyzer.print_results()

    saver = ResultSaver(analyzer.result, "output/result.json")
    saver.save_json()


main()