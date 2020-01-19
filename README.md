# count
  A program to calculate data<br>
  Version 2.2.0

# Command
  We have several command to control data, you can find them by typing `key`.
  * `(v)add`
    >Add data<br>
    *add KEY:VALUE*<br>
    *add KEY:VALUE1, VALUE2...*<br>
    *vadd VALUE*<br>
    *vadd VALUE1, VALUE2...*
  * `(v)del`
    >Del data<br>
    *del KEY*<br>
    *vdel [ALL]VALUE*
  * `find`
    >Find data<br>
    *find KEY*
  * `info`
    >Show information of data<br>
    *info*
  * `key`
    >Show full key-word list<br>
    *key*
  * `load`
    > Load data from hard disk<br>
    *load FILE*
  * `quit`
    >Quit<br>
    *quit*
  * `show`
    >Show data<br>
    *show*
  * `store`
    > Store data<br>
    *store FILE*
# Save Your Data
  Your data are too complex? Don't worry, you don't need input them one by one, you can create a file.<br>
  The file format is particularly simple:<br>
  * Tag<br>
    TAGNAME:> Just support `DICT:` and `VALUE:`
  * Detail<br>
    Under tag
    * DICT
      See `DICT`
    * VALUE
      See
