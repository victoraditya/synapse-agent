import asyncio
import json
import logging
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException, Security
from pydantic import BaseModel
from typing import Dict, Any

from coordinator import CoordinatorAgent
from security import verify_api_key

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Project Synapse API", version="1.0.0")

# In-memory session tracking for the Bidi-Streaming
active_sessions: Dict[str, WebSocket] = {}

class OnboardingRequest(BaseModel):
    merchant_id: str
    document_url: str

@app.get("/")
async def root():
    return {"status": "ok", "service": "Synapse Agent Engine"}

@app.post("/api/v1/onboard")
async def start_onboarding(request: OnboardingRequest, api_key: str = Security(verify_api_key)):
    """
    Kicks off the autonomous onboarding FSM process
    """
    coordinator = CoordinatorAgent(request.merchant_id, request.document_url)
    
    # Run the FSM asynchronously in the background so we don't block the API
    asyncio.create_task(coordinator.run_fsm())
    
    return {
        "status": "accepted",
        "merchant_id": request.merchant_id,
        "message": "Onboarding FSM started. Monitor progress via /live websocket."
    }

@app.websocket("/live")
async def websocket_endpoint(websocket: WebSocket):
    """
    Bidi-Streaming endpoint for Human-in-the-Loop Voice Barge-in.
    Connects to Gemini Live API to interpret spoken interruptions.
    """
    await websocket.accept()
    session_id = str(id(websocket))
    active_sessions[session_id] = websocket
    logger.info(f"New Live Session connected: {session_id}")

    try:
        while True:
            # We would normally stream this audio buffer directly to Gemini Live API
            # using google-genai SDK's async websocket client here.
            data = await websocket.receive_text()
            
            # Simulated handle of human barge-in
            if "barge-in" in data.lower() or "stop" in data.lower():
                logger.warning(f"HUMAN BARGE-IN DETECTED on session {session_id}. Pausing Coordinator.")
                await websocket.send_text(json.dumps({"event": "system_paused", "message": "Coordinator Agent paused for human review."}))
            else:
                await websocket.send_text(json.dumps({"event": "audio_ack", "message": "Audio chunk received"}))
                
    except WebSocketDisconnect:
        logger.info(f"Live Session {session_id} disconnected")
        del active_sessions[session_id]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
