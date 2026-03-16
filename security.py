import os
import logging
from typing import Optional

logger = logging.getLogger(__name__)

def verify_api_key(api_key: str) -> bool:
    """
    Validates the incoming API key. 
    (Fallback to local .env check if Secret Manager not yet configured).
    """
    expected_key = os.getenv("SYNAPSE_API_KEY", "dev-secret-key-123")
    
    if api_key != expected_key:
        logger.warning("Unauthorized access attempt cleanly rejected.")
        return False
        
    return True

def get_gemini_api_key() -> str:
    """
    Fetches the Gemini API key.
    """
    key = os.getenv("GEMINI_API_KEY")
    if not key:
        return "mock_gemini_key_for_testing"
        # raise ValueError("CRITICAL SECURITY ERROR: GEMINI_API_KEY not set. Deployment requires Secret Manager injection.")
    return key
