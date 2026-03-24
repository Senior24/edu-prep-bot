from handlers import commands, leaderboard, change_lang

routers_list = [
    commands.router,
    leaderboard.router,
    change_lang.router
]
