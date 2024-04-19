from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

class Handler(ABC):
    """
    The Handler interface declares a method for building the chain of handlers.
    It also declares a method for executing a request.
    """

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    """
    The default chaining behavior can be implemented inside a base handler
    class.
    """

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        # Returning a handler from here will let us link handlers in a
        # convenient way like this:
        # monkey.set_next(squirrel).set_next(dog)
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None
    
class PrimoHandler(AbstractHandler):
    def es_primo(self, number):
        if number < 2:
            return False
        for i in range(2, number):
            if number % i == 0:
                return False
        return True
    
    def handle(self, number: Any) -> str:
        
        if self.es_primo(number):
            return f"PrimoHandler consumió el número {number}"
        else:
            return super().handle(number)
        
class ParHandler(AbstractHandler):
    def handle(self, number: Any) -> str:
        if number % 2 == 0:
            return f"ParHandler consumió el número {number}"
        else:
            return super().handle(number) # Figura en consola como 'None'
        
def client_code(handler: Handler) -> None:
    """
    The client code is usually suited to work with a single handler. In most
    cases, it is not even aware that the handler is part of a chain.
    """
    
    for number in range(1, 101):
        print(handler.handle(number))
        


primo = PrimoHandler()
par = ParHandler()

primo.set_next(par)

client_code(primo) 
    