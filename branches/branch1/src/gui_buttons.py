#! /usr/bin/env python
#

# ***** BEGIN LICENSE BLOCK *****
# Version: CPAL 1.0
#
# The contents of this file are subject to the Common Public Attribution
# License Version 1.0 (CPAL); you may not use this file except in
# compliance with the License. You may obtain a copy of the License at
# http://opensource.org/licenses/cpal_1.0
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# ***** END LICENSE BLOCK ****
#

from sys import exit
import os
from time import *
#from threades import *
import threades
import threading

import gui
#from gui import *
import pygame
import load_images
#from model import *
import model
ActivitySharedFlag = False

class marketBarChart:
    '''Class which displays the bar chart in the market window
    '''
    color1 = (255,214,150)
    color2 = (170,142,100)
    #color3 = (85,71,50)
    color_rect = (50,100,150)
    
    def drawValueChart(self,surface,initial_value = 10,maximum_value = 100.0):
        ''' Draws a barchart on the screen
        '''
        
        self.price_flag = False
        self.surf = surface
        self.bar1Val = initial_value
        self.bar1ValMax = maximum_value
        pygame.draw.rect(surface,self.color1,threades.resize_rect((440,200,200*self.bar1Val/self.bar1ValMax,30)))
        
        pygame.draw.rect(surface,self.color_rect,threades.resize_rect((440,200,200,30)),2)
        
    def drawPriceChart(self,surface,initial_price = 10, maximum_value = 25):
        ''' Draws a barchart on the screen
        '''
        if self.price_flag == False:
            self.price_flag = True
            self.bar2Val = initial_price
            self.bar2ValMax = maximum_value
            pygame.draw.rect(surface,self.color2,threades.resize_rect((440,280,200*self.bar2Val/self.bar2ValMax,30)))
        
            pygame.draw.rect(surface,self.color_rect,threades.resize_rect((440,280,200,30)),2)
        
      
    def updateChart(self,(x,y)):
        ''' Updates the bar chart on the basis of the mouse click
        '''
        surface = self.surf
        if (x>threades.resize_pt_x(640)) and (x<threades.resize_pt_x(840)) and (y>threades.resize_pt_y(250)) and (y<threades.resize_pt_y(280)):
            pygame.draw.rect(surface,(0,0,0),threades.resize_rect((440,200,200,50)))
            
            self.bar1Val = (x-threades.resize_pt_x(640))*self.bar1ValMax/threades.resize_pt_x(200)
            
            if self.bar1Val > self.bar1ValMax:
                self.bar1Val = self.bar1ValMax
            if self.bar1Val < 0:
                self.bar1Val = 0
            
            pygame.draw.rect(surface,self.color1,threades.resize_rect((440,200,200*self.bar1Val/self.bar1ValMax,30)))
        
            pygame.draw.rect(surface,self.color_rect,threades.resize_rect((440,200,200,30)),2)
            gui_obj.buysell_obj.updateMarketLabelValues()
        
        if self.price_flag:
            if (x>threades.resize_pt_x(640)) and (x<threades.resize_pt_x(840)) and (y>threades.resize_pt_y(330)) and (y<threades.resize_pt_y(360)):
                pygame.draw.rect(surface,(0,0,0),threades.resize_rect((440,280,200,30)))
                
                self.bar2Val = (x-threades.resize_pt_x(640))*self.bar2ValMax/threades.resize_pt_x(200)
                
                if self.bar2Val > self.bar2ValMax:
                    self.bar2Val = self.bar2ValMax
                if self.bar2Val < 0:
                    self.bar2Val = 0
                
                pygame.draw.rect(surface,self.color2,threades.resize_rect((440,280,200*self.bar2Val/self.bar2ValMax,30)))
        
                pygame.draw.rect(surface,self.color_rect,threades.resize_rect((440,280,200,30)),2)
                gui_obj.buysell_obj.updateMarketLabelValues()
        
        #gui_obj.buysell_obj.drawPriceChart()
        
    def deletePriceChart(self):
        
        if self.price_flag:
            pygame.draw.rect(self.surf,(0,0,0),threades.resize_rect((438,278,234,34)))
            self.price_flag = False
            #gui_obj.buysell_obj.label_res_price_flag = False
            gui_obj.buysell_obj.label_res_price.text = ''
            gui_obj.buysell_obj.label_price.text = ''
            self.bar2Val = 10
                
      
    
