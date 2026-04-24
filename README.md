# Gesture-Control-System-using-Arduino
Gesture control is the ability to recognize and interpret human body movements to interact with a computer system without physical contact. This project implements a hand gesture-based control system using ultrasonic sensors and Arduino.


- **Offline Gestures:** Processed after interaction (e.g., activating a menu)
- **Online Gestures:** Real-time gestures used for direct manipulation like scrolling or switching tabs

---

## ⚙️ Working Principle
This system uses **two ultrasonic sensors** connected to an Arduino to detect hand movements.

- Sensors measure the distance between hand and sensor
- Data is sent to the computer via **serial communication (USB)**
- A **Python program** reads this data
- Using **PyAutoGUI**, gestures are converted into keyboard/mouse actions

📍 **Sensor Placement:**
- Both sensors are placed on top of the laptop screen
- One on the left and one on the right

---

## ✋ Hand Gestures & Actions

| Gesture | Action |
|--------|--------|
| Hand moves away (Right Sensor) | Scroll Down / Decrease Volume |
| Hand moves closer (Right Sensor) | Scroll Up / Increase Volume |
| Swipe Right Sensor | Next Tab |
| Swipe Left Sensor | Previous Tab / Play-Pause |
| Swipe across both sensors | Task Switching |

---

## Tasks Performed
- Scroll Up / Down on web pages  
- Increase / Decrease volume  
- Switch browser tabs  
- Play/Pause video (VLC)  
- Task switching  


## Technologies Used
- **Arduino**
- **Ultrasonic Sensors (HC-SR04)**
- **Python**
- **PyAutoGUI Library**
- **Serial Communication (USB)**

## Applications
- Virtual Reality (VR)
- Augmented Reality (AR)
- Touchless computing systems
- 3D design interaction
- Assistive technology (e.g., sign language systems)

## Project Concept
The system detects hand distance using ultrasonic sensors. Based on predefined distance thresholds and motion patterns, gestures are recognized. These gestures are then translated into system commands using Python.

---

## Future Scope
- Integration with AI for gesture recognition  
- Improved accuracy using camera-based tracking  
- Use in smart homes and IoT systems  
- Touchless interfaces for healthcare environments  

---

## Conclusion
This project demonstrates a simple yet effective way to control a computer without physical interaction. It highlights the potential of gesture-based interfaces in modern human-computer interaction systems.
