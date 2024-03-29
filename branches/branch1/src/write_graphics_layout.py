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

import pickle
output = open('graphics_layout.pkl', 'wb')


# Saving the positions of all the facilities
workshop_posn_list = [(200,2550),(2000,5000),  (6500,400),  (6000,5300)]
pickle.dump(workshop_posn_list, output)
house_posn_list = [(800,2000),(1000,2600),(1400,3300),(2000,2000),(2000,2600),  (2800,3800),(3800,3800),(3200,4500),  (5200,500),(4600,1100),(5500,1100),(6200,1600),(5000,1800),(5800,2200),(5200,2500),  (5000,3600),(5800,3500),(6500,3300),(6000,4100),(6750,3800),(6900,4500)]
pickle.dump(house_posn_list, output)
hospital_posn_list = [(1400,3900), (7700,2200), (4500,4200)]
pickle.dump(hospital_posn_list, output)
school_posn_list = [(2700,2000), (6100,2500), (7200,3000)]
pickle.dump(school_posn_list, output)
farm_posn_list = [(300,500),(3000,500), (7400,800), (7500,3600)]
pickle.dump(farm_posn_list, output)
fountain_posn_list = [(2100,1200),(2200,3000),(3600,3500), (4500,1800),(6900,2000), (5900,3000),(6000,4800)]
pickle.dump(fountain_posn_list, output)

facilities_posn_list = [house_posn_list,school_posn_list,hospital_posn_list,workshop_posn_list,farm_posn_list,fountain_posn_list]
pickle.dump(facilities_posn_list, output)
# Saving the attributes for the villagers with each facility
workshop_villagers = [ [ ('Man',(0,2400,1200,1500)), ('Man',(0,2400,1200,1500)) ], [ ('Man',(1500,4500,1200,1500)), ('Man',(1500,4500,1200,1500)) ], [ ('Man',(6200,0,1200,1500)), ('Man',(6200,0,1200,1500)) ], [ ('Man',(5500,4500,1200,1500)), ('Man',(5500,4500,1200,1500)) ] ]
pickle.dump(workshop_villagers, output)
house_villagers = [ [ ('Woman',(600,1800,2400,2000)), ('Woman',(600,1800,2400,2000)), ('Woman',(600,1800,2400,2000)), ('Boy',(600,1800,2400,2000)), ('Boy',(600,1800,2400,2000)), ('Girl',(600,1800,2400,2000)), ('Girl',(600,1800,2400,2000)) ],[],[],[],[], [ ('Woman',(2500,3500,2000,2000)), ('Woman',(2500,3500,2000,2000)), ('Boy',(2500,3500,2000,2000)), ('Girl',(2500,3500,2000,2000))],[],[], [ ('Man',(4500,0,2500,3000)), ('Woman',(4500,0,2500,3000)), ('Girl',(4500,0,2500,3000)), ('Girl',(4500,0,2500,3000)), ('Boy',(4500,0,2500,3000)), ('Boy',(4500,0,2500,3000)) ],[],[],[],[],[],[], [ ('Man',(4500,3000,3500,1800)), ('Woman',(4500,3000,3500,1800)), ('Woman',(4500,3000,3500,1800)), ('Boy',(4500,3000,3500,1800)), ('Girl',(4500,3000,3500,1800)) ],[],[],[],[],[] ]
pickle.dump(house_villagers, output)
hospital_villagers = [ [ ('Man',(1000,3500,1200,1200)), ('Woman',(1000,3500,1200,1200)), ('Boy',(1000,3500,1200,1200)), ('Girl',(1000,3500,1200,1200)) ], [ ('Man',(7400,1800,1200,1200)), ('Woman',(7400,1800,1200,1200)), ('Boy',(7400,1800,1200,1200)), ('Girl',(7400,1800,1200,1200)) ], [ ('Man',(4500,4000,1200,1200)), ('Woman',(4500,4000,1200,1200)), ('Boy',(4500,4000,1200,1200)), ('Girl',(4500,4000,1200,1200)) ] ]
pickle.dump(hospital_villagers, output)
school_villagers = [ [ ('Boy',(2500,1800,1500,1500)), ('Boy',(2500,1800,1500,1500)), ('Girl',(2500,1800,1500,1500)) ], [ ('Boy',(1800,5800,1500,1500)), ('Girl',(1800,5800,1500,1500)), ('Girl',(1800,5800,1500,1500)) ], [ ('Boy',(7000,2800,1500,1500)), ('Boy',(7000,2800,1500,1500)), ('Girl',(7000,2800,1500,1500)) ] ]
pickle.dump(school_villagers, output)
farm_villagers = [ [ ('Woman',(0,0,1000,1000)), ('Man',(0,0,1000,1000)) ], [ ('Woman',(2500,0,1000,1000)), ('Man',(2500,0,1000,1000)) ], [ ('Woman',(7000,600,1000,1000)), ('Man',(7000,600,1000,1000)) ], [ ('Woman',(7000,3500,1000,1000)), ('Man',(7000,3500,1000,1000)) ] ]
pickle.dump(farm_villagers, output)
fountain_villagers = [ [],[],[],[],[],[],[] ]
pickle.dump(fountain_villagers, output)
facility_villagers = { 'WORKSHOP':workshop_villagers , 'HOUSE':house_villagers , 'HOSPITAL':hospital_villagers , 'SCHOOL':school_villagers , 'FARM':farm_villagers,'FOUNTAIN':fountain_villagers }
pickle.dump(facility_villagers, output)

