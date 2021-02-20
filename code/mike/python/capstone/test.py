# fuction to pull call of duty user stats
def cod_stats():
    platform = input('What platform is the user? (pc/ps4/xbox): ').lower()
    username = input('Enter Call of Duty Username: ')
    if platform == 'pc':
        username = username.replace('#', '%23')
    stats = f'https://codstats.net/warzone/profile/{platform}/{username}'
    return stats


print(cod_stats())