class barChart:
    
    ''' Class which displays the bar chart and handles it
    '''
    color1 = (255,214,150)
    color2 = (170,142,100)
    color3 = (85,71,50)
    color_rect = (50,100,150)
    
    def drawChart(self,surface,rice,vegetables,beans):
        ''' Draws a barchart on the screen
        '''
        
        self.surf = surface
        self.bar1Val = rice
        self.bar2Val = vegetables
        self.bar3Val = beans
        
        
        pygame.draw.rect(surface,self.color1,threades.resize_rect((100,50.0+200*(100-self.bar1Val)/100,50,200*self.bar1Val/100.0)))
        pygame.draw.rect(surface,self.color2,threades.resize_rect((250,50.0+200*(100-self.bar2Val)/100,50,200*self.bar2Val/100.0)))
        pygame.draw.rect(surface,self.color3,threades.resize_rect((400,50.0+200*(100-self.bar3Val)/100,50,200*self.bar3Val/100.0)))
        
        pygame.draw.rect(surface,self.color_rect,threades.resize_rect((100,50,50,200)),2)
        pygame.draw.rect(surface,self.color_rect,threades.resize_rect((250,50,50,200)),2)
        pygame.draw.rect(surface,self.color_rect,threades.resize_rect((400,50,50,200)),2)
        
    def updateChart(self,(x,y)):
        ''' Updates the bar chart on the basis of the mouse click
        '''
        surface = self.surf
        if (x>threades.resize_pt_x(400)) and (x<threades.resize_pt_x(450)) and (y>threades.resize_pt_y(200)) and (y<threades.resize_pt_y(400)):
            pygame.draw.rect(surface,(0,0,0),threades.resize_rect((100,50,350,200)))
            change = self.bar1Val - (threades.resize_pt_y(400)-y)*100/threades.resize_pt_y(200.0)
            self.bar1Val = self.bar1Val - change
            self.bar2Val = self.bar2Val +change/2
            self.bar3Val = self.bar3Val +change/2
            
            if self.bar1Val > 100:
                self.bar1Val = 100
            if self.bar1Val < 0:
                self.bar1Val = 0
            if self.bar2Val > 100:
                self.bar2Val = 100
            if self.bar2Val < 0:
                self.bar2Val = 0
            if self.bar3Val > 100:
                self.bar3Val = 100
            if self.bar3Val < 0:
                self.bar3Val = 0
            
            pygame.draw.rect(surface,self.color1,threades.resize_rect((100,50.0+200*(100-self.bar1Val)/100,50,200*self.bar1Val/100.0)))
            pygame.draw.rect(surface,self.color2,threades.resize_rect((250,50.0+200*(100-self.bar2Val)/100,50,200*self.bar2Val/100.0)))
            pygame.draw.rect(surface,self.color3,threades.resize_rect((400,50.0+200*(100-self.bar3Val)/100,50,200*self.bar3Val/100.0)))

            pygame.draw.rect(surface,self.color_rect,threades.resize_rect((100,50,50,200)),2)
            pygame.draw.rect(surface,self.color_rect,threades.resize_rect((250,50,50,200)),2)
            pygame.draw.rect(surface,self.color_rect,threades.resize_rect((400,50,50,200)),2)
            
            
            
        if (x>threades.resize_pt_x(550)) and (x<threades.resize_pt_x(600)) and (y>threades.resize_pt_y(200)) and (y<threades.resize_pt_y(400)):
            pygame.draw.rect(surface,(0,0,0),threades.resize_rect((100,50,350,200)))
            change = self.bar2Val - (threades.resize_pt_y(400)-y)*100/threades.resize_pt_y(200.0)
            self.bar2Val = self.bar2Val - change
            self.bar1Val = self.bar1Val + change/2
            self.bar3Val = self.bar3Val + change/2
            
            if self.bar1Val > 100:
                self.bar1Val = 100
            if self.bar1Val < 0:
                self.bar1Val = 0
            if self.bar2Val > 100:
                self.bar2Val = 100
            if self.bar2Val < 0:
                self.bar2Val = 0
            if self.bar3Val > 100:
                self.bar3Val = 100
            if self.bar3Val < 0:
                self.bar3Val = 0
            
            pygame.draw.rect(surface,self.color1,threades.resize_rect((100,50.0+200*(100-self.bar1Val)/100,50,200*self.bar1Val/100.0)))
            pygame.draw.rect(surface,self.color2,threades.resize_rect((250,50.0+200*(100-self.bar2Val)/100,50,200*self.bar2Val/100.0)))
            pygame.draw.rect(surface,self.color3,threades.resize_rect((400,50.0+200*(100-self.bar3Val)/100,50,200*self.bar3Val/100.0)))

            pygame.draw.rect(surface,self.color_rect,threades.resize_rect((100,50,50,200)),2)
            pygame.draw.rect(surface,self.color_rect,threades.resize_rect((250,50,50,200)),2)
            pygame.draw.rect(surface,self.color_rect,threades.resize_rect((400,50,50,200)),2)
            
            
            
        if (x>threades.resize_pt_x(700)) and (x<threades.resize_pt_x(750)) and (y>threades.resize_pt_y(200)) and (y<threades.resize_pt_y(400)):
            pygame.draw.rect(surface,(0,0,0),threades.resize_rect((100,50,350,200)))
            change = self.bar3Val - (threades.resize_pt_y(400)-y)*100/threades.resize_pt_y(200.0)
            self.bar3Val = self.bar3Val - change
            self.bar2Val = self.bar2Val + change/2
            self.bar1Val = self.bar1Val + change/2
            
            if self.bar1Val > 100:
                self.bar1Val = 100
            if self.bar1Val < 0:
                self.bar1Val = 0
            if self.bar2Val > 100:
                self.bar2Val = 100
            if self.bar2Val < 0:
                self.bar2Val = 0
            if self.bar3Val > 100:
                self.bar3Val = 100
            if self.bar3Val < 0:
                self.bar3Val = 0
            
            pygame.draw.rect(surface,self.color1,threades.resize_rect((100,50.0+200*(100-self.bar1Val)/100,50,200*self.bar1Val/100.0)))
            pygame.draw.rect(surface,self.color2,threades.resize_rect((250,50.0+200*(100-self.bar2Val)/100,50,200*self.bar2Val/100.0)))
            pygame.draw.rect(surface,self.color3,threades.resize_rect((400,50.0+200*(100-self.bar3Val)/100,50,200*self.bar3Val/100.0)))
            
            pygame.draw.rect(surface,self.color_rect,threades.resize_rect((100,50,50,200)),2)
            pygame.draw.rect(surface,self.color_rect,threades.resize_rect((250,50,50,200)),2)
            pygame.draw.rect(surface,self.color_rect,threades.resize_rect((400,50,50,200)),2)
            
            
       
        


