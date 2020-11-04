# LVM Automation Using Ansible

lvm_automate.yml is the main playbook which imports tasks from other playbooks during the play. Copy all the playbooks to a directory and run the main playbook lvm_automate.yml as shown below.

* ansible-playbook -i ansible_hosts lvm_ansible.yml *

_where ansible_hosts will be your inventory file_


Note :- Currently i have implemented only two actions of lvcreate and lvremove but if you understood these , creating other actions will be just a walk in the park.
        Also i haven't added support for xfs filesystem yet , will add it soon
