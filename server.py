from aiohttp import web
import datetime

TODAY = datetime.datetime.today()

def setup(app):
    app.add_routes([web.get("/api/v1/yesterday", yesterday)])


def yesterday(request):
    yesterdays_date = TODAY - datetime.timedelta(days=1)
    return web.json_response({"yesterday": yesterdays_date.strftime("%Y-%d-%m")})


if __name__ == "__main__":
    app = web.Application()
    setup(app)
    web.run_app(app, port=9999)

