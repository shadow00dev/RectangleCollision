# RectangleCollision
This is a rectangle collision for python

# how to install

pip install RectangleCollision

# how does this work

Checks for collisions using boundary box detection.<br>
If the source position is equal or greater than the destination position and it's width *(and same for y/height)*,
then there's a collision.

# Examples

See [examples](examples/) for a list of examples, mainly using [Pyglet](https://github.com/pyglet/pyglet/) as graphical engine.

    if collision.rectangle(object1x, object1y, object2x,object2y,object1width,object1height,object2width,object2height):
        #this wont work but this will shows you a "example" we have an example(the example uses pyglet)
        print('colided')
 
# credits
 
 1. me
 2. Riley *(`Comrade Riley#2451`)*

I made the library and Riley *(`Comrade Riley#2451` on Discord)* gave me the method to do so.