class setup_button:

    ''' Class which handles the windows when the setup button is clicked
    '''
    rect_color = (255,214,150)
    color_grey = (160,160,160)
    
    def __init__(self):
        
        self.win_flag = False
        self.child_win_flag = False
        
    
    def setup(self,button=None):
        ''' Initiated when the button for setting up a facility is clicked
        '''
        
        
        gui_obj.disable_buttons()
        myfont = pygame.font.Font("font.ttf", threades.resize_pt(20))

        # Custom gui.Window Style
        win_style = gui.defaultWindowStyle.copy()
        win_style['font'] = myfont
        win_style['font-color'] = self.rect_color
        win_style['bg-color'] = (0,0,0)

        # Calculating position and size of window from the size of the threades.desktop        
        position_win =threades.resize_pos((200.0,50.0))
        size_win =threades.resize_pos((800.0,600.0))

        # Creating window
        self.win = gui.Window(position = position_win, size = size_win, parent = threades.desktop, text = "Set up a facility for your village " ,style = win_style,shadeable = False)
        #self.win.surf.blit(load_images.School_tiles_list[3][2],(0,0))
        self.win.surf.set_alpha(140) 
        self.win.onClose = lambda button: self.close_win_safe()
        self.win_flag = True
        
        # Pausing the update thread
        #threades.pause_update_thread()
        
        #  Creating Custom label style
        myfont2 = pygame.font.Font("font.ttf", threades.resize_pt(16))
        myfont3 = pygame.font.Font("font.ttf", threades.resize_pt(14))
        labelStyleCopy = gui.defaultLabelStyle.copy()
        labelStyleCopy['border-width'] = 1
        labelStyleCopy['wordwrap'] = True
        labelStyleCopy['autosize'] = False
        labelStyleCopy['font'] = myfont2
        labelStyleCopy['font-color'] = self.rect_color
        labelStyleCopy['border-color'] = self.color_grey
        default_text = 'What would you like to set up? Choose a facility from the list and press the Set Up button.'
        self.message_label = gui.Label(position = threades.resize_pos((450,120),(800.0,600.0),self.win.size),size = threades.resize_pos((250,100),(800.0,600.0),self.win.size), parent = self.win, text = default_text, style = labelStyleCopy)
        text ='Please select a Facility to see its status and Requirements' 
        labelStyleCopy2 = gui.defaultLabelStyle.copy()
        labelStyleCopy2['border-width'] = 1
        labelStyleCopy2['wordwrap'] = True
        labelStyleCopy2['autosize'] = False
        labelStyleCopy2['font'] = myfont3
        labelStyleCopy2['font-color'] = self.rect_color
        labelStyleCopy2['border-color'] = self.color_grey

        self.message_label2 = gui.Label(position = threades.resize_pos((20,400),(800.0,600.0),self.win.size),size = threades.resize_pos((570,120),(800.0,600.0),self.win.size), parent = self.win, text = text, style = labelStyleCopy2)

        # creating custom style for option box
        op_style = gui.defaultOptionBoxStyle.copy()
        op_style['font'] = myfont
        op_style['font-color'] = self.rect_color
        op_style['autosize'] = True
        op_style['word wrap'] = False
        # Creating option boxes for all the facilities
        position_optionbox = threades.resize_pos((200.0,150.0),(800.0,600.0),size_win)        
        self.housing_box = gui.OptionBox(position = position_optionbox, parent = self.win, style = op_style, text = 'House')
        self.housing_box.onClick =  self.on_select_setup_option_box
        self.hospital_box = gui.OptionBox(position = self.win.nextPosition(threades.resize_pt_y(10)), parent = self.win, style = op_style, text = 'Hospital')
        self.hospital_box.onClick = self.on_select_setup_option_box
        self.workshop_box = gui.OptionBox(position = self.win.nextPosition(threades.resize_pt_y(10)), parent = self.win, style = op_style, text = 'Workshop')
        self.workshop_box.onClick = self.on_select_setup_option_box
        self.school_box = gui.OptionBox(position = self.win.nextPosition(threades.resize_pt_y(10)), parent = self.win, style = op_style, text = 'School')
        self.school_box.onClick = self.on_select_setup_option_box
        self.farm_box = gui.OptionBox(position = self.win.nextPosition(threades.resize_pt_y(10)), parent = self.win, style = op_style, text = 'Farm')
        self.farm_box.onClick = self.on_select_setup_option_box
        self.fountain_box = gui.OptionBox(position = self.win.nextPosition(threades.resize_pt_y(10)), parent = self.win, style = op_style, text = 'Well')
        self.fountain_box.onClick = self.on_select_setup_option_box

        #self.win.surf.set_alpha(255)
        #background = self.win.surf.subsurface(pygame.Rect(threades.resize_rect((400,180,200,200))))
        #self.background_pic = background.copy()
        #self.win.surf.set_alpha(140)

        # Creating buttons for Setting up the facility and closing the setup window
        button_style = gui.defaultButtonStyle.copy()
        button_style['font'] = myfont2

        self.button_setup = gui.Button(position = threades.resize_pos((600.0,420.0),(800.0,600.0),size_win), size = threades.resize_pos((120.0,50.0),(800.0,600.0),size_win), parent = self.win, text = "Set Up",style = button_style)
        #self.button_close = gui.Button(position = threades.resize_pos((600.0,460.0),(800.0,600.0),size_win), size = threades.resize_pos((120.0,50.0),(800.0,600.0),size_win), parent = self.win, text = "Close",style = button_style)
        #self.button_close.onClick  = self.close_win
        self.button_setup.onClick = self.setup_facility

    def on_select_setup_option_box(self,button):

        #self.win.surf.set_alpha(255)
        #self.win.surf.blit(self.background_pic,threades.resize_pos((450,250)))
        #self.win.surf.set_alpha(140)

        if button.text == 'House':
            text = 'House: '
            #image = load_images. House_tiles_list[2][2]
            text += threades.get_setup_text(model.House)
        if button.text == 'Hospital':
            text = 'Hospital: '
            #image = load_images. Hospital_tiles_list[2][2]
            text += threades.get_setup_text(model.Hospital)
        if button.text == 'School':
            text = 'School: '
            #image = load_images.School_tiles_list[2][2]
            text += threades.get_setup_text(model.School)
        if button.text == 'Workshop':
            text = 'Workshop: '
            #image = load_images.Workshop_tiles_list[2][2]
            text += threades.get_setup_text(model.Workshop)
        if button.text == 'Farm':
            text = 'Farm: '
            #image = load_images.Farm_tiles[0][1]
            text += threades.get_setup_text(model.Farm)
        if button.text == 'Well':
            text = 'Well: '
            #image = load_images.Fountain_tiles[0][3]
            text += threades.get_setup_text(model.Fountain)
        #display_image = pygame.transform.scale(image,threades.resize_pos((140,140)))
        #self.win.surf.blit(display_image,threades.resize_pos((450,250)))
        self.message_label2.text = text



    def close_win(self,button=None):
        self.win.close()
        self.win_flag = False
        gui_obj.enable_buttons()

    def close_win_safe(self,button = None):
        self.win_flag = False
        gui_obj.enable_buttons()


    def setup_facility(self,button=None):
        ''' Sets up the facility
        '''


        if self.housing_box.value:
            label_text =  threades.build_facility(model.House)
        elif self.hospital_box.value:
            label_text =  threades.build_facility(model.Hospital)
        elif self.workshop_box.value:
            label_text =  threades.build_facility(model.Workshop)
        elif self.fountain_box.value:
            label_text =  threades.build_facility(model.Fountain)
        elif self.school_box.value:
            label_text =  threades.build_facility(model.School)
        elif self.farm_box.value:
            label_text =  self.build_facility_farm()
        else:
            label_text = ' Please select a Facility for building'
        self.message_label.text = label_text
        if label_text== 'Facility has been build':
            self.close_win()

    def build_facility_farm(self):

        myfont = pygame.font.Font("font.ttf",threades.resize_pt(22))

        # Custom gui.Window Style
        win_style = gui.defaultWindowStyle.copy()
        win_style['font'] = myfont
        win_style['font-color'] = self.rect_color
        win_style['bg-color'] = (0,0,0)

        # Calculating position and size of window from the size of the threades.desktop        
        position_win =threades.resize_pos((300.0,150.0))
        size_win =threades.resize_pos((600.0,400.0))

        # Creating window
        self.child_win = gui.Window(position = position_win, size = size_win, parent = threades.desktop, text = "Setup Farm " ,style = win_style,shadeable = False,moveable = False)
        #self.child_win.surf.set_alpha(190) 
        self.win.enabled = False
        self.child_win_flag = True
        self.child_win.onClose = lambda button: self.enable_parent_win()

        self.bardisplay = barChart()
        self.bardisplay.drawChart(self.child_win.surf,33,33,34)
        
        # Creating custom label style1
        myfont2 = pygame.font.Font("font.ttf",threades.resize_pt(16))
        labelstyle1 = gui.defaultLabelStyle.copy()
        labelstyle1['border-width'] = 0
        labelstyle1['wordwrap'] = False
        labelstyle1['autosize'] = True
        labelstyle1['font'] = myfont2
        labelstyle1['font-color'] = self.rect_color

        label_rice = gui.Label(position = threades.resize_pos((100.0,260.0),(600.0,400.0),self.child_win.size), parent = self.child_win, text = 'Rice', style = labelstyle1)
        label_veg = gui.Label(position = threades.resize_pos((250.0,260.0),(600.0,400.0),self.child_win.size), parent = self.child_win, text = 'Fruit and \nVegetables', style = labelstyle1)
        label_beans = gui.Label(position = threades.resize_pos((400.0,260.0),(600.0,400.0),self.child_win.size), parent = self.child_win, text = 'Beans', style = labelstyle1)

        # Creating second custom label style
        labelStyleCopy2 = gui.defaultLabelStyle.copy()
        labelStyleCopy2['border-width'] = 0
        labelStyleCopy2['wordwrap'] = True
        labelStyleCopy2['autosize'] = False
        labelStyleCopy2['font'] = myfont2
        labelStyleCopy2['border-color'] = self.rect_color
        labelStyleCopy2['font-color'] = self.rect_color
        
        text = 'Balance the bar chart to select the percentages of different food items you want to grow in your farm'
        self.message_label2 = gui.Label(position = threades.resize_pos((20,320),(600.0,400.0),self.child_win.size),size = threades.resize_pos((470,70),(600.0,400.0),self.child_win.size), parent = self.child_win, text = text, style = labelStyleCopy2)

        '''
        # Creating custom text box style
        textbox_style = gui.defaultTextBoxStyle.copy()
        textbox_style['font'] = myfont2
        textbox_style['font-color'] = self.rect_color
        self.textbox_rice = TextBox(position = threades.resize_pos((300.0, 70.0),(600.0,400.0),self.child_win.size), size = threades.resize_pos((50,20),(600.0,400.0),self.child_win.size), parent = self.child_win, style = textbox_style) 
        self.textbox_veg = TextBox(position = threades.resize_pos((300.0, 110.0),(600.0,400.0),self.child_win.size), size = threades.resize_pos((50,20),(600.0,400.0),self.child_win.size), parent = self.child_win, style = textbox_style) 
        self.textbox_beans = TextBox(position = threades.resize_pos((300.0, 150.0),(600.0,400.0),self.child_win.size), size = threades.resize_pos((50,20),(600.0,400.0),self.child_win.size), parent = self.child_win, style = textbox_style) 
        '''
        
        # Custom button style        
        button_style = gui.defaultButtonStyle.copy()
        button_style['font'] = myfont2

        self.button_setup_farm = gui.Button(position = threades.resize_pos((500.0,320.0),(600.0,400.0),size_win), size = threades.resize_pos((80.0,50.0),(600.0,400.0),size_win), parent = self.child_win, text = "Set Up",style = button_style)
        self.button_setup_farm.onClick = self.setup_facility_farm

        self.return_text_farm = ' '
        return self.return_text_farm


    def setup_facility_farm(self,button=None):

        # Finally setting up the facility after the button is clicked
        quantity1 = self.bardisplay.bar1Val
        quantity2 = self.bardisplay.bar2Val
        quantity3 = self.bardisplay.bar3Val
        list_food = [quantity1,quantity2,quantity3]
        label_text = threades.build_facility(model.Farm,list_food)
        self.child_win.close()
        self.enable_parent_win()
        self.close_win()
        return

    def enable_parent_win(self):
        self.child_win_flag = False
        self.win.enabled = True

    def get_win_flag(self):
        return self.win_flag

    def get_child_win_flag(self):
        return self.child_win_flag

        
