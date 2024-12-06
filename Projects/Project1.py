import codesters

from codesters import StageClass

stage = StageClass()

stage.set_background("winter")

q1 = codesters.Square(100, 100, 200, 'yellow')
q2 = codesters.Square(-100, 100, 200, 'blue')
q3 = codesters.Square(-100, -100, 200, 'red')
q4 = codesters.Square(100, -100, 200, 'black')

s1 = codesters.Sprite("drake", 100, 100)
s1.set_size(0.6)
s2 = codesters.Sprite("chill guy", -100, -100)
s2.set_size(0.1)
s3 = codesters.Sprite("twinkie", 100, -100)
s3.set_size(0.7)
s4 = codesters.Sprite("basketball", -100, 100)
s4.set_size(2)

message1 = codesters.Text("Jackquell G",0,220,"black")
message2 = codesters.Text("Goodbye",0,-220,"black")