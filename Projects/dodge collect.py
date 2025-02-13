#Section 1 - Setup
import codesters, random
from codesters import StageClass
stage = StageClass()
stage.disable_floor()
object_speed = 5
score = 0

# Section 2 - Objects
player = codesters.Sprite("lebron")
object = codesters.Sprite("trophy")
stage.set_background("court")
def falling_object():
    global object_speed, score
    
    if score < 100:
        y = random.randint(-50,50)
        object.set_x_speed = 5
        x = 400
        object = codesters.Sprite("trophy", x, y)
        object.set_size(0.5)

stage.event_interval(falling_object, 2)
        

# Section 3 - Collision
def collision(player, object):
    global score

    if object.get_image_name() == "trophy":
        stage.remove_sprite(object)
        object_speed += 1
        if score == 100:
            player.say(f"You are now lore-accurate lebron!")
        else:
            player.say(f"{score} champions",0.5)
        
player.event_collision(collision)


# Section 4 - Controls

# Right Key
def go_up():
    player.move_up(10)

player.event_key("up", go_up)

def go_down():
    player.move_down(10)

player.event_key("down", go_down)