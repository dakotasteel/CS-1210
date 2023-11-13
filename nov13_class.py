"""
CS 1210
In Class Exercise
Dakota Marosi
November 13th, 2023
Dictionary Practice
"""

# Practice with nested dictionaries
student_profiles = {'eporcupi' : 
                    {'NAME' : {'first' : 'Egbert',
                              'last' : 'Porcupine'},
                    'MAJOR' : 'CS',
                    'COURSES' : ('CS1210', 'CS1080', 
                                 'MATH2055', 'ANTH1100')},

                    'epickle' : 
                    {'NAME' : {'first' : 'Edwina',
                              'last' : 'Pickle'},
                    'MAJOR' : 'BIOL',
                    'COURSES' : ('BIOL1450', 'BIOL1070', 
                                 'MATH2248', 'CHEM1150')},
                    
                    'wquux' : 
                    {'NAME' : {'first' : 'Winston',
                               'last' : 'Quux'},
                    'MAJOR' : 'ARTS',
                    'COURSES' : ('ARTS2100', 'ARTS2750', 
                                 'CS1210', 'ARTH1990')},
                    
                    'mgarply' : 
                    {'NAME' : {'first' : 'Mephista',
                               'last' : 'Garply'},
                    'MAJOR' : 'ENSC',
                    'COURSES' : ('ENSC2300', 'GEOG1170',
                                'FS2020', 'STAT2870')}}

''' 
Bercause dictionaries are mutable, like a list, they will still be modified
in the outside scope, even if you return something like a None value.
The below is an example of this! :)
'''

d = {'foo': 'bar'}
def modify_dictionary(d_):
    d_['new_item'] = 'new_value'
    return None
modify_dictionary(d)
print(d)
