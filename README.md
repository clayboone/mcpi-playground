# Playing with the `mcpi` API

## Install

I've used Windows for this.

1. Install Minecraft with a 1.7.10 profile.
2. Install Forge via the official Windows installer.
3. Download [McpiApiMod](https://github.com/kbsriram/mcpiapi) and move it to your `%APPDATA%\.minecraft\mods` folder.
4. Clone this repo and cd into it with:

```sh
git clone https://github.com/tenerhades/mcpi-playground

cd mcpi-playground
```

After that, load up Minecraft, swap over to the Forge profile that's been created automatically, and start the game.

## Run

At this point, you should have a command prompt open in the `mcpi-playground` folder with some `*.py` programs inside of it. And the game should be running with the McpiApiMod mod loaded.

Make a new world and pick a program to run, then run it with:

```sh
python <program-name.py>
```

I like to edit my code with VS Code and I like it to run automatically when I save. To do this, you can borrow a program called `nodemon` from the NPM universe.

As long as there's a "shabang" line at the top of the file (eg. "`#!/usr/bin/env python3`"), then you can run the file and automatically restart it when the the file changes with:

```sh
nodemon <program-name.py>
```

Installing Node.js and NPM is outside of the scope of this README.
