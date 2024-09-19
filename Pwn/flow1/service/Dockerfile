# this is default bound to port 5000
FROM pwn.red/jail

COPY --from=ubuntu:22.04 / /srv
COPY --chmod=755 flow /srv/app/run
COPY flag.txt /srv/app/flag.txt

# To run this Dockerfile, put it in the same folder with the `flow` file and a dummy `flag.txt` to test 
# then run the following commands
# docker build -t rep-flow1 .
# docker run -d -p 5000:5000 --name rep-flow1 --privileged rep-flow1

# then in order to interact with the a local "remote" server, run
# nc / ncat localhost 5000

# The purpose of using this Dockerfile is to have an environment that immediately mimics that of the actual challenge server

# In this case, the server is running an Ubuntu Linux distribution, which may lead to other behavior if you are running it in Debian Linux