# Android Emulator Chalupa Box Generator
This script can be used to generate Taco Bell accounts to get a free $5 chalupa box.
A form of payment is needed, however there will be no charge to it if the reward is used correctly. I'm not responsible if you mess this up and you just pay for your food like a normal person.

## Installation
Make sure you have python installed. I used 3.7. 
Install [Bluestacks](https://www.bluestacks.com/download.html). Log into whatever Google account and download the Taco Bell account.
Make sure to be on the "Account" page when starting the script. (located on the bottom right of the screen). See Image below. 

![Image](https://i.imgur.com/k0apmHk.png)

Run the script, and then follow the steps that are given with the prompts. Make sure to read them carefully.
After running the script, the accounts will be in `accounts.csv` that can be opened with Excel.

## Troubleshooting
Q: My app doesn't look like the one above. Why?
A: In Bluestacks, change the display settings to to be 1080p, landscape (tablet mode), 240dpi. Reload Bluestacks and retry script.

Q: When starting the script, the mouse moves but not to the right positions.
A: Make sure the emulator window is where the mouse coordinates were recorded. If you are unable to line it up correctly, then delete the `coords.json` file that is next to the script.

Q: There is no free chalupa box in rewards after making an account.
A: It's probably past December 15th, 2020. The offer doesn't exist anymore

Q: Why did you make this script?
A: Educational purposes only.