#adding the terrain part
back_image_level1 = [
        # 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66
        [22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,23, 5, 5, 5, 5, 5, 5, 5, 5, 5,16,29,29,29,29,29,29,29,29],#, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],#1
        [22,22,22,22,22,22,22,22, 7, 8,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22, 7,34,35, 5, 5, 5, 5, 5, 5, 5, 5, 5,12, 3, 4,29,29,29,29,29,29],#, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],#2
        [22,22,22,22, 7,34,34,34,35,33, 8,22,22,22,22,22,22,22,22,22,22,22,22, 7,34,35, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,12, 4, 2, 4,29,29,29],#, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],#3
        [22,22, 7,34,35, 5, 5, 5, 5, 5,33, 8, 7,34, 8,22, 7,34, 8,22, 7,34,34,35, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 1, 5, 5, 5, 5,12,13,16,29,29,29],#, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],#4
        [ 7,34,35, 5, 5, 5, 5, 5, 5, 5, 5,33,35, 5,33,34,35, 5,33,34,35, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,12,13, 5, 5, 5, 5, 5, 0,28,29,29,29],#, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,21, 5,23, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],#5
        [35, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 9,10,11, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,12, 4,29,29,29],#, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],#6
        [ 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 9,20,22,19,11, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0,27,28,29,29,29],#, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],#7
        [ 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 1,12,13, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,21,22,22,22,23, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,12, 4,29,29,29,29],#, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],#8
        [ 5, 5, 5, 5, 5, 5, 5, 5, 5,12,13, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,21,22,22, 7,35, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,16,29,29,29,29],#, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],#9 
        [ 5, 5, 5, 5, 5, 5, 5, 5, 9,11, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,33,34,34,35, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,16,29,29,29,29],#, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],#10
        [ 5, 5, 5, 5, 5, 5, 9,10,20,23, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,12, 4,29,29,29],#,, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],#11
        [ 5, 5, 5, 5, 5, 5,21,22,22,23, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,12, 4,29,29],#,, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],#12
        [ 5, 5, 5, 5, 5, 5,33, 8,22,19,11, 5, 5, 5, 5, 9,10,11, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,16,29,29],#, 5, 5, 5, 5, 5, 9,10,11, 5, 5, 5, 9,10,11, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],#13
        [ 0, 1, 5, 5, 5, 5, 5,21,22, 7,35, 5, 5, 5, 5,21,22,23, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,12, 4,29],#, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,21,22,23, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],#14
        [12,13, 5, 5, 5, 5, 5,21,22,23, 5, 5, 5, 5, 5,33,34,35, 5, 5, 5, 5, 5, 5, 9,11, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,12, 3],#, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],#15
        [ 1, 5, 5, 5, 5, 5, 5,33,34,35, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,33,35, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 1, 5, 5, 5],#, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],#16
        [14, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 1, 5, 5, 5, 5, 5,12,13, 5, 5, 5],#, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],#17
        [26, 1, 0,27, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,12,13, 5, 5, 5, 5, 5, 5, 5, 0, 1, 5],#, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],#18
        [29,14,12, 3,13, 5, 5, 5, 5, 9,10,11, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,12,13, 5],#, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],#19
        [ 2,13, 5, 5, 5, 5, 5, 5, 5,21,22,23, 5, 5, 5, 5, 5, 0, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],#, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],#20
        [13, 5, 5, 5, 5, 5, 5, 5, 5,33,34,35, 5, 5, 5, 5, 5,12,13, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],#, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],#21
        [ 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 9,10,11, 5, 5, 5, 9,10,11, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],#, 5, 5, 5, 5, 5, 9,10,11, 5, 5, 5, 9,10,11, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],#22
        [ 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,21,22,23, 5, 5, 5,21,22,23, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],#, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,21,22,23, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],#23
        [ 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,33,34,35, 5, 5, 5,33,34,35, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 9,10,10],#, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],#24
        [ 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 9,11, 5, 5, 5,21,22,22],#, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],#25
        [ 5, 5, 5, 5, 5, 5, 9,11, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,33,35, 5, 5, 5,33, 8,22],#, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],#26
        [27, 1, 5, 5, 9,10,20,23, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 9,11, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,21,22],#,, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],#27
        [29,26, 1, 5,21,22,22,23, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,33,35, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,21,22],#, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],#28
        [29,29,14, 5,33,34,34,35, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 9,11, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 9,10,20,22],#, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],#29
        [29,29,14, 5, 5, 5, 0, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 9,20,19,10,10,11, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,33, 8,22,22],#, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],#30
        [29,29,26, 1, 5, 0,28,26, 1, 5, 5, 5, 5, 5, 5, 9,10,10,20,22,22,22,22,19,11, 5, 5, 9,10,11, 5, 5, 5, 9,10,11, 5, 5, 5, 9,10,11, 5,21,22,22],#,10,11, 5, 5, 5, 9,10,11, 5, 5, 5, 9,10,11, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],#31
        [29,29,29,26,27,28,29,29,14, 5, 5, 5, 5, 5, 5,21,22,22,22,22,22,22,22,22,19,11, 5,21,22,23, 5, 5, 5,21,22,23, 5, 5, 5,21,22,23, 5,21,22,22],#,22,23, 5, 5, 5,21,22,23, 5, 5, 5,21,22,23, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],#32
        [29,29,29,29,29,29,29,29,26, 1, 5, 5, 5, 5, 5,21,22,22,22,22,22,22,22,22,22,19,10,20,22,23, 5, 5, 5,33,34,35, 5, 5, 9,20,22,19,10,20,22,22],#,34,35, 5, 5, 5,33,34,35, 5, 5, 5,33,34,35, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],#33
        [29,29,29,29,29,29,29,29,29,14, 5, 5, 5, 5, 5,21,22,22,22,22,22,22,22,22,22,22,22,22,22,23, 5, 5, 5, 5, 5, 5, 5, 5,21,22,22,22,22,22,22,22],#, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],#34
    ]

pickle.dump(back_image_level1, output)


output.close()
