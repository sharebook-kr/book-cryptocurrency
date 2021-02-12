# korbit websocket connection
import websockets
import asyncio 

async def korbit_ws_client():
    uri = "wss://ws.korbit.co.kr/v1/user/push"

    async with websockets.connect(uri) as websocket: 
        greeting = await websocket.recv() 
        print(greeting)

async def main():
    await korbit_ws_client()

asyncio.run(main())