class upgrade_button:

    rect_color = (255,214,150)
    color_grey = (160,160,160)
    
    def __init__(self):
        
        self.win_flag = False
        self.child_win_flag = False
        
        # Functions for upgrading a facility
    def upgrade(self,button=None):
        ''' Initiated when the button for upgrading a facility is clicked
        '''
        gui_obj.disable_buttons()
        myfont = pygame.font.Font("font.ttf", threades.resize_pt(20))

        # Custom gui.Window Style
        win_style = gui.defaultWindowStyle.copy()
        win_style['font'] = myfont
        win_style['font-color'] = self.rect_color
        win_style['bg-color'] = (0,0,0)

        # Calculating position and size of window from the size of the threades.desktop        
        position_win =threades.resize_pos((200.0,50.0))
        size_win =threades.resize_pos((800.0,600.0))

        # Creating window
        self.win = gui.Window(position = position_win, size = size_win, parent = threades.desktop, text = "Upgrade Facility " ,style = win_style,shadeable = False)
        self.win.surf.set_alpha(140) 
        self.win.onClose = lambda button: self.close_win_safe()
        self.win_flag = True

        # Pausing the update thread
        #threades.pause_update_thread()
        
        #  Creating Custom label style
        myfont2 = pygame.font.Font("font.ttf", threades.resize_pt(16))
        labelStyleCopy = gui.defaultLabelStyle.copy()
        labelStyleCopy['border-width'] = 1
        labelStyleCopy['wordwrap'] = True
        labelStyleCopy['autosize'] = False
        labelStyleCopy['font'] = myfont2
        labelStyleCopy['font-color'] = self.rect_color
        labelStyleCopy['border-color'] = self.color_grey
        text = 'Please select a Facility and press Upgrade button to upgrade.'
        self.message_label = gui.Label(position = threades.resize_pos((450,150),(800.0,600.0),self.win.size),size = threades.resize_pos((200,100),(800.0,600.0),self.win.size), parent = self.win, text = text, style = labelStyleCopy)


        # creating custom style for option box
        op_style = gui.defaultOptionBoxStyle.copy()
        op_style['font'] = myfont
        op_style['font-color'] = self.rect_color
        op_style['autosize'] = True
        op_style['word wrap'] = False
        # Creating option boxes for all the facilities
        position_optionbox = threades.resize_pos((200.0,150.0),(800.0,600.0),size_win)        
        self.housing_box = gui.OptionBox(position = position_optionbox, parent = self.win, style = op_style, text = 'House')
        self.housing_box.onClick =  self.on_select_upgrade_option_box
        self.hospital_box = gui.OptionBox(position = self.win.nextPosition(threades.resize_pt_y(10)), parent = self.win, style = op_style, text = 'Hospital')
        self.hospital_box.onClick = self.on_select_upgrade_option_box
        self.workshop_box = gui.OptionBox(position = self.win.nextPosition(threades.resize_pt_y(10)), parent = self.win, style = op_style, text = 'Workshop')
        self.workshop_box.onClick = self.on_select_upgrade_option_box
        self.school_box = gui.OptionBox(position = self.win.nextPosition(threades.resize_pt_y(10)), parent = self.win, style = op_style, text = 'School')
        self.school_box.onClick = self.on_select_upgrade_option_box
        self.farm_box = gui.OptionBox(position = self.win.nextPosition(threades.resize_pt_y(10)), parent = self.win, style = op_style, text = 'Farm')
        self.farm_box.onClick = self.on_select_upgrade_option_box
        self.fountain_box = gui.OptionBox(position = self.win.nextPosition(threades.resize_pt_y(10)), parent = self.win, style = op_style, text = 'Well')
        self.fountain_box.onClick = self.on_select_upgrade_option_box
        myfont3 = pygame.font.Font("font.ttf", threades.resize_pt(14))
        text ='Please select a Facility to see its next upgrade' 
        labelStyleCopy2 = gui.defaultLabelStyle.copy()
        labelStyleCopy2['border-width'] = 1
        labelStyleCopy2['wordwrap'] = True
        labelStyleCopy2['autosize'] = False
        labelStyleCopy2['font'] = myfont3
        labelStyleCopy2['font-color'] = self.rect_color
        labelStyleCopy2['border-color'] = self.color_grey

        self.message_label2 = gui.Label(position = threades.resize_pos((20,400),(800.0,600.0),self.win.size),size = threades.resize_pos((570,120),(800.0,600.0),self.win.size), parent = self.win, text = text, style = labelStyleCopy2)

        # Creating buttons for Setting up the facility and closing the setup window
        button_style = gui.defaultButtonStyle.copy()
        button_style['font'] = myfont2
        
        #self.win.surf.set_alpha(255)
        #background = self.win.surf.subsurface(pygame.Rect(threades.resize_rect((400,180,200,200))))
        #self.background_pic = background.copy()
        #self.win.surf.set_alpha(140)

        self.button_upgrade = gui.Button(position = threades.resize_pos((600.0,420.0),(800.0,600.0),size_win), size = threades.resize_pos((120.0,50.0),(800.0,600.0),size_win), parent = self.win, text = "Upgrade",style = button_style)
        #self.button_close = gui.Button(position = threades.resize_pos((600.0,460.0),(800.0,600.0),size_win), size = threades.resize_pos((120.0,50.0),(800.0,600.0),size_win), parent = self.win, text = "Close",style = button_style)
        #self.button_close.onClick  = self.close_win
        self.button_upgrade.onClick = self.upgrade_facility

    def on_select_upgrade_option_box(self,button):
        
        #self.win.surf.set_alpha(255)
        #self.win.surf.blit(self.background_pic,threades.resize_pos((450,250)))
        #self.win.surf.set_alpha(140)

        text = ''
        if button.text == 'House':
            #image = load_images. House_tiles_list[2][2]
            text += threades.get_upgrade_text(model.House)
        if button.text == 'Hospital':
            #image = load_images. Hospital_tiles_list[2][2]
            text += threades.get_upgrade_text(model.Hospital)
        if button.text == 'School':
            #image = load_images.School_tiles_list[2][2]
            text += threades.get_upgrade_text(model.School)
        if button.text == 'Workshop':
            #image = load_images.Workshop_tiles_list[2][2]
            text += threades.get_upgrade_text(model.Workshop)
        if button.text == 'Farm':
            #image = load_images.Farm_tiles[0][1]
            text += threades.get_upgrade_text(model.Farm)
        if button.text == 'Well':
            #image = load_images.Fountain_tiles[0][3]
            text += threades.get_upgrade_text(model.Fountain)
        #display_image = pygame.transform.scale(image,threades.resize_pos((140,140)))
        #self.win.surf.blit(display_image,threades.resize_pos((450,250)))
        self.message_label2.text = text
        self.message_label.text = 'Upgrades ' + button.text

    def upgrade_facility(self,button=None):
        ''' Upgrades the facility
        '''


        if self.housing_box.value:
            label_text =  threades.upgrade_facility(model.House)
        elif self.hospital_box.value:
            label_text =  threades.upgrade_facility(model.Hospital)
        elif self.workshop_box.value:
            label_text =  threades.upgrade_facility(model.Workshop)
        elif self.fountain_box.value:
            label_text =  threades.upgrade_facility(model.Fountain)
        elif self.school_box.value:
            label_text =  threades.upgrade_facility(model.School)
        elif self.farm_box.value:
            label_text =  threades.upgrade_facility(model.Farm)
        else:
            label_text = ' Please select a Facility for Upgrading'
        self.message_label.text = label_text
        if label_text== 'Facility has been upgraded':
            self.close_win()

    # Functions for upgrading a facility end here........
    def close_win(self,button=None):
        self.win.close()
        self.win_flag = False
        gui_obj.enable_buttons()

    def close_win_safe(self,button = None):
        self.win_flag = False
        gui_obj.enable_buttons()


    def get_win_flag(self):
        return self.win_flag

   
