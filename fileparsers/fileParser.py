from datetime import datetime
import os


import os


print(f'.TXT SCANNER --> progfram')
website_list = []
count = 0
hrefdata = 'hrefdata.txt'
cwd = os.getcwd()
href_loc = str(cwd) + f'/{hrefdata}'
href_str = f'[SYSTEM]** Dump The Text Data To: [{href_loc}] ** [SYSTEM]'
print(href_str)



print('Scanned List from .txt')

class fileParser:
    def __init__(self, filename):
        self.filename = filename

    def addToList(self, href_loc):
        count = 0
        with open(href_loc) as f:
            for href in open(href_loc):
                website_list = f.readlines(count)
                index = 0
                count += 1
                for iterate in website_list:
                    if index < count:
                        print(f'[SYS]** ADDED {iterate}')
                    else:
                        break
                print(f'[SYSTEM] Found {count} items in .txt')
                break

    ## This function reads the data from a file
    def read_file(filename):
        with open(filename, 'r') as f:
            data = f.read()
        return data


    ## This function writes the data to a file
    def write_file(filename, data):
        if os.path.isfile(filename):
            with open(filename, 'a') as f:
                f.write('\n' + data)
        else:
            with open(filename, 'w') as f:
                f.write(data)


class autostart:
    def __init__(self, filename):
        self.filename = filename

    def print_time(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        data = "Current Time = " + current_time
        return data
    def makeFile(self):
        fileParser.write_file('hrefdata.txt', autostart.print_time())
        pwd00 = input('Enter the file name to write to (.txt): ')
        write_file=(pwd00, '')


## RUN THE PROGRA WITH PRINT TIME CLASS APPENDED, SO YOU HAVE A DATE-TIME STAMP
#autostart.run_writeFile().print_time("hrefdata.txt")


print("href loc: ", href_loc)
autostart.print_time('hrefdata.txt')
autostart.makeFile('hrefdata.txt')

fileParser.write_file('hrefdata.txt', autostart.print_time('hrefdata.txt'))

# String	Meaning	Equivalent to
# @reboot	once on system startup
# @yearly	once yearly	0 0 1 1 *
# @monthly	once a month	0 0 1 * *
# @weekly	once a week	0 0 * * 0
# @daily	once a day	0 0 * * *
# @midnight	once a day at midnight	0 0 * * *
# @hourly	once an hour	0 * * * *
# once a minute	* * * * *
# once every day of the week	* * * * 1-5
# once every specific day, at a specific time (Sunday at 12:30)
#
