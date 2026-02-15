#Secure-ssh.sh
#Christopher Lavalette
#creates a new ssh user using $1 parameter
#adds a public key from the local repo or curled from the remote repo
#removes  roots ability to ssh in

useradd -m $1

mkdir /home/$1/.ssh

cp ../public-keys/$1.pub /home/$1/.ssh/authorized_keys

chown -R $1:$1 /home/$1/.ssh/
chown 700 /home/$1/.ssh
chown 600 /home/$1/.ssh/authorized_keys

sed -i 's/PermitRootLogin yes / PermitRootLogin no/' /etc/ssh/sshd_config

systemctl restart sshd

echo "User created and SSH is secured!"
