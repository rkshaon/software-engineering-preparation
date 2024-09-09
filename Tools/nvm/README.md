# nvm
`nvm` stands for `Node Version Manager`. It is a tool that allows you to manage multiple versions of `Node.js` on a single machine. 

With `nvm`, anyone can easily install, switch between, and manage different versions of `Node.js` and `npm` (Node Package Manager).

## Install
### macOS / Linux
Open a terminal and execute the command below.

```shell
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
```

Then need to add `nvm` on shell profile. To do so, the following line have to add in `.bashrc`, `.bash_profile`, or `.zshrc` file.
```shell
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm
```

Then restart terminal or run the following command.
```shell
source ~/.bashrc
```
for `bashrc`

```shell
source ~/.zshrc
```
for `zshrc`

### Windows
[Download and install `nvm-windows`](https://github.com/coreybutler/nvm-windows/releases)

## Use
### Install node
```shell
nvm install x
```
Replace `x` by a node version.

Like install node.js 18
```shell
nvm install 18
```

Like install node.js 20
```shell
nvm install 20
```

### Listing all node version
```shell
nvm ls
```

Output will be like below.
```shell
       v18.20.4
->     v20.15.1
         system
default -> 18 (-> v18.20.4)
iojs -> N/A (default)
unstable -> N/A (default)
node -> stable (-> v20.15.1) (default)
stable -> 20.15 (-> v20.15.1) (default)
lts/* -> lts/iron (-> v20.15.1)
lts/argon -> v4.9.1 (-> N/A)
lts/boron -> v6.17.1 (-> N/A)
lts/carbon -> v8.17.0 (-> N/A)
lts/dubnium -> v10.24.1 (-> N/A)
lts/erbium -> v12.22.12 (-> N/A)
lts/fermium -> v14.21.3 (-> N/A)
lts/gallium -> v16.20.2 (-> N/A)
lts/hydrogen -> v18.20.4
lts/iron -> v20.15.1
```
This means node.js v20.15.1 is used here.

### Switch
Consider you want to switch `node.js v18` from current version.
```shell
nvm use 18
```

### Set Default node.js Version
```shell
nvm alias default 20
```
This will set default `node.js` version in shell.

### Verify Version
```shell
node -v
```

#### References
- [nvm on GitHub](https://github.com/nvm-sh/nvm)


