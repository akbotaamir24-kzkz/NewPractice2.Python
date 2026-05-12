import json


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