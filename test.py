"""from graphiti_core import Graphiti
from graphiti_core.nodes import EpisodeType
import openai
import os
from datetime import datetime
os.environ["OPENAI_API_KEY"] = "123"

client = openai.OpenAI()
client.api_base = "http://http://172.24.191.22:4000/v1/chat/completions"
graphiti = Graphiti("bolt://localhost:7687", "neo4j", "12345678", llm_client=client)
# Initialize the graph database with graphiti's indices. This only needs to be done once.
episodes = [
    "Kamala Harris is the Attorney General of California. She was previously "
    "the district attorney for San Francisco.",
    "As AG, Harris was in office from January 3, 2011 – January 3, 2017",
]
for i, episode in enumerate(episodes):
    graphiti.add_episode(
        name=f"Freakonomics Radio {i}",
        episode_body=episode,
        source=EpisodeType.text,
        source_description="podcast",
        reference_time=datetime.now()
    )"""

import asyncio
from graphiti_core import Graphiti
from graphiti_core.nodes import EpisodeType
import os
from datetime import datetime
os.environ["OPENAI_API_KEY"] = "sk-1234"

# Initialize the Graphiti client
graphiti = Graphiti("bolt://localhost:7687", "neo4j", "12345678")

# Define an asynchronous function to build indices and constraints
async def initialize_graphiti():
    """
    episodes = [
        "Kamala Harris is the Attorney General of California. She was previously "
        "the district attorney for San Francisco.",
        "As AG, Harris was in office from January 3, 2011 – January 3, 2017",
    ]
    for i, episode in enumerate(episodes):
        await graphiti.add_episode(
            name=f"Freakonomics Radio {i}",
            episode_body=episode,
            source=EpisodeType.text,
            source_description="podcast",
            reference_time=datetime.now()
        )"""
    results = await graphiti.search('When was Kamala in Office?')
    print(results[0].fact)

# Run the asynchronous function
if __name__ == "__main__":
    asyncio.run(initialize_graphiti())


    