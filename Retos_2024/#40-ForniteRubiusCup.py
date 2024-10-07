""" /*
* EJERCICIO:
 * ¡Rubius tiene su propia skin en Fortnite!
 * Y va a organizar una competición para celebrarlo.
 * Esta es la lista de participantes:
 * https: // x.com/Rubiu5/status/1840161450154692876
 *
 * Desarrolla un programa que obtenga el número de seguidores en
 * Twitch de cada participante, la fecha de creación de la cuenta
 * y ordene los resultados en dos listados.
 * - Usa el API de Twitch: https: // dev.twitch.tv/docs/api/reference
 *   (NO subas las credenciales de autenticación)
 * - Crea un ranking por número de seguidores y por antigüedad.
 * - Si algún participante no tiene usuario en Twitch, debe reflejarlo.
 */
 """

""" >> > from operator import itemgetter
>> > L = [[0, 1, 'f'], [4, 2, 't'], [9, 4, 'afsd']]
>> > sorted(L, key=itemgetter(2))
[[9, 4, 'afsd'], [0, 1, 'f'], [4, 2, 't']] """


from operator import itemgetter
from twitchAPI.twitch import Twitch
from twitchAPI.helper import first
import asyncio
import requests
import json
from prettytable import PrettyTable
CLIENT_ID = 'Crealo en twitch'
CLIENT_SECRET = 'Crealo en twitch'
AUTH = 'Crealo en twitch'

URL = 'https://api.twitch.tv/helix/users?login='
URL_FOLLOWERS = 'https://api.twitch.tv/helix/channels/followers?broadcaster_id='
authURL = 'https://id.twitch.tv/oauth2/token'
Client_ID = CLIENT_ID
Secret = CLIENT_SECRET

AutParams = {'client_id': Client_ID,
             'client_secret': Secret,
             'grant_type': 'client_credentials'
             }
streamers = ["abby", "ache", "adricontreras", "agustin", "alexby", "ampeter", "ander",
             "arigameplays", "arigeli", "auronplay", "axozer", "beniju", "bycarlitos",
             "byviruzz", "carrera", "celopan", "cheeto", "crystalmolly", "darioemehache",
             "dheylo", "djmariio", "doble", "elvisa", "elyas360", "folagor", "thegrefg", "guanyar",
             "hika", "hiper", "ibai", "ibelky", "illojuan", "imantado", "irinaisasia", "jesskiu",
             "jopa", "jordiwild", "kenaisouza", "keroro", "kiddkeo", "kikorivera", "knekro", "koko",
             "kronnozober", "leviathan", "litkillah", "lolalolita", "lolito", "luh", "luzu",
             "mangel", "mayichi", "melo", "missasinfonia", "mixwell", "jaggerprincesa", "nategentile7",
             "nexxuz", "nia", "nilojeda", "nissaxter", "ollie", "orslok", "outconsumer", "papigavitv",
             "paracetamor", "patica1999", "paulagonu", "pausenpaii", "perxitaa", "nosoyplex", "polispol1",
             "quackity", "recuerdop", "revenant", "rivers", "robertpg", "roier", "rojuu", "rubius",
             "shadoune666", "silithur", "spok_sponha", "spreen", "spursito", "bystaxx", "suzyroxx",
             "vicens", "vituber", "werlyb", "xavi", "xcry", "elxokas", "thezarcort", "zeling", "zormanworld"]

streamers_results = []


def Check(streamer: str):

    results = []
    streamer_id = ''
    created_at = ''
    streamer_followers = ''

    AutCall = requests.post(url=authURL, params=AutParams)
    access_token = AutCall.json()['access_token']

    head = {
        'Client-ID': Client_ID,
        'Authorization':  "Bearer " + access_token
    }

    # Get Streamer ID y created date
    URL_ID_STREAMER = URL + streamer
    r = requests.get(URL_ID_STREAMER, headers=head).json()['data']

    if r:
        r = r[0]
        if r['id'] != ' ' and r['created_at'] != ' ':
            streamer_id = r['id']
            created_at = r['created_at']
        else:
            streamer_id = 'No es streamer'

    else:
        streamer_id = 'No es streamer'

    # Get Followers
    URL_FOLLOW = URL_FOLLOWERS + streamer_id
    x = requests.get(URL_FOLLOW, headers=head).json()

    if x:
        x = x['total']
        if x != ' ':
            streamer_followers = x
        else:
            streamer_followers = 'No es streamer'
    else:
        streamer_followers = 'No es streamer'

    results.append(streamer)
    results.append(streamer_followers)
    results.append(created_at[0:10])
    streamers_results.append(results)


def rubius_cup():

    for participant in streamers:
        Check(participant)

    # Ranking by followers
    ranking_followers = sorted(
        streamers_results, key=itemgetter(1), reverse=True)

    print("Ranking por seguidores")
    for x in range(10):
        print(
            f"{x+1}:{ranking_followers[x][0]},{ranking_followers[x][1]}")

    print("-------------------------------------------------------------")
    # Ranking by create date
    ranking_date = sorted(
        streamers_results, key=itemgetter(2))

    print("Ranking por antigüedad")
    for x in range(10):
        print(
            f"{x+1}:{ranking_date[x][0]},{ranking_date[x][2]}")


def main():

    rubius_cup()


if __name__ == "__main__":
    main()
