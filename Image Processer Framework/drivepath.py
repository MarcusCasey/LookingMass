""" Return the drive names in the system 

This file contains the methods used to grab the different drives using 
kivy's file explorer. Most of this code is original, however it was 
created using Kivy's documentation listed on their website, as well as 
reading into python's drive exploring capabilities. The code handles 
whether an operating system is windows, mac, or linux and adapts 
adequetly to allow file exploring to occur.


  Typical usage example:

  values: drivepath.get_drive_names()
  on_text: fc.path = drivepath.get_path(self.text)
"""
from string import ascii_uppercase
from kivy.utils import platform
from os import listdir

if platform == 'win':
    from ctypes import windll, create_unicode_buffer, c_wchar_p, sizeof


def get_win_drive_names():
    """Grabs windows drive names

    This function will grab the different drive names for windows.
    Windows handles drive assignment annoyingly compared to unix,
    and requires custom parsing in order to grab all drives.

        Args:
        
            none, this is an assignment fnc that returns drive names

        """
    volumeNameBuffer = create_unicode_buffer(1024)
    fileSystemNameBuffer = create_unicode_buffer(1024)
    serial_number = None
    max_component_length = None
    file_system_flags = None
    drive_names = []
    bitmask = (bin(windll.kernel32.GetLogicalDrives())[2:])[
        ::-1] 
    drive_letters = [ascii_uppercase[i] + ':/' for i,
                     v in enumerate(bitmask) if v == '1']

    for d in drive_letters:
        rc = windll.kernel32.GetVolumeInformationW(c_wchar_p(d), volumeNameBuffer, sizeof(volumeNameBuffer),
                                                   serial_number, max_component_length, file_system_flags,
                                                   fileSystemNameBuffer, sizeof(fileSystemNameBuffer))
        if rc:
            drive_names.append(
                f'{volumeNameBuffer.value}({d[:2]})')  
    return drive_names


def get_drive_names():
    """Used by the application to assign a variable drive names

    This function handles which operating system is being used, 
    linux/mac or windows and uses the applicable native functions
    to list directory 

        Args:
        
            none, this is an assignment fnc that assigns drives

        """
    if platform == 'win':
        names = get_win_drive_names()
    elif platform == 'macosx':
        names = listdir('/Volumes')
    elif platform == 'linux':
        names = ['/']
    return names


def get_path(spinner_text):
    
    """Used by the application to grab paths of files

    This function will grab the path of the selected file.
    The path is generated different for each operating system
    through a series of appended strings. 

        Args:
        
            The input is the grabbed file name from the application
            which is then used to generate the full path based on the OS
        """
    if platform == 'win':
        new_path = spinner_text[-3:-1] + '/'
    elif platform == 'macosx':
        new_path = '/Volumes/' + spinner_text
    elif platform == 'linux':
        new_path = spinner_text
    return new_path
