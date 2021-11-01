
import re

def limpia (x):

    """
    THIS FUNCTION WILL HELP US TO CLEAN 'Activities' COLUMN. 
    FOR EVERYTHING RELATED TO THE ACTIVITY... RETURNS THE ACTIVITY
    """
    dicc_activities = {  
        'Surfing': '.*urf.*|.*Paddl.*|.*board.*|.*Board.*|.+Surf.*|.*swell.*|.*wave.*',
        'Swimming' : '.*swi.*|.*mmi.*|.*bath.*|.*ading.*|.*swim.*',
        'Fishing' : '.*fish.*|.*shin.*|.*fead.*',
        'Diving' : '.*fish.*|.*spear.*|.*div.*|.*phot.*|.*subm.*|.*merged.*|.*sank.*|.*snor.*',
        'Boating' : '.*kay.*|.*yak.*|.*banana.*|.*sail.*|.*sail.*|.*nfla.*|.*ancho.*|.*sk.*'}

    for key,values in dicc_activities.items():

        if re.match(values, x):
            return key 
        
    return "Unknown" 


def specie (x):

    """
    THIS FUNCTION WILL HELP US TO CLEAN 'Species' COLUMN. 
    FOR EVERYTHING RELATED TO THE SPECIES... RETURNS THE SPECIE
    """
    dicc_species = {  
        'White shark': '.*white.*|.*great.*|.*hite.*|.*grea.*',
        'Tiger shark' : '.*tig.*|.*ger.*',
        'Bull shark' : '.*bull.*|.*ull.*',
        'Whitetip shark' : '.*tip.*',
        'Shortfin Mako Shark' : '.*fin.*|.*shor.*|.*mak.*|.*ko.*',
        'Blacktip Shark' : '.*bla.*|.*ack.*',
        'Hammerhead Shark' : '.*ham.*|.*mmer.*|.*head.*',
        'Sand Tiger Shark' : '.*san.*'}

    for key,values in dicc_species.items():

        if re.match(values, x):
            return key 
        
    return "Unknown" 


def hour (x):

    """
    THIS FUNCTION WILL HELP US TO RETURN ONLY THE CATEGORY OF THE DAY (SUNRISE, MORNING, NOON, AFTERNOON, EVENING, NIGHT)
    BY DOING THIS, WE WILL GET THE HOUR OF THE DAY
    """

    horarios = {
        'Sunrise': ['04', '05', '06', '07'], 
        'Morning': ['08', '09','10','11'], 
        'Noon': ['12', '13', '14', '15'], 
        'Afternoon': ['16', '17', '18','19'],
        'Evening' : ['20', '21', '22','23'],
        'Night' : ['00', '01', '02','03']}
    
    for key, values in horarios.items():
        
        if x[0:2] in values:
            return key

    return x