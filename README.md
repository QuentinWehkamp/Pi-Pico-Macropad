# Pi-Pico-Marcopad
(Please read the whole README before doing this project)  
A Macropad using the Raspberry Pi Pico, programmed with CircuitPython.  
I have included all the files.  

## 3D Print info
There are a couple of problems with the 3D model lid, the 2nd button sometimes doesn't completely return to the original position but still functions.
Also, the base is pretty warped when the two parts are put together and it's a tight fit.  
I printed it on my stock Ender 3 at 100% infill, with pretty much stock settings on CURA Slicer.  
The lid is printed at 0.20mm layer height(you can try a higher quality for a smoother corner).  
The Base is printed at 0.26mm layer height(for a faster print).  

## Code info
It is programmed with [Circuitpython](https://circuitpython.org/board/raspberry_pi_pico/) for pi pico.  
You have to install circuitpython on your Pico and include the Adafruit_hid library.  
The code isn't amazing but it works.

## PCB info
The pico is surface mount to the pcb so i can be challenging to solder on.  
The PCB is ready to order with the gerber file but i also added the pcb file and the design file.  
**The Components you will need are.**  
13 pcb mount Cherry MX switches or another switch that would fit in the Cherry MX Footprint.  
2 smd 0603 led and 0603 resistor(So you don't burn out the led)(also only the top led is used in my code so you could only get one).  
And a Raspberry Pi Pico ofcourse.  
**I personally used.**  
13 PCB mounted Cherry MX Blue switches.  
[Blue LED](https://lcsc.com/product-detail/Light-Emitting-Diodes-LED_Everlight-Elec-19-217-BHC-ZL1M2RY-3T_C72041.html) - [corresponding resistor](https://lcsc.com/product-detail/Chip-Resistor-Surface-Mount_Viking-Tech-ARG03FTC1470_C217738.html).  
[Green LED](https://lcsc.com/product-detail/Light-Emitting-Diodes-LED_0603-Green-light_C72043.html) - [corresponding resistor](https://lcsc.com/product-detail/Chip-Resistor-Surface-Mount_Viking-Tech-ARG03FTC3090_C217955.html).  
