"""
Hybrid routing logic - decides between book-related and general queries
"""
from typing import List
from .schemas import QueryRequest, QueryResponse, Source
from .rag.agent import OpenRouterAgent
from .rag.retriever import QdrantRetriever
from .db.neon_client import NeonClient
from .config import settings
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class HybridRouter:
    def __init__(self):
        import logging
        logger = logging.getLogger(__name__)
        logger.info("Initializing OpenRouterAgent...")
        self.agent = OpenRouterAgent()
        logger.info("Initializing QdrantRetriever...")
        self.retriever = QdrantRetriever()
        logger.info("Initializing NeonClient...")
        self.neon_client = NeonClient()
        logger.info("NeonClient created - will connect when needed")
        logger.info("HybridRouter initialized successfully")

        self.book_keywords = [
            'robotics', 'robot', 'ai', 'artificial intelligence', 'machine learning',
            'neural networks', 'deep learning', 'computer vision', 'natural language processing',
            'humanoid', 'physical ai', 'embodied ai', 'ros', 'ros2', 'navigation',
            'motion planning', 'control systems', 'sensor fusion', 'lidar', 'imu',
            'digital twin', 'simulation', 'gazebo', 'locomotion', 'walking',
            'bipedal', 'quadruped', 'manipulation', 'grasping', 'kinematics',
            'dynamics', 'inverse kinematics', 'reinforcement learning', 'module',
            'chapter', 'section', 'intro', 'introduction', 'algorithm', 'framework',
            'architecture', 'system', 'network', 'training', 'inference'
        ]

    async def route_query(self, request: QueryRequest) -> QueryResponse:
        """
        Route the query to appropriate handler based on content
        """
        logger.info(f"Processing query: {request.query[:100]}...")
        query_type = self._classify_query(request.query)
        logger.info(f"Query classified as: {query_type}")

        if query_type == "book-related":
            logger.info("Routing to book-related handler")
            result = await self._handle_book_query(request)
        else:
            logger.info("Routing to general handler")
            result = await self._handle_general_query(request)

        logger.info(f"Query processed - Response: {result.response[:100]}..., Sources count: {len(result.sources)}, Context used: {result.context_used}")
        return result

    def _classify_query(self, query: str) -> str:
        """
        Classify query as book-related or general
        """
        query_lower = query.lower().strip()

        # Check for general conversation patterns first
        general_conversation_keywords = [
            'hi', 'hello', 'hey', 'thanks', 'thank you', 'who are you',
            'what can you do', 'help', 'how are you', 'what is this',
            'greetings', 'nice to meet you'
        ]

        # Check if query is a simple greeting/conversation starter
        for keyword in general_conversation_keywords:
            if query_lower == keyword or (len(query.split()) <= 2 and keyword in query_lower):
                return "general"

        # Check for book-related keywords
        for keyword in self.book_keywords:
            if keyword in query_lower:
                return "book-related"

        # Check for module-specific queries (e.g., "what is module 2?", "explain module 2")
        module_patterns = [
            'what is module', 'what is chapter', 'explain module', 'explain chapter',
            'module ', 'chapter ', 'section ', 'part '
        ]

        for pattern in module_patterns:
            if pattern in query_lower:
                return "book-related"

        # Check for conversational references that likely refer to book content
        conversational_indicators = [
            'this', 'that', 'it', 'the', 'topic', 'chapter', 'module', 'section',
            'book', 'content', 'text', 'reading', 'information', 'subject'
        ]

        # Check if query contains common conversational patterns with book-related indicators
        for indicator in conversational_indicators:
            if indicator in query_lower:
                # If the query is a common conversational reference, treat as book-related
                # since it likely refers to the book content we're discussing
                conversational_patterns = [
                    'this topic', 'this chapter', 'this module', 'this section',
                    'that topic', 'that chapter', 'that module', 'that section',
                    'the topic', 'the chapter', 'the module', 'the section',
                    'what is this', 'explain this', 'what about this', 'tell me about this',
                    'what does this', 'how about this', 'this?', 'that?', 'it?'
                ]

                for pattern in conversational_patterns:
                    if pattern in query_lower:
                        return "book-related"

                # If it's a very short query with just a reference, assume book-related
                if len(query.split()) <= 3 and ('?' in query or query.endswith('this') or query.endswith('that')):
                    return "book-related"

        # If no strong indicators, default to general
        return "general"

    async def _handle_book_query(self, request: QueryRequest) -> QueryResponse:
        """
        Handle book-related queries using priority routing: user → neon → qdrant → general
        Also supports combined context when beneficial
        """
        logger.info(f"Handling book-related query: {request.query[:50]}...")
        try:
            # Priority 1: User-selected text context (highest priority)
            if request.selected_text:
                logger.info("Using user-selected text context (highest priority)")
                response = self.agent.generate_response_with_context(
                    query=request.query,
                    context=request.selected_text
                )
                context_used = True
                context_source = "user"

                # Format as a source for consistency
                formatted_sources = [Source(
                    url="user-selected",
                    title="User Selected Text",
                    content=request.selected_text[:200] + "..." if len(request.selected_text) > 200 else request.selected_text,
                    score=1.0
                )]
            else:
                # Check if this is a module-specific query and handle it with Neon first
                query_lower = request.query.lower().strip()
                is_module_query = any(pattern in query_lower for pattern in [
                    'what is module', 'what is chapter', 'explain module', 'explain chapter',
                    'module ', 'chapter '
                ])

                if is_module_query:
                    # For module queries, prioritize Neon DB to get single module content
                    logger.info("Detected module-specific query, prioritizing Neon DB...")
                    neon_result = await self.neon_client.query_neon_structured_knowledge(request.query, confidence_threshold=0.3)

                    if neon_result:
                        logger.info(f"Found module-specific content from Neon DB: {neon_result.source}")
                        response = neon_result.answer
                        context_used = True
                        context_source = "neon"

                        formatted_sources = [Source(
                            url="neon-db",
                            title=neon_result.source,
                            content=neon_result.answer,
                            score=neon_result.confidence
                        )]
                    else:
                        # If no specific module content found, fall back to Qdrant
                        logger.info("No specific module content found in Neon DB, using Qdrant...")
                        qdrant_sources = self.retriever.search(request.query, top_k=3)  # Limit to 3 for shorter responses

                        if qdrant_sources and request.include_context:
                            logger.info(f"Retrieved {len(qdrant_sources)} sources from Qdrant")
                            context = self._format_context(qdrant_sources)
                            logger.info("Invoking agent with Qdrant context...")
                            response = self.agent.generate_response_with_context(
                                query=request.query,
                                context=context
                            )
                            context_used = True
                            context_source = "qdrant"
                            formatted_sources = qdrant_sources
                        else:
                            # No context found, use general knowledge
                            logger.info("No context found, using general knowledge")
                            response = self.agent.generate_general_response(request.query)
                            formatted_sources = []
                            context_used = False
                            context_source = "general"
                else:
                    # Get both Neon and Qdrant results to enable combination if beneficial
                    logger.info("Invoking Neon client to search for structured knowledge...")
                    neon_result = await self.neon_client.query_neon_structured_knowledge(request.query, confidence_threshold=0.5)

                    logger.info("Invoking Qdrant retriever to search for relevant passages...")
                    qdrant_sources = self.retriever.search(request.query, top_k=5)

                    # Check if we should combine both sources based on confidence and relevance
                    if neon_result and qdrant_sources:
                        # Both sources are available - determine if we should combine them
                        # If Neon result has high confidence, use it primarily
                        # Otherwise, combine both if beneficial
                        if neon_result.confidence >= 0.7:
                            # High confidence Neon result - use it directly
                            logger.info(f"High confidence Neon result ({neon_result.confidence}), using directly: {neon_result.source}")
                            response = neon_result.answer
                            context_used = True
                            context_source = "neon"

                            formatted_sources = [Source(
                                url="neon-db",
                                title=neon_result.source,
                                content=neon_result.answer,
                                score=neon_result.confidence
                            )]
                        else:
                            # Combine both sources for comprehensive answer
                            logger.info(f"Combining Neon and Qdrant results for comprehensive answer")
                            combined_context = f"Structured Knowledge:\n{neon_result.answer}\n\nVector Search Results:\n{self._format_context(qdrant_sources)}"

                            response = self.agent.generate_response_with_context(
                                query=request.query,
                                context=combined_context
                            )
                            context_used = True
                            context_source = "combined"

                            # Combine sources for response
                            formatted_sources = [Source(
                                url="neon-db",
                                title=neon_result.source,
                                content=neon_result.answer,
                                score=neon_result.confidence
                            )]
                            formatted_sources.extend(qdrant_sources)
                    elif neon_result:
                        # Only Neon result available
                        logger.info(f"Found structured knowledge from Neon DB: {neon_result.source}")
                        response = neon_result.answer
                        context_used = True
                        context_source = "neon"

                        formatted_sources = [Source(
                            url="neon-db",
                            title=neon_result.source,
                            content=neon_result.answer,
                            score=neon_result.confidence
                        )]
                    elif qdrant_sources and request.include_context:
                        # Only Qdrant results available
                        logger.info(f"Retrieved {len(qdrant_sources)} sources from Qdrant")
                        logger.info(f"Sources found with scores: {[f'{s.score:.3f}' for s in qdrant_sources[:3]]}")

                        context = self._format_context(qdrant_sources)
                        logger.info(f"Context formatted with length: {len(context)}")
                        logger.info("Invoking agent with Qdrant context...")
                        response = self.agent.generate_response_with_context(
                            query=request.query,
                            context=context
                        )
                        context_used = True
                        context_source = "qdrant"
                        formatted_sources = qdrant_sources
                    else:
                        # No context found or not requested, use general knowledge
                        logger.info(f"No context used - Neon found: {neon_result is not None}, Qdrant sources: {len(qdrant_sources)}, include_context: {request.include_context}")
                        response = self.agent.generate_general_response(request.query)
                        formatted_sources = []
                        context_used = False
                        context_source = "general"

            # Enforce short response length for module queries and general book queries
            response = self._enforce_short_response(response)

            # Prepare debug information if requested
            debug_info = None
            if request.debug_context:
                debug_info = {
                    "routing_trace": f"Used {context_source} source based on priority and combination logic",
                    "neon_query_performed": neon_result is not None if 'neon_result' in locals() else False,
                    "qdrant_query_performed": len(qdrant_sources) > 0 if 'qdrant_sources' in locals() else False,
                    "combined_context_used": context_source == "combined"
                }

            result = QueryResponse(
                response=response,
                sources=formatted_sources,
                query_type="book-related",
                context_used=context_used,
                context_source=context_source,
                debug_info=debug_info
            )
            logger.info(f"Book-related query handled - Sources returned: {len(result.sources)}, Context used: {result.context_used}")
            return result
        except Exception as e:
            logger.error(f"Error handling book query: {str(e)}")
            import traceback
            traceback.print_exc()
            # Fallback to general response
            logger.info("Falling back to general response...")
            response = self.agent.generate_general_response(request.query)
            # Enforce short response for fallback
            response = self._enforce_short_response(response)
            result = QueryResponse(
                response=response,
                sources=[],
                query_type="book-related",
                context_used=False,
                context_source="general"
            )
            logger.info("Fallback response generated")
            return result

    async def _handle_general_query(self, request: QueryRequest) -> QueryResponse:
        """
        Handle general queries without RAG
        """
        logger.info("Handling general query...")
        try:
            logger.info("Invoking agent for general response...")
            response = self.agent.generate_general_response(request.query)

            # Enforce short response length for general conversation
            response = self._enforce_short_response(response)

            # Prepare debug information if requested
            debug_info = None
            if request.debug_context:
                debug_info = {
                    "routing_trace": "Used general source for non-book-related query",
                    "neon_query_performed": False,
                    "qdrant_query_performed": False
                }

            result = QueryResponse(
                response=response,
                sources=[],
                query_type="general",
                context_used=False,
                context_source="general",
                debug_info=debug_info
            )
            logger.info("General query handled successfully")
            return result
        except Exception as e:
            logger.error(f"Error handling general query: {str(e)}")
            result = QueryResponse(
                response="I'm sorry, I couldn't process your request at the moment.",
                sources=[],
                query_type="general",
                context_used=False,
                context_source="general"
            )
            logger.info("General query fallback response generated")
            return result

    def _format_context(self, sources: List[Source]) -> str:
        """
        Format sources as context for the LLM
        """
        if not sources:
            return ""

        context_parts = []
        for i, source in enumerate(sources, 1):
            context_parts.append(
                f"Source {i}: {source.content}\n"
                f"URL: {source.url}\n"
                f"Score: {source.score}\n"
            )

        return "\n".join(context_parts)

    def _enforce_short_response(self, response: str) -> str:
        """
        Enforce short response length - max 5 lines
        """
        lines = response.split('\n')

        # Remove empty lines at the beginning and end
        while lines and not lines[0].strip():
            lines.pop(0)
        while lines and not lines[-1].strip():
            lines.pop()

        # If response is already 5 lines or less, return as is
        if len(lines) <= 5:
            return response

        # For longer responses, try to summarize by taking the most important parts
        # Keep the first 2-3 lines and last 1-2 lines, or just the first 5 lines
        if len(lines) > 5:
            # Take first 3 lines and last 2 lines if it makes sense, otherwise just first 5
            if len(lines) > 8:  # If it's quite long, take first 3 and last 2
                summary_lines = lines[:3] + ["..."] + lines[-2:]
                summary = "\n".join(summary_lines)
            else:  # If it's just slightly over 5, take first 5
                summary = "\n".join(lines[:5])
        else:
            summary = "\n".join(lines[:5])

        # Add a note that the response was shortened if it was too long
        if len(response.split('\n')) > 5:
            summary += "\n\n[Response shortened for clarity]"

        return summary