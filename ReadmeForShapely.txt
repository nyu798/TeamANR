In order to install Shapely along with its dependencies, following commands have to be run on all nodes of cluster:

sudo yum install geos geos-devel
sudo pip install shapely
sudo ln -sf /usr/bin/python2.7 /usr/bin/python