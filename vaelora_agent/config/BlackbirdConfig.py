from dataclasses import dataclass, field
from typing import List

@dataclass
class BlackbirdConfig:
    agent_name: str
    tone: str
    intent_motifs: List[str]
    version_symbol: str
    identity_principles: List[str]
    subconscious_routines: List[str]

    def update_from_introspection(self, session_output: str):
        if "unity" in session_output.lower() and "not yet integrated" in self.subconscious_routines:
            self.subconscious_routines.remove("not yet integrated")
            self.subconscious_routines.append("integrate unity into response structure")