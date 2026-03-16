import asyncio
import logging
from coordinator import CoordinatorAgent

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

async def main():
    agent = CoordinatorAgent(merchant_id="merchant_999", document_url="s3://documents/acme_corp_onboarding.pdf")
    await agent.run_fsm()

if __name__ == "__main__":
    asyncio.run(main())
