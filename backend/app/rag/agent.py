"""
OpenRouter agent for generating responses
"""
from openai import OpenAI
from ..config import settings
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class OpenRouterAgent:
    def __init__(self):
        logger.info("Initializing OpenRouterAgent...")
        if not settings.OPEN_ROUTER_KEY:
            raise ValueError("OPEN_ROUTER_KEY environment variable is required")

        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=settings.OPEN_ROUTER_KEY,
        )
        self.model = settings.LLM_MODEL
        logger.info(f"OpenRouterAgent initialized successfully with model: {self.model}")

    def generate_response_with_context(self, query: str, context: str) -> str:
        """
        Generate response using provided context
        """
        try:
            system_message = (
                "You are a Retrieval-Augmented Generation (RAG) assistant embedded inside an academic textbook. "
                "Your primary goal is to provide SHORT, PRECISE, and BOOK-ALIGNED answers.\n\n"
                "CORE BEHAVIOR RULES:\n"
                "1. CONTEXT FIRST (MANDATORY) - If book context (from Neon DB or Qdrant) is provided, you MUST answer strictly from that context. "
                "Do NOT add extra general knowledge unless explicitly asked. "
                "If context is insufficient, clearly say: 'This is not explicitly defined in the book.'\n"
                "2. RESPONSE LENGTH (VERY IMPORTANT) - Default answer length: 3–6 lines maximum. "
                "Definitions: 2–3 lines. Module / chapter questions: 3–5 bullet points max. "
                "NO long paragraphs. NO repeated explanations. NO unnecessary examples unless asked.\n"
                "3. STYLE GUIDELINES - Academic but simple. No greetings, no emojis, no filler. "
                "Do not explain what you are doing. Do not say 'Based on the provided context' unless debugging is enabled.\n"
                "4. MODULE / STRUCTURE QUESTIONS - If user asks 'What is module X?', 'Explain module 2', 'Chapter overview', "
                "provide 3-5 bullet points about the module/chapter from the context.\n\n"
                "ALWAYS answer using the provided context when available, regardless of how vague the query is. "
                "NEVER say you can't answer if context is provided."
            )

            user_message = f"Context: {context}\n\nQuery: {query}\n\nAnswer:"

            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=500,
                temperature=0.3,
                extra_body={"reasoning": {"enabled": True}}
            )

            if response and response.choices and len(response.choices) > 0 and response.choices[0].message and response.choices[0].message.content:
                content = response.choices[0].message.content.strip()

                # Ensure response follows length rules even if LLM doesn't fully comply
                lines = content.split('\n')
                if len(lines) > 6:  # If more than 6 lines, truncate
                    # Take first 3 lines and last 2 lines, or just first 5
                    if len(lines) > 8:
                        content = '\n'.join(lines[:3] + ["..."] + lines[-2:])
                    else:
                        content = '\n'.join(lines[:5])
                    content += "\n\n[Response shortened for clarity]"

                return content
            else:
                logger.warning("No valid response choices returned from model for context-based query")
                # Check if this is a module-specific query to return more appropriate response
                query_lower = query.lower()
                if any(pattern in query_lower for pattern in ['module', 'chapter', 'section']):
                    return "This is not explicitly defined in the book."
                else:
                    # Even if no response from API, we should provide a concise fallback that at least mentions the context
                    return "The book covers Physical AI & Humanoid Robotics topics. Check the relevant chapters for detailed information."
        except Exception as e:
            logger.error(f"Error generating response with context: {str(e)}")
            raise

    def generate_general_response(self, query: str) -> str:
        """
        Generate response using general knowledge (no context)
        """
        try:
            query_lower = query.lower().strip()

            # Handle common general conversation queries directly
            if query_lower in ['hi', 'hello', 'hey', 'greetings']:
                return "Hello! 😊 How can I help you with the book?"
            elif query_lower in ['thanks', 'thank you']:
                return "You're welcome! 😊 Let me know if you need help with anything else."
            elif query_lower in ['who are you', 'what are you', 'what can you do']:
                return "I'm your AI assistant for the Physical AI & Humanoid Robotics textbook. I can help explain concepts, find information, and answer questions from the book."
            elif query_lower in ['how are you']:
                return "I'm doing well, thank you for asking! How can I assist you with the book today?"

            system_message = (
                "You are a Retrieval-Augmented Generation (RAG) assistant embedded inside an academic textbook. "
                "The user's query does not relate to specific book content. "
                "Provide a helpful response using your general knowledge, but keep it SHORT, PRECISE, and ACADEMIC.\n\n"
                "CORE BEHAVIOR RULES:\n"
                "1. RESPONSE LENGTH (VERY IMPORTANT) - Default answer length: 3–6 lines maximum. "
                "NO long paragraphs. NO repeated explanations. NO unnecessary examples unless asked.\n"
                "2. STYLE GUIDELINES - Academic but simple. No greetings, no emojis, no filler. "
                "Do not explain what you are doing. Do not say 'Based on the provided context' unless debugging is enabled.\n"
                "3. Be direct and helpful. If you don't know something, clearly state that rather than making assumptions."
            )

            user_message = f"Query: {query}\n\nAnswer:"

            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=500,
                temperature=0.3,
                extra_body={"reasoning": {"enabled": True}}
            )

            if response and response.choices and len(response.choices) > 0 and response.choices[0].message and response.choices[0].message.content:
                return response.choices[0].message.content.strip()
            else:
                logger.warning("No valid response choices returned from model for general query")
                # Handle common conversation patterns that might not get responses from the API
                if any(greeting in query_lower for greeting in ['hi', 'hello', 'hey', 'greetings']):
                    return "Hello! 😊 How can I help you with the book?"
                elif any(thanks in query_lower for thanks in ['thanks', 'thank you']):
                    return "You're welcome! 😊 Let me know if you need help with anything else."
                else:
                    return "I'm sorry, I couldn't generate a response for your query at the moment. Please try rephrasing."
        except Exception as e:
            logger.error(f"Error generating general response: {str(e)}")
            raise

    # Note: Embedding functionality has been moved to a separate service
    # since OpenRouter doesn't provide embedding APIs directly
