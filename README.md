# getsys

#### are you nosey?
##### no? well, you're probably lying.

---


## what's this?

### getsys is a simple python script that aims to harvest as much system information as reasonably possible using just some simple modules.
by default, it prints out recursively the dictionary it manages to gather.

of course, you can build this into a wider system in which the dictionary is simply imported and its values can be further passed along in your program or project.
*in such a case, please see the licensing info at the bottom of this README.md for details on usage and the mandation of attribution(s).*

at such a point, you could choose which values to pass along to wherever you please!


## dependencies

at the time of writing, getsys relies on the following:
  - `psutil>=5.9.0` (version 5.9.0 or later seems to be advisable)
  - `py-cpuinfo>=9.0.0` (version 9.0.0 or later seems to be advisable)

*any testing on versions before the current ones on the day of writing and publishing has not taken place.*


## installing dependencies

##### you can use our nifty little `requirements.txt` file in the **root of the repo** to **install these automagically**:

  - having cloned the repo or downloaded its contents, make sure **your current working directory is the root of the repo**, or **where our `requirements.txt` resides** ('`getsys/`')

  - to check you've got pip installed and it's all ready to go here, you can run:

    ```
    pip --version
    ```

  - run, in a terminal:

    ```
    pip install -r requirements.txt
    ```

  then you should be about good to go!


## licensing, terms of use and attributions (*yawn*)

##### this code, this project and this work are collectively licensed under the GNU Affero General Public License 3.0 (AGPL-3.0), as declared, defined and published by the Free Software Foundation.

this entails the following:

  - you may use this code in your own projects, but **only if the project is also open source and licensed under the same GNU AGPL-3.0 license**, or **a later revision** of it.
  - **attribution is required**; you **must be upfront in your usage of this code**, work or resource in your project, **providing credit** with upfront transparency.
  - you should be reasonably upfront about changes you have made if the variant of this code that you use in your project deviates from what you borrowed.
  - however, **such derivative works are indeed permitted**, and shouldn't be prohibited by the license, **assuming proper attribution and credit is given**, and **this is also in an open source project** under the AGPL-3.0 or a newer revision.

TL;DR: you can do pretty much whatever you want with this code; fork it, bop it, twist it, pull it, squeeze it, eat it (but maybe don't do that), **so long as you give credits to this project** and **don't make this closed source or copyrighted**.

also, **this activity / project also needs to be under the AGPL-3.0** or **any newer revision according to the license**.

this software as distributed comes with absolutely no warranty, not even the implied warranties of being fit-for-purpose 

---

## enjoy!
i hope you might get some use out of this, whether you implement it into your own open source project, or just use it to learn about the modules we've used.
###### copyleft oreohive @ oreohive.org 2024 (coming soon!) - | - licensed under the AGPL-3.0 - | - attributions are required!

##### 

    this program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    this program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY - without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE - to the extent
    permitted by applicable law.

    see the GNU Affero General Public License for more details.

    you should have received a copy of the GNU Affero General Public License
    along with this program. if not, see https://www.gnu.org/licenses.
