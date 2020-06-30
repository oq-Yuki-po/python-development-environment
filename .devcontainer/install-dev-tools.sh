apt-get update
apt-get install -y \
git \
bash-completion
git config --global user.name $GIT_USER
git config --global user.email $GIT_EMAIL
echo "source /etc/bash_completion" >> ~/.bashrc