# pybutton
Easily create interactable button objects in PyGame with just a few lines of code.

Pybutton is used to create button objects from class objects defined in the file. These buttons are fully customizable; can be updated in-execution of code; and contain several methods for displaying hover effects and executing commands when clicked. As of this launch version, the only buton object is the 'rect' rectangle button. This module is not really a professional product; rather it is made by a student for students as an alternative to the tedious, excessive amount of code it takes to create a button in PyGame.

# Button Class Objects

To create a button object, ```import pybutton```, and set ```my_var = pybutton.button_object()```. No object requires values to be passed to it to initiate, though such will be required to make the button usable. Below are tye button objects, followed by their initiation values set equal to their default, and an explanation of what they do. Then comes the object's methods — the functions that can be called upon the button to make it function.

* rect(pos=(0, 0), width=100, height=50, text='', bg=(255, 255, 255), fg=(0, 0, 0), font='timesnewroman', pixel=False, thickness=0, command=None, border=0, margin=10, bc=(255, 0, 0), hover_bg=None, hover_fg=None, hover_border=5, hover_bc=(0, 255, 0), hover_text=None, hover_margin=None, hover_font=None, hover_pixel=False, image=None, hover_image=None)<br>
  Rectangular button object.<br>
  Values:
    * ```pos = (0, 0)``` Position of top-left corner of button object
    * ```width = 100``` Width
    * ```height = 50``` Height
    * ```border = 0``` Thickness of border to wrap button with
    * ```text = ""``` Text to display on butto; defaults to no text
    * ```font = "timesnewroman"``` Font to use on text \[Add exception for if font is not found\]
    * ```pixel = False``` Pixelate text or not
    * ```margin = 10``` Margin of spacing to put between text and border/button edge; negative value blows text out of button
    * ```image = None``` Image to display on button background, behind text; will be automatically scaled to size like text using ```margin```; takes either image file path or predefined PyGame Image object — note that the former sometimes fails, and is not advised; defaults to no image
    * ```bg = (255, 255, 255)``` Background color of button; defaults to black
    * ```bc = (255, 0, 0)``` Border color; defaults to red
    * ```fg = (0, 0, 0)``` Foreground (text) color; defaults to white
    * ```thickness = 0``` Thickness of button background; does not inhibit placement of objects of the button; defaults to solid background
    * ```command = None``` Function to execute when button is clicked
    * ```hover_border = None``` Thickness of border to wrap button with while the same is touching the mouse cursor; defaults to ```border```
    * ```hover_text = None``` Text to display when button is touching mouse cursor; defaults to ```text```
    * ```hover_font = None``` Font to use on text displayed while button is touching the mouse cursor; defaults to ```text```
    * ```hover_pixel = False``` Pixelate the text displayed when button is touching the mouse cursor or not
    * ```hover_margin = None``` Margin of spacing to put between text and border/button edge while the same is touching the mouse cursor; negative value blows text out of button; defaults to ```margin```
    * ```hover_image = None``` Image to display on button background, behind text, when button is touching the mouse cursor; will automatically be scaled to size like text using ```hover_margin```; takes either image file path or predefined PyGame Image object — note that the former sometimes fails, and is not advised; defaults to ```image```
    * ```hover_bg = None``` Background color of button while the same is touching the mouse cursor; defaults to ```bg```
    * ```hover_bc = None``` Border color while button is touching mouse cursor; defaults to ```bc```
    * ```hover_fg = None``` Foreground (text) color while button is touching the mouse cursor; defaults to ```fg```
    
