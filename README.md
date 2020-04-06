# AnagramApp
An internet facing web service accepting a single word and deriving all possible anagrams

Tools Used:
1. AWS - EC2 (For testing purpose, a free-tier EC2 instance can be used)
2. AWS - Security Groups (Allowed port 5001 to access application from internet)
3. VPC
4. Docker - To create application container
5. Docker Hub - To publish the image used to build the container.
6. Github - SCM

Python/HTML

Installation Steps:
1. Clone the source code or download the archive. You can follow link https://git-scm.com/downloads to install git if not available on your host machine.
2. Install Docker using below commands on Linux/CentOS machines
   - sudo yum install -y yum-utils device-mapper-persistent-data lvm2
   - sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
   -  sudo yum install docker-ce docker-ce-cli containerd.io
   - sudo systemctl start docker
    
  Or, you can follow the official documentation to install Docker on your host machine. 
   - https://docs.docker.com/install/linux/docker-ce/centos/
     
3. Run Python container using below command in the source code directory.
   - docker run -d --name anagram_container -p 5001:5000 -v /tmp/anagram_logs:/tmp archanapunia/anagram
   
   Or, you can build your own custom image from the sample Dockerfile.
   
4. The Web application should be accessible at http://YourMachineIP:5001
   

