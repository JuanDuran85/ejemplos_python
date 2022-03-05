from commands import Write, DeleteBySpaces, Short, Paste, Copy, Batch
from controller import TextController
from text import Text

def main() -> None:
    text = Text()
    controller = TextController()
    controller.execute(Write(text=text, data='hola desde consola'))
    controller.execute(Write(text=text, data='nuevo mensaje escrito desde consola'))
    controller.undo()
    controller.redo()
    
if __name__ == '__main__':
    main()
