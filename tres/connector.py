from abc import ABC, abstractmethod

from tres.models import AnalysisInput, Finding


class Connector(ABC):
    
    @abstractmethod
    def collect(self, analysis_input: AnalysisInput) -> list[Finding]:
        """Collect findings from a specific source."""
        raise NotImplementedError