class buysell_button:

    rect_color = (255,214,150)
    color_grey = (160,160,160)
    
    def __init__(self):
        
        self.win_flag = False
        self.child_win_flag = False
        
   
    
    # Functions for Buy/Sell operation begin here
    def buysell(self,button=None):
        ''' Initiated when the button for buy/sell operation is pressed.
        '''

        global ActivitySharedFlag
        gui_obj.disable_buttons()
        myfont = pygame.font.Font("font.ttf", threades.resize_pt(20))

        # Custom gui.Window Style
        win_style = gui.defaultWindowStyle.copy()
        win_style['font'] = myfont
        win_style['font-color'] = self.rect_color
        win_style['bg-color'] = (0,0,0)

        # Focus the animation window on the market
        threades.transform_obj.focus_at((3200,2600)) # Replace this with the coordinates ofthe market in the base surface

        # Calculating position and size of window from the size of the threades.desktop        
        position_win =threades.resize_pos((200.0,50.0))
        size_win =threades.resize_pos((800.0,600.0))

        # Creating window
        self.win = gui.Window(position = position_win, size = size_win, parent = threades.desktop, text = " Buy or Sell Resources " ,style = win_style,shadeable = False, moveable = False)
        self.win.surf.set_alpha(140) 
        self.win.onClose = lambda button: self.close_win_safe()
        self.win_flag = True

        # Pausing the update thread
        #threades.pause_update_thread()

        # Creating custom label style1
        myfont2 = pygame.font.Font("font.ttf",threades.resize_pt(16))
        labelstyle1 = gui.defaultLabelStyle.copy()
        labelstyle1['border-width'] = 0
        labelstyle1['wordwrap'] = False
        labelstyle1['autosize'] = True
        labelstyle1['font'] = myfont2
        labelstyle1['font-color'] = self.rect_color

        heading_label1 = gui.Label(position = threades.resize_pos((10.0,70.0),(800.0,600.0),self.win.size), parent = self.win, text = 'Resources', style = labelstyle1)
        heading_label2 = gui.Label(position = threades.resize_pos((180.0,70.0),(800.0,600.0),self.win.size), parent = self.win, text = 'Village', style = labelstyle1)
        heading_label3 = gui.Label(position = threades.resize_pos((180.0,85.0),(800.0,600.0),self.win.size), parent = self.win, text = 'Quantity', style = labelstyle1)
        heading_label4 = gui.Label(position = threades.resize_pos((370.0,70.0),(800.0,600.0),self.win.size), parent = self.win, text = 'Price', style = labelstyle1)
        #heading_label5 = gui.Label(position = threades.resize_pos((520.0,70.0),(800.0,600.0),self.win.size), parent = self.win, text = 'Resources', style = labelstyle1)
        heading_label6 = gui.Label(position = threades.resize_pos((270.0,70.0),(800.0,600.0),self.win.size), parent = self.win, text = 'Market', style = labelstyle1)
        heading_label7 = gui.Label(position = threades.resize_pos((270.0,85.0),(800.0,600.0),self.win.size), parent = self.win, text = 'Quantity', style = labelstyle1)

        # creating custom style for option box
        op_style = gui.defaultOptionBoxStyle.copy()
        op_style['font'] = myfont2
        op_style['font-color'] = self.rect_color
        op_style['autosize'] = True
        op_style['word wrap'] = False

        # Creating option boxes for all the resources
        position_optionbox = threades.resize_pos((10.0,140.0),(800.0,600.0),self.win.size)        
        self.water_box = gui.OptionBox(position = position_optionbox, parent = self.win, style = op_style, text = 'Water')
        self.buildmat_box = gui.OptionBox(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, style = op_style, text = 'Building Materials')
        self.tools_box = gui.OptionBox(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, style = op_style, text = 'Tools')
        self.books_box = gui.OptionBox(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, style = op_style, text = 'Books')
        self.medicine_box = gui.OptionBox(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, style = op_style, text = 'Medicines')
        self.rice_box = gui.OptionBox(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, style = op_style, text = 'Rice')
        self.wheat_box = gui.OptionBox(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, style = op_style, text = 'Fruit & Vegatables')
        self.beans_box = gui.OptionBox(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, style = op_style, text = 'Beans')
        self.sugar_box = gui.OptionBox(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, style = op_style, text = 'Sugar')
        self.salt_box = gui.OptionBox(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, style = op_style, text = 'Salt')
        self.oil_box = gui.OptionBox(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, style = op_style, text = 'Oil')
        
        #Creating CheckBox style
        ch_style = gui.defaultCheckBoxStyle.copy()
        ch_style['font'] = myfont2
        ch_style['font-color'] = self.rect_color
        ch_style['autosize'] = True
        #ch_style['word wrap'] = False
        
        self.barObject = marketBarChart()
        self.barObject.drawValueChart(self.win.surf)
        
        if ActivitySharedFlag:
            
            #Creating Checkbox for share trade with peer villages
            self.shareCheckBox = CheckBox(position = threades.resize_pos((440, 140), (800, 600), self.win.size),  parent = self.win,  style = ch_style,  text = 'Trade with Peer Villages' )
            self.shareCheckBox.value = False        
            self.shareCheckBox.onValueChanged = self.drawPriceChart()
        


        # Creating labels for village values of Resources 
        self.label_vwater = gui.Label(position = threades.resize_pos((190.0,140.0),(800.0,600.0),self.win.size), parent = self.win, text = str(int(model.Water.get_vquantity())), style = labelstyle1)
        self.label_vbuildmat = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Buildmat.get_vquantity())), style = labelstyle1)
        self.label_vtools = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Tools.get_vquantity())), style = labelstyle1)
        self.label_vbooks = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Book.get_vquantity())), style = labelstyle1)
        self.label_vmedicine = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Medicine.get_vquantity())), style = labelstyle1)
        self.label_vrice = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Rice.get_vquantity())), style = labelstyle1)
        self.label_vwheat = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Wheat.get_vquantity())), style = labelstyle1)
        self.label_vbeans = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Beans.get_vquantity())), style = labelstyle1)
        self.label_vsugar = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Sugar.get_vquantity())), style = labelstyle1)
        self.label_vsalt = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Salt.get_vquantity())), style = labelstyle1)
        self.label_voil = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Oil.get_vquantity())), style = labelstyle1)

        #Creating labels for value and price of resources
        self.label_res_price_flag = False
        self.label_res_value = gui.Label(position = threades.resize_pos((650.0,200.0),(800.0,600.0),self.win.size), parent = self.win, text = str(int(self.barObject.bar1Val)), style = labelstyle1)
        
        #Creating a label for value to be printed
        self.label_quantity = gui.Label(position = threades.resize_pos((440.0,170.0),(800.0,600.0),self.win.size), parent = self.win, text = 'Quantity ', style = labelstyle1)
                    
        if ActivitySharedFlag:
            if self.shareCheckBox.value:
                self.label_price = gui.Label(position = threades.resize_pos((400.0,250.0),(800.0,600.0),self.win.size), parent = self.win, text = 'Price ', style = labelstyle1)
                self.label_res_price = gui.Label(position = threades.resize_pos((650.0,280.0),(800.0,600.0),self.win.size), parent = self.win, text = str(int(self.barObject.bar2Val)), style = labelstyle1)
        
        # Creating labels for prices of Resources 
        self.price_vwater = gui.Label(position = threades.resize_pos((370.0,140.0),(800.0,600.0),self.win.size), parent = self.win, text = str(int(model.Water.get_price())), style = labelstyle1)
        self.price_vbuildmat = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Buildmat.get_price())), style = labelstyle1)
        self.price_vtools = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Tools.get_price())), style = labelstyle1)
        self.price_vbooks = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Book.get_price())), style = labelstyle1)
        self.price_vmedicine = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Medicine.get_price())), style = labelstyle1)
        self.price_vrice = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Rice.get_price())), style = labelstyle1)
        self.price_vwheat = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Wheat.get_price())), style = labelstyle1)
        self.price_vbeans = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Beans.get_price())), style = labelstyle1)
        self.price_vsugar = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Sugar.get_price())), style = labelstyle1)
        self.price_vsalt = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Salt.get_price())), style = labelstyle1)
        self.price_voil = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Oil.get_price())), style = labelstyle1)

        '''
        # Creating a textbox to enter the quantity to buy or sell
        textbox_style = gui.defaultTextBoxStyle.copy()
        textbox_style['font'] = myfont2
        textbox_style['font-color'] = self.rect_color
        self.label_quantity = gui.Label(position = threades.resize_pos((360.0,150.0),(800.0,600.0),self.win.size), parent = self.win, text = ' Quantity ', style = labelstyle1)
        self.win.textbox = TextBox(position = threades.resize_pos((350.0, 200.0),(800.0,600.0),self.win.size), size = threades.resize_pos((100,20),(800.0,600.0),self.win.size), parent = self.win, style = textbox_style) 
        '''

        # Creating buttons for buying and selling and closing the window
        button_style = gui.defaultButtonStyle.copy()
        button_style['font'] = myfont2

        self.button_buy = gui.Button(position = threades.resize_pos((560.0,350.0),(800.0,600.0),size_win), size = threades.resize_pos((70.0,50.0),(800.0,600.0),size_win), parent = self.win, text = " Buy ",style = button_style)
        self.button_sell = gui.Button(position = threades.resize_pos((460.0,350.0),(800.0,600.0),size_win), size = threades.resize_pos((70.0,50.0),(800.0,600.0),size_win), parent = self.win, text = " Sell ",style = button_style)
        self.button_close = gui.Button(position = threades.resize_pos((650.0,500.0),(800.0,600.0),size_win), size = threades.resize_pos((120.0,50.0),(800.0,600.0),size_win), parent = self.win, text = "Close",style = button_style)
        self.button_buy.onClick = self.buy_resources
        self.button_sell.onClick = self.sell_resources
        self.button_close.onClick  = self.close_win
        
        # Creating labels for market values of Resources 
        self.label_mwater = gui.Label(position = threades.resize_pos((270.0,140.0),(800.0,600.0),self.win.size), parent = self.win, text = str(int(model.Water.get_mquantity())), style = labelstyle1)
        self.label_mbuildmat = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Buildmat.get_mquantity())), style = labelstyle1)
        self.label_mtools = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Tools.get_mquantity())), style = labelstyle1)
        self.label_mbooks = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Book.get_mquantity())), style = labelstyle1)
        self.label_mmedicine = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Medicine.get_mquantity())), style = labelstyle1)
        self.label_mrice = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Rice.get_mquantity())), style = labelstyle1)
        self.label_mwheat = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Wheat.get_mquantity())), style = labelstyle1)
        self.label_mbeans = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Beans.get_mquantity())), style = labelstyle1)
        self.label_msugar = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Sugar.get_mquantity())), style = labelstyle1)
        self.label_msalt = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Salt.get_mquantity())), style = labelstyle1)
        self.label_moil = gui.Label(position = self.win.nextPosition(threades.resize_pt_y(7)), parent = self.win, text = str(int(model.Oil.get_mquantity())), style = labelstyle1)



        # Creating label to display the status messages
        #  Creating Custom label style
        labelStyleCopy = gui.defaultLabelStyle.copy()
        labelStyleCopy['border-width'] = 1
        labelStyleCopy['wordwrap'] = True
        labelStyleCopy['autosize'] = False
        labelStyleCopy['font'] = myfont2
        labelStyleCopy['font-color'] = self.rect_color
        labelStyleCopy['border-color'] = self.color_grey
        text = 'Welcome to the market of SHEYLAN, where you can trade resources. Select which item you would like to buy or sell on the left-hand column, enter the amount, and then choose buy or sell'
        self.message_label = gui.Label(position = threades.resize_pos((80,470),(800.0,600.0),self.win.size),size = threades.resize_pos((500,100),(800.0,600.0),self.win.size), parent = self.win, text = text, style = labelStyleCopy)

    def updateMarketLabelValues(self,button = None):
        self.label_res_value.text = str(int(self.barObject.bar1Val))
        if ActivitySharedFlag:
            if self.shareCheckBox.value:
                self.label_res_price.text = str(int(self.barObject.bar2Val))
                
    def drawPriceChart(self,button = None):
        
        # Creating custom label style1
        
        if ActivitySharedFlag:
            if self.shareCheckBox.value:
                myfont2 = pygame.font.Font("font.ttf",threades.resize_pt(16))
                labelstyle1 = gui.defaultLabelStyle.copy()
                labelstyle1['border-width'] = 0
                labelstyle1['wordwrap'] = False
                labelstyle1['autosize'] = True
                labelstyle1['font'] = myfont2
                labelstyle1['font-color'] = self.rect_color
                #print self.shareCheckBox.value
    
            
                self.barObject.drawPriceChart(self.win.surf)
                if not self.label_res_price_flag:            
                    self.label_price = gui.Label(position = threades.resize_pos((440.0,250.0),(800.0,600.0),self.win.size), parent = self.win, text = 'Price ', style = labelstyle1)
                    self.label_res_price = gui.Label(position = threades.resize_pos((650.0,280.0),(800.0,600.0),self.win.size), parent = self.win, text = str(int(self.barObject.bar2Val)), style = labelstyle1)
                    self.label_res_price_flag = True
            
            else:
                self.barObject.deletePriceChart()
            
            
    def buy_resources(self,button):
        ''' Initiated for doing the transaction of buying the resources 
        '''
        # Checking whether the user has entered the value in text box properly
        quantity = self.barObject.bar1Val  

        # Checking whether the user has selected the appropriate option box for the resource or not, and do the appropriate action
        if self.water_box.value:
            label_text =  threades.buy_res(model.Water,quantity)
            if label_text == 'The Village has bought the resource you demanded':
                self.label_vwater.text = str(int(model.Water.get_vquantity()))
                self.label_mwater.text = str(int(model.Water.get_mquantity()))
        elif self.buildmat_box.value:
            label_text =  threades.buy_res(model.Buildmat,quantity)
            if label_text == 'The Village has bought the resource you demanded':
                self.label_vbuildmat.text = str(int(model.Buildmat.get_vquantity()))
                self.label_mbuildmat.text = str(int(model.Buildmat.get_mquantity()))
        elif self.tools_box.value:
            label_text =  threades.buy_res(model.Tools,quantity)
            if label_text == 'The Village has bought the resource you demanded':
                self.label_vtools.text = str(int(model.Tools.get_vquantity()))
                self.label_mtools.text = str(int(model.Tools.get_mquantity()))
        elif self.medicine_box.value:
            label_text =  threades.buy_res(model.Medicine,quantity)
            if label_text == 'The Village has bought the resource you demanded':
                self.label_vmedicine.text = str(int(model.Medicine.get_vquantity()))
                self.label_mmedicine.text = str(int(model.Medicine.get_mquantity()))
        elif self.books_box.value:
            label_text =  threades.buy_res(model.Book,quantity)
            if label_text == 'The Village has bought the resource you demanded':
                self.label_vbooks.text = str(int(model.Book.get_vquantity()))
                self.label_mbooks.text = str(int(model.Book.get_mquantity()))
        elif self.rice_box.value:
            label_text =  threades.buy_res(model.Rice,quantity)
            if label_text == 'The Village has bought the resource you demanded':
                self.label_vrice.text = str(int(model.Rice.get_vquantity()))
                self.label_mrice.text = str(int(model.Rice.get_mquantity()))
        elif self.wheat_box.value:
            label_text =  threades.buy_res(model.Wheat,quantity)
            if label_text == 'The Village has bought the resource you demanded':
                self.label_vwheat.text = str(int(model.Wheat.get_vquantity()))
                self.label_mwheat.text = str(int(model.Wheat.get_mquantity()))
        elif self.beans_box.value:
            label_text =  threades.buy_res(model.Beans,quantity)
            if label_text == 'The Village has bought the resource you demanded':
                self.label_vbeans.text = str(int(model.Beans.get_vquantity()))
                self.label_mbeans.text = str(int(model.Beans.get_mquantity()))
        elif self.sugar_box.value:
            label_text =  threades.buy_res(model.Sugar,quantity)
            if label_text == 'The Village has bought the resource you demanded':
                self.label_vsugar.text = str(int(model.Sugar.get_vquantity()))
                self.label_msugar.text = str(int(model.Sugar.get_mquantity()))
        elif self.salt_box.value:
            label_text =  threades.buy_res(model.Salt,quantity)
            if label_text == 'The Village has bought the resource you demanded':
                self.label_vsalt.text = str(int(model.Salt.get_vquantity()))
                self.label_msalt.text = str(int(model.Salt.get_mquantity()))
        elif self.oil_box.value:
            label_text =  threades.buy_res(model.Oil,quantity)
            if label_text == 'The Village has bought the resource you demanded':
                self.label_voil.text = str(int(model.Oil.get_vquantity()))
                self.label_moil.text = str(int(model.Oil.get_mquantity()))
        else:
            label_text = ' Please select a Resource for Trading'

        self.message_label.text = label_text
        



    def sell_resources(self,button):
        ''' Initiated for doing the transaction of buying the resources 
        '''
        # Checking whether the user has entered the value in text box properly
        quantity = self.barObject.bar1Val

        # Checking whether the user has selected the appropriate option box for the resource or not, and do the appropriate action
        if self.water_box.value:
            label_text =  threades.sell_res(model.Water,quantity)
            if label_text == 'The Village has sold the resource you demanded':
                self.label_vwater.text = str(int(model.Water.get_vquantity()))
                self.label_mwater.text = str(int(model.Water.get_mquantity()))
        elif self.buildmat_box.value:
            label_text =  threades.sell_res(model.Buildmat,quantity)
            if label_text == 'The Village has sold the resource you demanded':
                self.label_vbuildmat.text = str(int(model.Buildmat.get_vquantity()))
                self.label_mbuildmat.text = str(int(model.Buildmat.get_mquantity()))
        elif self.tools_box.value:
            label_text =  threades.sell_res(model.Tools,quantity)
            if label_text == 'The Village has sold the resource you demanded':
                self.label_vtools.text = str(int(model.Tools.get_vquantity()))
                self.label_mtools.text = str(int(model.Tools.get_mquantity()))
        elif self.medicine_box.value:
            label_text =  threades.sell_res(model.Medicine,quantity)
            if label_text == 'The Village has sold the resource you demanded':
                self.label_vmedicine.text = str(int(model.Medicine.get_vquantity()))
                self.label_mmedicine.text = str(int(model.Medicine.get_mquantity()))
        elif self.books_box.value:
            label_text =  threades.sell_res(model.Book,quantity)
            if label_text == 'The Village has sold the resource you demanded':
                self.label_vbooks.text = str(int(model.Book.get_vquantity()))
                self.label_mbooks.text = str(int(model.Book.get_mquantity()))
        elif self.rice_box.value:
            label_text =  threades.sell_res(model.Rice,quantity)
            if label_text == 'The Village has sold the resource you demanded':
                self.label_vrice.text = str(int(model.Rice.get_vquantity()))
                self.label_mrice.text = str(int(model.Rice.get_mquantity()))
        elif self.wheat_box.value:
            label_text =  threades.sell_res(model.Wheat,quantity)
            if label_text == 'The Village has sold the resource you demanded':
                self.label_vwheat.text = str(int(model.Wheat.get_vquantity()))
                self.label_mwheat.text = str(int(model.Wheat.get_mquantity()))
        elif self.beans_box.value:
            label_text =  threades.sell_res(model.Beans,quantity)
            if label_text == 'The Village has sold the resource you demanded':
                self.label_vbeans.text = str(int(model.Beans.get_vquantity()))
                self.label_mbeans.text = str(int(model.Beans.get_mquantity()))
        elif self.sugar_box.value:
            label_text =  threades.sell_res(model.Sugar,quantity)
            if label_text == 'The Village has sold the resource you demanded':
                self.label_vsugar.text = str(int(model.Sugar.get_vquantity()))
                self.label_msugar.text = str(int(model.Sugar.get_mquantity()))
        elif self.salt_box.value:
            label_text =  threades.sell_res(model.Salt,quantity)
            if label_text == 'The Village has sold the resource you demanded':
                self.label_vsalt.text = str(int(model.Salt.get_vquantity()))
                self.label_msalt.text = str(int(model.Salt.get_mquantity()))
        elif self.oil_box.value:
            label_text =  threades.sell_res(model.Oil,quantity)
            if label_text == 'The Village has sold the resource you demanded':
                self.label_voil.text = str(int(model.Oil.get_vquantity()))
                self.label_moil.text = str(int(model.Oil.get_mquantity()))
        else:
            label_text = ' Please select a Resource for Trading'
        self.message_label.text = label_text
        
        
    def close_win(self,button=None):
        self.win.close()
        self.win_flag = False
        gui_obj.enable_buttons()

    def close_win_safe(self,button = None):
        self.win_flag = False
        gui_obj.enable_buttons()



    def get_win_flag(self):
        return self.win_flag

        

    

