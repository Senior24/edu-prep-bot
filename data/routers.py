from handlers import commands, leaderboard, change_lang, tests

routers_list = [
    commands.router,
    tests.router,
    leaderboard.router,
    change_lang.router
]
