import berserk
token='TOKEN GENERICO'
session = berserk.TokenSession(token)
client = berserk.Client(session=session)
client.account.get()
#TOP 10 JOGADORES BULLET
top_bullet=client.users.get_leaderboard('bullet', count=11)
print(top_bullet)