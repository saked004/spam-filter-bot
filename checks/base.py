from abc import ABC, abstractmethod

class Check(ABC):
    @abstractmethod
    def is_flagged(self, message) -> bool:
        """Abstract method to be implemented by all checks."""
        pass
