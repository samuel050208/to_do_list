import os
base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, "toDoList.txt")


class data_manager:
    def loadTxt(self):
        print("manager: Reading data...")
        with open(file_path, "r", encoding = "utf-8") as file:
            self.toDoList_temp = file.read()
        return self.toDoList_temp
    
    def lengthList(self):
        with open(file_path, "r", encoding = "utf-8") as file:
            linesFile = file.readlines()
            lines = len(linesFile)
            return lines
    
    def saveToFile(self, entry):
        print("manager: Saving data to file...")
        text = entry
        length = self.lengthList() + 1

        with open(file_path, "a", encoding = "utf-8") as file:
            file.write(str(length) + ". " + text + "\n")

    def removeToDo(self, index):
        try:
            print("manager: Removing To-Do in line " + str(index) + "...")
            # Reading
            with open(file_path, "r", encoding = "utf-8") as file:
                lines = file.readlines()

            # Removing
            del lines[index]

            # Renumbering
            lines_new = []
            with open(file_path, "w", encoding = "utf-8") as file:
                for i, line in enumerate(lines):
                    text = line.split(". ", 1)[1].strip() 
                    file.write(f"{i + 1}. {text}\n")
        except:
            print("manager: List is empty...")

    def clearFile(self):
        with open(file_path, "w", encoding = "utf-8"):
            print("manager: File cleared...")
            pass