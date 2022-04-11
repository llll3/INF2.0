yes | apt update
yes | apt upgrade
yes | pkg install python3 git nano
rm -rf $HOME/../usr/etc/bash.bashrc
cp $HOME/INF2.0/bmb/bash.bashrc ../usr/etc/
source $HOME/../usr/etc/bash.bashrc
clear -x
echo 'Чтобы запустить программу напишите INF2.0'
