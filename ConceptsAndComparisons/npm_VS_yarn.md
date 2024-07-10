# npm vs Yarn
Both `npm` and `Yarn` are package managers for `JavaScript` that help developers manage project dependencies. Each has its own features, advantages, and disadvantages.

- `npm` stands for `Node Package Manager`
- `Yarn` stands for `Yet Another Resource Negotiator`

## Overview
### npm (Node Package Manager)
- Developed by **npm, Inc.** as the default package manager for `Node.js`.
- Comes installed with `Node.js`.
- Commands: `npm install`, `npm update`, `npm uninstall`.

### Yarn
- Developed by **Facebook** as an alternative to `npm`.
- Focuses on speed, reliability, and deterministic dependency management.
- Commands: `yarn add`, `yarn upgrade`, `yarn remove`.

## Installation
### npm
```
npm install -g npm
```

### Yarn
```
npm install -g yarn
```

## Speed
### npm
- Slower dependency installation.
- Improved performance in recent versions, especially with npm 5 and above.

### Yarn
- Faster than npm due to parallel downloads and efficient caching.
- Utilizes lock files to ensure faster installs.

## Dependency Management
### npm
- Uses package-lock.json to lock dependency versions.
- Potential issues with non-deterministic installations in earlier versions.

### Yarn
- Uses yarn.lock to lock dependency versions.
- Ensures deterministic installations across all environments.

## Offline Capability
### npm
- Limited offline capability.
- Improved with the addition of caching in later versions.


### Yarn
- Strong offline support due to caching of every package it downloads.
- Allows installation of dependencies without an internet connection if they were previously installed.

## Security
### npm
- Vulnerable to dependency tampering due to the central repository approach.
- Improved with the introduction of npm audit to scan for vulnerabilities.

### Yarn
- Enhanced security by using checksums to verify the integrity of packages.
- Automatically verifies packages before installation.

## CLI Commands
### Different Commands
| Task | npm Command | Yarn Command |
| ---- | ---- | ---- |
| Install packages | `npm install` | `yarn` or `yarn install` |
| Add a package | `npm install < package >` or `npm install < package_name@version_number >` | `yarn add < package >` or `yarn add < package_name@version_number >` |
| Remove a package | `npm uninstall < package >` | `yarn remove < package >` |
| Update packages | `npm update` | `yarn upgrade` |
| Install globally | `npm install -g < package >` | `yarn global add < package >` |
| Install dev package | `npm install < package_name > –save-dev` | `yarn add < package_name > –dev` |
| Update dev package	| `npm update < package_name >` or `npm update < package_name@version_number >` | `yarn upgrade < package_name >` or `yarn upgrade < package_name@version_number >` |
| View package | `npm view < package_name >` | `yarn info < package_name >` |

### Same Commands
| Task | npm | Yarn |
| ---- | ---- | ---- |
| Initialization | `npm init` | `yarn init` |
| Running Scripts | `npm run [script]` | `yarn run [script]` |
| Listing Dependencies | `npm list` | `yarn list` |
| Testing | `npm test` | `yarn test` |
| Linking Packages | `npm link` | `yarn link` |
| Authentication | `npm login` | `yarn login` |
| Authentication | `npm logout` | `yarn logout` |
| Publishing Packages | `npm publish` | `yarn publish` |

## Community and Ecosystem
### npm
- Larger community and longer history.
- More widely used due to being the default for Node.js.

### Yarn
- Strong adoption, especially in large-scale projects and enterprises.
- Collaborative community with frequent updates and improvements.

## Conclusion
- `Choose npm` if you prefer a default, well-integrated package manager with `Node.js` and are comfortable with its ecosystem.
- `Choose Yarn` if you need faster installs, deterministic dependency management, better offline capabilities, and enhanced security.

#### References
- [GeeksForGeeks.org](https://www.geeksforgeeks.org/difference-between-npm-and-yarn/)
- ChatGPT