Image Integrity Check
==========================
A simple Python3 script about checking image files integrity.

Supported file types are bmp, jpeg, gif, pbm, pgm, png, ppm, xbm and tiff.

Options
-------

**Usage:** python3 img-chk.py [options]

**Optional arguments:**
  
  `-h, --help`                              Show help about this program
  
   `-d DIR, --dir DIR`                      Dir path to check. Default is current directory.
   
   `-e EXTENSION, --extension EXTENSION`    Files extension. The default behaviour is to check all supported
                                            filetypes. If this option is set then only files with the 
                                            specified extension will be checked
   
   `-o OUTPUT, --output OUTPUT`             Output file path. If set prints report to the specified file.
   
   `-r, --recursive`                        Recursive descent into subdirectories. By default only the specified
                                            directory is checked.
   
   `-v, --verbose`                          Verbose info to std output


 
*this is a work in progress*