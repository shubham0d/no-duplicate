#!/usr/bin/python
#duplicate file deleting utility
#Copyright (C) 2015 shubham dubey
#<https://github.com/shubham0d/no-duplicate>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>

#A simple python based utility that can delete duplicate files from any directory.
#
#including sub-directory scan is also a feature
#but md5deep utility have to be already installed.


# Import Modules

import commands
import linecache
import os


#program to delete the duplicate files in any directory
#it is based on fact that hash value of two same file are same
# even if there names are diffrent.

#\033[xm are used for ansi colour code.
os.system("clear")
print """\033[33m
                ####################################################
                #A tool to delete duplicate files from your system.#
                ####################################################
                \033[34m   contact/mail_at_sdubey504@gmail.com
                \033[0m"""

#this program first find and save the hash value of all the
# files in a directory at /tmp/duplicate.txt using md5deep
# and md5sum utility and then will compare them one by one.


directory=raw_input("enter the path of directory to search:")

#want the option to find duplicates from sub directory also..??
sub_true=raw_input("Scan sub-directory?\033[91m(y|n)\033[0m:")


print

#large and lots of files make it take quite a time.
print("\033[36mPlease wait while processing\033[91m...\033[0m")

if sub_true=='y':

        #save all the filename with their hash value in a file using
        # md5deep utility.
        #syntax for saved result is:
        #a4c6334194e87025e2a4c7ae9646a733  /root/test
        #-r option enable sub-directory check.

        commands.getoutput("md5deep -r "+directory+"* >/tmp/duplicate.txt")

        #will read number of lines i.e files from /tmp/duplicate.txt
        num_lines=sum(1 for line in open('/tmp/duplicate.txt'))

        #file is opened to  read its line one by one
        _file=open('/tmp/duplicate.txt','r')


        #in this tuple all the duplicate files name will get saved.
        duplicates=[]

        for line in range(num_lines):

                #if it is last line then does'nt need to compare
                #line=num_lines-1 bcuz line variable is starting from 0
                if int(line)==num_lines-1:
                        break

                #crt_line is the line which will get compared to all the lines at down.
                #since line start from 0
                crt_line=line+1
                text=_file.readline()

                #will grep only the hash value from that line
                hash_one=commands.getoutput("echo '"+text+"' |cut -d' ' -f1")

                #loop_ln is  the line to which crt_line will get compared to see
                #if hash are same or not.
                loop_ln=crt_line+1

                while int(loop_ln)!=int(num_lines):

                        #loop_ln will increase to cmpr all the lines till end.
                        match_ln=linecache.getline("/tmp/duplicate.txt",loop_ln)
                        hash_two=commands.getoutput("echo '"+match_ln+"' |cut -d' ' -f1")

                        if hash_one==hash_two:

                                #if hash are equal then file frm crt_line will get added
                                #to duplicate tuple.
                                duplicates.append(text)
                                break

                        loop_ln=loop_ln+1


        _file.close()

        #will tell the no of duplicate file found.
        total_dup=len(duplicates)
        print
        print("\033[34m\033[1m"+str(total_dup)+" \033[91mduplicate file found!\033[0m\033[22m")
        print


        x=1
        while int(x)==1:
                print("\033[91mPress 1)\033[0mto view them")
                choice=raw_input("\033[91mPress 2)\033[0mto delete them:")

                if int(choice)==1:
                        print
                        print("\033[91m\033[4mDuplicate files:\033[0m\033[24m")

                        for total_fls in range(total_dup):

                                #will show all the value frm tuple which are duplicate file.
                                output=duplicates[total_fls]

                                #only show file name not its hash value with.
                                print (output[34:])
                                x=1


                if int(choice)==2:

                        for x in range(total_dup):

                                du=duplicates[x]

                                #to grep only filename from line
                                filename=du[34:]

                                #at the end of file \n will remove
                                filename=commands.getoutput("echo '"+filename+"'|cut -d'\n' -f1")
                                os.remove(filename)

                                print("file \033[91m"+filename+"\033[0m successfully \033[91mremoved\033[0m.")

                        x=0
                        print
                        print("\033[35m\033[4mall duplicate files successfully deleted.\033[0m\033[24m\033[33m:)\033[0m")


if sub_true=='n':

        #same procedure but -r option will get remove from md5deep or md5sum
        commands.getoutput("md5sum "+directory+"* >/tmp/duplicate.txt")
        num_lines=sum(1 for line in open('/tmp/duplicate.txt'))
        _file=open('/tmp/duplicate.txt','r')

        duplicates=[]


        for line in range(num_lines):

                if int(line)==num_lines-1:
                        break

                crt_line=line+1
                text=_file.readline()

                hash_one=commands.getoutput("echo '"+text+"' |cut -d' ' -f1")
                loop_ln=crt_line+1

                while int(loop_ln)!=int(num_lines):
                        match_ln=linecache.getline("/tmp/duplicate.txt",loop_ln)
                        hash_two=commands.getoutput("echo '"+match_ln+"' |cut -d' ' -f1")

                        if hash_one==hash_two:

                                duplicates.append(text)
                                break

                        loop_ln=loop_ln+1

        _file.close()
        total_dup=len(duplicates)
        print
        print("\033[34m\033[1m"+str(total_dup)+" \033[91mduplicate file found!\033[0m\033[22m")
        print

        x=1
        while int(x)==1:

                print("\033[91mPress 1)\033[0mto view them")
                choice=raw_input("\033[91mPress 2)\033[0mto delete them:")

                if int(choice)==1:

                        print
                        print("\033[91m\033[4mDuplicate files:\033[0m\033[24m")

                        for total_fls in range(total_dup):
                                output=duplicates[total_fls]
                                print (output[34:])
                                x=1


                if int(choice)==2:

                        for x in range(total_dup):

                                du=duplicates[x]
                                filename=du[34:]
                                filename=commands.getoutput("echo '"+filename+"'|cut -d'\n' -f1")
                                os.remove(filename)

                                print("file \033[91m"+filename+"\033[0m successfully \033[91mremoved\033[0m.")

                        x=0
                        print
                        print("\033[35m\033[4mall duplicate files successfully deleted.\033[0m\033[24m\033[33m:)\033[0m")
