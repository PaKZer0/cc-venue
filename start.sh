#!/usr/bin/env bash
system=$(uname -m)


# if we're working with an arm based system, build required images
if [ $system = "armv7l" ];
then
	mainfolder=$(pwd)
	# check if icecast and inspircd images are present
	dockerout=$(docker images --format "{{.Repository}}")
	
	# if not we'll build them
	echo $dockerout | grep 'moul/icecast' &> /dev/null
	if [ $? != 0 ]; then
	   echo "Build icecast image"
	   tmpfolder=$(mktemp -d)
	   git clone https://github.com/moul/docker-icecast.git $tmpfolder
	   docker build -t moul/icecast:latest $tmpfolder
	   rm -Rf $tmpfolder
	fi
	
	echo $dockerout | grep 'inspircd/inspircd-docker' &> /dev/null
	if [ $? != 0 ]; then
	   echo "Build inspircd image"
	   tmpfolder=$(mktemp -d)
	   git clone https://github.com/inspircd/inspircd-docker.git $tmpfolder
	   docker build -t inspircd/inspircd-docker:latest $tmpfolder
	   rm -Rf $tmpfolder
	fi
fi

docker-compose up -d
