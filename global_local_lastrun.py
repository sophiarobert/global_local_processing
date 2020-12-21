#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.4),
    on Mon Dec 21 16:11:24 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.4'
expName = 'global_local'  # from the Builder filename that created this script
expInfo = {'participant': '', 'design': '1', 'position': '2'}
dlg = gui.DlgFromDict(dictionary=expInfo, sort_keys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/sophia/Documents/PycharmProjects/Global_Local_Study/global_local_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1792, 1120], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "screen_scale"
screen_scaleClock = core.Clock()
oldt=0
x_size=8.560
y_size=5.398
screen_height=0

if win.units=='norm':
    x_scale=.05
    y_scale=.1
    dbase = .0001
    unittext=' norm units'
    vsize=2
elif win.units=='pix':
    x_scale=60
    y_scale=40
    dbase = .1
    unittext=' pixels'
    vsize=win.size[1]
else:
    x_scale=.05
    y_scale=.05
    dbase = .0001
    unittext=' height units'
    vsize=1

# h = tan(degrees = 2) x (distance = 49.53)
height = 1.7296*2
width = 1.7296*2
width3deg = 3.47618705978
width4deg = 3.47618705978
text_top = visual.TextStim(win=win, name='text_top',
    text='Resize this image to match the size of a credit card with arrow keys',
    font='Arial',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_bottom = visual.TextStim(win=win, name='text_bottom',
    text='Press Space when you’re finished',
    font='Arial',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
ccimage = visual.ImageStim(
    win=win,
    name='ccimage', 
    image='bankcard.png', mask=None,
    ori=0, pos=(0, 0), size=(x_size*x_scale, y_size*y_scale),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-4.0)

# Initialize components for Routine "pracInstruct"
pracInstructClock = core.Clock()

fixColor_opts = ["black", "white"];
shuffle(fixColor_opts);
pfS1 = [0,1,0,1]
shuffle(pfS1)
prac1_fixColSwitch = [0]+pfS1+[0];
pfS2 = [0,1,0,1]
shuffle(pfS2)
prac2_fixColSwitch = [0]+pfS2+[0];

if int(expInfo['position'] ) == 2:
    fixColorIdx_Run1 =  [1, 0, 0, 0, 0, 0, 0, 1, 
                                    1, 0, 0, 0, 0, 0, 0, 1, 
                                    1, 0, 0, 0, 0, 0, 0, 1, 
                                   1, 0, 0, 0, 0, 0, 0, 1, 
                                   1, 0, 0, 0, 0, 0, 0, 1, 
                                   1, 0, 0, 0, 0, 0, 0, 1, 
                                   1, 0, 0, 0, 0, 0, 0, 1, 
                                   1, 0, 0, 0, 0, 0, 0, 1, 
                                   1, 0, 0, 0, 0, 0, 0, 1, 
                                   1, 0, 0, 0, 0, 0, 0, 1, 
                                   1, 0, 0, 0, 0, 0, 0, 1,
                                   1, 0, 0, 0, 0, 0, 0, 1];
    shuffle(fixColorIdx_Run1);
    fixColorIdx_Run2 = [1, 0, 0, 0, 0, 0, 0, 1, 
                                   1, 0, 0, 0, 0, 0, 0, 1, 
                                   1, 0, 0, 0, 0, 0, 0, 1, 
                                   1, 0, 0, 0, 0, 0, 0, 1, 
                                   1, 0, 0, 0, 0, 0, 0, 1, 
                                   1, 0, 0, 0, 0, 0, 0, 1, 
                                   1, 0, 0, 0, 0, 0, 0, 1, 
                                   1, 0, 0, 0, 0, 0, 0, 1, 
                                   1, 0, 0, 0, 0, 0, 0, 1, 
                                   1, 0, 0, 0, 0, 0, 0, 1, 
                                   1, 0, 0, 0, 0, 0, 0, 1,
                                   1, 0, 0, 0, 0, 0, 0, 1];
    shuffle(fixColorIdx_Run2);
else:
    fixColorIdx_Run1 =  [1, 0, 0, 0,
                                        1, 0, 0, 0,
                                        1, 0, 0, 0,
                                        1, 0, 0, 0,
                                        1, 0, 0, 0,
                                        1, 0, 0, 0,
                                        1, 0, 0, 0,
                                        1, 0, 0, 0,
                                        1, 0, 0, 0,
                                        1, 0, 0, 0,
                                        1, 0, 0, 0,
                                        1, 0, 0, 0];
    shuffle(fixColorIdx_Run1);
    fixColorIdx_Run2 = [1, 0, 0, 0,
                                        1, 0, 0, 0,
                                        1, 0, 0, 0,
                                        1, 0, 0, 0,
                                        1, 0, 0, 0,
                                        1, 0, 0, 0,
                                        1, 0, 0, 0,
                                        1, 0, 0, 0,
                                        1, 0, 0, 0,
                                        1, 0, 0, 0,
                                        1, 0, 0, 0,
                                        1, 0, 0, 0];
    shuffle(fixColorIdx_Run2);
prac_instr1 = visual.ImageStim(
    win=win,
    name='prac_instr1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.75*1.77, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
start_exp_press = keyboard.Keyboard()

# Initialize components for Routine "pracInstruct2"
pracInstruct2Clock = core.Clock()
prac_instr2 = visual.ImageStim(
    win=win,
    name='prac_instr2', 
    image='Designs/prac_instr2.png', mask=None,
    ori=0, pos=(0, 0), size=(0.75*1.77, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "pracInstruct3"
pracInstruct3Clock = core.Clock()
prac_instr3 = visual.ImageStim(
    win=win,
    name='prac_instr3', 
    image='Designs/prac_instr3.png', mask=None,
    ori=0, pos=(0, 0), size=(0.75*1.77, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "hand_hold_instr"
hand_hold_instrClock = core.Clock()
if expInfo['design'] == '1':
    hand_hold_ex1 = 'Designs/design1_run1_ex.png'
    handHoldCorr1 = 'j'
    hold_hand_R1_img = 'Stimuli/HofS2.jpg'
    hand_hold_ex2 = 'Designs/design1_run2_ex.png'
    handHoldCorr2 = 'j'
    hold_hand_R2_img = 'Stimuli/SofH2.jpg'
    hand_hold_feedback1corr = 'Designs/hand_hold_local_corr.png'
    hand_hold_feedback1incorr = 'Designs/hand_hold_local_incorr.png'
    hand_hold_feedback2corr = 'Designs/hand_hold_global_corr.png'
    hand_hold_feedback2incorr = 'Designs/hand_hold_global_incorr.png'    
elif expInfo['design'] == '2':
    hand_hold_ex1 = 'Designs/design2_run1_ex.png'
    handHoldCorr1 = 'j'
    hold_hand_R1_img = 'Stimuli/SofH2.jpg'
    hand_hold_ex2 = 'Designs/design2_run2_ex.png'
    handHoldCorr2 = 'j'
    hold_hand_R2_img = 'Stimuli/HofS2.jpg'
    hand_hold_feedback1corr = 'Designs/hand_hold_global_corr.png'
    hand_hold_feedback1incorr = 'Designs/hand_hold_global_incorr.png'
    hand_hold_feedback2corr = 'Designs/hand_hold_local_corr.png'
    hand_hold_feedback2incorr = 'Designs/hand_hold_local_incorr.png' 
elif expInfo['design'] == '3':
    hand_hold_ex1 = 'Designs/design3_run1_ex.png'
    handHoldCorr1 = 'f'
    hold_hand_R1_img = 'Stimuli/SofH2.jpg'
    hand_hold_ex2 = 'Designs/design3_run2_ex.png'
    handHoldCorr2 = 'f'
    hold_hand_R2_img = 'Stimuli/HofS2.jpg'
    hand_hold_feedback1corr = 'Designs/hand_hold_global_corr.png'
    hand_hold_feedback1incorr = 'Designs/hand_hold_global_incorr.png'
    hand_hold_feedback2corr = 'Designs/hand_hold_local_corr.png'
    hand_hold_feedback2incorr = 'Designs/hand_hold_local_incorr.png'    
elif expInfo['design'] == '4':
    hand_hold_ex1 = 'Designs/design4_run1_ex.png'
    handHoldCorr1 = 'f'
    hold_hand_R1_img = 'Stimuli/HofS2.jpg'
    hand_hold_ex2 = 'Designs/design4_run2_ex.png'
    handHoldCorr2 = 'f'
    hold_hand_R2_img = 'Stimuli/SofH2.jpg'
    hand_hold_feedback1corr = 'Designs/hand_hold_local_corr.png'
    hand_hold_feedback1incorr = 'Designs/hand_hold_local_incorr.png'
    hand_hold_feedback2corr = 'Designs/hand_hold_global_corr.png'
    hand_hold_feedback2incorr = 'Designs/hand_hold_global_incorr.png' 
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.75*1.77, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
key_resp_9 = keyboard.Keyboard()

# Initialize components for Routine "hand_hold_trial"
hand_hold_trialClock = core.Clock()
text_8 = visual.TextStim(win=win, name='text_8',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
hand_hold_resp = keyboard.Keyboard()

# Initialize components for Routine "hand_hold_feedback"
hand_hold_feedbackClock = core.Clock()
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.75*1.77, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
key_resp_8 = keyboard.Keyboard()

# Initialize components for Routine "prac_instr_run1"
prac_instr_run1Clock = core.Clock()
if int(expInfo['design'])==1:
    instructions_run1 = 'Designs/design1_run1.png'
    cond_file_run1 = 'Designs/design1_run1.csv'
elif int(expInfo['design'])==2:
    instructions_run1 = 'Designs/design2_run1.png'
    cond_file_run1 = 'Designs/design2_run1.csv'
elif int(expInfo['design'])==3:
    instructions_run1 = 'Designs/design3_run1.png'
    cond_file_run1 = 'Designs/design3_run1.csv'
elif int(expInfo['design'])==4:
    instructions_run1 = 'Designs/design4_run1.png'
    cond_file_run1 = 'Designs/design4_run1.csv'

Pinstructions_imageR1 = visual.ImageStim(
    win=win,
    name='Pinstructions_imageR1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.75*1.75, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "startPrac"
startPracClock = core.Clock()

# Initialize components for Routine "pracFixR1"
pracFixR1Clock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "prac_img"
prac_imgClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
prac_image = visual.ImageStim(
    win=win,
    name='prac_image', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
prac_resp = keyboard.Keyboard()
prac_fix_resp = keyboard.Keyboard()

# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
imFeedback = visual.ImageStim(
    win=win,
    name='imFeedback', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
feedback_msg = visual.TextStim(win=win, name='feedback_msg',
    text='default text',
    font='Arial',
    pos=(0, -0.25), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "checkPrac1"
checkPrac1Clock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "trial_instr_run1"
trial_instr_run1Clock = core.Clock()
if expInfo['design']=='1':
    instructions_run1 = 'Designs/design1_run1.png'
    cond_file_run1 = 'Designs/design1_run1.csv'
elif expInfo['design']=='2':
    instructions_run1 = 'Designs/design2_run1.png'
    cond_file_run1 = 'Designs/design2_run1.csv'
elif expInfo['design']=='3':
    instructions_run1 =  'Designs/design3_run1.png'
    cond_file_run1 = 'Designs/design3_run1.csv'
elif expInfo['design']=='4':
    instructions_run1 =  'Designs/design4_run1.png'
    cond_file_run1 = 'Designs/design4_run1.csv'

Trial_run1 = 1
Total_run1 = 96

Trial_run2 = 1
Total_run2 = 96/2

if expInfo['position']=='2':
    positionRows = [0,1,2,3,4,5,6,7]
if expInfo['position']=='1':
    positionRows = [0,1,2,3]
if expInfo['position']=='3':
    positionRows = [4,5,6,7]
instructions_imageR1 = visual.ImageStim(
    win=win,
    name='instructions_imageR1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.75*1.77, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "trialFixR1"
trialFixR1Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
fix_resp1_1 = keyboard.Keyboard()

# Initialize components for Routine "trial_img"
trial_imgClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
trial_image = visual.ImageStim(
    win=win,
    name='trial_image', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
trial_resp = keyboard.Keyboard()
fix_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "btwn_trial_GJ"
btwn_trial_GJClock = core.Clock()
image_4 = visual.ImageStim(
    win=win,
    name='image_4', 
    image='Designs/baby_dory_GJ.png', mask=None,
    ori=0, pos=(0, 0), size=(0.4, 0.4*1.83),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)

# Initialize components for Routine "hand_hold_instr"
hand_hold_instrClock = core.Clock()
if expInfo['design'] == '1':
    hand_hold_ex1 = 'Designs/design1_run1_ex.png'
    handHoldCorr1 = 'j'
    hold_hand_R1_img = 'Stimuli/HofS2.jpg'
    hand_hold_ex2 = 'Designs/design1_run2_ex.png'
    handHoldCorr2 = 'j'
    hold_hand_R2_img = 'Stimuli/SofH2.jpg'
    hand_hold_feedback1corr = 'Designs/hand_hold_local_corr.png'
    hand_hold_feedback1incorr = 'Designs/hand_hold_local_incorr.png'
    hand_hold_feedback2corr = 'Designs/hand_hold_global_corr.png'
    hand_hold_feedback2incorr = 'Designs/hand_hold_global_incorr.png'    
elif expInfo['design'] == '2':
    hand_hold_ex1 = 'Designs/design2_run1_ex.png'
    handHoldCorr1 = 'j'
    hold_hand_R1_img = 'Stimuli/SofH2.jpg'
    hand_hold_ex2 = 'Designs/design2_run2_ex.png'
    handHoldCorr2 = 'j'
    hold_hand_R2_img = 'Stimuli/HofS2.jpg'
    hand_hold_feedback1corr = 'Designs/hand_hold_global_corr.png'
    hand_hold_feedback1incorr = 'Designs/hand_hold_global_incorr.png'
    hand_hold_feedback2corr = 'Designs/hand_hold_local_corr.png'
    hand_hold_feedback2incorr = 'Designs/hand_hold_local_incorr.png' 
elif expInfo['design'] == '3':
    hand_hold_ex1 = 'Designs/design3_run1_ex.png'
    handHoldCorr1 = 'f'
    hold_hand_R1_img = 'Stimuli/SofH2.jpg'
    hand_hold_ex2 = 'Designs/design3_run2_ex.png'
    handHoldCorr2 = 'f'
    hold_hand_R2_img = 'Stimuli/HofS2.jpg'
    hand_hold_feedback1corr = 'Designs/hand_hold_global_corr.png'
    hand_hold_feedback1incorr = 'Designs/hand_hold_global_incorr.png'
    hand_hold_feedback2corr = 'Designs/hand_hold_local_corr.png'
    hand_hold_feedback2incorr = 'Designs/hand_hold_local_incorr.png'    
elif expInfo['design'] == '4':
    hand_hold_ex1 = 'Designs/design4_run1_ex.png'
    handHoldCorr1 = 'f'
    hold_hand_R1_img = 'Stimuli/HofS2.jpg'
    hand_hold_ex2 = 'Designs/design4_run2_ex.png'
    handHoldCorr2 = 'f'
    hold_hand_R2_img = 'Stimuli/SofH2.jpg'
    hand_hold_feedback1corr = 'Designs/hand_hold_local_corr.png'
    hand_hold_feedback1incorr = 'Designs/hand_hold_local_incorr.png'
    hand_hold_feedback2corr = 'Designs/hand_hold_global_corr.png'
    hand_hold_feedback2incorr = 'Designs/hand_hold_global_incorr.png' 
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.75*1.77, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
key_resp_9 = keyboard.Keyboard()

# Initialize components for Routine "hand_hold_trial"
hand_hold_trialClock = core.Clock()
text_8 = visual.TextStim(win=win, name='text_8',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
hand_hold_resp = keyboard.Keyboard()

# Initialize components for Routine "hand_hold_feedback"
hand_hold_feedbackClock = core.Clock()
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.75*1.77, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
key_resp_8 = keyboard.Keyboard()

# Initialize components for Routine "prac_instr_run2"
prac_instr_run2Clock = core.Clock()
if expInfo['design']=='1':
    instructions_run2 = 'Designs/design1_run2.png'
    cond_file_run2 = 'Designs/design1_run2.csv'
elif expInfo['design']=='2':
    instructions_run2 = 'Designs/design2_run2.png'
    cond_file_run2 = 'Designs/design2_run2.csv'
elif expInfo['design']=='3':
    instructions_run2 =  'Designs/design3_run2.png'
    cond_file_run2 = 'Designs/design3_run2.csv'
elif expInfo['design']=='4':
    instructions_run2 =  'Designs/design4_run2.png'
    cond_file_run2 = 'Designs/design4_run2.csv'

if expInfo['position']=='2':
    rand8Idx = [0,1,2,3,4,5,6,7];
    shuffle(rand8Idx)
    randRows_run2 = rand8Idx[0:4]
elif expInfo['position']=='1':
    rand4Idx = [0,1,2,3];
    shuffle(rand4Idx)
    randRows_run2 = rand4Idx
elif expInfo['position']=='3':
    rand4Idx = [4,5,6,7];
    shuffle(rand4Idx)
    randRows_run2 = rand4Idx
Pinstructions_imageR2 = visual.ImageStim(
    win=win,
    name='Pinstructions_imageR2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.75*1.77, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "startPrac"
startPracClock = core.Clock()

# Initialize components for Routine "pracFixR2"
pracFixR2Clock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
fix_respP2_1 = keyboard.Keyboard()

# Initialize components for Routine "prac_img"
prac_imgClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
prac_image = visual.ImageStim(
    win=win,
    name='prac_image', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
prac_resp = keyboard.Keyboard()
prac_fix_resp = keyboard.Keyboard()

# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
imFeedback = visual.ImageStim(
    win=win,
    name='imFeedback', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
feedback_msg = visual.TextStim(win=win, name='feedback_msg',
    text='default text',
    font='Arial',
    pos=(0, -0.25), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "checkPrac2"
checkPrac2Clock = core.Clock()
text_9 = visual.TextStim(win=win, name='text_9',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_10 = keyboard.Keyboard()

# Initialize components for Routine "trial_instr_run2"
trial_instr_run2Clock = core.Clock()
if expInfo['design']=='1':
    instructions_run2 = 'Designs/design1_run2.png'
    cond_file_run2 = 'Designs/design1_run2.csv'
elif expInfo['design']=='2':
    instructions_run2 = 'Designs/design2_run2.png'
    cond_file_run2 = 'Designs/design2_run2.csv'
elif expInfo['design']=='3':
    instructions_run2 =  'Designs/design3_run2.png'
    cond_file_run2 = 'Designs/design3_run2.csv'
elif expInfo['design']=='4':
    instructions_run2 =  'Designs/design4_run2.png'
    cond_file_run2 = 'Designs/design4_run2.csv'
instructions_imageR2 = visual.ImageStim(
    win=win,
    name='instructions_imageR2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.75*1.77, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "trialFixR2"
trialFixR2Clock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
fix_resp2_1 = keyboard.Keyboard()

# Initialize components for Routine "trial_img"
trial_imgClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
trial_image = visual.ImageStim(
    win=win,
    name='trial_image', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
trial_resp = keyboard.Keyboard()
fix_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "btwn_trial_GJ"
btwn_trial_GJClock = core.Clock()
image_4 = visual.ImageStim(
    win=win,
    name='image_4', 
    image='Designs/baby_dory_GJ.png', mask=None,
    ori=0, pos=(0, 0), size=(0.4, 0.4*1.83),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)

# Initialize components for Routine "trial_instr_run1"
trial_instr_run1Clock = core.Clock()
if expInfo['design']=='1':
    instructions_run1 = 'Designs/design1_run1.png'
    cond_file_run1 = 'Designs/design1_run1.csv'
elif expInfo['design']=='2':
    instructions_run1 = 'Designs/design2_run1.png'
    cond_file_run1 = 'Designs/design2_run1.csv'
elif expInfo['design']=='3':
    instructions_run1 =  'Designs/design3_run1.png'
    cond_file_run1 = 'Designs/design3_run1.csv'
elif expInfo['design']=='4':
    instructions_run1 =  'Designs/design4_run1.png'
    cond_file_run1 = 'Designs/design4_run1.csv'

Trial_run1 = 1
Total_run1 = 96

Trial_run2 = 1
Total_run2 = 96/2

if expInfo['position']=='2':
    positionRows = [0,1,2,3,4,5,6,7]
if expInfo['position']=='1':
    positionRows = [0,1,2,3]
if expInfo['position']=='3':
    positionRows = [4,5,6,7]
instructions_imageR1 = visual.ImageStim(
    win=win,
    name='instructions_imageR1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.75*1.77, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "trialFixR1"
trialFixR1Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
fix_resp1_1 = keyboard.Keyboard()

# Initialize components for Routine "trial_img"
trial_imgClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
trial_image = visual.ImageStim(
    win=win,
    name='trial_image', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
trial_resp = keyboard.Keyboard()
fix_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "btwn_trial_GJ"
btwn_trial_GJClock = core.Clock()
image_4 = visual.ImageStim(
    win=win,
    name='image_4', 
    image='Designs/baby_dory_GJ.png', mask=None,
    ori=0, pos=(0, 0), size=(0.4, 0.4*1.83),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)

# Initialize components for Routine "trial_instr_run2"
trial_instr_run2Clock = core.Clock()
if expInfo['design']=='1':
    instructions_run2 = 'Designs/design1_run2.png'
    cond_file_run2 = 'Designs/design1_run2.csv'
elif expInfo['design']=='2':
    instructions_run2 = 'Designs/design2_run2.png'
    cond_file_run2 = 'Designs/design2_run2.csv'
elif expInfo['design']=='3':
    instructions_run2 =  'Designs/design3_run2.png'
    cond_file_run2 = 'Designs/design3_run2.csv'
elif expInfo['design']=='4':
    instructions_run2 =  'Designs/design4_run2.png'
    cond_file_run2 = 'Designs/design4_run2.csv'
instructions_imageR2 = visual.ImageStim(
    win=win,
    name='instructions_imageR2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.75*1.77, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "trialFixR2"
trialFixR2Clock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
fix_resp2_1 = keyboard.Keyboard()

# Initialize components for Routine "trial_img"
trial_imgClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
trial_image = visual.ImageStim(
    win=win,
    name='trial_image', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
trial_resp = keyboard.Keyboard()
fix_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "EndScreen"
EndScreenClock = core.Clock()
image_5 = visual.ImageStim(
    win=win,
    name='image_5', 
    image='Designs/baby_squirt_GJ.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5*1.6, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "screen_scale"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
screen_scaleComponents = [text_top, text_bottom, ccimage]
for thisComponent in screen_scaleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
screen_scaleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "screen_scale"-------
while continueRoutine:
    # get current time
    t = screen_scaleClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=screen_scaleClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    keys=event.getKeys()
    
    if len(keys):
        if t-oldt<.5:
            dscale=5*dbase
            oldt=t
        else:
            dscale=dbase
            oldt=t
        if 'space' in keys:
            continueRoutine=False
        elif 'up' in keys:
            y_scale=round((y_scale+dscale)*10000)/10000
        elif 'down' in keys:
            y_scale=round((y_scale-dscale)*10000)/10000
        elif 'left' in keys:
            x_scale=round((x_scale-dscale)*10000)/10000
        elif 'right' in keys:
            x_scale=round((x_scale+dscale)*10000)/10000
        screen_height=round(vsize*10/y_scale)/10
        ccimage.size=[x_size*x_scale, y_size*y_scale]
        
    
    # *text_top* updates
    if text_top.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_top.frameNStart = frameN  # exact frame index
        text_top.tStart = t  # local t and not account for scr refresh
        text_top.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_top, 'tStartRefresh')  # time at next scr refresh
        text_top.setAutoDraw(True)
    
    # *text_bottom* updates
    if text_bottom.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_bottom.frameNStart = frameN  # exact frame index
        text_bottom.tStart = t  # local t and not account for scr refresh
        text_bottom.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_bottom, 'tStartRefresh')  # time at next scr refresh
        text_bottom.setAutoDraw(True)
    
    # *ccimage* updates
    if ccimage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ccimage.frameNStart = frameN  # exact frame index
        ccimage.tStart = t  # local t and not account for scr refresh
        ccimage.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ccimage, 'tStartRefresh')  # time at next scr refresh
        ccimage.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in screen_scaleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "screen_scale"-------
for thisComponent in screen_scaleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('X Scale',x_scale)
thisExp.addData('Y Scale',y_scale)

# the Routine "screen_scale" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "pracInstruct"-------
continueRoutine = True
# update component parameters for each repeat
hand_hold_run = 1
prac_instr1.setImage('Designs/prac_instr1.png')
start_exp_press.keys = []
start_exp_press.rt = []
_start_exp_press_allKeys = []
# keep track of which components have finished
pracInstructComponents = [prac_instr1, start_exp_press]
for thisComponent in pracInstructComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
pracInstructClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "pracInstruct"-------
while continueRoutine:
    # get current time
    t = pracInstructClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=pracInstructClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *prac_instr1* updates
    if prac_instr1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        prac_instr1.frameNStart = frameN  # exact frame index
        prac_instr1.tStart = t  # local t and not account for scr refresh
        prac_instr1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prac_instr1, 'tStartRefresh')  # time at next scr refresh
        prac_instr1.setAutoDraw(True)
    
    # *start_exp_press* updates
    waitOnFlip = False
    if start_exp_press.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
        # keep track of start time/frame for later
        start_exp_press.frameNStart = frameN  # exact frame index
        start_exp_press.tStart = t  # local t and not account for scr refresh
        start_exp_press.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_exp_press, 'tStartRefresh')  # time at next scr refresh
        start_exp_press.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(start_exp_press.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(start_exp_press.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if start_exp_press.status == STARTED and not waitOnFlip:
        theseKeys = start_exp_press.getKeys(keyList=['space'], waitRelease=False)
        _start_exp_press_allKeys.extend(theseKeys)
        if len(_start_exp_press_allKeys):
            start_exp_press.keys = _start_exp_press_allKeys[-1].name  # just the last key pressed
            start_exp_press.rt = _start_exp_press_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pracInstructComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "pracInstruct"-------
for thisComponent in pracInstructComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "pracInstruct" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "pracInstruct2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
pracInstruct2Components = [prac_instr2, key_resp_6]
for thisComponent in pracInstruct2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
pracInstruct2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "pracInstruct2"-------
while continueRoutine:
    # get current time
    t = pracInstruct2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=pracInstruct2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *prac_instr2* updates
    if prac_instr2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        prac_instr2.frameNStart = frameN  # exact frame index
        prac_instr2.tStart = t  # local t and not account for scr refresh
        prac_instr2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prac_instr2, 'tStartRefresh')  # time at next scr refresh
        prac_instr2.setAutoDraw(True)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pracInstruct2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "pracInstruct2"-------
for thisComponent in pracInstruct2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "pracInstruct2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "pracInstruct3"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
# keep track of which components have finished
pracInstruct3Components = [prac_instr3, key_resp_7]
for thisComponent in pracInstruct3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
pracInstruct3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "pracInstruct3"-------
while continueRoutine:
    # get current time
    t = pracInstruct3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=pracInstruct3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *prac_instr3* updates
    if prac_instr3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        prac_instr3.frameNStart = frameN  # exact frame index
        prac_instr3.tStart = t  # local t and not account for scr refresh
        prac_instr3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prac_instr3, 'tStartRefresh')  # time at next scr refresh
        prac_instr3.setAutoDraw(True)
    
    # *key_resp_7* updates
    waitOnFlip = False
    if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
        # keep track of start time/frame for later
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.tStart = t  # local t and not account for scr refresh
        key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_7.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_7.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_7_allKeys.extend(theseKeys)
        if len(_key_resp_7_allKeys):
            key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
            key_resp_7.rt = _key_resp_7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pracInstruct3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "pracInstruct3"-------
for thisComponent in pracInstruct3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "pracInstruct3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "hand_hold_instr"-------
continueRoutine = True
# update component parameters for each repeat
left_right=''
rand_side=''
if expInfo['position'] == '0':
    xPosition = 0
elif expInfo['position'] == '2':
    left_right = [0,1]
    shuffle(left_right)
    rand_side = [0]
    if rand_side == 0: #left
        xPosition = -(width4deg*x_scale)
    else: #right
        xPosition = width4deg*x_scale
elif expInfo['position'] == '1':
    xPosition = -(width4deg*x_scale)
elif expInfo['position'] == '3':
    xPosition = width4deg*x_scale

if hand_hold_run == 1:
    hand_hold_ex = hand_hold_ex1
    handHoldCorr = handHoldCorr1
    hold_hand_img = hold_hand_R1_img
    hand_hold_feedbackcorr = hand_hold_feedback1corr
    hand_hold_feedbackincorr = hand_hold_feedback1incorr
else:
    hand_hold_ex = hand_hold_ex2
    handHoldCorr = handHoldCorr2
    hold_hand_img = hold_hand_R2_img
    hand_hold_feedbackcorr = hand_hold_feedback2corr
    hand_hold_feedbackincorr = hand_hold_feedback2incorr

image_2.setImage(hand_hold_ex)
key_resp_9.keys = []
key_resp_9.rt = []
_key_resp_9_allKeys = []
# keep track of which components have finished
hand_hold_instrComponents = [image_2, key_resp_9]
for thisComponent in hand_hold_instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
hand_hold_instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "hand_hold_instr"-------
while continueRoutine:
    # get current time
    t = hand_hold_instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=hand_hold_instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_2* updates
    if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_2.frameNStart = frameN  # exact frame index
        image_2.tStart = t  # local t and not account for scr refresh
        image_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
        image_2.setAutoDraw(True)
    
    # *key_resp_9* updates
    waitOnFlip = False
    if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.tStart = t  # local t and not account for scr refresh
        key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_9.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_9.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_9_allKeys.extend(theseKeys)
        if len(_key_resp_9_allKeys):
            key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
            key_resp_9.rt = _key_resp_9_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in hand_hold_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "hand_hold_instr"-------
for thisComponent in hand_hold_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "hand_hold_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "hand_hold_trial"-------
continueRoutine = True
# update component parameters for each repeat
image.setPos((xPosition, 0))
image.setSize((width*x_scale, height*y_scale))
image.setImage(hold_hand_img)
hand_hold_resp.keys = []
hand_hold_resp.rt = []
_hand_hold_resp_allKeys = []
# keep track of which components have finished
hand_hold_trialComponents = [text_8, image, hand_hold_resp]
for thisComponent in hand_hold_trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
hand_hold_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "hand_hold_trial"-------
while continueRoutine:
    # get current time
    t = hand_hold_trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=hand_hold_trialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_8* updates
    if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_8.frameNStart = frameN  # exact frame index
        text_8.tStart = t  # local t and not account for scr refresh
        text_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
        text_8.setAutoDraw(True)
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    
    # *hand_hold_resp* updates
    waitOnFlip = False
    if hand_hold_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        hand_hold_resp.frameNStart = frameN  # exact frame index
        hand_hold_resp.tStart = t  # local t and not account for scr refresh
        hand_hold_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(hand_hold_resp, 'tStartRefresh')  # time at next scr refresh
        hand_hold_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(hand_hold_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(hand_hold_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if hand_hold_resp.status == STARTED and not waitOnFlip:
        theseKeys = hand_hold_resp.getKeys(keyList=['f', 'j'], waitRelease=False)
        _hand_hold_resp_allKeys.extend(theseKeys)
        if len(_hand_hold_resp_allKeys):
            hand_hold_resp.keys = _hand_hold_resp_allKeys[-1].name  # just the last key pressed
            hand_hold_resp.rt = _hand_hold_resp_allKeys[-1].rt
            # was this correct?
            if (hand_hold_resp.keys == str(handHoldCorr)) or (hand_hold_resp.keys == handHoldCorr):
                hand_hold_resp.corr = 1
            else:
                hand_hold_resp.corr = 0
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in hand_hold_trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "hand_hold_trial"-------
for thisComponent in hand_hold_trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_8.started', text_8.tStartRefresh)
thisExp.addData('text_8.stopped', text_8.tStopRefresh)
# check responses
if hand_hold_resp.keys in ['', [], None]:  # No response was made
    hand_hold_resp.keys = None
    # was no response the correct answer?!
    if str(handHoldCorr).lower() == 'none':
       hand_hold_resp.corr = 1;  # correct non-response
    else:
       hand_hold_resp.corr = 0;  # failed to respond (incorrectly)
# store data for thisExp (ExperimentHandler)
thisExp.addData('hand_hold_resp.keys',hand_hold_resp.keys)
thisExp.addData('hand_hold_resp.corr', hand_hold_resp.corr)
if hand_hold_resp.keys != None:  # we had a response
    thisExp.addData('hand_hold_resp.rt', hand_hold_resp.rt)
thisExp.nextEntry()
# the Routine "hand_hold_trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "hand_hold_feedback"-------
continueRoutine = True
# update component parameters for each repeat
feedHHim=''

print(hand_hold_run)
print(hand_hold_resp.keys)
print(handHoldCorr)
print(hand_hold_feedback1corr)
if hand_hold_run == 1:
    if hand_hold_resp.keys == handHoldCorr:
        feedHHim = hand_hold_feedback1corr
    else:
        feedHHim = hand_hold_feedback1incorr
else:
    if hand_hold_resp.keys == handHoldCorr:
        feedHHim = hand_hold_feedback2corr
    else:
        feedHHim = hand_hold_feedback2incorr

print(feedHHim)
image_3.setImage(feedHHim)
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
# keep track of which components have finished
hand_hold_feedbackComponents = [image_3, key_resp_8]
for thisComponent in hand_hold_feedbackComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
hand_hold_feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "hand_hold_feedback"-------
while continueRoutine:
    # get current time
    t = hand_hold_feedbackClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=hand_hold_feedbackClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_3* updates
    if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_3.frameNStart = frameN  # exact frame index
        image_3.tStart = t  # local t and not account for scr refresh
        image_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
        image_3.setAutoDraw(True)
    
    # *key_resp_8* updates
    waitOnFlip = False
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
            key_resp_8.rt = _key_resp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in hand_hold_feedbackComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "hand_hold_feedback"-------
for thisComponent in hand_hold_feedbackComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "hand_hold_feedback" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "prac_instr_run1"-------
continueRoutine = True
# update component parameters for each repeat
Pinstructions_imageR1.setImage(instructions_run1)
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
prac_instr_run1Components = [Pinstructions_imageR1, key_resp]
for thisComponent in prac_instr_run1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
prac_instr_run1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "prac_instr_run1"-------
while continueRoutine:
    # get current time
    t = prac_instr_run1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=prac_instr_run1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Pinstructions_imageR1* updates
    if Pinstructions_imageR1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Pinstructions_imageR1.frameNStart = frameN  # exact frame index
        Pinstructions_imageR1.tStart = t  # local t and not account for scr refresh
        Pinstructions_imageR1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Pinstructions_imageR1, 'tStartRefresh')  # time at next scr refresh
        Pinstructions_imageR1.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in prac_instr_run1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "prac_instr_run1"-------
for thisComponent in prac_instr_run1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "prac_instr_run1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
repeats = data.TrialHandler(nReps=10, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='repeats')
thisExp.addLoop(repeats)  # add the loop to the experiment
thisRepeat = repeats.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRepeat.rgb)
if thisRepeat != None:
    for paramName in thisRepeat:
        exec('{} = thisRepeat[paramName]'.format(paramName))

for thisRepeat in repeats:
    currentLoop = repeats
    # abbreviate parameter names if possible (e.g. rgb = thisRepeat.rgb)
    if thisRepeat != None:
        for paramName in thisRepeat:
            exec('{} = thisRepeat[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "startPrac"-------
    continueRoutine = True
    # update component parameters for each repeat
    numIncorr_fix = 0
    numIncorr_miss = 0
    numIncorr_img = 0
    
    rand4Idx = ''
    rand8Idx = ''
    if int(expInfo['position'])==2:
        rand8Idx = [0,1,2,3,4,5,6,7];
        shuffle(rand8Idx)
        randRows_run1 = rand8Idx[0:6]
    elif int(expInfo['position'])==1:
        rand4Idx = [0,1,2,3,0,1];
        shuffle(rand4Idx)
        randRows_run1 = rand4Idx
    elif int(expInfo['position'])==3:
        rand4Idx = [4,5,6,7,4,5];
        shuffle(rand4Idx)
        randRows_run1 = rand4Idx
    
    pTrial_run1 = 1
    pracTotal_run1 = 6
    pTrial_run2 = 1
    pracTotal_run2 = 6
    
    # keep track of which components have finished
    startPracComponents = []
    for thisComponent in startPracComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    startPracClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "startPrac"-------
    while continueRoutine:
        # get current time
        t = startPracClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=startPracClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in startPracComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "startPrac"-------
    for thisComponent in startPracComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "startPrac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    prac_trials_run1 = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(cond_file_run1, selection=randRows_run1),
        seed=None, name='prac_trials_run1')
    thisExp.addLoop(prac_trials_run1)  # add the loop to the experiment
    thisPrac_trials_run1 = prac_trials_run1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPrac_trials_run1.rgb)
    if thisPrac_trials_run1 != None:
        for paramName in thisPrac_trials_run1:
            exec('{} = thisPrac_trials_run1[paramName]'.format(paramName))
    
    for thisPrac_trials_run1 in prac_trials_run1:
        currentLoop = prac_trials_run1
        # abbreviate parameter names if possible (e.g. rgb = thisPrac_trials_run1.rgb)
        if thisPrac_trials_run1 != None:
            for paramName in thisPrac_trials_run1:
                exec('{} = thisPrac_trials_run1[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "pracFixR1"-------
        continueRoutine = True
        # update component parameters for each repeat
        trialMsg = "Practice: " + str(pTrial_run1) + ' of ' + str(pracTotal_run1)
        if pTrial_run1-1 == 0:
            currFix = fixColor_opts[0]
            corrfixResp = None
        else:
            if prac1_fixColSwitch[pTrial_run1-1] == 1:
                if currFix == 'white':
                    currFix = 'black'
                    corrfixResp = 'space'
                elif currFix == 'black':
                    currFix = 'white'
                    corrfixResp = 'space'
            else:
                currFix = currFix
                corrfixResp = None
        a = 1.25 # min ITI
        b = 1.75 # max ITI
        fixDur = (b-a) * random()+a
        
        if int(expInfo['position']) == 0:
            xPosition = 0
        elif int(expInfo['position']) == 2:
            if side == 'left':
                xPosition = -(width4deg*x_scale)
            elif side == 'right':
                xPosition = width4deg*x_scale
        elif int(expInfo['position']) == 1:
            xPosition = -(width4deg*x_scale)
        elif int(expInfo['position']) == 3:
            xPosition = width4deg*x_scale
        
        thisExp.addData('fixpR1', prac1_fixColSwitch[pTrial_run1-1])
        text.setColor(currFix, colorSpace='rgb')
        # keep track of which components have finished
        pracFixR1Components = [text]
        for thisComponent in pracFixR1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        pracFixR1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "pracFixR1"-------
        while continueRoutine:
            # get current time
            t = pracFixR1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=pracFixR1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                text.setAutoDraw(True)
            if text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text.tStartRefresh + fixDur-frameTolerance:
                    # keep track of stop time/frame for later
                    text.tStop = t  # not accounting for scr refresh
                    text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                    text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in pracFixR1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "pracFixR1"-------
        for thisComponent in pracFixR1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        pTrial_run1 = pTrial_run1 + 1
        # the Routine "pracFixR1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "prac_img"-------
        continueRoutine = True
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        text_5.setColor(currFix, colorSpace='rgb')
        prac_image.setPos((xPosition, 0))
        prac_image.setSize((width*x_scale, height*y_scale))
        prac_image.setImage(imFile)
        prac_resp.keys = []
        prac_resp.rt = []
        _prac_resp_allKeys = []
        prac_fix_resp.keys = []
        prac_fix_resp.rt = []
        _prac_fix_resp_allKeys = []
        # keep track of which components have finished
        prac_imgComponents = [text_5, prac_image, prac_resp, prac_fix_resp]
        for thisComponent in prac_imgComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        prac_imgClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "prac_img"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = prac_imgClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=prac_imgClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_5* updates
            if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_5.frameNStart = frameN  # exact frame index
                text_5.tStart = t  # local t and not account for scr refresh
                text_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
                text_5.setAutoDraw(True)
            if text_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_5.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    text_5.tStop = t  # not accounting for scr refresh
                    text_5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
                    text_5.setAutoDraw(False)
            
            # *prac_image* updates
            if prac_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prac_image.frameNStart = frameN  # exact frame index
                prac_image.tStart = t  # local t and not account for scr refresh
                prac_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prac_image, 'tStartRefresh')  # time at next scr refresh
                prac_image.setAutoDraw(True)
            if prac_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > prac_image.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    prac_image.tStop = t  # not accounting for scr refresh
                    prac_image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(prac_image, 'tStopRefresh')  # time at next scr refresh
                    prac_image.setAutoDraw(False)
            
            # *prac_resp* updates
            waitOnFlip = False
            if prac_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prac_resp.frameNStart = frameN  # exact frame index
                prac_resp.tStart = t  # local t and not account for scr refresh
                prac_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prac_resp, 'tStartRefresh')  # time at next scr refresh
                prac_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(prac_resp.clock.reset)  # t=0 on next screen flip
            if prac_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > prac_resp.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    prac_resp.tStop = t  # not accounting for scr refresh
                    prac_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(prac_resp, 'tStopRefresh')  # time at next scr refresh
                    prac_resp.status = FINISHED
            if prac_resp.status == STARTED and not waitOnFlip:
                theseKeys = prac_resp.getKeys(keyList=['f', 'j'], waitRelease=False)
                _prac_resp_allKeys.extend(theseKeys)
                if len(_prac_resp_allKeys):
                    prac_resp.keys = _prac_resp_allKeys[-1].name  # just the last key pressed
                    prac_resp.rt = _prac_resp_allKeys[-1].rt
                    # was this correct?
                    if (prac_resp.keys == str(corr)) or (prac_resp.keys == corr):
                        prac_resp.corr = 1
                    else:
                        prac_resp.corr = 0
            
            # *prac_fix_resp* updates
            waitOnFlip = False
            if prac_fix_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prac_fix_resp.frameNStart = frameN  # exact frame index
                prac_fix_resp.tStart = t  # local t and not account for scr refresh
                prac_fix_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prac_fix_resp, 'tStartRefresh')  # time at next scr refresh
                prac_fix_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(prac_fix_resp.clock.reset)  # t=0 on next screen flip
            if prac_fix_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > prac_fix_resp.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    prac_fix_resp.tStop = t  # not accounting for scr refresh
                    prac_fix_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(prac_fix_resp, 'tStopRefresh')  # time at next scr refresh
                    prac_fix_resp.status = FINISHED
            if prac_fix_resp.status == STARTED and not waitOnFlip:
                theseKeys = prac_fix_resp.getKeys(keyList=['space'], waitRelease=False)
                _prac_fix_resp_allKeys.extend(theseKeys)
                if len(_prac_fix_resp_allKeys):
                    prac_fix_resp.keys = _prac_fix_resp_allKeys[-1].name  # just the last key pressed
                    prac_fix_resp.rt = _prac_fix_resp_allKeys[-1].rt
                    # was this correct?
                    if (prac_fix_resp.keys == str(corrfixResp)) or (prac_fix_resp.keys == corrfixResp):
                        prac_fix_resp.corr = 1
                    else:
                        prac_fix_resp.corr = 0
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in prac_imgComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "prac_img"-------
        for thisComponent in prac_imgComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if prac_resp.keys in ['', [], None]:  # No response was made
            prac_resp.keys = None
            # was no response the correct answer?!
            if str(corr).lower() == 'none':
               prac_resp.corr = 1;  # correct non-response
            else:
               prac_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for prac_trials_run1 (TrialHandler)
        prac_trials_run1.addData('prac_resp.keys',prac_resp.keys)
        prac_trials_run1.addData('prac_resp.corr', prac_resp.corr)
        if prac_resp.keys != None:  # we had a response
            prac_trials_run1.addData('prac_resp.rt', prac_resp.rt)
        # check responses
        if prac_fix_resp.keys in ['', [], None]:  # No response was made
            prac_fix_resp.keys = None
            # was no response the correct answer?!
            if str(corrfixResp).lower() == 'none':
               prac_fix_resp.corr = 1;  # correct non-response
            else:
               prac_fix_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for prac_trials_run1 (TrialHandler)
        prac_trials_run1.addData('prac_fix_resp.keys',prac_fix_resp.keys)
        prac_trials_run1.addData('prac_fix_resp.corr', prac_fix_resp.corr)
        if prac_fix_resp.keys != None:  # we had a response
            prac_trials_run1.addData('prac_fix_resp.rt', prac_fix_resp.rt)
        
        # ------Prepare to start Routine "Feedback"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        feedIM =''
        if prac_resp.keys == corr: 
            if prac_fix_resp.corr == 1:
                feedIM = 'Stimuli/greenCheck.png'
                prac_msg = 'Well done!'
            else:
                numIncorr_fix = numIncorr_fix + 1
                feedIM = 'Stimuli/redWrong.png'
                if corrfixResp == 'space':
                    prac_msg = 'Oops, you missed the cross response.'
                else:
                    prac_msg = 'Oops, you pressed space when there was no fix change.'
        elif prac_resp.keys != corr:
            if prac_resp.keys == None:
               feedIM = 'Stimuli/redWrong.png'
               numIncorr_miss = numIncorr_miss + 1
               if corrfixResp == 'space':
                    numIncorr_fix = numIncorr_fix + 1
               prac_msg = 'Oops, time ran out. That\'s ok, try again!' 
            else:
                if prac_fix_resp.corr == 1:
                    feedIM = 'Stimuli/redWrong.png'
                    numIncorr_img = numIncorr_img + 1
                    if corrfixResp == 'space':
                        prac_msg = 'Good job! You got pressed space when the cross changed! But the picture response was wrong.'
                    else:
                        prac_msg = 'Oops, the picture response was wrong.'
                else:
                    numIncorr_img = numIncorr_img + 1
                    numIncorr_fix = numIncorr_fix + 1
                    feedIM = 'Stimuli/redWrong.png'
                    if corrfixResp == 'space':
                        prac_msg = 'Oops, you missed the cross change and the picture response was wrong.'
                    else:
                        prac_msg = 'Oops, you press space when the cross didn\'t change and the picture response was wrong.'
        
        
        imFeedback.setImage(feedIM)
        feedback_msg.setText(prac_msg)
        # keep track of which components have finished
        FeedbackComponents = [imFeedback, feedback_msg]
        for thisComponent in FeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        FeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Feedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = FeedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=FeedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *imFeedback* updates
            if imFeedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                imFeedback.frameNStart = frameN  # exact frame index
                imFeedback.tStart = t  # local t and not account for scr refresh
                imFeedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imFeedback, 'tStartRefresh')  # time at next scr refresh
                imFeedback.setAutoDraw(True)
            if imFeedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > imFeedback.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    imFeedback.tStop = t  # not accounting for scr refresh
                    imFeedback.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(imFeedback, 'tStopRefresh')  # time at next scr refresh
                    imFeedback.setAutoDraw(False)
            
            # *feedback_msg* updates
            if feedback_msg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_msg.frameNStart = frameN  # exact frame index
                feedback_msg.tStart = t  # local t and not account for scr refresh
                feedback_msg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_msg, 'tStartRefresh')  # time at next scr refresh
                feedback_msg.setAutoDraw(True)
            if feedback_msg.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback_msg.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback_msg.tStop = t  # not accounting for scr refresh
                    feedback_msg.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(feedback_msg, 'tStopRefresh')  # time at next scr refresh
                    feedback_msg.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Feedback"-------
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        prac_trials_run1.addData('feedback_msg.started', feedback_msg.tStartRefresh)
        prac_trials_run1.addData('feedback_msg.stopped', feedback_msg.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'prac_trials_run1'
    
    
    # ------Prepare to start Routine "checkPrac1"-------
    continueRoutine = True
    # update component parameters for each repeat
    if (numIncorr_fix + numIncorr_miss + numIncorr_img) < 3 and (numIncorr_fix != 2):
        prac_feedback = 'Great job! You are now ready for the real game. \nPress Space to see the instructions again.'
        repeats.finished = True
    else:
        if numIncorr_fix > 1 and numIncorr_img < 2 and numIncorr_miss < 2:
            prac_feedback = 'Good job with the pictures! \n You missed ' + str(numIncorr_fix) + ' of the two fix changes. \n In the real game, make sure you press Space as soon as you see it change!\n\n Let\'s try some more practice. \n Press Space to start.'
        elif numIncorr_fix < 2 and numIncorr_img > 1 and numIncorr_miss < 2:
            prac_feedback = 'Good job, you got ' + str(2-numIncorr_fix) + ' of the 2 fix changes! \nYou missed ' + str(numIncorr_img) + ' of the pictures. \n Sometimes the big letter and the little letters are different. \nMake sure you focus on the right ones and press the right keys! \n\nLet\'s try some more practice. \n Press Space to start.'
        elif numIncorr_fix < 2 and numIncorr_img < 2 and numIncorr_miss > 1:
            prac_feedback = 'You missed ' + str(numIncorr_miss) + ' of the trials because the time was up. That\'s ok, in the real game the pictures will stay on, but try to go as fast as you can. \n\n Press Space to practice more.'
        else:
            prac_feedback = 'Nice try! You missed ' + str(numIncorr_img) + ' of the picture responses, ' + str(numIncorr_fix) + ' of the two fix changes, and ' + str(numIncorr_miss) + ' trials went by too fast. \n\nLet\'s try another round of practice. \nPress Space to start.'
    text_7.setText(prac_feedback

)
    key_resp_5.keys = []
    key_resp_5.rt = []
    _key_resp_5_allKeys = []
    # keep track of which components have finished
    checkPrac1Components = [text_7, key_resp_5]
    for thisComponent in checkPrac1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    checkPrac1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "checkPrac1"-------
    while continueRoutine:
        # get current time
        t = checkPrac1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=checkPrac1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_7* updates
        if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_7.frameNStart = frameN  # exact frame index
            text_7.tStart = t  # local t and not account for scr refresh
            text_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
            text_7.setAutoDraw(True)
        
        # *key_resp_5* updates
        waitOnFlip = False
        if key_resp_5.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.tStart = t  # local t and not account for scr refresh
            key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_5.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_5_allKeys.extend(theseKeys)
            if len(_key_resp_5_allKeys):
                key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in checkPrac1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "checkPrac1"-------
    for thisComponent in checkPrac1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "checkPrac1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 10 repeats of 'repeats'


# ------Prepare to start Routine "trial_instr_run1"-------
continueRoutine = True
# update component parameters for each repeat
instructions_imageR1.setImage(instructions_run1)
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
trial_instr_run1Components = [instructions_imageR1, key_resp_2]
for thisComponent in trial_instr_run1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_instr_run1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trial_instr_run1"-------
while continueRoutine:
    # get current time
    t = trial_instr_run1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_instr_run1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_imageR1* updates
    if instructions_imageR1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_imageR1.frameNStart = frameN  # exact frame index
        instructions_imageR1.tStart = t  # local t and not account for scr refresh
        instructions_imageR1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_imageR1, 'tStartRefresh')  # time at next scr refresh
        instructions_imageR1.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_instr_run1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_instr_run1"-------
for thisComponent in trial_instr_run1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "trial_instr_run1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_run1 = data.TrialHandler(nReps=6, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(cond_file_run1, selection=positionRows),
    seed=None, name='trials_run1')
thisExp.addLoop(trials_run1)  # add the loop to the experiment
thisTrials_run1 = trials_run1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_run1.rgb)
if thisTrials_run1 != None:
    for paramName in thisTrials_run1:
        exec('{} = thisTrials_run1[paramName]'.format(paramName))

for thisTrials_run1 in trials_run1:
    currentLoop = trials_run1
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_run1.rgb)
    if thisTrials_run1 != None:
        for paramName in thisTrials_run1:
            exec('{} = thisTrials_run1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trialFixR1"-------
    continueRoutine = True
    # update component parameters for each repeat
    if Trial_run1-1 == 0:
        currFix = fixColor_opts[0]
    else:
        if fixColorIdx_Run1[Trial_run1-1] == 0:
            currFix = currFix
        elif fixColorIdx_Run1[Trial_run1-1] == 1:
            if currFix == 'white':
                currFix = 'black'
            elif currFix == 'black':
                currFix = 'white'
    
    a = 1.25 # min ITI
    b = 1.75 # max ITI
    fixDur = (b-a) * random()+a
    
    if expInfo['position'] == '0':
        xPosition = 0
    elif expInfo['position'] == '2':
        if side == 'left':
            xPosition = -(width4deg*x_scale)
        elif side == 'right':
            xPosition = width4deg*x_scale
    elif expInfo['position'] == '1':
        xPosition = -(width4deg*x_scale)
    elif expInfo['position'] == '3':
        xPosition = width4deg*x_scale
    
    thisExp.addData('fixR1', fixColorIdx_Run1[Trial_run1-1])
    text_2.setColor(currFix, colorSpace='rgb')
    fix_resp1_1.keys = []
    fix_resp1_1.rt = []
    _fix_resp1_1_allKeys = []
    # keep track of which components have finished
    trialFixR1Components = [text_2, fix_resp1_1]
    for thisComponent in trialFixR1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialFixR1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trialFixR1"-------
    while continueRoutine:
        # get current time
        t = trialFixR1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialFixR1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + fixDur-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                text_2.setAutoDraw(False)
        
        # *fix_resp1_1* updates
        waitOnFlip = False
        if fix_resp1_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_resp1_1.frameNStart = frameN  # exact frame index
            fix_resp1_1.tStart = t  # local t and not account for scr refresh
            fix_resp1_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_resp1_1, 'tStartRefresh')  # time at next scr refresh
            fix_resp1_1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(fix_resp1_1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(fix_resp1_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if fix_resp1_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_resp1_1.tStartRefresh + fixDur-frameTolerance:
                # keep track of stop time/frame for later
                fix_resp1_1.tStop = t  # not accounting for scr refresh
                fix_resp1_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix_resp1_1, 'tStopRefresh')  # time at next scr refresh
                fix_resp1_1.status = FINISHED
        if fix_resp1_1.status == STARTED and not waitOnFlip:
            theseKeys = fix_resp1_1.getKeys(keyList=['space'], waitRelease=False)
            _fix_resp1_1_allKeys.extend(theseKeys)
            if len(_fix_resp1_1_allKeys):
                fix_resp1_1.keys = _fix_resp1_1_allKeys[-1].name  # just the last key pressed
                fix_resp1_1.rt = _fix_resp1_1_allKeys[-1].rt
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialFixR1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trialFixR1"-------
    for thisComponent in trialFixR1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Trial_run1 = Trial_run1 + 1
    trials_run1.addData('text_2.started', text_2.tStartRefresh)
    trials_run1.addData('text_2.stopped', text_2.tStopRefresh)
    # check responses
    if fix_resp1_1.keys in ['', [], None]:  # No response was made
        fix_resp1_1.keys = None
    trials_run1.addData('fix_resp1_1.keys',fix_resp1_1.keys)
    if fix_resp1_1.keys != None:  # we had a response
        trials_run1.addData('fix_resp1_1.rt', fix_resp1_1.rt)
    trials_run1.addData('fix_resp1_1.started', fix_resp1_1.tStartRefresh)
    trials_run1.addData('fix_resp1_1.stopped', fix_resp1_1.tStopRefresh)
    # the Routine "trialFixR1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "trial_img"-------
    continueRoutine = True
    # update component parameters for each repeat
    text_6.setColor(currFix, colorSpace='rgb')
    trial_image.setPos((xPosition, 0))
    trial_image.setSize((width*x_scale,height*y_scale))
    trial_image.setImage(imFile)
    trial_resp.keys = []
    trial_resp.rt = []
    _trial_resp_allKeys = []
    fix_resp_2.keys = []
    fix_resp_2.rt = []
    _fix_resp_2_allKeys = []
    # keep track of which components have finished
    trial_imgComponents = [text_6, trial_image, trial_resp, fix_resp_2]
    for thisComponent in trial_imgComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_imgClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial_img"-------
    while continueRoutine:
        # get current time
        t = trial_imgClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_imgClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_6* updates
        if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            text_6.setAutoDraw(True)
        
        # *trial_image* updates
        if trial_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_image.frameNStart = frameN  # exact frame index
            trial_image.tStart = t  # local t and not account for scr refresh
            trial_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_image, 'tStartRefresh')  # time at next scr refresh
            trial_image.setAutoDraw(True)
        
        # *trial_resp* updates
        waitOnFlip = False
        if trial_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_resp.frameNStart = frameN  # exact frame index
            trial_resp.tStart = t  # local t and not account for scr refresh
            trial_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_resp, 'tStartRefresh')  # time at next scr refresh
            trial_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(trial_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(trial_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if trial_resp.status == STARTED and not waitOnFlip:
            theseKeys = trial_resp.getKeys(keyList=['f', 'j'], waitRelease=False)
            _trial_resp_allKeys.extend(theseKeys)
            if len(_trial_resp_allKeys):
                trial_resp.keys = _trial_resp_allKeys[-1].name  # just the last key pressed
                trial_resp.rt = _trial_resp_allKeys[-1].rt
                # was this correct?
                if (trial_resp.keys == str(corr)) or (trial_resp.keys == corr):
                    trial_resp.corr = 1
                else:
                    trial_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *fix_resp_2* updates
        waitOnFlip = False
        if fix_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_resp_2.frameNStart = frameN  # exact frame index
            fix_resp_2.tStart = t  # local t and not account for scr refresh
            fix_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_resp_2, 'tStartRefresh')  # time at next scr refresh
            fix_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(fix_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(fix_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if fix_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = fix_resp_2.getKeys(keyList=['space'], waitRelease=False)
            _fix_resp_2_allKeys.extend(theseKeys)
            if len(_fix_resp_2_allKeys):
                fix_resp_2.keys = _fix_resp_2_allKeys[-1].name  # just the last key pressed
                fix_resp_2.rt = _fix_resp_2_allKeys[-1].rt
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_imgComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_img"-------
    for thisComponent in trial_imgComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_run1.addData('text_6.started', text_6.tStartRefresh)
    trials_run1.addData('text_6.stopped', text_6.tStopRefresh)
    trials_run1.addData('trial_image.started', trial_image.tStartRefresh)
    trials_run1.addData('trial_image.stopped', trial_image.tStopRefresh)
    # check responses
    if trial_resp.keys in ['', [], None]:  # No response was made
        trial_resp.keys = None
        # was no response the correct answer?!
        if str(corr).lower() == 'none':
           trial_resp.corr = 1;  # correct non-response
        else:
           trial_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_run1 (TrialHandler)
    trials_run1.addData('trial_resp.keys',trial_resp.keys)
    trials_run1.addData('trial_resp.corr', trial_resp.corr)
    if trial_resp.keys != None:  # we had a response
        trials_run1.addData('trial_resp.rt', trial_resp.rt)
    trials_run1.addData('trial_resp.started', trial_resp.tStartRefresh)
    trials_run1.addData('trial_resp.stopped', trial_resp.tStopRefresh)
    # check responses
    if fix_resp_2.keys in ['', [], None]:  # No response was made
        fix_resp_2.keys = None
    trials_run1.addData('fix_resp_2.keys',fix_resp_2.keys)
    if fix_resp_2.keys != None:  # we had a response
        trials_run1.addData('fix_resp_2.rt', fix_resp_2.rt)
    trials_run1.addData('fix_resp_2.started', fix_resp_2.tStartRefresh)
    trials_run1.addData('fix_resp_2.stopped', fix_resp_2.tStopRefresh)
    # the Routine "trial_img" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 6 repeats of 'trials_run1'


# ------Prepare to start Routine "btwn_trial_GJ"-------
continueRoutine = True
routineTimer.add(1.500000)
# update component parameters for each repeat
hand_hold_run = 2
# keep track of which components have finished
btwn_trial_GJComponents = [image_4]
for thisComponent in btwn_trial_GJComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
btwn_trial_GJClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "btwn_trial_GJ"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = btwn_trial_GJClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=btwn_trial_GJClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_4* updates
    if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_4.frameNStart = frameN  # exact frame index
        image_4.tStart = t  # local t and not account for scr refresh
        image_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
        image_4.setAutoDraw(True)
    if image_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_4.tStartRefresh + 1.5-frameTolerance:
            # keep track of stop time/frame for later
            image_4.tStop = t  # not accounting for scr refresh
            image_4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_4, 'tStopRefresh')  # time at next scr refresh
            image_4.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in btwn_trial_GJComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "btwn_trial_GJ"-------
for thisComponent in btwn_trial_GJComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_4.started', image_4.tStartRefresh)
thisExp.addData('image_4.stopped', image_4.tStopRefresh)

# ------Prepare to start Routine "hand_hold_instr"-------
continueRoutine = True
# update component parameters for each repeat
left_right=''
rand_side=''
if expInfo['position'] == '0':
    xPosition = 0
elif expInfo['position'] == '2':
    left_right = [0,1]
    shuffle(left_right)
    rand_side = [0]
    if rand_side == 0: #left
        xPosition = -(width4deg*x_scale)
    else: #right
        xPosition = width4deg*x_scale
elif expInfo['position'] == '1':
    xPosition = -(width4deg*x_scale)
elif expInfo['position'] == '3':
    xPosition = width4deg*x_scale

if hand_hold_run == 1:
    hand_hold_ex = hand_hold_ex1
    handHoldCorr = handHoldCorr1
    hold_hand_img = hold_hand_R1_img
    hand_hold_feedbackcorr = hand_hold_feedback1corr
    hand_hold_feedbackincorr = hand_hold_feedback1incorr
else:
    hand_hold_ex = hand_hold_ex2
    handHoldCorr = handHoldCorr2
    hold_hand_img = hold_hand_R2_img
    hand_hold_feedbackcorr = hand_hold_feedback2corr
    hand_hold_feedbackincorr = hand_hold_feedback2incorr

image_2.setImage(hand_hold_ex)
key_resp_9.keys = []
key_resp_9.rt = []
_key_resp_9_allKeys = []
# keep track of which components have finished
hand_hold_instrComponents = [image_2, key_resp_9]
for thisComponent in hand_hold_instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
hand_hold_instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "hand_hold_instr"-------
while continueRoutine:
    # get current time
    t = hand_hold_instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=hand_hold_instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_2* updates
    if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_2.frameNStart = frameN  # exact frame index
        image_2.tStart = t  # local t and not account for scr refresh
        image_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
        image_2.setAutoDraw(True)
    
    # *key_resp_9* updates
    waitOnFlip = False
    if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.tStart = t  # local t and not account for scr refresh
        key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_9.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_9.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_9_allKeys.extend(theseKeys)
        if len(_key_resp_9_allKeys):
            key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
            key_resp_9.rt = _key_resp_9_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in hand_hold_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "hand_hold_instr"-------
for thisComponent in hand_hold_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "hand_hold_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "hand_hold_trial"-------
continueRoutine = True
# update component parameters for each repeat
image.setPos((xPosition, 0))
image.setSize((width*x_scale, height*y_scale))
image.setImage(hold_hand_img)
hand_hold_resp.keys = []
hand_hold_resp.rt = []
_hand_hold_resp_allKeys = []
# keep track of which components have finished
hand_hold_trialComponents = [text_8, image, hand_hold_resp]
for thisComponent in hand_hold_trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
hand_hold_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "hand_hold_trial"-------
while continueRoutine:
    # get current time
    t = hand_hold_trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=hand_hold_trialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_8* updates
    if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_8.frameNStart = frameN  # exact frame index
        text_8.tStart = t  # local t and not account for scr refresh
        text_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
        text_8.setAutoDraw(True)
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    
    # *hand_hold_resp* updates
    waitOnFlip = False
    if hand_hold_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        hand_hold_resp.frameNStart = frameN  # exact frame index
        hand_hold_resp.tStart = t  # local t and not account for scr refresh
        hand_hold_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(hand_hold_resp, 'tStartRefresh')  # time at next scr refresh
        hand_hold_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(hand_hold_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(hand_hold_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if hand_hold_resp.status == STARTED and not waitOnFlip:
        theseKeys = hand_hold_resp.getKeys(keyList=['f', 'j'], waitRelease=False)
        _hand_hold_resp_allKeys.extend(theseKeys)
        if len(_hand_hold_resp_allKeys):
            hand_hold_resp.keys = _hand_hold_resp_allKeys[-1].name  # just the last key pressed
            hand_hold_resp.rt = _hand_hold_resp_allKeys[-1].rt
            # was this correct?
            if (hand_hold_resp.keys == str(handHoldCorr)) or (hand_hold_resp.keys == handHoldCorr):
                hand_hold_resp.corr = 1
            else:
                hand_hold_resp.corr = 0
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in hand_hold_trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "hand_hold_trial"-------
for thisComponent in hand_hold_trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_8.started', text_8.tStartRefresh)
thisExp.addData('text_8.stopped', text_8.tStopRefresh)
# check responses
if hand_hold_resp.keys in ['', [], None]:  # No response was made
    hand_hold_resp.keys = None
    # was no response the correct answer?!
    if str(handHoldCorr).lower() == 'none':
       hand_hold_resp.corr = 1;  # correct non-response
    else:
       hand_hold_resp.corr = 0;  # failed to respond (incorrectly)
# store data for thisExp (ExperimentHandler)
thisExp.addData('hand_hold_resp.keys',hand_hold_resp.keys)
thisExp.addData('hand_hold_resp.corr', hand_hold_resp.corr)
if hand_hold_resp.keys != None:  # we had a response
    thisExp.addData('hand_hold_resp.rt', hand_hold_resp.rt)
thisExp.nextEntry()
# the Routine "hand_hold_trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "hand_hold_feedback"-------
continueRoutine = True
# update component parameters for each repeat
feedHHim=''

print(hand_hold_run)
print(hand_hold_resp.keys)
print(handHoldCorr)
print(hand_hold_feedback1corr)
if hand_hold_run == 1:
    if hand_hold_resp.keys == handHoldCorr:
        feedHHim = hand_hold_feedback1corr
    else:
        feedHHim = hand_hold_feedback1incorr
else:
    if hand_hold_resp.keys == handHoldCorr:
        feedHHim = hand_hold_feedback2corr
    else:
        feedHHim = hand_hold_feedback2incorr

print(feedHHim)
image_3.setImage(feedHHim)
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
# keep track of which components have finished
hand_hold_feedbackComponents = [image_3, key_resp_8]
for thisComponent in hand_hold_feedbackComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
hand_hold_feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "hand_hold_feedback"-------
while continueRoutine:
    # get current time
    t = hand_hold_feedbackClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=hand_hold_feedbackClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_3* updates
    if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_3.frameNStart = frameN  # exact frame index
        image_3.tStart = t  # local t and not account for scr refresh
        image_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
        image_3.setAutoDraw(True)
    
    # *key_resp_8* updates
    waitOnFlip = False
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
            key_resp_8.rt = _key_resp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in hand_hold_feedbackComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "hand_hold_feedback"-------
for thisComponent in hand_hold_feedbackComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "hand_hold_feedback" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "prac_instr_run2"-------
continueRoutine = True
# update component parameters for each repeat
Pinstructions_imageR2.setImage(instructions_run2)
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
prac_instr_run2Components = [Pinstructions_imageR2, key_resp_3]
for thisComponent in prac_instr_run2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
prac_instr_run2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "prac_instr_run2"-------
while continueRoutine:
    # get current time
    t = prac_instr_run2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=prac_instr_run2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Pinstructions_imageR2* updates
    if Pinstructions_imageR2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Pinstructions_imageR2.frameNStart = frameN  # exact frame index
        Pinstructions_imageR2.tStart = t  # local t and not account for scr refresh
        Pinstructions_imageR2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Pinstructions_imageR2, 'tStartRefresh')  # time at next scr refresh
        Pinstructions_imageR2.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in prac_instr_run2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "prac_instr_run2"-------
for thisComponent in prac_instr_run2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "prac_instr_run2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
repeats2 = data.TrialHandler(nReps=5, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='repeats2')
thisExp.addLoop(repeats2)  # add the loop to the experiment
thisRepeats2 = repeats2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRepeats2.rgb)
if thisRepeats2 != None:
    for paramName in thisRepeats2:
        exec('{} = thisRepeats2[paramName]'.format(paramName))

for thisRepeats2 in repeats2:
    currentLoop = repeats2
    # abbreviate parameter names if possible (e.g. rgb = thisRepeats2.rgb)
    if thisRepeats2 != None:
        for paramName in thisRepeats2:
            exec('{} = thisRepeats2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "startPrac"-------
    continueRoutine = True
    # update component parameters for each repeat
    numIncorr_fix = 0
    numIncorr_miss = 0
    numIncorr_img = 0
    
    rand4Idx = ''
    rand8Idx = ''
    if int(expInfo['position'])==2:
        rand8Idx = [0,1,2,3,4,5,6,7];
        shuffle(rand8Idx)
        randRows_run1 = rand8Idx[0:6]
    elif int(expInfo['position'])==1:
        rand4Idx = [0,1,2,3,0,1];
        shuffle(rand4Idx)
        randRows_run1 = rand4Idx
    elif int(expInfo['position'])==3:
        rand4Idx = [4,5,6,7,4,5];
        shuffle(rand4Idx)
        randRows_run1 = rand4Idx
    
    pTrial_run1 = 1
    pracTotal_run1 = 6
    pTrial_run2 = 1
    pracTotal_run2 = 6
    
    # keep track of which components have finished
    startPracComponents = []
    for thisComponent in startPracComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    startPracClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "startPrac"-------
    while continueRoutine:
        # get current time
        t = startPracClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=startPracClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in startPracComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "startPrac"-------
    for thisComponent in startPracComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "startPrac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    prac_trials_run2 = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(cond_file_run2, selection=randRows_run2),
        seed=None, name='prac_trials_run2')
    thisExp.addLoop(prac_trials_run2)  # add the loop to the experiment
    thisPrac_trials_run2 = prac_trials_run2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPrac_trials_run2.rgb)
    if thisPrac_trials_run2 != None:
        for paramName in thisPrac_trials_run2:
            exec('{} = thisPrac_trials_run2[paramName]'.format(paramName))
    
    for thisPrac_trials_run2 in prac_trials_run2:
        currentLoop = prac_trials_run2
        # abbreviate parameter names if possible (e.g. rgb = thisPrac_trials_run2.rgb)
        if thisPrac_trials_run2 != None:
            for paramName in thisPrac_trials_run2:
                exec('{} = thisPrac_trials_run2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "pracFixR2"-------
        continueRoutine = True
        # update component parameters for each repeat
        trialMsg = "Practice: " + str(pTrial_run2) + ' of ' + str(pracTotal_run2)
        if pTrial_run2-1 == 0:
            currFix = fixColor_opts[0]
            corrfixResp = None
        else:
            if prac2_fixColSwitch[pTrial_run2-1] == 0:
                currFix = currFix
                corrfixResp = None
            elif  prac2_fixColSwitch[pTrial_run2-1] == 1:
                if currFix == 'white':
                    currFix = 'black'
                    corrfixResp = 'space'
                elif currFix == 'black':
                    currFix = 'white'
                    corrfixResp = 'space'
        a = 1.25 # min ITI
        b = 1.75 # max ITI
        fixDur = (b-a) * random()+a
        
        if expInfo['position'] == '0':
            xPosition = 0
        elif expInfo['position'] == '2':
            if side == 'left':
                xPosition = -(width4deg*x_scale)
            elif side == 'right':
                xPosition = width4deg*x_scale
        elif expInfo['position'] == '1':
            xPosition = -(width4deg*x_scale)
        elif expInfo['position'] == '3':
            xPosition = width4deg*x_scale
        
        thisExp.addData('fixpR2', prac2_fixColSwitch[pTrial_run2-1])
        text_3.setColor(currFix, colorSpace='rgb')
        fix_respP2_1.keys = []
        fix_respP2_1.rt = []
        _fix_respP2_1_allKeys = []
        # keep track of which components have finished
        pracFixR2Components = [text_3, fix_respP2_1]
        for thisComponent in pracFixR2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        pracFixR2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "pracFixR2"-------
        while continueRoutine:
            # get current time
            t = pracFixR2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=pracFixR2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_3* updates
            if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_3.frameNStart = frameN  # exact frame index
                text_3.tStart = t  # local t and not account for scr refresh
                text_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                text_3.setAutoDraw(True)
            if text_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_3.tStartRefresh + fixDur-frameTolerance:
                    # keep track of stop time/frame for later
                    text_3.tStop = t  # not accounting for scr refresh
                    text_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                    text_3.setAutoDraw(False)
            
            # *fix_respP2_1* updates
            waitOnFlip = False
            if fix_respP2_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix_respP2_1.frameNStart = frameN  # exact frame index
                fix_respP2_1.tStart = t  # local t and not account for scr refresh
                fix_respP2_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix_respP2_1, 'tStartRefresh')  # time at next scr refresh
                fix_respP2_1.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(fix_respP2_1.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(fix_respP2_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if fix_respP2_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix_respP2_1.tStartRefresh + fixDur-frameTolerance:
                    # keep track of stop time/frame for later
                    fix_respP2_1.tStop = t  # not accounting for scr refresh
                    fix_respP2_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fix_respP2_1, 'tStopRefresh')  # time at next scr refresh
                    fix_respP2_1.status = FINISHED
            if fix_respP2_1.status == STARTED and not waitOnFlip:
                theseKeys = fix_respP2_1.getKeys(keyList=['space'], waitRelease=False)
                _fix_respP2_1_allKeys.extend(theseKeys)
                if len(_fix_respP2_1_allKeys):
                    fix_respP2_1.keys = _fix_respP2_1_allKeys[-1].name  # just the last key pressed
                    fix_respP2_1.rt = _fix_respP2_1_allKeys[-1].rt
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in pracFixR2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "pracFixR2"-------
        for thisComponent in pracFixR2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        pTrial_run2 = pTrial_run2 + 1
        # check responses
        if fix_respP2_1.keys in ['', [], None]:  # No response was made
            fix_respP2_1.keys = None
        prac_trials_run2.addData('fix_respP2_1.keys',fix_respP2_1.keys)
        if fix_respP2_1.keys != None:  # we had a response
            prac_trials_run2.addData('fix_respP2_1.rt', fix_respP2_1.rt)
        # the Routine "pracFixR2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "prac_img"-------
        continueRoutine = True
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        text_5.setColor(currFix, colorSpace='rgb')
        prac_image.setPos((xPosition, 0))
        prac_image.setSize((width*x_scale, height*y_scale))
        prac_image.setImage(imFile)
        prac_resp.keys = []
        prac_resp.rt = []
        _prac_resp_allKeys = []
        prac_fix_resp.keys = []
        prac_fix_resp.rt = []
        _prac_fix_resp_allKeys = []
        # keep track of which components have finished
        prac_imgComponents = [text_5, prac_image, prac_resp, prac_fix_resp]
        for thisComponent in prac_imgComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        prac_imgClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "prac_img"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = prac_imgClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=prac_imgClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_5* updates
            if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_5.frameNStart = frameN  # exact frame index
                text_5.tStart = t  # local t and not account for scr refresh
                text_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
                text_5.setAutoDraw(True)
            if text_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_5.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    text_5.tStop = t  # not accounting for scr refresh
                    text_5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
                    text_5.setAutoDraw(False)
            
            # *prac_image* updates
            if prac_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prac_image.frameNStart = frameN  # exact frame index
                prac_image.tStart = t  # local t and not account for scr refresh
                prac_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prac_image, 'tStartRefresh')  # time at next scr refresh
                prac_image.setAutoDraw(True)
            if prac_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > prac_image.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    prac_image.tStop = t  # not accounting for scr refresh
                    prac_image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(prac_image, 'tStopRefresh')  # time at next scr refresh
                    prac_image.setAutoDraw(False)
            
            # *prac_resp* updates
            waitOnFlip = False
            if prac_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prac_resp.frameNStart = frameN  # exact frame index
                prac_resp.tStart = t  # local t and not account for scr refresh
                prac_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prac_resp, 'tStartRefresh')  # time at next scr refresh
                prac_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(prac_resp.clock.reset)  # t=0 on next screen flip
            if prac_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > prac_resp.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    prac_resp.tStop = t  # not accounting for scr refresh
                    prac_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(prac_resp, 'tStopRefresh')  # time at next scr refresh
                    prac_resp.status = FINISHED
            if prac_resp.status == STARTED and not waitOnFlip:
                theseKeys = prac_resp.getKeys(keyList=['f', 'j'], waitRelease=False)
                _prac_resp_allKeys.extend(theseKeys)
                if len(_prac_resp_allKeys):
                    prac_resp.keys = _prac_resp_allKeys[-1].name  # just the last key pressed
                    prac_resp.rt = _prac_resp_allKeys[-1].rt
                    # was this correct?
                    if (prac_resp.keys == str(corr)) or (prac_resp.keys == corr):
                        prac_resp.corr = 1
                    else:
                        prac_resp.corr = 0
            
            # *prac_fix_resp* updates
            waitOnFlip = False
            if prac_fix_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prac_fix_resp.frameNStart = frameN  # exact frame index
                prac_fix_resp.tStart = t  # local t and not account for scr refresh
                prac_fix_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prac_fix_resp, 'tStartRefresh')  # time at next scr refresh
                prac_fix_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(prac_fix_resp.clock.reset)  # t=0 on next screen flip
            if prac_fix_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > prac_fix_resp.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    prac_fix_resp.tStop = t  # not accounting for scr refresh
                    prac_fix_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(prac_fix_resp, 'tStopRefresh')  # time at next scr refresh
                    prac_fix_resp.status = FINISHED
            if prac_fix_resp.status == STARTED and not waitOnFlip:
                theseKeys = prac_fix_resp.getKeys(keyList=['space'], waitRelease=False)
                _prac_fix_resp_allKeys.extend(theseKeys)
                if len(_prac_fix_resp_allKeys):
                    prac_fix_resp.keys = _prac_fix_resp_allKeys[-1].name  # just the last key pressed
                    prac_fix_resp.rt = _prac_fix_resp_allKeys[-1].rt
                    # was this correct?
                    if (prac_fix_resp.keys == str(corrfixResp)) or (prac_fix_resp.keys == corrfixResp):
                        prac_fix_resp.corr = 1
                    else:
                        prac_fix_resp.corr = 0
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in prac_imgComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "prac_img"-------
        for thisComponent in prac_imgComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if prac_resp.keys in ['', [], None]:  # No response was made
            prac_resp.keys = None
            # was no response the correct answer?!
            if str(corr).lower() == 'none':
               prac_resp.corr = 1;  # correct non-response
            else:
               prac_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for prac_trials_run2 (TrialHandler)
        prac_trials_run2.addData('prac_resp.keys',prac_resp.keys)
        prac_trials_run2.addData('prac_resp.corr', prac_resp.corr)
        if prac_resp.keys != None:  # we had a response
            prac_trials_run2.addData('prac_resp.rt', prac_resp.rt)
        # check responses
        if prac_fix_resp.keys in ['', [], None]:  # No response was made
            prac_fix_resp.keys = None
            # was no response the correct answer?!
            if str(corrfixResp).lower() == 'none':
               prac_fix_resp.corr = 1;  # correct non-response
            else:
               prac_fix_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for prac_trials_run2 (TrialHandler)
        prac_trials_run2.addData('prac_fix_resp.keys',prac_fix_resp.keys)
        prac_trials_run2.addData('prac_fix_resp.corr', prac_fix_resp.corr)
        if prac_fix_resp.keys != None:  # we had a response
            prac_trials_run2.addData('prac_fix_resp.rt', prac_fix_resp.rt)
        
        # ------Prepare to start Routine "Feedback"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        feedIM =''
        if prac_resp.keys == corr: 
            if prac_fix_resp.corr == 1:
                feedIM = 'Stimuli/greenCheck.png'
                prac_msg = 'Well done!'
            else:
                numIncorr_fix = numIncorr_fix + 1
                feedIM = 'Stimuli/redWrong.png'
                if corrfixResp == 'space':
                    prac_msg = 'Oops, you missed the cross response.'
                else:
                    prac_msg = 'Oops, you pressed space when there was no fix change.'
        elif prac_resp.keys != corr:
            if prac_resp.keys == None:
               feedIM = 'Stimuli/redWrong.png'
               numIncorr_miss = numIncorr_miss + 1
               if corrfixResp == 'space':
                    numIncorr_fix = numIncorr_fix + 1
               prac_msg = 'Oops, time ran out. That\'s ok, try again!' 
            else:
                if prac_fix_resp.corr == 1:
                    feedIM = 'Stimuli/redWrong.png'
                    numIncorr_img = numIncorr_img + 1
                    if corrfixResp == 'space':
                        prac_msg = 'Good job! You got pressed space when the cross changed! But the picture response was wrong.'
                    else:
                        prac_msg = 'Oops, the picture response was wrong.'
                else:
                    numIncorr_img = numIncorr_img + 1
                    numIncorr_fix = numIncorr_fix + 1
                    feedIM = 'Stimuli/redWrong.png'
                    if corrfixResp == 'space':
                        prac_msg = 'Oops, you missed the cross change and the picture response was wrong.'
                    else:
                        prac_msg = 'Oops, you press space when the cross didn\'t change and the picture response was wrong.'
        
        
        imFeedback.setImage(feedIM)
        feedback_msg.setText(prac_msg)
        # keep track of which components have finished
        FeedbackComponents = [imFeedback, feedback_msg]
        for thisComponent in FeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        FeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Feedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = FeedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=FeedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *imFeedback* updates
            if imFeedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                imFeedback.frameNStart = frameN  # exact frame index
                imFeedback.tStart = t  # local t and not account for scr refresh
                imFeedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imFeedback, 'tStartRefresh')  # time at next scr refresh
                imFeedback.setAutoDraw(True)
            if imFeedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > imFeedback.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    imFeedback.tStop = t  # not accounting for scr refresh
                    imFeedback.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(imFeedback, 'tStopRefresh')  # time at next scr refresh
                    imFeedback.setAutoDraw(False)
            
            # *feedback_msg* updates
            if feedback_msg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_msg.frameNStart = frameN  # exact frame index
                feedback_msg.tStart = t  # local t and not account for scr refresh
                feedback_msg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_msg, 'tStartRefresh')  # time at next scr refresh
                feedback_msg.setAutoDraw(True)
            if feedback_msg.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback_msg.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback_msg.tStop = t  # not accounting for scr refresh
                    feedback_msg.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(feedback_msg, 'tStopRefresh')  # time at next scr refresh
                    feedback_msg.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Feedback"-------
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        prac_trials_run2.addData('feedback_msg.started', feedback_msg.tStartRefresh)
        prac_trials_run2.addData('feedback_msg.stopped', feedback_msg.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'prac_trials_run2'
    
    
    # ------Prepare to start Routine "checkPrac2"-------
    continueRoutine = True
    # update component parameters for each repeat
    if (numIncorr_fix + numIncorr_miss + numIncorr_img) < 3 and (numIncorr_fix != 2):
        repeats2.finished = True
        prac_feedback = 'Great Job! \n Now we are going to play the real game. \n Press Space to see the instructions again.'
    else:
        if numIncorr_fix > 1 and numIncorr_img < 2 and numIncorr_miss < 2:
            prac_feedback = 'Good job! \nYou missed ' + str(numIncorr_fix) + ' of the fix changes. \n In the real game, make sure you press Space as soon as you see it change!\n\n Let\'s try some more practice. \n Press Space to start.'
        elif numIncorr_img > 1 and numIncorr_fix < 2 and numIncorr_miss < 2:
            prac_feedback = 'Good job! \nYou missed ' + str(numIncorr_img) + ' of the images. \n Sometimes the big letter and the little letters are different. \nMake sure you focus on the right ones and press the right keys! \n\nLet\'s try some more practice. \n Press Space to start.'
        elif numIncorr_miss > 0 and numIncorr_img < 2 and numIncorr_fix < 2:
            prac_feedback = 'You missed ' + str(numIncorr_miss) + ' of the trials because the time was up. That\'s ok, in the real game the image will stay on, but try to go as fast as you can. \n\n Press Space to practice more.'
        else:
            prac_feedback = 'Let\'s try one more round of practice. \n\n Press Space to begin.'
    text_9.setText(prac_feedback)
    key_resp_10.keys = []
    key_resp_10.rt = []
    _key_resp_10_allKeys = []
    # keep track of which components have finished
    checkPrac2Components = [text_9, key_resp_10]
    for thisComponent in checkPrac2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    checkPrac2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "checkPrac2"-------
    while continueRoutine:
        # get current time
        t = checkPrac2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=checkPrac2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_9* updates
        if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_9.frameNStart = frameN  # exact frame index
            text_9.tStart = t  # local t and not account for scr refresh
            text_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
            text_9.setAutoDraw(True)
        
        # *key_resp_10* updates
        waitOnFlip = False
        if key_resp_10.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_resp_10.frameNStart = frameN  # exact frame index
            key_resp_10.tStart = t  # local t and not account for scr refresh
            key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
            key_resp_10.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_10.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_10.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_10_allKeys.extend(theseKeys)
            if len(_key_resp_10_allKeys):
                key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
                key_resp_10.rt = _key_resp_10_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in checkPrac2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "checkPrac2"-------
    for thisComponent in checkPrac2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_10.keys in ['', [], None]:  # No response was made
        key_resp_10.keys = None
    repeats2.addData('key_resp_10.keys',key_resp_10.keys)
    if key_resp_10.keys != None:  # we had a response
        repeats2.addData('key_resp_10.rt', key_resp_10.rt)
    # the Routine "checkPrac2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 5 repeats of 'repeats2'


# ------Prepare to start Routine "trial_instr_run2"-------
continueRoutine = True
# update component parameters for each repeat
instructions_imageR2.setImage(instructions_run2)
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
trial_instr_run2Components = [instructions_imageR2, key_resp_4]
for thisComponent in trial_instr_run2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_instr_run2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trial_instr_run2"-------
while continueRoutine:
    # get current time
    t = trial_instr_run2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_instr_run2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_imageR2* updates
    if instructions_imageR2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_imageR2.frameNStart = frameN  # exact frame index
        instructions_imageR2.tStart = t  # local t and not account for scr refresh
        instructions_imageR2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_imageR2, 'tStartRefresh')  # time at next scr refresh
        instructions_imageR2.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_instr_run2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_instr_run2"-------
for thisComponent in trial_instr_run2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "trial_instr_run2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_run2 = data.TrialHandler(nReps=6, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(cond_file_run2, selection=positionRows),
    seed=None, name='trials_run2')
thisExp.addLoop(trials_run2)  # add the loop to the experiment
thisTrials_run2 = trials_run2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_run2.rgb)
if thisTrials_run2 != None:
    for paramName in thisTrials_run2:
        exec('{} = thisTrials_run2[paramName]'.format(paramName))

for thisTrials_run2 in trials_run2:
    currentLoop = trials_run2
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_run2.rgb)
    if thisTrials_run2 != None:
        for paramName in thisTrials_run2:
            exec('{} = thisTrials_run2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trialFixR2"-------
    continueRoutine = True
    # update component parameters for each repeat
    if Trial_run2-1 == 0:
        currFix = fixColor_opts[0]
    else:
        if fixColorIdx_Run2[Trial_run2-1] == 0:
            currFix = currFix
        elif fixColorIdx_Run2[Trial_run2-1] == 1:
            if currFix == 'white':
                currFix = 'black'
            elif currFix == 'black':
                currFix = 'white'
    
    a = 1.25 # min ITI
    b = 1.75 # max ITI
    fixDur = (b-a) * random()+a
    
    if int(expInfo['position']) == 0:
        xPosition = 0
    elif int(expInfo['position']) == 2:
        if side == 'left':
            xPosition = -(width4deg*x_scale)
        elif side == 'right':
            xPosition = width4deg*x_scale
    elif int(expInfo['position']) == 1:
        xPosition = -(width4deg*x_scale)
    elif (expInfo['position']) == 3:
        xPosition = width4deg*x_scale
    
    thisExp.addData('fixR2', fixColorIdx_Run2[Trial_run2-1])
    text_4.setColor(currFix, colorSpace='rgb')
    fix_resp2_1.keys = []
    fix_resp2_1.rt = []
    _fix_resp2_1_allKeys = []
    # keep track of which components have finished
    trialFixR2Components = [text_4, fix_resp2_1]
    for thisComponent in trialFixR2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialFixR2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trialFixR2"-------
    while continueRoutine:
        # get current time
        t = trialFixR2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialFixR2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + fixDur-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                text_4.setAutoDraw(False)
        
        # *fix_resp2_1* updates
        waitOnFlip = False
        if fix_resp2_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_resp2_1.frameNStart = frameN  # exact frame index
            fix_resp2_1.tStart = t  # local t and not account for scr refresh
            fix_resp2_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_resp2_1, 'tStartRefresh')  # time at next scr refresh
            fix_resp2_1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(fix_resp2_1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(fix_resp2_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if fix_resp2_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_resp2_1.tStartRefresh + fixDur-frameTolerance:
                # keep track of stop time/frame for later
                fix_resp2_1.tStop = t  # not accounting for scr refresh
                fix_resp2_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix_resp2_1, 'tStopRefresh')  # time at next scr refresh
                fix_resp2_1.status = FINISHED
        if fix_resp2_1.status == STARTED and not waitOnFlip:
            theseKeys = fix_resp2_1.getKeys(keyList=['space'], waitRelease=False)
            _fix_resp2_1_allKeys.extend(theseKeys)
            if len(_fix_resp2_1_allKeys):
                fix_resp2_1.keys = _fix_resp2_1_allKeys[-1].name  # just the last key pressed
                fix_resp2_1.rt = _fix_resp2_1_allKeys[-1].rt
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialFixR2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trialFixR2"-------
    for thisComponent in trialFixR2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Trial_run2 = Trial_run2 + 1
    trials_run2.addData('text_4.started', text_4.tStartRefresh)
    trials_run2.addData('text_4.stopped', text_4.tStopRefresh)
    # check responses
    if fix_resp2_1.keys in ['', [], None]:  # No response was made
        fix_resp2_1.keys = None
    trials_run2.addData('fix_resp2_1.keys',fix_resp2_1.keys)
    if fix_resp2_1.keys != None:  # we had a response
        trials_run2.addData('fix_resp2_1.rt', fix_resp2_1.rt)
    trials_run2.addData('fix_resp2_1.started', fix_resp2_1.tStartRefresh)
    trials_run2.addData('fix_resp2_1.stopped', fix_resp2_1.tStopRefresh)
    # the Routine "trialFixR2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "trial_img"-------
    continueRoutine = True
    # update component parameters for each repeat
    text_6.setColor(currFix, colorSpace='rgb')
    trial_image.setPos((xPosition, 0))
    trial_image.setSize((width*x_scale,height*y_scale))
    trial_image.setImage(imFile)
    trial_resp.keys = []
    trial_resp.rt = []
    _trial_resp_allKeys = []
    fix_resp_2.keys = []
    fix_resp_2.rt = []
    _fix_resp_2_allKeys = []
    # keep track of which components have finished
    trial_imgComponents = [text_6, trial_image, trial_resp, fix_resp_2]
    for thisComponent in trial_imgComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_imgClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial_img"-------
    while continueRoutine:
        # get current time
        t = trial_imgClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_imgClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_6* updates
        if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            text_6.setAutoDraw(True)
        
        # *trial_image* updates
        if trial_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_image.frameNStart = frameN  # exact frame index
            trial_image.tStart = t  # local t and not account for scr refresh
            trial_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_image, 'tStartRefresh')  # time at next scr refresh
            trial_image.setAutoDraw(True)
        
        # *trial_resp* updates
        waitOnFlip = False
        if trial_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_resp.frameNStart = frameN  # exact frame index
            trial_resp.tStart = t  # local t and not account for scr refresh
            trial_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_resp, 'tStartRefresh')  # time at next scr refresh
            trial_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(trial_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(trial_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if trial_resp.status == STARTED and not waitOnFlip:
            theseKeys = trial_resp.getKeys(keyList=['f', 'j'], waitRelease=False)
            _trial_resp_allKeys.extend(theseKeys)
            if len(_trial_resp_allKeys):
                trial_resp.keys = _trial_resp_allKeys[-1].name  # just the last key pressed
                trial_resp.rt = _trial_resp_allKeys[-1].rt
                # was this correct?
                if (trial_resp.keys == str(corr)) or (trial_resp.keys == corr):
                    trial_resp.corr = 1
                else:
                    trial_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *fix_resp_2* updates
        waitOnFlip = False
        if fix_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_resp_2.frameNStart = frameN  # exact frame index
            fix_resp_2.tStart = t  # local t and not account for scr refresh
            fix_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_resp_2, 'tStartRefresh')  # time at next scr refresh
            fix_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(fix_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(fix_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if fix_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = fix_resp_2.getKeys(keyList=['space'], waitRelease=False)
            _fix_resp_2_allKeys.extend(theseKeys)
            if len(_fix_resp_2_allKeys):
                fix_resp_2.keys = _fix_resp_2_allKeys[-1].name  # just the last key pressed
                fix_resp_2.rt = _fix_resp_2_allKeys[-1].rt
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_imgComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_img"-------
    for thisComponent in trial_imgComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_run2.addData('text_6.started', text_6.tStartRefresh)
    trials_run2.addData('text_6.stopped', text_6.tStopRefresh)
    trials_run2.addData('trial_image.started', trial_image.tStartRefresh)
    trials_run2.addData('trial_image.stopped', trial_image.tStopRefresh)
    # check responses
    if trial_resp.keys in ['', [], None]:  # No response was made
        trial_resp.keys = None
        # was no response the correct answer?!
        if str(corr).lower() == 'none':
           trial_resp.corr = 1;  # correct non-response
        else:
           trial_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_run2 (TrialHandler)
    trials_run2.addData('trial_resp.keys',trial_resp.keys)
    trials_run2.addData('trial_resp.corr', trial_resp.corr)
    if trial_resp.keys != None:  # we had a response
        trials_run2.addData('trial_resp.rt', trial_resp.rt)
    trials_run2.addData('trial_resp.started', trial_resp.tStartRefresh)
    trials_run2.addData('trial_resp.stopped', trial_resp.tStopRefresh)
    # check responses
    if fix_resp_2.keys in ['', [], None]:  # No response was made
        fix_resp_2.keys = None
    trials_run2.addData('fix_resp_2.keys',fix_resp_2.keys)
    if fix_resp_2.keys != None:  # we had a response
        trials_run2.addData('fix_resp_2.rt', fix_resp_2.rt)
    trials_run2.addData('fix_resp_2.started', fix_resp_2.tStartRefresh)
    trials_run2.addData('fix_resp_2.stopped', fix_resp_2.tStopRefresh)
    # the Routine "trial_img" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 6 repeats of 'trials_run2'


# ------Prepare to start Routine "btwn_trial_GJ"-------
continueRoutine = True
routineTimer.add(1.500000)
# update component parameters for each repeat
hand_hold_run = 2
# keep track of which components have finished
btwn_trial_GJComponents = [image_4]
for thisComponent in btwn_trial_GJComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
btwn_trial_GJClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "btwn_trial_GJ"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = btwn_trial_GJClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=btwn_trial_GJClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_4* updates
    if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_4.frameNStart = frameN  # exact frame index
        image_4.tStart = t  # local t and not account for scr refresh
        image_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
        image_4.setAutoDraw(True)
    if image_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_4.tStartRefresh + 1.5-frameTolerance:
            # keep track of stop time/frame for later
            image_4.tStop = t  # not accounting for scr refresh
            image_4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_4, 'tStopRefresh')  # time at next scr refresh
            image_4.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in btwn_trial_GJComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "btwn_trial_GJ"-------
for thisComponent in btwn_trial_GJComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_4.started', image_4.tStartRefresh)
thisExp.addData('image_4.stopped', image_4.tStopRefresh)

# ------Prepare to start Routine "trial_instr_run1"-------
continueRoutine = True
# update component parameters for each repeat
instructions_imageR1.setImage(instructions_run1)
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
trial_instr_run1Components = [instructions_imageR1, key_resp_2]
for thisComponent in trial_instr_run1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_instr_run1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trial_instr_run1"-------
while continueRoutine:
    # get current time
    t = trial_instr_run1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_instr_run1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_imageR1* updates
    if instructions_imageR1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_imageR1.frameNStart = frameN  # exact frame index
        instructions_imageR1.tStart = t  # local t and not account for scr refresh
        instructions_imageR1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_imageR1, 'tStartRefresh')  # time at next scr refresh
        instructions_imageR1.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_instr_run1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_instr_run1"-------
for thisComponent in trial_instr_run1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "trial_instr_run1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_run3 = data.TrialHandler(nReps=6, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(cond_file_run1, selection=positionRows),
    seed=None, name='trials_run3')
thisExp.addLoop(trials_run3)  # add the loop to the experiment
thisTrials_run3 = trials_run3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_run3.rgb)
if thisTrials_run3 != None:
    for paramName in thisTrials_run3:
        exec('{} = thisTrials_run3[paramName]'.format(paramName))

for thisTrials_run3 in trials_run3:
    currentLoop = trials_run3
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_run3.rgb)
    if thisTrials_run3 != None:
        for paramName in thisTrials_run3:
            exec('{} = thisTrials_run3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trialFixR1"-------
    continueRoutine = True
    # update component parameters for each repeat
    if Trial_run1-1 == 0:
        currFix = fixColor_opts[0]
    else:
        if fixColorIdx_Run1[Trial_run1-1] == 0:
            currFix = currFix
        elif fixColorIdx_Run1[Trial_run1-1] == 1:
            if currFix == 'white':
                currFix = 'black'
            elif currFix == 'black':
                currFix = 'white'
    
    a = 1.25 # min ITI
    b = 1.75 # max ITI
    fixDur = (b-a) * random()+a
    
    if expInfo['position'] == '0':
        xPosition = 0
    elif expInfo['position'] == '2':
        if side == 'left':
            xPosition = -(width4deg*x_scale)
        elif side == 'right':
            xPosition = width4deg*x_scale
    elif expInfo['position'] == '1':
        xPosition = -(width4deg*x_scale)
    elif expInfo['position'] == '3':
        xPosition = width4deg*x_scale
    
    thisExp.addData('fixR1', fixColorIdx_Run1[Trial_run1-1])
    text_2.setColor(currFix, colorSpace='rgb')
    fix_resp1_1.keys = []
    fix_resp1_1.rt = []
    _fix_resp1_1_allKeys = []
    # keep track of which components have finished
    trialFixR1Components = [text_2, fix_resp1_1]
    for thisComponent in trialFixR1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialFixR1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trialFixR1"-------
    while continueRoutine:
        # get current time
        t = trialFixR1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialFixR1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + fixDur-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                text_2.setAutoDraw(False)
        
        # *fix_resp1_1* updates
        waitOnFlip = False
        if fix_resp1_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_resp1_1.frameNStart = frameN  # exact frame index
            fix_resp1_1.tStart = t  # local t and not account for scr refresh
            fix_resp1_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_resp1_1, 'tStartRefresh')  # time at next scr refresh
            fix_resp1_1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(fix_resp1_1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(fix_resp1_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if fix_resp1_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_resp1_1.tStartRefresh + fixDur-frameTolerance:
                # keep track of stop time/frame for later
                fix_resp1_1.tStop = t  # not accounting for scr refresh
                fix_resp1_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix_resp1_1, 'tStopRefresh')  # time at next scr refresh
                fix_resp1_1.status = FINISHED
        if fix_resp1_1.status == STARTED and not waitOnFlip:
            theseKeys = fix_resp1_1.getKeys(keyList=['space'], waitRelease=False)
            _fix_resp1_1_allKeys.extend(theseKeys)
            if len(_fix_resp1_1_allKeys):
                fix_resp1_1.keys = _fix_resp1_1_allKeys[-1].name  # just the last key pressed
                fix_resp1_1.rt = _fix_resp1_1_allKeys[-1].rt
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialFixR1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trialFixR1"-------
    for thisComponent in trialFixR1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Trial_run1 = Trial_run1 + 1
    trials_run3.addData('text_2.started', text_2.tStartRefresh)
    trials_run3.addData('text_2.stopped', text_2.tStopRefresh)
    # check responses
    if fix_resp1_1.keys in ['', [], None]:  # No response was made
        fix_resp1_1.keys = None
    trials_run3.addData('fix_resp1_1.keys',fix_resp1_1.keys)
    if fix_resp1_1.keys != None:  # we had a response
        trials_run3.addData('fix_resp1_1.rt', fix_resp1_1.rt)
    trials_run3.addData('fix_resp1_1.started', fix_resp1_1.tStartRefresh)
    trials_run3.addData('fix_resp1_1.stopped', fix_resp1_1.tStopRefresh)
    # the Routine "trialFixR1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "trial_img"-------
    continueRoutine = True
    # update component parameters for each repeat
    text_6.setColor(currFix, colorSpace='rgb')
    trial_image.setPos((xPosition, 0))
    trial_image.setSize((width*x_scale,height*y_scale))
    trial_image.setImage(imFile)
    trial_resp.keys = []
    trial_resp.rt = []
    _trial_resp_allKeys = []
    fix_resp_2.keys = []
    fix_resp_2.rt = []
    _fix_resp_2_allKeys = []
    # keep track of which components have finished
    trial_imgComponents = [text_6, trial_image, trial_resp, fix_resp_2]
    for thisComponent in trial_imgComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_imgClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial_img"-------
    while continueRoutine:
        # get current time
        t = trial_imgClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_imgClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_6* updates
        if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            text_6.setAutoDraw(True)
        
        # *trial_image* updates
        if trial_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_image.frameNStart = frameN  # exact frame index
            trial_image.tStart = t  # local t and not account for scr refresh
            trial_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_image, 'tStartRefresh')  # time at next scr refresh
            trial_image.setAutoDraw(True)
        
        # *trial_resp* updates
        waitOnFlip = False
        if trial_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_resp.frameNStart = frameN  # exact frame index
            trial_resp.tStart = t  # local t and not account for scr refresh
            trial_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_resp, 'tStartRefresh')  # time at next scr refresh
            trial_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(trial_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(trial_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if trial_resp.status == STARTED and not waitOnFlip:
            theseKeys = trial_resp.getKeys(keyList=['f', 'j'], waitRelease=False)
            _trial_resp_allKeys.extend(theseKeys)
            if len(_trial_resp_allKeys):
                trial_resp.keys = _trial_resp_allKeys[-1].name  # just the last key pressed
                trial_resp.rt = _trial_resp_allKeys[-1].rt
                # was this correct?
                if (trial_resp.keys == str(corr)) or (trial_resp.keys == corr):
                    trial_resp.corr = 1
                else:
                    trial_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *fix_resp_2* updates
        waitOnFlip = False
        if fix_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_resp_2.frameNStart = frameN  # exact frame index
            fix_resp_2.tStart = t  # local t and not account for scr refresh
            fix_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_resp_2, 'tStartRefresh')  # time at next scr refresh
            fix_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(fix_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(fix_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if fix_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = fix_resp_2.getKeys(keyList=['space'], waitRelease=False)
            _fix_resp_2_allKeys.extend(theseKeys)
            if len(_fix_resp_2_allKeys):
                fix_resp_2.keys = _fix_resp_2_allKeys[-1].name  # just the last key pressed
                fix_resp_2.rt = _fix_resp_2_allKeys[-1].rt
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_imgComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_img"-------
    for thisComponent in trial_imgComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_run3.addData('text_6.started', text_6.tStartRefresh)
    trials_run3.addData('text_6.stopped', text_6.tStopRefresh)
    trials_run3.addData('trial_image.started', trial_image.tStartRefresh)
    trials_run3.addData('trial_image.stopped', trial_image.tStopRefresh)
    # check responses
    if trial_resp.keys in ['', [], None]:  # No response was made
        trial_resp.keys = None
        # was no response the correct answer?!
        if str(corr).lower() == 'none':
           trial_resp.corr = 1;  # correct non-response
        else:
           trial_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_run3 (TrialHandler)
    trials_run3.addData('trial_resp.keys',trial_resp.keys)
    trials_run3.addData('trial_resp.corr', trial_resp.corr)
    if trial_resp.keys != None:  # we had a response
        trials_run3.addData('trial_resp.rt', trial_resp.rt)
    trials_run3.addData('trial_resp.started', trial_resp.tStartRefresh)
    trials_run3.addData('trial_resp.stopped', trial_resp.tStopRefresh)
    # check responses
    if fix_resp_2.keys in ['', [], None]:  # No response was made
        fix_resp_2.keys = None
    trials_run3.addData('fix_resp_2.keys',fix_resp_2.keys)
    if fix_resp_2.keys != None:  # we had a response
        trials_run3.addData('fix_resp_2.rt', fix_resp_2.rt)
    trials_run3.addData('fix_resp_2.started', fix_resp_2.tStartRefresh)
    trials_run3.addData('fix_resp_2.stopped', fix_resp_2.tStopRefresh)
    # the Routine "trial_img" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 6 repeats of 'trials_run3'


# ------Prepare to start Routine "btwn_trial_GJ"-------
continueRoutine = True
routineTimer.add(1.500000)
# update component parameters for each repeat
hand_hold_run = 2
# keep track of which components have finished
btwn_trial_GJComponents = [image_4]
for thisComponent in btwn_trial_GJComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
btwn_trial_GJClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "btwn_trial_GJ"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = btwn_trial_GJClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=btwn_trial_GJClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_4* updates
    if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_4.frameNStart = frameN  # exact frame index
        image_4.tStart = t  # local t and not account for scr refresh
        image_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
        image_4.setAutoDraw(True)
    if image_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_4.tStartRefresh + 1.5-frameTolerance:
            # keep track of stop time/frame for later
            image_4.tStop = t  # not accounting for scr refresh
            image_4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_4, 'tStopRefresh')  # time at next scr refresh
            image_4.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in btwn_trial_GJComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "btwn_trial_GJ"-------
for thisComponent in btwn_trial_GJComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_4.started', image_4.tStartRefresh)
thisExp.addData('image_4.stopped', image_4.tStopRefresh)

# ------Prepare to start Routine "trial_instr_run2"-------
continueRoutine = True
# update component parameters for each repeat
instructions_imageR2.setImage(instructions_run2)
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
trial_instr_run2Components = [instructions_imageR2, key_resp_4]
for thisComponent in trial_instr_run2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial_instr_run2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trial_instr_run2"-------
while continueRoutine:
    # get current time
    t = trial_instr_run2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial_instr_run2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_imageR2* updates
    if instructions_imageR2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_imageR2.frameNStart = frameN  # exact frame index
        instructions_imageR2.tStart = t  # local t and not account for scr refresh
        instructions_imageR2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_imageR2, 'tStartRefresh')  # time at next scr refresh
        instructions_imageR2.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trial_instr_run2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial_instr_run2"-------
for thisComponent in trial_instr_run2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "trial_instr_run2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_run4 = data.TrialHandler(nReps=6, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(cond_file_run2, selection=positionRows),
    seed=None, name='trials_run4')
thisExp.addLoop(trials_run4)  # add the loop to the experiment
thisTrials_run4 = trials_run4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_run4.rgb)
if thisTrials_run4 != None:
    for paramName in thisTrials_run4:
        exec('{} = thisTrials_run4[paramName]'.format(paramName))

for thisTrials_run4 in trials_run4:
    currentLoop = trials_run4
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_run4.rgb)
    if thisTrials_run4 != None:
        for paramName in thisTrials_run4:
            exec('{} = thisTrials_run4[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trialFixR2"-------
    continueRoutine = True
    # update component parameters for each repeat
    if Trial_run2-1 == 0:
        currFix = fixColor_opts[0]
    else:
        if fixColorIdx_Run2[Trial_run2-1] == 0:
            currFix = currFix
        elif fixColorIdx_Run2[Trial_run2-1] == 1:
            if currFix == 'white':
                currFix = 'black'
            elif currFix == 'black':
                currFix = 'white'
    
    a = 1.25 # min ITI
    b = 1.75 # max ITI
    fixDur = (b-a) * random()+a
    
    if int(expInfo['position']) == 0:
        xPosition = 0
    elif int(expInfo['position']) == 2:
        if side == 'left':
            xPosition = -(width4deg*x_scale)
        elif side == 'right':
            xPosition = width4deg*x_scale
    elif int(expInfo['position']) == 1:
        xPosition = -(width4deg*x_scale)
    elif (expInfo['position']) == 3:
        xPosition = width4deg*x_scale
    
    thisExp.addData('fixR2', fixColorIdx_Run2[Trial_run2-1])
    text_4.setColor(currFix, colorSpace='rgb')
    fix_resp2_1.keys = []
    fix_resp2_1.rt = []
    _fix_resp2_1_allKeys = []
    # keep track of which components have finished
    trialFixR2Components = [text_4, fix_resp2_1]
    for thisComponent in trialFixR2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialFixR2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trialFixR2"-------
    while continueRoutine:
        # get current time
        t = trialFixR2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialFixR2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + fixDur-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                text_4.setAutoDraw(False)
        
        # *fix_resp2_1* updates
        waitOnFlip = False
        if fix_resp2_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_resp2_1.frameNStart = frameN  # exact frame index
            fix_resp2_1.tStart = t  # local t and not account for scr refresh
            fix_resp2_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_resp2_1, 'tStartRefresh')  # time at next scr refresh
            fix_resp2_1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(fix_resp2_1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(fix_resp2_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if fix_resp2_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_resp2_1.tStartRefresh + fixDur-frameTolerance:
                # keep track of stop time/frame for later
                fix_resp2_1.tStop = t  # not accounting for scr refresh
                fix_resp2_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix_resp2_1, 'tStopRefresh')  # time at next scr refresh
                fix_resp2_1.status = FINISHED
        if fix_resp2_1.status == STARTED and not waitOnFlip:
            theseKeys = fix_resp2_1.getKeys(keyList=['space'], waitRelease=False)
            _fix_resp2_1_allKeys.extend(theseKeys)
            if len(_fix_resp2_1_allKeys):
                fix_resp2_1.keys = _fix_resp2_1_allKeys[-1].name  # just the last key pressed
                fix_resp2_1.rt = _fix_resp2_1_allKeys[-1].rt
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialFixR2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trialFixR2"-------
    for thisComponent in trialFixR2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Trial_run2 = Trial_run2 + 1
    trials_run4.addData('text_4.started', text_4.tStartRefresh)
    trials_run4.addData('text_4.stopped', text_4.tStopRefresh)
    # check responses
    if fix_resp2_1.keys in ['', [], None]:  # No response was made
        fix_resp2_1.keys = None
    trials_run4.addData('fix_resp2_1.keys',fix_resp2_1.keys)
    if fix_resp2_1.keys != None:  # we had a response
        trials_run4.addData('fix_resp2_1.rt', fix_resp2_1.rt)
    trials_run4.addData('fix_resp2_1.started', fix_resp2_1.tStartRefresh)
    trials_run4.addData('fix_resp2_1.stopped', fix_resp2_1.tStopRefresh)
    # the Routine "trialFixR2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "trial_img"-------
    continueRoutine = True
    # update component parameters for each repeat
    text_6.setColor(currFix, colorSpace='rgb')
    trial_image.setPos((xPosition, 0))
    trial_image.setSize((width*x_scale,height*y_scale))
    trial_image.setImage(imFile)
    trial_resp.keys = []
    trial_resp.rt = []
    _trial_resp_allKeys = []
    fix_resp_2.keys = []
    fix_resp_2.rt = []
    _fix_resp_2_allKeys = []
    # keep track of which components have finished
    trial_imgComponents = [text_6, trial_image, trial_resp, fix_resp_2]
    for thisComponent in trial_imgComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_imgClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial_img"-------
    while continueRoutine:
        # get current time
        t = trial_imgClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_imgClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_6* updates
        if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            text_6.setAutoDraw(True)
        
        # *trial_image* updates
        if trial_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_image.frameNStart = frameN  # exact frame index
            trial_image.tStart = t  # local t and not account for scr refresh
            trial_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_image, 'tStartRefresh')  # time at next scr refresh
            trial_image.setAutoDraw(True)
        
        # *trial_resp* updates
        waitOnFlip = False
        if trial_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_resp.frameNStart = frameN  # exact frame index
            trial_resp.tStart = t  # local t and not account for scr refresh
            trial_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_resp, 'tStartRefresh')  # time at next scr refresh
            trial_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(trial_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(trial_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if trial_resp.status == STARTED and not waitOnFlip:
            theseKeys = trial_resp.getKeys(keyList=['f', 'j'], waitRelease=False)
            _trial_resp_allKeys.extend(theseKeys)
            if len(_trial_resp_allKeys):
                trial_resp.keys = _trial_resp_allKeys[-1].name  # just the last key pressed
                trial_resp.rt = _trial_resp_allKeys[-1].rt
                # was this correct?
                if (trial_resp.keys == str(corr)) or (trial_resp.keys == corr):
                    trial_resp.corr = 1
                else:
                    trial_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *fix_resp_2* updates
        waitOnFlip = False
        if fix_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_resp_2.frameNStart = frameN  # exact frame index
            fix_resp_2.tStart = t  # local t and not account for scr refresh
            fix_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_resp_2, 'tStartRefresh')  # time at next scr refresh
            fix_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(fix_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(fix_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if fix_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = fix_resp_2.getKeys(keyList=['space'], waitRelease=False)
            _fix_resp_2_allKeys.extend(theseKeys)
            if len(_fix_resp_2_allKeys):
                fix_resp_2.keys = _fix_resp_2_allKeys[-1].name  # just the last key pressed
                fix_resp_2.rt = _fix_resp_2_allKeys[-1].rt
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_imgComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_img"-------
    for thisComponent in trial_imgComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_run4.addData('text_6.started', text_6.tStartRefresh)
    trials_run4.addData('text_6.stopped', text_6.tStopRefresh)
    trials_run4.addData('trial_image.started', trial_image.tStartRefresh)
    trials_run4.addData('trial_image.stopped', trial_image.tStopRefresh)
    # check responses
    if trial_resp.keys in ['', [], None]:  # No response was made
        trial_resp.keys = None
        # was no response the correct answer?!
        if str(corr).lower() == 'none':
           trial_resp.corr = 1;  # correct non-response
        else:
           trial_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_run4 (TrialHandler)
    trials_run4.addData('trial_resp.keys',trial_resp.keys)
    trials_run4.addData('trial_resp.corr', trial_resp.corr)
    if trial_resp.keys != None:  # we had a response
        trials_run4.addData('trial_resp.rt', trial_resp.rt)
    trials_run4.addData('trial_resp.started', trial_resp.tStartRefresh)
    trials_run4.addData('trial_resp.stopped', trial_resp.tStopRefresh)
    # check responses
    if fix_resp_2.keys in ['', [], None]:  # No response was made
        fix_resp_2.keys = None
    trials_run4.addData('fix_resp_2.keys',fix_resp_2.keys)
    if fix_resp_2.keys != None:  # we had a response
        trials_run4.addData('fix_resp_2.rt', fix_resp_2.rt)
    trials_run4.addData('fix_resp_2.started', fix_resp_2.tStartRefresh)
    trials_run4.addData('fix_resp_2.stopped', fix_resp_2.tStopRefresh)
    # the Routine "trial_img" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 6 repeats of 'trials_run4'


# ------Prepare to start Routine "EndScreen"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
EndScreenComponents = [image_5]
for thisComponent in EndScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "EndScreen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EndScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_5* updates
    if image_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_5.frameNStart = frameN  # exact frame index
        image_5.tStart = t  # local t and not account for scr refresh
        image_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_5, 'tStartRefresh')  # time at next scr refresh
        image_5.setAutoDraw(True)
    if image_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_5.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            image_5.tStop = t  # not accounting for scr refresh
            image_5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_5, 'tStopRefresh')  # time at next scr refresh
            image_5.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "EndScreen"-------
for thisComponent in EndScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_5.started', image_5.tStartRefresh)
thisExp.addData('image_5.stopped', image_5.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
