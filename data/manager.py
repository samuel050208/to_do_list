import os
class DataManager:
    def get_path(self):
        base = os.path.join(os.path.expanduser("~"), "AppData", "Local", "ToDoList")
        return os.path.join(base, "toDoList.txt")

    def ensure_file(self, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)

        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8") as f:
                f.write("")

    def loadTxt(self):
        print("manager: Reading data...")
        path = self.get_path()
        self.ensure_file(path)
        with open(path, "r", encoding = "utf-8") as file:
            self.toDoList_temp = file.read()
        return self.toDoList_temp
    
    def lengthList(self):
        path = self.get_path()
        with open(path, "r", encoding = "utf-8") as file:
            linesFile = file.readlines()
            lines = len(linesFile)
            return lines
    
    def saveToFile(self, entry):
        path = self.get_path()
        print("manager: Saving data to file...")
        text = entry
        length = self.lengthList() + 1

        with open(path, "a", encoding = "utf-8") as file:
            file.write(str(length) + ". " + text + "\n")

    def removeToDo(self, index):
        path = self.get_path()
        try:
            print("manager: Removing To-Do in line " + str(index) + "...")
            # Reading
            with open(path, "r", encoding = "utf-8") as file:
                lines = file.readlines()

            # Removing
            del lines[index]

            # Renumbering
            lines_new = []
            with open(path, "w", encoding = "utf-8") as file:
                for i, line in enumerate(lines):
                    text = line.split(". ", 1)[1].strip() 
                    file.write(f"{i + 1}. {text}\n")
        except:
            print("manager: List is empty...")

    def clearFile(self):
        path = self.get_path()
        with open(path, "w", encoding = "utf-8"):
            print("manager: File cleared...")
            pass