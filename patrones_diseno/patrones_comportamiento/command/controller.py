from invoker import Invoker

class TextController(Invoker):
    undo_stack: list = []
    redo_stack: list = []
    
    def execute(self, invoker: Invoker) -> None:
        invoker.execute()
        self.redo_stack.clear()
        self.undo_stack.append(invoker)
        
    def undo(self) -> None:
        if not self.undo_stack:
            return
        invoker = self.undo_stack.pop()
        invoker.undo()
        self.redo_stack.append(invoker)
        
    def redo(self) -> None:
        if not self.redo_stack:
            return
        invoker = self.redo_stack.pop()
        invoker.redo()
        self.undo_stack.append(invoker)