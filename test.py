# Import client library
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

qdrant_client = QdrantClient(host='localhost', port=6333)

qdrant_client.recreate_collection(
    collection_name='startups',
    vectors_config=VectorParams(size=768, distance=Distance.COSINE),
)