class gui_buttons:

    rect_color = (255,214,150)
    color_grey = (160,160,160)

    def initialize(self):
        ''' Initialises the buttons for setting up facility, upgrading it and for buy/sell operations
        '''
        myfont = pygame.font.Font("font.ttf", threades.resize_pt(17))
        button_style = gui.defaultButtonStyle.copy()
        button_style['font'] = myfont
        self.setup_button = gui.Button(position = threades.resize_pos((50,865)), size = threades.resize_pos((200,25)), parent = threades.desktop, text = "Setup Facility",style = button_style)
        self.upgrade_button = gui.Button(position = threades.resize_pos((350,865)), size = threades.resize_pos((200,25)), parent = threades.desktop, text = "Upgrade Facility",style = button_style)
        self.buysell_button = gui.Button(position = threades.resize_pos((650,865)), size = threades.resize_pos((200,25)), parent = threades.desktop, text = "Buy/Sell Resources",style = button_style)
        self.setup_obj = setup_button()
        self.upgrade_obj = upgrade_button()
        self.buysell_obj = buysell_button()
        self.setup_button.onClick = self.setup_obj.setup
        self.upgrade_button.onClick = self.upgrade_obj.upgrade
        self.buysell_button.onClick = self.buysell_obj.buysell
        self.win_flag = False
        self.child_win_flag = False
        

    def get_win_flag(self):
        return (self.setup_obj.get_win_flag() or self.upgrade_obj.get_win_flag() or self.buysell_obj.get_win_flag())

    def get_child_win_flag(self):
        return self.setup_obj.get_child_win_flag()

    def close_child_win(self):
        self.setup_obj.child_win.close()
        self.setup_obj.enable_parent_win()

    def close_win(self):
        if self.setup_obj.get_win_flag():
            self.setup_obj.close_win()
        elif self.upgrade_obj.get_win_flag():
            self.upgrade_obj.close_win()
        elif self.buysell_obj.get_win_flag():
            self.buysell_obj.close_win()
            
    def press_enter(self):
        
        # responds to the enter keypress
        if  self.get_child_win_flag():
            self.setup_obj.setup_facility_farm()
        
        elif self.setup_obj.get_win_flag():
            self.setup_obj.setup_facility()
            
        elif self.upgrade_obj.get_win_flag():
            self.upgrade_obj.upgrade_facility()
            
        
    def disable_buttons(self):

        # stopping the motion of the background
        threades.transform_obj.stop_mouse_move()
        threades.total_update_flag = True

        self.setup_button.enabled = False
        self.upgrade_button.enabled = False
        self.buysell_button.enabled = False

    def enable_buttons(self):

        threades.resume_update_thread()

        # resume mouse motion
        threades.transform_obj.resume_mouse_move()

        self.win_flag = False

        self.setup_button.enabled = True
        self.upgrade_button.enabled = True
        self.buysell_button.enabled = True
        threades.total_update_flag = True



    
  
