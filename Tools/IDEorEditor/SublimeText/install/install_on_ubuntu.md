# Install Sublime Text on Ubuntu

Copy and excute every command on Terminal.

## Step 1: Install GPG key
The apt repository contains packages for both x86-64 and arm64.

Install the GPG key:

```
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/sublimehq-archive.gpg > /dev/null
``` 

## Step 2: Select channel to use

#### Stable
```
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
```

#### Dev
```
echo "deb https://download.sublimetext.com/ apt/dev/" | sudo tee /etc/apt/sourc
```

## Step 3: Update and Install Sublime Text
```
sudo apt update
sudo apt install sublime-text
```

## Step 4 (Optional): If fails
If this fails ensure apt is set up to work with https sources:

```
sudo apt install apt-transport-https
```

### [Reference](https://www.sublimetext.com/docs/linux_repositories.html#apt)