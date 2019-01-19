#TODO
    # - properly implement the built in intents
import json
import challonge

USER = "haydunce" 
KEY = "yCYu1uKVX10iNrRh5vJfy48ReZC2iQ0Kchi4xzMs"
TOURNAMENT_NAME = "HackAZ"

challonge.set_credentials(USER, KEY)
tournament = challonge.tournaments.show(TOURNAMENT_NAME)
participants = challonge.participants.index(tournament["id"])
matches = challonge.matches.index(tournament["id"])

#Custom Intents Functions
#-------------------------------------------------------
def start_tournament():
    global tournament
    challonge.tournaments.start(tournament["id"])
    return "The tournament has started"

def get_num_participants():
    global participants
    return len(participants)

def get_participant(id):
    global participants
    for p in (participants):
        if p['id'] == id:
            return p['name']
    return null

def next_match():
    global matches
    global participants
    current_match = 0
    for m in matches
        if(m['state'] == "open")
            current_match = m
            break
    player1 = get_participant(current_match['player1_id'])
    player2 = get_participant(current_match['player2_id'])
    string = ("The next match is number " + str(self.match_index+1) + " with " + player1 + " and " + player2)
    return string

#combines the information into an actual response

def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event, context)

    elif event['request']['type'] == "IntentRequest":
        return intent_router(event, context)

def on_launch(event, context):
    return statement("Bracketier","something works")

def intent_router(event, context):
    intent = event['request']['intent']['name']
    
    #required intents 
    if intent == "AMAZON.CancelIntent":
        return cancel_intent()
    
    if intent == "AMAZON.HelpIntent":
        return help_intent()
    
    if intent == "AMAZON.StopIntent":
        return stop_itent()

    #custom intents

    if intent == "StartTournament":
        return start_tournament()

#Built in Intents Functions
#-------------------------------------------------------
def cancel_intent():
    return statement("cancel","You want to cancel")
def help_intent():
    return statement("help","You want help")
def stop_intent():
    return statement("stop","You want to stop")

# usedul builder stuff

def statement(title, body):
    speechlet = {}
    speechlet['outputSpeech'] = build_PlainSpeech(body)
    speechlet['card'] = build_SimpleCard(title, body)
    speechlet['shouldEndSession'] = True
    return build_response(speechlet)

def conversation(title, body, session_attrs):
    speechlet = {}
    speechlet['outputSpeech'] = build_PlainSpeech(body)
    speechlet['card'] = build_SimpleCard(title, body)
    speechlet['shouldEndSession'] = False
    return build_response(speechlet, session_attributes = session_attrs)

def build_PlainSpeech(body):
    speech = {}
    speech['type'] = 'PlainText'
    speech['text'] = body
    return speech

def build_response(message, session_attributes={}):
    response = {}
    response['version'] = '1.0'
    response['sessionAttributes'] = session_attributes
    response['response'] = message
    return response


def build_SimpleCard(title, body):
    card = {}
    card['type'] = 'Simple'
    card['title'] = title
    card['content'] = body
