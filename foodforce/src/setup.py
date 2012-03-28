#! /usr/bin/env/python

from distutils.core import setup
import os

MODULES = ['activity',
'chat',
'check_read_g_layout',
'defaultStyle',
'display_pannel',
'Exceptions',
'facilities',
'game_events',
'game_sharing',
'gui_buttons',
'gui',
'indicators',
'intial',
'initialize',
'interactor',
'level_change',
'load_images',
'model',
'natural_calamities',
'olpc_setup',
'proceduralFlow',
'profiling',
'run',
'setup',
'texts',
'threads',
'write_graphics_layout',
'write_storyboard']


SCRIPT = ['Foodforce2.py']

DATA_FILES=[('storyboards',[os.path.join("storyboards","storyboard1","images","character images","ajmal.png"),
                            os.path.join("storyboards","storyboard1","images","character images","kamat.png"),
                            os.path.join("storyboards","storyboard1","images","character images","panch.png"),
                            os.path.join("storyboards","storyboard1","images","character images","priest.png"),
                            os.path.join("storyboards","storyboard1","images","character images","son.png"),
                            os.path.join("storyboards","storyboard1","images","character images","sukhdev.png"),
                            os.path.join("storyboards","storyboard1","images","character images","villager.png")])
                                                                             ,('data', [os.path.join("data","tileset2.png"), 
                                                                                        os.path.join("data","logo.png"),
                                                                                        os.path.join("data","earthquake1.png"),
                                                                                        os.path.join("data","earthquake2.png"),
                                                                                        os.path.join("data","earthquake3.png"),
                                                                                        os.path.join("data","fountain.png"),
                                                                                        os.path.join("data","farm.png"),
                                                                                        os.path.join("data","top.png"),
                                                                                        os.path.join("data","Wfpwork.png"),
                                                                                        os.path.join("data","house_upgrade0.png"),
                                                                                        os.path.join("data","house_upgrade1.png"),
                                                                                        os.path.join("data","house_upgrade2.png"),
                                                                                        os.path.join("data","house_upgrade3.png"),
                                                                                        os.path.join("data","market.png"),
                                                                                        os.path.join("data","People.png"),
                                                                                        os.path.join("data","school_upgrade0.png"),
                                                                                        os.path.join("data","school_upgrade1.png"),
                                                                                        os.path.join("data","school_upgrade2.png"),
                                                                                        os.path.join("data","school_upgrade3.png"),
                                                                                        os.path.join("data","hospital_upgrade0.png"),
                                                                                        os.path.join("data","hospital_upgrade1.png"),
                                                                                        os.path.join("data","hospital_upgrade2.png"),
                                                                                        os.path.join("data","hospital_upgrade3.png"),
                                                                                        os.path.join("data","workshop_upgrade0.png"),
                                                                                        os.path.join("data","workshop_upgrade1.png"), 
                                                                                        os.path.join("data","workshop_upgrade2.png"),
                                                                                        os.path.join("data","workshop_upgrade3.png"),
                                                                                        os.path.join("data","soundtrack.ogg"),
                                                                                        os.path.join("data","dot_fountain.png"),
                                                                                        os.path.join("data","dot_farm.png"),
                                                                                        os.path.join("data","dot_workshop.png"),
                                                                                        os.path.join("data","dot_school.png"),
                                                                                        os.path.join("data","dot_hospital.png"),
                                                                                        os.path.join("data","dot_house.png"),
                                                                                        os.path.join("data","dot_market.png"),
                                                                                        os.path.join("data",'Happy.png'),
                                                                                        os.path.join("data",'prosper.png'),
                                                                                        os.path.join("data",'drought.png'),
                                                                                        os.path.join("data",'earthquake_st.png'),
                                                                                        os.path.join("data","WFPLOGO.png"),
                                                                                        os.path.join("data","map.png")])
                                                                                                                                 ,('art', [os.path.join('art','button.png')
                                                                                                                                          ,os.path.join('art','closebutton.png')
                                                                                                                                          ,os.path.join('art','optionbox.png')
                                                                                                                                          ,os.path.join('art','shadebutton.png')
                                                                                                                                          ,os.path.join('art','checkbox.png')
                                                                                                                                          ,os.path.join('art','combobox.png')
                                                                                                                                          ,os.path.join('art','ff2_cursor.xbm')
                                                                                                                                          ,os.path.join('art','ff2_cursor-mask.xbm')                                        
                                                                                                                                          ,os.path.join('art','imageBox.png')
                                                                                                                                          ,os.path.join('art','chatBox.png')                                                                                                                                                                                                                         
                                                                                                                                           ,os.path.join('art','button_green.png')])
                                                         ,('.',['font.ttf'
                                                                ,'data.pkl'
                                                                ,'graphics_layout.pkl'
                                                                ,'storyboard.pkl'
                                                                ,'data2.pkl'
                                                                ,'data3.pkl'
                                                                ,'data4.pkl'
                                                                ,'data5.pkl'
                                                                ,'data6.pkl'
                                                                ,'data7.pkl'
                                                                ,'data8.pkl']) ]

setup(
    name='Foodforce2',
    version='1.0',
    author='Mohit Taneja',
    maintainer='Grivan Thapar',
    long_description='FoodForce2 is an effort towards eliminating the world hunger and providing an intutive platorm for children to learn and sharpen their analytical skills',
	license='GPLv2+',
    description='Educational Learning Game Built On PyGame',
    url='http://www.foodforce2.com',
    requires='pygame',
    py_modules=MODULES,
    scripts = SCRIPT,
    data_files = DATA_FILES
    
)
