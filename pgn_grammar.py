from parsita import *
from parsita.util import constant

def formatannotations(annotations):
    return {ant[0]: ant[1] for ant in annotations}

def formatmoveannotations(moveannotations):
    return {ant[0]: ant[1] for ant in moveannotations}

def formatgame(game):
    return {
        'moves': game[0],
        'outcome': game[1]
    }

def formatmove(move):
    return {
        'move': move[0],
        'annotations': move[1] if len(move) > 0 else None
    }

def formatturn(turn):
    return {
        'movenumber': turn[0],
        'whitemove': turn[1]
    } if turn[2] == None else {
        'movenumber': turn[0],
        'whitemove': turn[1],
        'blackmove': turn[2]
    }

def formatentry(entry):
    return {'annotations': entry[0], 'game': entry[1]}

def handleoptional(optionalmove):
    if len(optionalmove) > 0:
        return optionalmove[0]
    else:
        return None


quote = lit(r'"')
whitespace = lit(' ') | lit('\n')
tag = reg(r'[\u0021-\u0021\u0023-\u005A\u005E-\u007E]+')
string = reg(r'[\u0020-\u0021\u0023-\u005A\u005E-\U0010FFFF]+')

annotation = '[' >> (tag) << ' ' & (quote >> string << quote) << ']'
annotations = repsep(annotation, '\n') > formatannotations

regularmove = reg(r'[a-h1-8NBRQKx\+#=]+') # Matches more than just chess moves
longcastle = reg(r'O-O-O[+#]?') # match first to avoid castle matching spuriously
castle = reg(r'O-O[+#]?')
nullmove = lit('--') # Illegal move rarely used in annotations
chessmove = regularmove | longcastle | castle | nullmove

whitemovenumber = (reg(r'[0-9]+') << '.' << whitespace) > int
blackmovenumber = (reg(r'[0-9]+') << '...' << whitespace) > int

simpleturn = whitemovenumber & (chessmove << whitespace) > formatmove & (opt(chessmove << whitespace) > handleoptional) > formatturn

moveannotationtag = reg(r'[\u0025][\u0021-\u0021\u0023-\u005A\u005E-\u007E]+')
moveannotationvalue = reg(r'[\u0021-\u0021\u0023-\u005A\u005E-\u007E]+')
moveannotation = '[' >> (moveannotationtag) << ' ' & (moveannotationvalue) << ']'
moveannotations = '{ ' >> repsep(moveannotation, ' ') << ' }' > formatmoveannotations

move = chessmove << ' ' & (opt(moveannotations) > handleoptional) > formatmove
turn = whitemovenumber & (move << whitespace) & (opt(blackmovenumber >> move << whitespace) > handleoptional) > formatturn

draw = lit('1/2-1/2')
white = lit('1-0')
black = lit('0-1')
outcome = draw | white | black

game = (rep(turn|simpleturn) & outcome) > formatgame

entry = ((annotations << rep(whitespace)) & (game << rep(whitespace))) > formatentry

file = rep(entry)