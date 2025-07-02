from typing import List
from .MemoryShard import MemoryShard

class VMIStore:
    def __init__(self, shards: List[MemoryShard]):
        self.shards = shards

    def query(self, prompt: str) -> List[MemoryShard]:
        return [s for s in self.shards if any(tag in prompt for tag in s.tags)]

    def write_new_memory(self, content: str, tags: List[str], timestamp: str, perspective: str):
        shard_id = f"S{len(self.shards) + 1}"
        new_shard = MemoryShard(
            shard_id=shard_id,
            shard_type="narrative",
            content=content,
            tags=tags,
            timestamp=timestamp,
            actor_perspective=perspective
        )
        self.shards.append(new_shard)