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

import pygame
from pygame.locals import *
from sys import exit
import os
from time import *
import threades
import threading
import game_events
import texts
import model
import gui_buttons
import random



class Earthquake(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        mask= pygame.surface.Surface((1200,560),SRCALPHA)
        mask.fill((0,0,0))
        mask.set_alpha(0)
        self.alpha = 0
        self.image = mask
        self.rect = self.image.get_rect()
        self.rect.move((0,0))
        self.counter = 0
        self.prev_disp = (0,0)
        self.move_dir = [(-20,-20),(-20,-10),(-20,0),(-20,10),(-20,20),(-10,-20),(-10,-20),(-10,0),(-10,10),(-10,20),(0,-20),(0,-10),(0,0),(0,10),(0,20),(10,-20),(10,-20),(10,0),(10,10),(10,20),(20,-20),(20,-10),(20,0),(20,10),(20,20)]
        # To close all open windows
        if gui_buttons.gui_obj.get_child_win_flag():
            gui_buttons.gui_obj.close_child_win()
            gui_buttons.gui_obj.close_win()
        elif gui_buttons.gui_obj.get_win_flag():
            gui_buttons.gui_obj.close_win()

    def update(self):

        global Hospital
        global House
        global School
        global Workshop
        global ppl


        self.counter +=1
        if self.counter <50:
            threades.transform_obj.move_free((-self.prev_disp[0],-self.prev_disp[1]))
            self.prev_disp = self.move_dir[int(random.random()*25)]
            threades.transform_obj.move_free(self.prev_disp)
        if self.counter >20 and self.counter <50:
            self.alpha +=8
            self.image.set_alpha(self.alpha)
        if self.counter==40:
            display_text = ' Your Village Sheylan has ben hit by an Earthquake'
            threades.message.push_message(display_text,'high')
        if self.counter == 80:
            display_earthquake_images()
            threades.demolish_facility('Hospital')
            threades.demolish_facility('House')
            threades.demolish_facility('House')
            threades.demolish_facility('House')
            threades.demolish_facility('School')
            threades.demolish_facility('Workshop')
            model.ppl.change_total_population(-10)
        if self.counter > 81:
            if self.alpha >2:
                self.alpha -=2
            self.image.set_alpha(self.alpha)
        if self.counter >180:
            event = game_events.Event(type = game_events.ACTIONCOMPLETEEVENT, facility_name = '', res_name = '' , res_quantity = 0)
            game_events.EventQueue.add(event)
            threades.natural_calamities.remove(earthquake)

def display_earthquake_images():

    image1 = pygame.image.load(os.path.join('data', 'earthquake1.png')).convert()
    threades.screen.blit(pygame.transform.scale(image1,threades.new_screen_size),(0,0))
    pygame.display.flip()
    sleep(3)

    image2 = pygame.image.load(os.path.join('data', 'earthquake2.png')).convert()
    threades.screen.blit(pygame.transform.scale(image2,threades.new_screen_size),(0,0))
    pygame.display.flip()
    sleep(3)

    image3 = pygame.image.load(os.path.join('data', 'earthquake3.png')).convert()
    threades.screen.blit(pygame.transform.scale(image3,threades.new_screen_size),(0,0))
    pygame.display.flip()
    sleep(3)
    
earthquake = None

def earthquake():
    ''' This method needs to be called when there is an earthquake in the
    village, it decreases the number of installations of some facilities and
    also reduce the population
    '''
    global earthquake

    earthquake  = Earthquake()
    threades.natural_calamities.add(earthquake)
