# EasyButton
Easily create interactable button objects in PyGame with just a few short lines of code.

EasyButton is used to create button objects from class objects defined in the ```easy_button.py``` module file. These buttons are fully customizable; can be updated and moved in-execution of code; and contain several methods for displaying hover effects and executing commands when clicked. As of this first launch version, the only button object is the 'rect' rectangle button. This module is not a professional product; rather, it is made by a student for other students as an alternative to the tedious, excessive amount of code it takes to create a working, interactive button in PyGame.

If you would like to Say Thanks for this project, then please [![Say Thanks Button](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/william%40thehalsteds.net "Say Thanks page").

# Button Class Objects

To create a button object, ```import easy_button```, and set ```my_button = easy_button.button_object()```. No object requires values to be passed to it to initiate, though such will be required to make the button usable. Following are headings for each button object; then comes a bulleted list of the object's methods — the functions that can be called upon the button to make it operate — and what they do. Each method is followed by a sublist of the values that can be passed to it and the same's defaults. The final bullet point is another sublist, of certain attributes of the whole class that are not covered by the method documentation, but may be of interest to the programmer; not all other attributes are present, however.

## EasyButton Attributes<br>
Variables of the EasyButton module that do not belong to any of its subclasses.<br>
  * ```__version__``` A variable that contains the version of EasyButton installed in your directory; the version that is being used.

## rect()<br>
Rectangular button object.<br>
  * ```__init__(pos=(0, 0), width=100, height=50, text='', bg=(255, 255, 255), fg=(0, 0, 0), font='timesnewroman', pixel=False, thickness=0, command=None, border=0, margin=10, bc=(255, 0, 0), hover_bg=None, hover_fg=None, hover_border=5, hover_bc=(0, 255, 0), hover_text=None, hover_margin=None, hover_font=None, hover_pixel=False, image=None, hover_image=None)```<br>
    This method is run upon creating the button object; it stores the buttons properties.
    * ```pos = (0, 0)``` Position of top-left corner of button object
    * ```width = 100``` Width
    * ```height = 50``` Height
    * ```border = 0``` Thickness of border with which to wrap button
    * ```text = ""``` Text to display on button; defaults to no text
    * ```font = "timesnewroman"``` Font to use on text
    * ```pixel = False``` Pixelate text or not
    * ```margin = 10``` Margin of spacing to put between ```text``` and ```image``` and border/button edge; negative value blows text out of button
    * ```image = None``` Image to display on button background, behind ```text```; will be automatically scaled smaller — not larger — to fit using ```margin```, like ```text```; takes either image file path or predefined PyGame Image object — note that the former sometimes fails (known error), and is not advised; defaults to no image
    * ```bg = (255, 255, 255)``` Background color of button; defaults to black
    * ```bc = (255, 0, 0)``` Border color; defaults to red
    * ```fg = (0, 0, 0)``` Foreground (text) color; defaults to white
    * ```thickness = 0``` Thickness of button background; does not inhibit placement of objects of the button; value less than width/height results in transparent button center; defaults to solid background
    * ```command = None``` Function to execute when button is clicked
    * ```hover_border = 5``` Thickness of border to wrap button with while the same is touching the mouse cursor
    * ```hover_text = None``` Text to display when button is touching mouse cursor; defaults to ```text```
    * ```hover_font = None``` Font to use on text displayed while button is touching the mouse cursor; defaults to ```text```
    * ```hover_pixel = False``` Pixelate the text displayed when button is touching the mouse cursor or not
    * ```hover_margin = None``` Margin of spacing to put between text and border/button edge while the same is touching the mouse cursor; negative value blows text out of button; defaults to ```margin```
    * ```hover_image = None``` Image to display on button background, behind text, when button is touching the mouse cursor; will automatically be scaled to size like text using ```hover_margin```; takes either image file path or predefined PyGame Image object — note that the former sometimes fails, and is not advised; defaults to ```image```
    * ```hover_bg = None``` Background color of button while the same is touching the mouse cursor; defaults to ```bg```
    * ```hover_bc = (0, 255, 0)``` Border color while button is touching mouse cursor; defaults to green
    * ```hover_fg = None``` Foreground (text) color while button is touching the mouse cursor; defaults to ```fg```
    
 * ```update(self)```<br>
 This method updates the button object's ```surface``` attribute so as to make it display updated properties. It is automatically run by the ```check_hover``` method when a change in ```hovering``` status is detected, or the text it is displaying varies from the text it should be displaying.
 
* ```draw(self, destination```<br>
 This method blits the button onto a PyGame Surface.
	* ```destination``` The PyGame Surface that the button is to be drawn to
  
* ```hover(self, point)```<br>
This method checks to see if the button is touching the mouse cursor; if it is, it updates the button's Surface to display the values specially entered for when the button is being hovered over.
	* ```point``` A tuple or list containing the ```x``` and ```y``` positions of the mouse

* ```check_hover(self, point)```<br>
This method checks to see whether the button is touching the mouse cursor and returns the according boolean value.
	* ```point``` A tuple or list containing the ```x``` and ```y``` positions of the mouse

* ```click(self, point, down)```<br>
This method checks whether or not the button has been clicked. If it has, then it executes the ```command``` function attribute of the button.
	* ```point``` A tuple or list containing the ```x``` and ```y``` positions of the mouse
	* ```down``` A boolean value stating whether or not the mouse is down

* ```check_click(self, point, down)```<br>
This method checks whether or not the button has been clicked, and returns the according boolean value.
	* ```point``` A tuple or list containing the ```x``` and ```y``` positions of the mouse
	* ```down``` A boolean value stating whether or not the mouse is down

* ```get_fonts(self)``` <br>
This method calls the PyGame ```font.get_fonts``` method and returns a list of all the available fonts that can be given as values for ```font``` and ```hover_font```.

* Attributes
	* ```surface``` The PyGame surface object that contains the image of the button which is updated by the ```update``` method and blitted to a PyGame Surface object by the ```draw``` method.
