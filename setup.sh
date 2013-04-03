#!/bin/sh
#
# Pierrick Koch - for morse.openrobots.org
# one line easy install:
#   mkdir ~/devel; cd ~/devel; sh <(wget http://pierriko.com/hanoi/setup.sh -qO-)
#

workspace=$(pwd)

[ "$workspace" = "$HOME" ] && echo "Create a new directory and run this script in it." && exit 1

echo -n "Install in ${workspace} ? [y/N] "
read ok
[ "y" != "$ok" ] && exit 1

mkdir -p ${workspace}/opt ${workspace}/tmp ${workspace}/src
cd ${workspace}/tmp

echo "Install Python 3.3"
(wget -cq http://python.org/ftp/python/3.3.0/Python-3.3.0.tar.bz2;
tar jxf Python-3.3.0.tar.bz2 && cd Python-3.3.0;
./configure prefix=${workspace} && make install) & pypid=$!

[ -z "$(uname -p | grep 64)" ] && arch="i686" || arch="x86_64"

BLENDER="blender-2.65a-linux-glibc211-$arch"
echo "Install ${BLENDER}"
(wget -cq http://download.blender.org/release/Blender2.65/${BLENDER}.tar.bz2;
tar jxf ${BLENDER}.tar.bz2 && mv ${BLENDER} ${workspace}/opt/blender) &

echo "Install MORSE 1.0 tarball"
(wget -cq https://github.com/laas/morse/archive/1.0_STABLE.tar.gz -O morse.tgz;
tar zxf morse.tgz && mv morse-1.0_STABLE ${workspace}/src/morse && wait $pypid && \
cd ${workspace}/src/morse && mkdir -p build && cd build && \
cmake -DCMAKE_INSTALL_PREFIX=${workspace} -DPYMORSE_SUPPORT=ON \
-DPYTHON_EXECUTABLE=${workspace}/bin/python3.3 -DBUILD_ROS_SUPPORT=ON .. && \
make install) &


echo "Setting up Pyhton CLI completion and history"

cat > ${workspace}/.pyrc << EOF
import os
import readline
histfile = os.path.join(os.path.expanduser("~"), ".pyhistory")
try:
    readline.read_history_file(histfile)
except IOError:
    pass

import rlcompleter
readline.parse_and_bind("tab: complete")
readline.parse_and_bind("ctrl-space: complete")

import atexit
atexit.register(readline.write_history_file, histfile)
del os, histfile, readline, rlcompleter
EOF

cat > ${workspace}/.bashrc << EOF
# Python CLI completion and history
export PYTHONSTARTUP=${workspace}/.pyrc
# Blender
export MORSE_BLENDER=${workspace}/opt/blender/blender
alias blender=${workspace}/opt/blender/blender
# Python
export PATH=\$PATH:${workspace}/bin
export PYTHONPATH=\$PYTHONPATH:${workspace}/lib/python3.3/dist-packages
EOF

#
# ROS specific
#

echo "Install Python YAML w/ python3.3"
(wget -cq http://pyyaml.org/download/pyyaml/PyYAML-3.10.tar.gz;
tar zxf PyYAML-3.10.tar.gz && cd PyYAML-3.10;
wait $pypid && ${workspace}/bin/python3.3 setup.py install) &

echo "Install distribute w/ python3.3"
wget -cq http://python-distribute.org/distribute_setup.py

echo "Wait for Python 3.3 install"
wait $pypid

${workspace}/bin/python3.3 distribute_setup.py

echo "[ -f /opt/ros/groovy/setup.bash ] && source /opt/ros/groovy/setup.bash" >> ${workspace}/.bashrc
echo "[ -f ${workspace}/.bashrc ] && source ${workspace}/.bashrc" >> ~/.bashrc

echo "Wait for background install to finish"
wait

ubuntu_codename=$(lsb_release -cs)
[ "0" != "$?" ] && echo "[ERROR] lsb_release: not running Ubuntu ?" && exit 1
echo "Install ROS on ${ubuntu_codename} in /opt needs to sudo"

sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros-latest.list'
wget http://packages.ros.org/ros.key -O - | sudo apt-key add -
sudo apt-get update
sudo apt-get install ros-groovy-desktop-full python-rosinstall git-svn git-cvs

sudo rosdep init
rosdep update

echo "Install rospkg w/ python3.3"
cd ${workspace}/tmp && git clone git://github.com/ros/rospkg.git
cd rospkg && git checkout 1.0.20
${workspace}/bin/python3.3 setup.py install
cd ${workspace}/tmp && git clone git://github.com/ros-infrastructure/catkin_pkg.git
cd catkin_pkg && git checkout 0.1.10
${workspace}/bin/python3.3 setup.py install
cd ${workspace}/tmp && git clone git://github.com/ros/catkin.git
cd catkin && git checkout 0.5.65
${workspace}/bin/python3.3 setup.py install

echo "done."
cd ${workspace}
