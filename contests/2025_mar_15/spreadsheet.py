class Spreadsheet:
    columns = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, rows: int):
        self.sheet = dict()
        # Initializes a spreadsheet with 26 columns
        for col in self.columns:
            for row in range(1, rows + 1):
                self.sheet[f"{col}{row}"] = 0

    def set_cell(self, cell: str, value: int) -> None:
        self.sheet[cell] = value

    def reset_cell(self, cell: str) -> None:
        self.sheet[cell] = 0

    def get_value(self, formula: str) -> int:
        first_ref, second_ref = formula[1:].split("+")
        val1 = self.sheet.get(first_ref, 0) if first_ref in self.sheet.keys() else int(first_ref)
        val2 = self.sheet.get(second_ref, 0) if second_ref in self.sheet.keys() else int(second_ref)
        return val1 + val2


# Your Spreadsheet object will be instantiated and called as such:

obj = Spreadsheet(rows=3)
obj.get_value("=5+7")
obj.set_cell("A1", 10)
obj.get_value("=A1+6")
