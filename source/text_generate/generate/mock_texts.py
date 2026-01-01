import random

MOCK_TEXTS = [
    """Apple banana computer door elephant flower guitar house ice juice kite lamp monkey notebook orange piano question radio star tree umbrella violin window xylophone yellow zoo airplane book cat dance eagle finger grass hat island jacket king lemon mountain""",
    
    """Quick brown fox jumps lazy dog green grass grows blue sky clear red car fast yellow sun warm black night cold white snow falls purple flowers bloom orange juice sweet brown bread fresh silver moon shines golden ring precious wooden table strong""",
    
    """Run walk jump swim fly climb drive sleep eat drink read write speak listen watch play work study think learn teach grow build create destroy help harm love hate like dislike want need have take give make break fix clean dirty""",
    
    """Paper pen pencil ruler eraser notebook folder backpack desk chair table lamp clock calendar phone charger cable keyboard mouse screen printer scanner copier speaker microphone camera lens battery memory card storage cloud network internet""",
    
    """Monday Tuesday Wednesday Thursday Friday Saturday Sunday January February March April May June July August September October November December spring summer autumn winter morning afternoon evening night dawn dusk midnight noon""",
    
    """North south east west up down left right front back inside outside above below near far high low deep shallow wide narrow long short big small heavy light fast slow hot cold warm cool dry wet dark light""",
    
    """Circle square triangle rectangle oval diamond heart star cross arrow line curve angle point edge corner surface space volume area length width height depth distance speed time weight mass force energy power""",
    
    """Coffee tea water milk juice soda beer wine bread cheese meat fish fruit vegetable rice pasta soup salad cake cookie chocolate ice cream salt pepper sugar honey butter oil vinegar sauce spice herb""",
    
    """House apartment building room kitchen bathroom bedroom living room garage garden yard fence wall floor ceiling window door roof basement attic stairs elevator escalator corridor hallway entrance exit""",
    
    """Car bus truck bike motorcycle train plane boat ship helicopter rocket submarine ambulance fire police taxi van tractor crane bulldozer excavator roller coaster bicycle scooter skateboard wagon cart""",
    
    """Forest river mountain valley desert ocean island beach cliff cave waterfall lake pond stream meadow field farm village city town capital country border bridge tunnel road highway path trail""",

    """Sun moon star planet galaxy universe comet asteroid meteor orbit rotation eclipse gravity atmosphere vacuum space time dimension quantum particle wave spectrum radiation telescope satellite""",

    """Heart lung brain stomach liver kidney blood bone muscle skin nerve cell tissue organ system pulse breath sweat tear saliva urine digestion metabolism health disease medicine vaccine""",

    """Family friend enemy stranger neighbor guest host teacher student doctor nurse engineer artist musician actor writer director producer manager worker employee employer customer client""",

    """Music song melody rhythm harmony note chord instrument orchestra band concert opera ballet dance theater cinema film television radio podcast album playlist singer composer lyrics""",

    """Sport game match competition tournament league team player coach referee score goal point win lose draw medal trophy cup prize championship victory defeat practice training exercise""",

    """Money cash coin currency wallet bank account credit debt loan interest tax price cost value profit loss salary wage income expense budget investment stock market economy trade""",

    """History future present past ancient medieval modern contemporary era age century millennium timeline event revolution war peace treaty agreement conflict battle victory empire kingdom""",

    """Science technology engineering mathematics physics chemistry biology geology astronomy medicine research experiment discovery invention innovation laboratory analysis data theory hypothesis""",

    """Art painting sculpture drawing sketch photography architecture design fashion style color shape form texture pattern light shadow perspective composition masterpiece exhibition gallery""",

    """Law justice court judge lawyer police crime punishment prison freedom right duty contract agreement property evidence testimony jury verdict sentence appeal constitution amendment""",

    """Religion faith belief god spirit soul heaven hell angel devil prayer temple church mosque synagogue meditation ritual ceremony tradition myth legend prophet priest monk nun""",

    """Education school university college classroom lesson homework exam test grade degree diploma certificate knowledge wisdom intelligence skill ability talent learning study research""",

    """Animal bird fish insect reptile amphibian mammal predator prey species evolution habitat extinction conservation zoo wildlife pet domestic wild fur feather scale paw claw wing""",

    """Emotion feeling love joy happiness sadness anger fear surprise disgust trust anticipation nostalgia jealousy envy pride shame guilt courage anxiety calm stress excitement pleasure""",

    """Government president minister parliament congress senate election vote campaign policy democracy republic monarchy dictatorship administration department ministry office official citizen""",

    """Communication language word sentence grammar alphabet letter speech conversation discussion argument debate presentation translation interpretation accent dialect slang idiom proverb""",

    """Transportation travel journey trip tour vacation holiday adventure exploration discovery map guide direction location destination arrival departure luggage ticket passport visa""",

    """Weather climate temperature humidity pressure wind rain snow hail storm thunder lightning hurricane tornado flood drought season forecast prediction cloud fog mist frost ice""",

    """Business company corporation factory office industry market product service production manufacturing distribution sales marketing advertising brand logo customer competition quality"""
]



def random_mock_text():
    return random.choice(MOCK_TEXTS)


