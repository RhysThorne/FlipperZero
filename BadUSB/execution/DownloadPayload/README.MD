# Payload Execution
Remote Access and Complete Control Over a Target's Computer

## This Is Not Plug N' Play + It is NOT Completely Finished

Based On https://github.com/UNC0V3R3D/Flipper_Zero-BadUsb/tree/main/BadUsb-Collection/Windows_Badusb/Execution/Invisible_DownExec_Zip_Extract
<details><summary>Use At Your Own Risk</summary>
 * I Am In No Way Responsible For How You Use This *
</details>

# How Is This Used
1. You need payload (meterpreter/reverse_tcp is good)
2. Your own GitHub Repo
3. A Compiled .exe/.bat/.ps1 payload 
5. FlipperZero or Other BadUSB Device

## How-To
1. Build a payload (Look up Meterpreter/TheFatRat)
2. Upload it to your OWN Github Page under Releases
3. Edit the Script so that the 'YOUR_GITHUB_RELEASES_PAGE' points to your releases (*https://github.com/YOUR_NAME/YOUR_REPO/releases/latest/download/NAME_OF_Payload.EXTENTION*)
4. It is Very Possible for Windows Defender to Detect the Download Depending On the Verison and Settings, I'm In the Process of Combining This With the '\FlipperZeroDB\BadUSB\general\Disable_Windows_Defender' So That it's undetected
5. Make Sure to Start the Listener in your terminal BEFORE Executing the BadUSB attack

## Plans For Update

1. Add Capability to Disable WinDefender
2. Add Clean Up + Safety Nets to Prevent Detection
