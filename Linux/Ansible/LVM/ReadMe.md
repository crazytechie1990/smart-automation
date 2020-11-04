#LVM Automation Using Ansible

lvm_automate.yml is the main playbook which imports tasks from other playbooks during the play. Copy all the playbooks to a directory and run the main playbook lvm_automate.yml as shown below.

*ansible-playbook -i ansible_hosts lvm_ansible.yml*

_where ansible_hosts will be your inventory file_
