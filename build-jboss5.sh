#!/bin/sh
file="jboss-5.1.0.GA-jdk6.zip"
rm -rf BUILD tmp || true
mkdir -p BUILD RPMS SRPMS

if [ ! -f SOURCES/$file ];
then
    wget "http://downloads.sourceforge.net/project/jboss/JBoss/JBoss-5.1.0.GA/jboss-5.1.0.GA-jdk6.zip?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fjboss%2Ffiles%2FJBoss%2FJBoss-5.1.0.GA%2F&ts=1360616527&use_mirror=iweb" -O SOURCES/$file
fi

rpmbuild -ba --target=noarch --define="_topdir $PWD" --define="_tmppath $PWD/tmp" --define="ver $version" jboss5.spec
