import os

class Memento:
    def __init__(self, file, content):
        self.file = file
        self.content = content

class FileWriterUtility:
    def __init__(self, file):
        self.file = file
        self.content = ""

    def write(self, string):
        self.content += string

    def save(self):
        return Memento(self.file, self.content)

    def undo(self, memento):
        self.file = memento.file
        self.content = memento.content

class FileWriterCaretaker:
    def __init__(self):
        self.saved_states = []

    def save(self, writer):
        # Guarda solo los últimos 4 estados
        if len(self.saved_states) > 3:
            self.saved_states.pop(0)
        self.saved_states.append(writer.save())

    def undo(self, writer, state_index=0):
        if state_index < len(self.saved_states):
            writer.undo(self.saved_states[-(state_index+1)])


if __name__ == '__main__':
    os.system("clear")
    caretaker = FileWriterCaretaker()
    writer = FileWriterUtility("GFG.txt")

    writer.write("Clase de IS2 en UADER\n")
    caretaker.save(writer)

    writer.write("Material adicional de la clase de patrones\n")
    caretaker.save(writer)

    writer.write("Material adicional de la clase de patrones II\n")
    caretaker.save(writer)
    
    writer.write("Material adicional de la clase de patrones III\n")
    caretaker.save(writer)
    
    caretaker.undo(writer, 0)  # Recupera el estado más reciente, el 0 se puede poner o no
    print(writer.content + "\n\n")

    caretaker.undo(writer, 1)  # Recupera el segundo estado más reciente
    print(writer.content + "\n\n")

    caretaker.undo(writer, 2)  # Recupera el tercer estado más reciente
    print(writer.content + "\n\n")
    
    caretaker.undo(writer, 3)  # Recupera el cuarto estado más reciente
    print(writer.content + "\n\n")
