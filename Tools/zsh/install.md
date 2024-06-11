# Install zsh

## Step 1: Install zsh

### MacOS
Execute the command below
```
brew install zsh
```

### Ubuntu
Execute the command below
```
sudo apt install zsh
```

### Fedora
Execute the command below
```
sudo dnf install zsh
```

## Step 2: Install `Oh My Zsh`
Copy and execute the command below
```
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

Now `Oh My Zsh` is installed. To use this 

## Step 3 (Optional): Install `PowerLevel10k`
Excute the command below

```
git clone https://github.com/romkatv/powerlevel10k.git $ZSH_CUSTOM/themes/powerlevel10k
```

## Step 4 (Optional): Configure `PowerLevel10k`
Open the file `~/.zshrc` and update `ZSH_THEME` value to `powerlevel10k`.

```
ZSH_THEME="powerlevel10k/powerlevel10k"
```

After this execute the command below on terminal.
```
p10k configure
```
And if this does not open the configuration option then restart the shell.

To restart the shell execute the command if you `bash`
```
exec bash
```

To restart the shell execute the command if you `zsh`
```
exec zsh
```


## Step 5 (Optional): Install `zsh-syntax-highlighting` plugin
Execute the command below
```
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```

## Step 6 (Optional): Install `zsh-autosuggestions` plugin
Execute the command below
```
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
```

## Step 7 (Optional): Activate plugins
If you have installed the plugins then you need to activate them. To do so, open the file `~/.zshrc` and add plugin name in `plugins` tuple.

Before
```
plugins=( git )
```
After
```
plugins=( git zsh-syntax-highlighting zsh-autosuggestions )
```


## Reference
#### [https://dev.to](https://dev.to/abdfnx/oh-my-zsh-powerlevel10k-cool-terminal-1no0)
