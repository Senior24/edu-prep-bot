from handlers import commands, leaderboard, change_lang, tests, host_test

routers_list = [
    commands.router,
    tests.router,
    leaderboard.router,
    change_lang.router,
    host_test.router
]
