# Escape
## Project Overview
Welcome to Escape, a captivating rocket launch simulation using OpenGL and Python! This project visualizes the thrilling process of a rocket launch, from countdown to lift-off, all the way to its journey in the sky. The simulation features a play button to initiate the countdown, realistic starry sky, moon, and detailed rocket movements.

## Features
### Play Button:
Starts the countdown for the rocket launch.

### Countdown Timer:
Displays a 3-second countdown before the rocket launch sequence begins.

### Realistic Rocket Launch:
Animates the rocket launch, including fumes and boosters.

###Starry Sky and Moon:
Creates a realistic outer space environment with stars and a moon.

### Grass and Launch Pad:
Simulates the rocket launch site with grass and a launch pad.

## Prerequisites
Before you begin, ensure you have met the following requirements:

Python 3.x
PyOpenGL
GLUT (OpenGL Utility Toolkit)

## Installation
### Clone the Repository

`sh
Copy code
git clone https://github.com/yourusername/escape.git
cd escape
Create a Virtual Environment (Optional but Recommended)
`
sh
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install Dependencies

sh
Copy code
pip install -r requirements.txt
If requirements.txt is not available, install the dependencies manually:

sh
Copy code
pip install PyOpenGL PyOpenGL_accelerate
Usage
Run the Simulation

sh
Copy code
python escape.py
Interaction

Click the Play Button on the screen to start the countdown.
Observe the rocket launch sequence once the countdown reaches zero.
File Structure
escape.py: Main script containing the simulation logic.
README.md: Project documentation.
requirements.txt: Python dependencies (optional, for pip installation).
How It Works
Main Components
Play Button: Drawn on the screen, initiates the countdown when clicked.
Countdown: Displays a 3-second countdown timer.
Rocket Launch: Handles the rocket's position and movement, including fumes and boosters.
Stars and Moon: Renders stars randomly in the sky and a moving moon for a realistic effect.
Grass and Launch Pad: Simulates the ground environment of the rocket launch site.
Key Functions
draw_play_button(): Draws the play button.
mouse_click(): Detects mouse clicks to start the countdown.
display_countdown(): Displays the countdown timer.
Rocket_on_Ground(): Renders the rocket on the ground before launch.
Moving_Rocket(): Animates the rocket's movement in the sky.
stars(), moon(), grass(): Render the sky elements.
Contributing
Contributions are always welcome! To contribute:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Make your changes.
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature/your-feature).
Open a Pull Request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
If you have any questions or suggestions, feel free to reach out:

Email: yourname@example.com
GitHub: yourusername
Enjoy the simulation, and happy coding! 🚀






