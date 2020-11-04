# AutomationUsingPythonAndAnsible
Mini automation  projects.

***Ansible***
Contains some useful ansible playbooks which you can modify as per your infrastructure.Currently it has only LVM automation playbook which automates lvcreate and lvremove operations for you. Creation of lvmsnapshot i did using a python script, but ofcourse once you will go through my playbooks they are so simple that you can easily modify them for the operations you are seeking.

***dumplogs.py***
Tool to read the log table from postgres database and filter out based on category,severity, start and end time.

***lvmsnaprevert.py***
Customizable tool to test patches/security fixes on a server , if something goes wrong just run this tool and revert ==
Tool to replace original volume on cloud server with an lvm snapshot , and after testing changes/security patches/fixes if you are not happy with the result , revert back with the same tool to original volume.


Please note :- Above tools should be understood and tested before being deployed in production. All my tools are kind of frameworks , which you can alter/modify based on your requirements.


