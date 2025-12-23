"""
Content ingestion script for the RAG system
This script ingests book content into Qdrant for RAG retrieval
"""
import os
import asyncio
import uuid
from typing import List, Dict
from app.config import settings
from app.rag.embeddings import EmbeddingService
from qdrant_client import QdrantClient
from qdrant_client.http import models
from qdrant_client.models import PointStruct
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ContentIngestor:
    def __init__(self):
        # Initialize embedding service
        self.embedding_service = EmbeddingService()

        # Initialize Qdrant client
        if settings.QDRANT_API_KEY:
            self.qdrant_client = QdrantClient(
                url=settings.QDRANT_URL,
                api_key=settings.QDRANT_API_KEY
            )
        else:
            self.qdrant_client = QdrantClient(url=settings.QDRANT_URL)

        self.collection_name = settings.COLLECTION_NAME

    def create_collection(self):
        """Create Qdrant collection if it doesn't exist"""
        try:
            # Check if collection exists
            collections = self.qdrant_client.get_collections()
            collection_names = [c.name for c in collections.collections]

            if self.collection_name in collection_names:
                logger.info(f"Collection {self.collection_name} already exists, reusing it")
                return

            # Create collection
            self.qdrant_client.create_collection(
                collection_name=self.collection_name,
                vectors_config=models.VectorParams(
                    size=1024,  # Match Cohere embedding size
                    distance=models.Distance.COSINE
                ),
            )

            logger.info(f"Created collection: {self.collection_name}")
        except Exception as e:
            logger.error(f"Error creating collection: {str(e)}")
            raise

    def chunk_text(self, text: str, chunk_size: int = 1000, overlap: int = 100) -> List[str]:
        """Split text into overlapping chunks"""
        chunks = []
        start = 0

        while start < len(text):
            end = start + chunk_size
            chunk = text[start:end]

            # Try to break on sentence boundary if possible
            if end < len(text):
                # Look for sentence endings near the end
                for sep in ['. ', '! ', '? ', '\n']:
                    last_sep = chunk.rfind(sep)
                    if last_sep > chunk_size * 0.8:  # Only if the separator is not too early
                        chunk = text[start:start + last_sep + len(sep)]
                        end = start + last_sep + len(sep)
                        break

            chunks.append(chunk.strip())
            start = end - overlap

            # Ensure we make progress
            if start >= len(text):
                break
            if end <= start:  # Prevent infinite loop
                start += chunk_size  # Fixed: was undefined variable, using chunk_size parameter

        return chunks

    def ingest_documents(self, documents: List[Dict]):
        """Ingest documents into Qdrant"""
        logger.info(f"Starting ingestion of {len(documents)} documents...")

        points = []
        for idx, doc in enumerate(documents):
            text = doc.get('content', '')
            url = doc.get('url', '')
            title = doc.get('title', f'Document_{idx}')

            # Chunk the text
            chunks = self.chunk_text(text)

            for chunk_idx, chunk in enumerate(chunks):
                if not chunk.strip():
                    continue

                try:
                    # Generate embedding for the chunk
                    embedding = self.embedding_service.embed_text(chunk)

                    # Create Qdrant point with proper UUID
                    point_id = str(uuid.uuid4())

                    point = PointStruct(
                        id=point_id,
                        vector=embedding,
                        payload={
                            "text": chunk,
                            "url": url,
                            "title": title,
                            "doc_id": str(idx),
                            "chunk_id": chunk_idx
                        }
                    )
                    points.append(point)

                except Exception as e:
                    logger.error(f"Error processing chunk {chunk_idx} of document {idx}: {str(e)}")
                    continue

        logger.info(f"Generated {len(points)} points for ingestion")

        if points:
            # Upload to Qdrant
            self.qdrant_client.upload_points(
                collection_name=self.collection_name,
                points=points
            )

            logger.info(f"Successfully ingested {len(points)} points into {self.collection_name}")
        else:
            logger.warning("No points were generated for ingestion")

    def ingest_sample_content(self):
        """Ingest sample book content for testing"""
        sample_docs = [
            {
                "title": "Introduction to Physical AI & Humanoid Robotics",
                "url": "https://example.com/intro",
                "content": """
Physical AI & Humanoid Robotics: An Introduction

Artificial Intelligence in physical systems represents a paradigm shift from traditional AI that operates on abstract data to AI that interacts with the physical world. This book explores the intersection of AI and physical systems, with a particular focus on humanoid robotics.

Key Concepts:
- Embodied AI: AI systems that interact with the physical world
- Digital Twins: Virtual replicas of physical systems
- Sensor Fusion: Combining data from multiple sensors
- Motion Planning: Algorithms for robot movement
- Control Systems: Methods for controlling robot behavior

Humanoid robotics combines mechanical engineering, electronics, and AI to create robots that mimic human form and behavior. These systems require sophisticated algorithms to handle perception, decision-making, and action in real-time physical environments.
                """
            },
            {
                "title": "ROS 2 Architecture",
                "url": "https://example.com/ros2",
                "content": """
ROS 2 (Robot Operating System 2) is a flexible framework for writing robot software. It's a collection of tools, libraries, and conventions that aim to simplify the task of creating complex and robust robot behavior across a wide variety of robot platforms.

Core Features:
- Distributed computing
- Package management
- Message passing
- Hardware abstraction
- Device drivers
- Libraries for common robot functions

ROS 2 uses DDS (Data Distribution Service) as its underlying communication layer, providing reliable, real-time communication between nodes. Nodes in ROS 2 are organized in a graph architecture where they exchange messages via topics, services, and actions.
                """
            },
            {
                "title": "Digital Twin Simulation",
                "url": "https://example.com/digital-twin",
                "content": """
Digital twin technology creates virtual replicas of physical systems. In robotics, digital twins serve as simulation environments where robots can be tested, trained, and optimized before deployment in the real world.

Benefits:
- Reduced development time
- Safe testing environment
- Optimization before deployment
- Predictive maintenance
- Scenario testing

Unity, Gazebo, and PyBullet are popular simulation platforms for creating digital twins of robotic systems. These platforms allow for physics-based simulation, sensor simulation, and realistic environment modeling.
                """
            },
            {
                "title": "Machine Learning in Robotics",
                "url": "https://example.com/ml-robotics",
                "content": """
Machine learning has revolutionized robotics by enabling robots to learn from experience and adapt to new situations. Key applications include:

Perception: Computer vision, object recognition, scene understanding
Control: Reinforcement learning for motor control, adaptive control systems
Planning: Path planning, motion planning, task planning
Learning: Imitation learning, transfer learning, few-shot learning

Deep reinforcement learning has shown particular promise for robotic control, allowing robots to learn complex behaviors through trial and error in simulated environments before transferring to real robots.
                """
            },
            {
                "title": "Sensor Fusion and Perception",
                "url": "https://example.com/sensors",
                "content": """
Robotic perception relies on multiple sensors to understand the environment. Sensor fusion combines data from different sensors to create a coherent understanding of the world.

Common Sensors:
- Cameras: RGB, depth, thermal
- LiDAR: 3D environment mapping
- IMU: Inertial measurement for orientation
- GPS: Global positioning
- Encoders: Joint position feedback
- Force/Torque: Contact sensing

Kalman filters, particle filters, and modern deep learning approaches are used for sensor fusion, each with their own strengths depending on the application requirements.
                """
            }
        ]

        self.ingest_documents(sample_docs)

def main():
    logger.info("Starting content ingestion process...")

    ingestor = ContentIngestor()

    # Create collection if needed
    ingestor.create_collection()

    # Ingest sample content (in a real system, you'd read from your book content)
    ingestor.ingest_sample_content()

    logger.info("Content ingestion completed!")

if __name__ == "__main__":
    main()