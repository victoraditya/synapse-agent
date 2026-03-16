import logging
import json
from typing import Dict, Any

logger = logging.getLogger(__name__)

class MemoryManager:
    """
    Hybrid Memory Architecture to store Process State.
    """
    def __init__(self, mode: str = "local"):
        self.mode = mode
        # In-memory mock for local dev ($0 cost)
        self._short_term: Dict[str, Any] = {}
        self._long_term: Dict[str, Any] = {}
        
        if self.mode == "cloud":
            # Initialize Firestore and Upstash Redis here
            pass

    async def save_short_term(self, session_id: str, key: str, value: Any):
        """
        Saves ephemeral UI interaction state (e.g. current DOM coordinates).
        Uses Redis or local dict.
        """
        if session_id not in self._short_term:
            self._short_term[session_id] = {}
        self._short_term[session_id][key] = value
        logger.debug(f"[Short-Term Memory] Saved '{key}' for session {session_id}")

    async def get_short_term(self, session_id: str, key: str) -> Any:
        return self._short_term.get(session_id, {}).get(key)

    async def save_long_term(self, merchant_id: str, state: Dict[str, Any]):
        """
        Saves authoritative Phase state.
        Uses Google Cloud Firestore or local dict.
        """
        self._long_term[merchant_id] = state
        logger.info(f"[Long-Term Memory] Committed Phase State for {merchant_id}")

    async def get_long_term(self, merchant_id: str) -> Dict[str, Any]:
        return self._long_term.get(merchant_id, {})

# Singleton instance for the app
memory = MemoryManager(mode="local")
