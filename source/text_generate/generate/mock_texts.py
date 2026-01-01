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
]


def random_mock_text():
    return random.choice(MOCK_TEXTS)


