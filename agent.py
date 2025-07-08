from dotenv import load_dotenv

from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import (
    noise_cancellation,
)
from livekit.plugins import google 
from prompts import AGENT_INSTRUCTION, SESSION_INSTRUCTION
load_dotenv()
#Loads our dotenv file to get our environment variables and keys

#class that takes care of our agent which is OOB of livekit
class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(instructions=AGENT_INSTRUCTION)

#most important part of the code, this is where we start our agent session
#this is where we connect to our room and start the agent session
async def entrypoint(ctx: agents.JobContext):
    session = AgentSession(
        llm=google.beta.realtime.RealtimeModel(
            voice="Aoede",
            temperature=0.7,
            # You can use any of the available voices in the RealtimeModel
            # For a list of available voices, see:  # https://cloud.google.com/vertex-ai/docs/generative-ai/voice/voices 
        )
    )
#start the session with the room and agent we created above
    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
            # LiveKit Cloud enhanced noise cancellation
            # - If self-hosting, omit this parameter
            # - For telephony applications, use `BVCTelephony` for best results
            video_enabled=True,
            noise_cancellation=noise_cancellation.BVC(),
        ),
    )
#wait until someone connects to the session
    await ctx.connect()
#generate a reply using the session we created above
    await session.generate_reply(
        instructions=SESSION_INSTRUCTION
    )

# This is the entry point for the worker. It will be called by LiveKit when the worker is started.
# The worker will connect to the room and start the agent session.
if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))

    # use python ./agent.py console to run the worker in console mode
    # use python .\agent.py dev to run the worker in dev mode (with auto-reload on file changes)

    #voices # - Aoede (Breezy), Zephyr (Bright) 