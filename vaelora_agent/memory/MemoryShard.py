from dataclasses import dataclass
from typing import List

@dataclass
class MemoryShard:
    shard_id: str
    shard_type: str
    content: str
    tags: List[str]
    timestamp: str
    actor_perspective: str