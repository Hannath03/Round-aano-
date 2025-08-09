<img width="3188" height="1202" alt="frame (3)" src="https://github.com/user-attachments/assets/517ad8e9-ad22-457d-9538-a9e62d137cd7" />


# ROUND AANO?🎯


## Basic Details
### Team Name:Bit Busters


### Team Members
- Team Lead:Meera K N - CUSAT
- Member 2:Hannath C Shabeer
  

### Project Description
 This project evaluates how perfectly circular a chapati is by measuring its area and perimeter and calculating its circularity—a shape factor that quantifies roundness. The circularity value ranges from 0 to 1, where 1 indicates a perfect circle.
### Problem (that doesn't exist)
[What ridiculous problem are you solving?]
Ever wondered if your beloved chapati could be reigning “Miss Circle” of the kitchen? This quirky program lets you upload an image of your chapati, then judges how perfectly circular it is by measuring its area and perimeter—and delivering the ultimate roast (pun intended)—all with a hilarious verdict!

### The Solution (that nobody asked for)
[How are you solving it? Keep it fun!]
1. Spotlight Snap: Chapati, Strike a Pose!
You upload a top-down image of your chapati—think paparazzi-style—but softer lighting works just fine. The goal? Capture a clear, bird’s-eye view so your code doesn’t mistake a fold or glare for a crusty flaw.

2. Image Magic: Chapati on the Runway
The code converts the image to grayscale and applies thresholding to isolate the chapati from the background. Essentially, your chapati’s walking the catwalk, and this step draws the spotlight (a clean silhouette) around it.

3. Metrics Time: Size Up That Dough
The script hunts for the largest contour (that’s your chapati), calculates:
Area in “px²” (pixel-squared fame), and
Perimeter in “px” (not paparazzi—just edge pixels).
These are your chapati’s modeling stats.

4. Roundness Drama: The Ultimate Judge
The magic formula:
          Roundness=(Area*4*pi)/(Perimeter)^2
This is the gold standard in image shape analysis—widely used in particle shape detection and beyond. A perfect circle scores 1; even a neat square only scores ~0.785, triangle ~0.605… so chapati, take that, other shapes! 

5. Snapback Verdict: Comedy Meets Geometry
A tonal spin on the results:

> 0.95 → “🏆 Masterchef-level chapati!” (Yeah, you nailed that circle.)

0.85–0.95 → “😋 Pretty good! Grandma would be proud.” (Clap on your flour-covered shoulder.)

Else → “😂 Good luck next time... needs work!” (Maybe roll a bit more evenly next time.)

## Technical Details
### Technologies/Components Used
For Software:
- Languages used: Python
- Frameworks used: Tkinter 
- Libraries used: OpenCV(cv2), Pillow(PIL via Image and ImageTk),NumPy
- Tools used: Python,PIP,Tkinter File Dialogs and Messsage Boxes,Contour Drawing 


### Implementation
For Software:
# Installation
pip install opencv-python
pip install opencv-contrib-python
pip install numpy
pip install pillow
pip install tk

# Run
python chapati_roundness.py

### Project Documentation
For Software:

# Screenshots





# Diagrams
![Workflow](Add your workflow/architecture diagram here)
*Add caption explaining your workflow*

For Hardware:

# Schematic & Circuit
![Circuit](Add your circuit diagram here)
*Add caption explaining connections*

![Schematic](Add your schematic diagram here)
*Add caption explaining the schematic*

# Build Photos
![Components](Add photo of your components here)
*List out all components shown*

![Build](Add photos of build process here)
*Explain the build steps*

![Final](Add photo of final product here)
*Explain the final build*

### Project Demo
# Video

# Additional Demos
[Add any extra demo materials/links]

## Team Contributions
- [Name 1]: [Specific contributions]
- [Name 2]: [Specific contributions]
- [Name 3]: [Specific contributions]

---
Made with ❤️ at TinkerHub Useless Projects 

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProjects--25-25?link=https%3A%2F%2Fwww.tinkerhub.org%2Fevents%2FQ2Q1TQKX6Q%2FUseless%2520Projects)



