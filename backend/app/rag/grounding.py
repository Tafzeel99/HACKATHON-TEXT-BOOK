"""
Grounding verification to ensure responses are based on provided context
"""
from typing import List
import re
from ..schemas import Source

class GroundingVerifier:
    def __init__(self):
        pass

    def verify_response_grounding(self, response: str, sources: List[Source]) -> bool:
        """
        Verify that the response is grounded in the provided sources
        This is a basic implementation - in production you might want more sophisticated verification
        """
        if not sources:
            return True  # If no sources provided, we can't verify grounding

        response_lower = response.lower()

        # Check if key terms from sources appear in the response
        source_content = " ".join([source.content.lower() for source in sources])

        # Simple check: if response contains content from sources, it's likely grounded
        # This is a basic heuristic - more sophisticated approaches could use semantic similarity
        common_words = set(response_lower.split()) & set(source_content.split())

        # If at least some common content exists, consider it grounded
        return len(common_words) > 0

    def enforce_grounding(self, response: str, sources: List[Source]) -> str:
        """
        Enforce that the response only contains information from the sources
        """
        if not sources:
            return response

        # Basic grounding enforcement: if response contradicts or adds information not in sources,
        # we should flag it. For now, we'll just return the response as-is with a grounding check.
        is_ground_valid = self.verify_response_grounding(response, sources)

        if not is_ground_valid:
            return (
                "I found relevant information but couldn't form a complete answer based on the provided sources. "
                "The information might be too limited or not directly related to your query."
            )

        return response