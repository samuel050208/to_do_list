from ui.main_window import load_window
from data.manager import data_manager


if __name__ == "__main__":
    def loader():
        data = manager.loadTxt()
        window.set_toDoList(data)
        window.activate_buttons()
        numb = manager.lengthList()
        window.deactivate_buttons(numb)

    def addButton_callback():
        print("main: Add button pressed...")
        entry = window.getText()
        length = manager.lengthList()
        if length < 10:
            manager.saveToFile(entry)
        else:
            print("main: List is full...")
        loader()

    def remButton_callback(index):
        print("main: Remove Button pressed...")
        manager.removeToDo(index)
        loader()

    def clearButton_callback():
        print("main: Clear button pressed...")
        manager.clearFile()
        loader()

    def exit_callback():
        print("main_window: Exit button pressed...")
        window.window_exit()
        

    print("main: Loading...")
    window = load_window(addButton_callback, clearButton_callback, remButton_callback, exit_callback)
    manager = data_manager()
    loader() 

    window.load_ui()