Make_NBUClients_Offline-Online_Patching
This is my collection of NBU Codes i use for an effective NBU Administration.

Below is a general description of python script.
make_clients.py
A simple python script to offline/online the backup clients. It is especially useful during the patching window where system admins request for suspend of backups but you cannot simply deactivate the policy because it has other clients which are not included for patching. So only option is to make them offline.All you need to do is to add a column of clients to a file and feed it to the script.

USAGE:

Windows :- Download the exe file for NBU Windows Environment

make_clients.exe --offline/--online -f <file_name>

Linux :- Download the bin file for NBU Linux Environment

make_clients.py --offline/--online -f <file_name>
