# Special Relativity Paradoxes
  This is the source code for an undergraduate research project involving paradoxes in special relativity. The project is for Yakima Valley College, spanning the summer quarter, through the end of the fall quarter of 2020. The program is written in Python 3.8, and the user interface is in Kivy 1.11.1.

# Research
  The project itself was to learn the languages and libraries to build an program, first to reproduce the results of previous research into the paradoxes, and then to develop it into an application with a user interface, allowing for ease of access and user input. A secondary benefit of using Kivy is that the finished application is cross-platform, and as such, will eventually be available for desktop and mobile devices.

  The plan for the project for the fall quarter of 2020, was to create the user interface, connect it to the logic code already created, and calculate new results with the user input, for at least the two paradoxes used in the original project: the 'Twin' paradox, and the 'Barn-Ladder' paradox. Then it was to display the results of the calculations graphically, while also printing them to a document, such as a CSV file, as the original program already does.

# Timeline
  I wanted to use Kivy for this project, mostly for its apparent ease of use, though it appeared to be less popular than other GUI packages (such as TKinter), but I initially had difficulty installing Kivy, due to its limitations to Python 2. Luckily, before I settled on something else, a new version of Kivy was released, and I could move forward.

  In the middle of development of the interface, the motherboard of my computer needed to be sent to the manufacturer for repair. I lost nearly a month of development time, much of which was spent waiting for the turnaround with the repair, but included attempts to repair it myself, and then setting up a completely new development operation on a separate machine.

  The silver lining in all of this came from Pydroid 3, a Python IDE for Android devices. Despite not generally liking to develop on my phone, Pydroid 3 is one of the IDEs I prefer. Then I found that Pydroid 3 came with Kivy built in. So during this lengthy downtime, I was able to continue developing the layout in the KV language.

  By the time I received my replacement motherboard, and was able to get back to development on my desktop, there was less than two weeks left to finish the program, and I had come to learn some things about Kivy that weren't as user-friendly as I had hoped, but I was able to finish a simple interface.

# Results
  For this project I have, to date, completed:
  <ul>
    <li>A simple Python program that will reproduce the results of the previous research for both the Twin and Ladder paradoxes.</li>
    <li>The program will print the results to a CSV file for review.</li>
    <li>A simple interface in Kivy, with user input fields, a button to call the calculation functions, and a spinner to change the screen between the different paradoxes.</li>
  </ul>

  Some issues that still need to be addressed:
  <ul>
    <li>The source code needs to be refactored to make better use of lists/dicts/tuples.</li>
    <li>Decimal... just all of it...</li>
    <li>Due to the loss of so much time, only the interface <s>is functional</s> exists, but it is not connected to the calculation logic from the original project.</li>
    <li>The calculation button and the user input fields of the interface are incomplete, and will halt its core functionality.</li>
    <li>The screen management system is missing, so the application only has a screen for the Twin paradox, and no navigation.</li>
  </ul>

# Continuing Development
  For the time being, I will continue developing this application, starting with correcting the issues above. Aside from that, some features I plan to include are:
  <ul>
    <li>Visualization of the coordinate transformations, in a graph for example</li>
    <li>Convert data output function from CSV to JSON</li>
    <li>Example inputs for users to try, such as coordinate data for Mars, or other galaxies</li>
    <li>Rebuild the Kivy interface in KivyMD</li>
    <li>Not a feature, but convert the application to a web app.</li>
  </ul>

  Once complete, I plan to release the application, initially, for Windows/MacOS/Linux, and for mobile devices (Android/iOS) when able.
