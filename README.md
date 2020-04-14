Demo of pyXBMCt and more.

at one point I was lost in the labyrinth of the different windows of the pyXBMCt library.
there were 4 main classes: AddonDialogWindow, AddonFullWindow, BlankDialogWindow and BlankFullWindow to make my windows.
 At one point I no longer knew which one had a header, a title, a background, which is transparent or 
 completely opaque etc ...
So I wrote a little script that lists the 4 classes in action.

Then I realized that I was missing something in the library to do exactly what I wanted: 
a window without header or title but with its own background, a kind of mix between AddonDialogWindow and 
BlankDialogWindow.
So I wrote a personal extension to the original library and I have two new classes: 
BackgroundDialogWindow and BackgroundFullWindow

I added them in this demo script.