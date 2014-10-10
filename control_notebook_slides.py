#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 Valerio Maggio <valeriomaggio@gmail.com>
# Licensed under the MIT License (MIT) - http://opensource.org/licenses/MIT

import os
import shlex, subprocess
from argparse import ArgumentParser

BLACK_LIST = ['index.ipynb', 'resources.ipynb', '00_programming_environment.ipynb']
NOTEBOOK_FOLDER_NAME = 'notebooks'
SLIDES_FOLDER_NAME = 'slides'

def nbconvert():
    """Select all the notebooks in the `NOTEBOOK_FOLDER_NAME` not appearing 
    in the `BLACK_LIST` and convert them to HTML slides! """
    
    # Get the list of notebooks available in the NOTEBOOK_FOLDER_NAME
    nb_folderpath = os.path.join(os.path.abspath(os.path.curdir), NOTEBOOK_FOLDER_NAME)
    notebook_file_list = filter(lambda f: os.path.isfile(os.path.join(nb_folderpath, f)) \
                                    and f.endswith('.ipynb') and not f.lower() in BLACK_LIST, 
                                os.listdir(nb_folderpath))
    notebook_file_path = [os.path.join('..', nb_folderpath, f) for f in notebook_file_list]
    
    # Compose the nbconvert command and split the arguments
    nbconvert_cmb = 'ipython nbconvert --to slides ' + ' '.join(notebook_file_path)
    nbconvert_args = shlex.split(nbconvert_cmb)

    # Change Current Working Directory and Move to the `Slides` folder
    os.chdir(os.path.join(os.path.abspath(os.path.curdir), SLIDES_FOLDER_NAME))
    
    print('='*75)
    print('\t\t Starting SLIDES generation')
    print('='*75)
    print('\n')
    proc = subprocess.Popen(nbconvert_args)
    try:
        outs, errs = proc.communicate()
    except Exception:
        proc.kill()
        outs, errs = proc.communicate()
        print('Slides generation exited with Errors!')
        print(errs)
    else:
        print('='*75)
        print('\t\t Slides generation terminated Successfully!! :)')
        print('='*75)
        print('\n')
        
def run_presentation():
    """Start serving slides available in the `SLIDE_FOLDER_NAME` starting from TOC"""
    
    
    
    # Check whether or not there exist HTML slides in the target folder
    slides_folderpath = os.path.join(os.path.abspath(os.path.curdir), SLIDES_FOLDER_NAME)
    available_slides = list(filter(lambda f: os.path.isfile(os.path.join(slides_folderpath, f)) \
                                and f.endswith('.slides.html'), os.listdir(slides_folderpath)))
       
    # Check for errors                         
    if not available_slides or not len(available_slides):
        print("The target Slides folder (i.e., {0}) does not contain any HTML file to serve".format(
                                                                            slides_folderpath))
        return
        
    if 'TOC.slides.html' not in available_slides:
        print("The target Slides folder (i.e., {0}) does not contain the TOC file to serve".format(
                                                                            slides_folderpath))
        return
    
    # So far, everything is fine...
    
    # Compose the nbconvert command and split the arguments
    nb_folderpath = os.path.join(os.path.abspath(os.path.curdir), NOTEBOOK_FOLDER_NAME)
    TOC_nb_filepath = os.path.join(nb_folderpath, 'TOC.ipynb')
    
    nbconvert_cmb = 'ipython nbconvert --to slides '+ TOC_nb_filepath +' --post serve'
    nbconvert_args = shlex.split(nbconvert_cmb)
    
    # Change Current Working Directory and Move to the `Slides` folder
    os.chdir(slides_folderpath)
    
    print('='*75)
    print('\t\t Serving Slides')
    print('='*75)
    print('\n')
    proc = subprocess.Popen(nbconvert_args)
    try:
        outs, errs = proc.communicate()
    except KeyboardInterrupt:
        proc.kill()
        outs, errs = proc.communicate()
        print('Stopping HTTP Server!')


if __name__ == '__main__':
    args_parser = ArgumentParser()
    args_parser.add_argument('-a', '--action', help='The action to perform', required=True,
                              choices=['convert', 'serve'], default='convert')
    
    args = args_parser.parse_args()
    if args.action == 'convert':
        nbconvert()
    else:
        run_presentation()
        
