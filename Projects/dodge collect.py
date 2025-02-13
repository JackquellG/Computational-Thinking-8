#Section 1 - Setup
import codesters, random
from codesters import StageClass
stage = StageClass()
stage.disable_all_walls()
object_speed = 5
score = 0
player = codesters.Sprite("lebron")
stage.set_background("court")


########################################


# Section 2 - Objects
def falling_object():
    global object_speed, score
    
    if score < 100:
        y = random.randint(-50,50)
        x = 400
        object = codesters.Sprite("trophy", x, y)
        object.set_x_speed(-5)
        object.set_size(0.1)
        player.set_size(0.2)

stage.event_interval(falling_object, 2)
        

########################################


# Section 3 - Collision
def collision(player, object):
    global score,object_speed

    if object.get_image_name() == "trophy":
        stage.remove_sprite(object)
        object_speed += 1
        score += 1
        if score == 100:
            player.say(f"You are now lore-accurate lebron!",5)
        elif score < 100:
            player.say(f"{score} champions",0.5)
        
player.event_collision(collision)


########################################


# Section 4 - Controls

# Right Key
def go_up():
    player.move_up(10)
player.event_key("up", go_up)

# Left Key
def go_down():
    player.move_down(10)
player.event_key("down", go_down)


########################################

########################################

########################################

# you did it! #