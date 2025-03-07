from aiohttp import web


async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        logger.info("client data")
        if msg.type == aiohttp.WSMsgType.TEXT:
            await ws.send_str(msg.data)
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print("ws connection closed with exception %s" % ws.exception())

    logger.info("websocket connection closed")

    return ws


app.add_routes(
    [
        web.get("/ws", websocket_handler),
    ]
)

web.run_app(app, port=8080)
