# hi10anime-hotlink-extractor
### This is simple python script to automate the process of getting the hotlink from hi10anime.com. Skipping the Ads entirely, put the whole thing into .txt file and also put it into clipboard, which after that you can add into batch downloader like IDM and use the feature of  "Add Batch Download using Clipboard"

#### Usage Steps :
1. Open hi10anime links, which contains anime that you would like to download. Like this one -> https://hi10anime.com/archives/46421
2. Press the little box, that will expand the links to the anime that you want to download
3. **IMPORTANT : DO NOT CLICK ANY LINKS THAT YOU DONT WANT TO DOWNLOAD, this can potentially cause duplicate download from other shortlinks**
4. Press the episode links that you want to download, wait a second, and **IMMEDIATELY CLOSE IT.**
5. Repeat for all the episodes you want to download (click to open -> wait 1 sec -> close the tab; you can use "ctrl+W" in chrome to close tab). __We do this, because we want to generate all the jtokens **ONLY** for the episodes that you want to download.__ (Like this https://sinbad.hi10anime.com/kBaraka/[Hi10]_Haikyuu!!_[BD_1080p]/(Hi10)_Haikyuu!!_S2_-_23_(BD_1080p)_(Sergey-Commie)_(EB7472A3).mkv?jtoken=7756035fb8 <-------)
7. Episodes links that unclicked in step 4 & 5 **WILL NOT** be downloaded
8.  After you do this, right click on empty space on the page, and download the complete html file, rename the html file into something easy like asd.html or asd.txt or anime.html whatever
9. Move the downloaded HTML file (we dont need the assets folder), to the same folder with the script (stringXtractor.py)
10. Run the python script in that folder

>python stringXtractor filename.html

This will generate txt file with all the hotlink of the episodes you clicked in step 4 and 5 in the same folder
and also put the whole link into clipboard.

TIPS : 
 -Open Internet Download Manager -> Tasks -> **"Add batch download from Clipboard"** -> Check All -> Downloads -> Enjoy :)
