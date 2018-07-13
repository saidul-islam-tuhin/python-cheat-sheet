"""
There are three way we can return multiple value from function.
    1. By List : return ['saidul islam', 'tuhin']
    2. By Tuple: return ('saidul islam', 'tuhin')
    3. By Dictionary(best practice ): return {'full_name':'saidul islam', 'nick_name':'tuhin'}
"""

def full_nick_name(full_name, nick_name):
    """ Return full name and nick name by dictionary """

    dic_data = {
        'full_name': full_name.title(),
        'nick_name': nick_name.upper(),
    }

    return dic_data

user_name = full_nick_name('saidul islam', 'tuhin')

print('Full name: ', user_name['full_name'])
print('Nick name: ', user_name['nick_name'])