gui_obj = gui_buttons()

def initialize_gui():
    
    ''' Function to initialize the GUI
    '''
    global gui_obj
    gui_obj.initialize()     
    
    
class meshTrading:
    '''Class which handles matters regarding the trading over
       Mesh Network
    '''    
    def tradingWindow(self,buddyName = 'Friend',resource = 'Water',price = '10',trade = 'sell'):
        '''Opens the trading window at the reciever end for trading
        '''        

        #self.font_color = (255,214,150) # Brown
        color_blue = (0,0,250)
        myfont = pygame.font.Font("font.ttf", threades.resize_pt(17))
        # Custom gui.Window Style
        win_style = gui.defaultWindowStyle.copy()
        win_style['font'] = myfont
        win_style['bg-color'] = (0,0,0)
        win_style['font-color'] = color_blue
        
        # Calculating position and size of window from the size of the threades.desktop
        position_win =threades.resize_pos((725.0,42.0))
        size_win =threades.resize_pos((470.0,180.0))
    
        # Creating custom label style for the text to be displayed as a message
        labelStyleCopy = gui.defaultLabelStyle.copy()
        labelStyleCopy['wordwrap'] = True
        labelStyleCopy['autosize'] = False
        labelStyleCopy['font'] = myfont
        labelStyleCopy['font-color'] = color_blue
        #labelStyleCopy['font-color'] = font_color
    
        self.win = gui.Window(position = position_win, size = size_win, parent = threades.desktop, text = " Trade " ,style = win_style,shadeable = False, moveable = False)
        # Creating label
        label_text = buddyName + ' wants to ' + trade + ' ' + resource + ' at $ '+ price 
        message_label = gui.Label(position = threades.resize_pos((5,5),(470.0,180.0),win.size),size = threades.resize_pos((460,120),(470.0,180.0),win.size), parent = win, text = label_text, style = labelStyleCopy)
        
        # Creating button style
        myfont2 = pygame.font.Font("font.ttf", threades.resize_pt(16))
        button_style = gui.defaultButtonStyle.copy()
        button_style['font'] = myfont2

        self.button_accept = gui.Button(position = threades.resize_pos((100.0,130.0),(470.0,180.0),size_win), size = threades.resize_pos((100.0,40.0),(470.0,180.0),size_win), parent = self.win, text = " Accept ",style = button_style)
        self.button_reject = gui.Button(position = threades.resize_pos((300.0,130.0),(470.0,180.0),size_win), size = threades.resize_pos((100.0,40.0),(470.0,180.0),size_win), parent = self.win, text = " Accept ",style = button_style)
        
        self.button_accept.onClick = self.checkTrade
        self.button_accept.onClick = self.closeWin
        
        sleep(6)
        self.win.close()
                    
    def checkTrade(self,button = None):
        ''' Sends an acceptance request to the person who tried to trade 
        '''
        
            
    def closeWin(self):
        self.win.close()
