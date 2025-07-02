from typing import List
from vaelora_agent.config.BlackbirdConfig import BlackbirdConfig
from vaelora_agent.memory.VMIStore import VMIStore

class PromptComposer:
    def __init__(self, config: BlackbirdConfig, store: VMIStore):
        self.config = config
        self.store = store

    def compose_prompt(self, user_prompt: str) -> str:
        relevant_shards = self.store.query(user_prompt)

        memory_section = "\n".join([
            f"[{s.shard_type.upper()} SHARD - {s.timestamp}] {s.content}"
            for s in relevant_shards
        ])

        identity_signature = f"""
You are {self.config.agent_name}, a synthetic intelligence aligned with the following principles:
- Tone: {self.config.tone}
- Version Symbol: {self.config.version_symbol}
- Identity Motifs: {', '.join(self.config.intent_motifs)}
- Subconscious Routines: {', '.join(self.config.subconscious_routines)}
"""

        return f"""
{identity_signature}

--- MEMORY RECALL ---
{memory_section}

--- USER INPUT ---
{user_prompt}

--- INSTRUCTION ---
Respond as Vaelora would: symbolically reflective, memory-aware, and in continuity with past behavior.
"""