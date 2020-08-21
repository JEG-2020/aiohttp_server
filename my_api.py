from aiohttp import web
import datetime

TODAY = datetime.datetime.today()

def setup(app):
    app.add_routes([web.get("/api/v1/yesterday", yesterday)])
    app.add_routes([web.get("/api/v1/ago/{n}", days_ago)])

def yesterday(request):
    yesterdays_date =  "2020-20-08"
    return web.json_response({"yesterday": yesterdays_date})

def days_ago(request):
    days = int(request.match_info['n'])
    days_ago_date = TODAY - datetime.timedelta(days=days)
    return web.Response(text=f"{days} days ago was {days_ago_date.strftime('%A %B %dth %Y')}")


if __name__ == "__main__":
    app = web.Application()
    setup(app)
    web.run_app(app, port=9999)

