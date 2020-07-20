from lettuce import *

@step('a user exists with username "try"')
def user_name(step, string):
    world.name = str(name)
