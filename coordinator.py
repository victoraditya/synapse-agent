import asyncio
import logging
from memory import memory
from navigator import NavigatorAgent

logger = logging.getLogger(__name__)

class CoordinatorAgent:
    """
    The 'Brain' of Project Synapse.
    An Asynchronous Finite State Machine (FSM) that dictates the workflow.
    """
    def __init__(self, merchant_id: str, document_url: str, broadcast_callback=None):
        self.merchant_id = merchant_id
        self.document_url = document_url
        self.state = "INIT"
        self.merchant_data = {}
        self.broadcast_callback = broadcast_callback
        
    async def _log_and_broadcast(self, msg: str):
        logger.info(msg)
        if self.broadcast_callback:
            await self.broadcast_callback(msg)

    async def run_fsm(self):
        """
        Main Event Loop for the agent FSM.
        """
        await self._log_and_broadcast(f"Starting Onboarding FSM for Merchant: {self.merchant_id}")
        
        try:
            await self.phase_1_extraction()
            await self.phase_2_risk_analysis()
            await self.phase_3_ui_entry()
            
            self.state = "COMPLETED"
            await memory.save_long_term(self.merchant_id, {"status": self.state, "data": self.merchant_data})
            await self._log_and_broadcast("Onboarding FSM Completed Successfully.")
            
        except Exception as e:
            self.state = "FAILED"
            logger.error(f"FSM Failed during phase {self.state}: {str(e)}")
            await memory.save_long_term(self.merchant_id, {"status": self.state, "error": str(e)})

    async def phase_1_extraction(self):
        """
        Phase 1: Download document, run OCR, use Gemini to extract structured JSON.
        """
        self.state = "PHASE_1_EXTRACTION"
        await self._log_and_broadcast(f"[{self.state}] Downloading and extracting {self.document_url}...")
        
        # Simulate processing time
        await asyncio.sleep(1.5)
        
        # Mock Extracted Data
        self.merchant_data = {
            "name": "Acme Corp LLC",
            "tax_id": "12-3456789",
            "business_type": "Retail"
        }
        await memory.save_short_term(self.merchant_id, "extracted_raw", self.merchant_data)

    async def phase_2_risk_analysis(self):
        """
        Phase 2: Review extracted data against risk policies.
        """
        self.state = "PHASE_2_RISK_ANALYSIS"
        await self._log_and_broadcast(f"[{self.state}] Analyzing data for Risk compliance...")
        
        await asyncio.sleep(1)
        
        # Mock Risk Analysis Result
        self.merchant_data["risk_score"] = 14  # Low risk
        self.merchant_data["approved"] = True

    async def phase_3_ui_entry(self):
        """
        Phase 3: Safely hand over control to the multimodal 'Eyes' to interact with the legacy ERP.
        """
        self.state = "PHASE_3_UI_ENTRY"
        await self._log_and_broadcast(f"[{self.state}] Delegating to Navigator Agent for ERP entry...")
        
        # Instantiate the Navigator pointing at our mock ERP
        target_url = "http://localhost:8080/mock_erp.html"  # In a real environment, this would be a remote ERP IP
        navigator = NavigatorAgent(target_url)
        
        actions = await navigator.analyze_form_and_fill(self.merchant_data)
        await navigator.execute_actions(actions)
