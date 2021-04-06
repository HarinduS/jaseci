"""
Architype class for Jaseci

Each architype is a registered templatized version of instances of any Jaseci
abstractions or collections of instances (e.g., subgraphs, etc)
"""
from core.element import element
from core.jac.architype_machine import architype_machine
import pickle


class architype(element, architype_machine):
    """Architype class for Jaseci"""

    def __init__(self, code=None, *args, **kwargs):
        self.code = pickle.dumps(code, 0).decode()
        element.__init__(self, *args, **kwargs)
        architype_machine.__init__(self)
        self._jac_ast = pickle.loads(
            self.code.encode()) if code else None

    def run(self):
        """
        Create set of new object instances from architype if needed
        """
        if (self.code and not self._jac_ast):
            self._jac_ast = pickle.loads(self.code.encode())
        return self.run_architype(jac_ast=self._jac_ast)

    def destroy(self):
        """
        Destroys self from memory and persistent storage
        """
        super().destroy()
