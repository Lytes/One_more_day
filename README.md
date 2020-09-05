# One_more_day
I was in a bad place mentally, so I'd download new songs every morning to have something to look forward to. 
I hope this script helps you.
Python wrapper script that downloads random new songs per day so you can find your own genre(s) or maybe just something to look forward to everyday.
Works for Termux too.


# Steps
```
pip3 install youtube-dl
pip install --upgrade youtube-dl
git clone https://github.com/Lytes/One_more_day.git
cd One_more_day
python3 main.py
```
Automatically creates OMD folder in user's home directory. For Termux, creates folder in internal storage.

# Configure
Open OMDConfig.py with your favorite text editor to 
1. Add more Youtube music channels
2. Change number of songs to download per day.
3. Change download directory
