"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Jared Brutcher.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg

#Turtle 1 Definition
turt1 = rg.SimpleTurtle('turtle')
thickness1 = 20

turt1.speed = 20
#Turtle 2 Definition
turt2 = rg.SimpleTurtle('turtle')
turt2.pen = rg.Pen('red',10)
turt2.speed = 20
#Turtle 1 Motion
for k in range(20):
    turt1.draw_circle(40-2*k)
    turt1.pen_up()
    turt1.forward(10)
    turt1.pen_down()
    turt1.pen = rg.Pen('blue', thickness1)
    thickness1 = thickness1/2















