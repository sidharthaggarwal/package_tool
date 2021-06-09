Tasks:
1. Automates setup of PHP Application
1. Install specific Debian packages
1. Remove specific Debian packages
1. Specify content and metadata for files and directories
1. Will check for services that need to be restarted

## Structure:
``` bash
  Server_Config/
  +-- bootstrap.sh
  +-- config.py
  +-- metadata.txt
  +-- packages
      +-- install.txt
      +-- uninstall.txt
```

## How to Configure:

* To install a package, add the package name to the text file labeled "install.txt" inside the "packages" directory. Each package name should be on it's own line without any trailing whitespace.
* For removing an installed package, follow you will do the same as you did to install a package. This time you will add the package names to the "uninstall.txt" file inside the "packages" directory.
* To set metadata and file content, you will need to add key value pairs into the "metadata.txt" file. Key value pairs must be separated by "=" and each on it's own line. Again, trailing whitespace should be avoided. Inside the metadata file, you will find examples from which you can edit.

## **_Usage_**

* Transfer directory to the destination server using the following syntax:

  ```bash
  scp -r tool/ your_username@remotehost
  ```

* CD into the directory

  ```bash
  cd tool/
  ```

* Make the scripts executable

  ```bash
  chmod +x config.py bootstrap.sh
  ```

* Install dependency

  ```bash
  ./bootstrap.sh
  ```

* Run the script

  ```bash
  python3 config.py
  ```


