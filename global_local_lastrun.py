#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.4),
    on Sun Oct 25 00:01:04 2020
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
expInfo = {'participant': '', 'design': '1', 'position': '1'}
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
height = 3.459
width = 3.459
text_top = visual.TextStim(win=win, name='text_top',
    text='Resize this image to match the size of a credit card with arrow keys',
    font='Arial',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_bottom = visual.TextStim(win=win, name='text_bottom',
    text='Press Space when you’re finished',
    font='Arial',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
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

fixColor_opts = ["orange", "pink"];
shuffle(fixColor_opts);
prac1_fixColSwitch = [0,0,0,1];
shuffle(prac1_fixColSwitch);
prac2_fixColSwitch = [0,0,0,1];
shuffle(prac2_fixColSwitch);
fixColorIdx_Run1 =  [0, 0, 0, 0, 0, 0, 0, 1, 
                                   0, 0, 0, 0, 0, 0, 0, 1, 
                                   0, 0, 0, 0, 0, 0, 0, 1, 
                                   0, 0, 0, 0, 0, 0, 0, 1, 
                                   0, 0, 0, 0, 0, 0, 0, 1, 
                                   0, 0, 0, 0, 0, 0, 0, 1, 
                                   0, 0, 0, 0, 0, 0, 0, 1, 
                                   0, 0, 0, 0, 0, 0, 0, 1, 
                                   0, 0, 0, 0, 0, 0, 0, 1, 
                                   0, 0, 0, 0, 0, 0, 0, 1, 
                                   0, 0, 0, 0, 0, 0, 0, 1,
                                   0, 0, 0, 0, 0, 0, 0, 1];
shuffle(fixColorIdx_Run1);
fixColorIdx_Run2 = [0, 0, 0, 0, 0, 0, 0, 1, 
                                   0, 0, 0, 0, 0, 0, 0, 1, 
                                   0, 0, 0, 0, 0, 0, 0, 1, 
                                   0, 0, 0, 0, 0, 0, 0, 1, 
                                   0, 0, 0, 0, 0, 0, 0, 1, 
                                   0, 0, 0, 0, 0, 0, 0, 1, 
                                   0, 0, 0, 0, 0, 0, 0, 1, 
                                   0, 0, 0, 0, 0, 0, 0, 1, 
                                   0, 0, 0, 0, 0, 0, 0, 1, 
                                   0, 0, 0, 0, 0, 0, 0, 1, 
                                   0, 0, 0, 0, 0, 0, 0, 1,
                                   0, 0, 0, 0, 0, 0, 0, 1];
shuffle(fixColorIdx_Run2);
start_exp_text = visual.TextStim(win=win, name='start_exp_text',
    text='You will play two games. \nBefore you start, let’s do some practice!\n\nAre you ready? \nPress Space to start practice!',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
start_exp_press = keyboard.Keyboard()

# Initialize components for Routine "prac_instr_run1"
prac_instr_run1Clock = core.Clock()
if expInfo['design']=='1':
    instructions_run1 = 'Designs/design1_run1.png'
    cond_file_run1 = 'Designs/design1_run1.csv'
elif expInfo['design']=='2':
    instructions_run1 = 'Designs/design2_run1.png'
    cond_file_run1 = 'Designs/design2_run1.csv'
elif expInfo['design']=='3':
    instructions_run1 = 'Designs/design3_run1.png'
    cond_file_run1 = 'Designs/design3_run1.csv'
elif expInfo['design']=='4':
    instructions_run1 = 'Designs/design4_run1.png'
    cond_file_run1 = 'Designs/design4_run1.csv'

rand8Idx = [0,1,2,3,4,5,6,7];
shuffle(rand8Idx)
rand4rows_run1 = rand8Idx[0:4]
Pinstructions_imageR1 = visual.ImageStim(
    win=win,
    name='Pinstructions_imageR1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.75*1.5, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "pracFixR1"
pracFixR1Clock = core.Clock()
pTrial_run1 = 1
pracTotal_run1 = 4

pTrial_run2 = 1
pracTotal_run2 = 4

text = visual.TextStim(win=win, name='text',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
fix_respP1_1 = keyboard.Keyboard()

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
prac_fix_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
imFeedback = visual.ImageStim(
    win=win,
    name='imFeedback', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
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
Total_run2 = 96
instructions_imageR1 = visual.ImageStim(
    win=win,
    name='instructions_imageR1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.75*1.5, 0.75),
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

rand8Idx = [0,1,2,3,4,5,6,7];
shuffle(rand8Idx)
rand4rows_run2 = rand8Idx[0:4]
Pinstructions_imageR2 = visual.ImageStim(
    win=win,
    name='Pinstructions_imageR2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.75*1.5, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
key_resp_3 = keyboard.Keyboard()

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
prac_fix_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
imFeedback = visual.ImageStim(
    win=win,
    name='imFeedback', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
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
    ori=0, pos=(0, 0), size=(0.75*1.5, 0.75),
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
allDone = visual.TextStim(win=win, name='allDone',
    text='You are all done. Thank you!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

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

thisExp.addData('text_top.started', text_top.tStartRefresh)
thisExp.addData('text_top.stopped', text_top.tStopRefresh)
thisExp.addData('text_bottom.started', text_bottom.tStartRefresh)
thisExp.addData('text_bottom.stopped', text_bottom.tStopRefresh)
thisExp.addData('ccimage.started', ccimage.tStartRefresh)
thisExp.addData('ccimage.stopped', ccimage.tStopRefresh)
# the Routine "screen_scale" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "pracInstruct"-------
continueRoutine = True
# update component parameters for each repeat
start_exp_press.keys = []
start_exp_press.rt = []
_start_exp_press_allKeys = []
# keep track of which components have finished
pracInstructComponents = [start_exp_text, start_exp_press]
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
    
    # *start_exp_text* updates
    if start_exp_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_exp_text.frameNStart = frameN  # exact frame index
        start_exp_text.tStart = t  # local t and not account for scr refresh
        start_exp_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_exp_text, 'tStartRefresh')  # time at next scr refresh
        start_exp_text.setAutoDraw(True)
    
    # *start_exp_press* updates
    waitOnFlip = False
    if start_exp_press.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
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
thisExp.addData('start_exp_text.started', start_exp_text.tStartRefresh)
thisExp.addData('start_exp_text.stopped', start_exp_text.tStopRefresh)
# the Routine "pracInstruct" was not non-slip safe, so reset the non-slip timer
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
thisExp.addData('Pinstructions_imageR1.started', Pinstructions_imageR1.tStartRefresh)
thisExp.addData('Pinstructions_imageR1.stopped', Pinstructions_imageR1.tStopRefresh)
# the Routine "prac_instr_run1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
prac_trials_run1 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(cond_file_run1, selection=rand4rows_run1),
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
    else:
        if prac1_fixColSwitch[pTrial_run1-1] == 0:
            currFix = currFix
        elif currFix == 'pink':
            currFix = 'orange'
        elif currFix == 'orange':
            currFix = 'pink'
     
    a = 1.25 # min ITI
    b = 1.75 # max ITI
    fixDur = (b-a) * random()+a
    
    if expInfo['position'] == '0':
        xPosition = 0
    elif expInfo['position'] == '1':
        if side == 'left':
            xPosition = -(width*x_scale)
        elif side == 'right':
            xPosition = width*x_scale
    
    thisExp.addData('fixpR1', prac1_fixColSwitch[pTrial_run1-1])
    text.setColor(currFix, colorSpace='rgb')
    fix_respP1_1.keys = []
    fix_respP1_1.rt = []
    _fix_respP1_1_allKeys = []
    # keep track of which components have finished
    pracFixR1Components = [text, fix_respP1_1]
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
        
        # *fix_respP1_1* updates
        waitOnFlip = False
        if fix_respP1_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_respP1_1.frameNStart = frameN  # exact frame index
            fix_respP1_1.tStart = t  # local t and not account for scr refresh
            fix_respP1_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_respP1_1, 'tStartRefresh')  # time at next scr refresh
            fix_respP1_1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(fix_respP1_1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(fix_respP1_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if fix_respP1_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix_respP1_1.tStartRefresh + fixDur-frameTolerance:
                # keep track of stop time/frame for later
                fix_respP1_1.tStop = t  # not accounting for scr refresh
                fix_respP1_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix_respP1_1, 'tStopRefresh')  # time at next scr refresh
                fix_respP1_1.status = FINISHED
        if fix_respP1_1.status == STARTED and not waitOnFlip:
            theseKeys = fix_respP1_1.getKeys(keyList=['space'], waitRelease=False)
            _fix_respP1_1_allKeys.extend(theseKeys)
            if len(_fix_respP1_1_allKeys):
                fix_respP1_1.keys = _fix_respP1_1_allKeys[-1].name  # just the last key pressed
                fix_respP1_1.rt = _fix_respP1_1_allKeys[-1].rt
        
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
    prac_trials_run1.addData('text.started', text.tStartRefresh)
    prac_trials_run1.addData('text.stopped', text.tStopRefresh)
    # check responses
    if fix_respP1_1.keys in ['', [], None]:  # No response was made
        fix_respP1_1.keys = None
    prac_trials_run1.addData('fix_respP1_1.keys',fix_respP1_1.keys)
    if fix_respP1_1.keys != None:  # we had a response
        prac_trials_run1.addData('fix_respP1_1.rt', fix_respP1_1.rt)
    prac_trials_run1.addData('fix_respP1_1.started', fix_respP1_1.tStartRefresh)
    prac_trials_run1.addData('fix_respP1_1.stopped', fix_respP1_1.tStopRefresh)
    # the Routine "pracFixR1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "prac_img"-------
    continueRoutine = True
    # update component parameters for each repeat
    text_5.setColor(currFix, colorSpace='rgb')
    prac_image.setPos((xPosition, 0))
    prac_image.setSize((width*x_scale, height*y_scale))
    prac_image.setImage(imFile)
    prac_resp.keys = []
    prac_resp.rt = []
    _prac_resp_allKeys = []
    prac_fix_resp_2.keys = []
    prac_fix_resp_2.rt = []
    _prac_fix_resp_2_allKeys = []
    # keep track of which components have finished
    prac_imgComponents = [text_5, prac_image, prac_resp, prac_fix_resp_2]
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
    while continueRoutine:
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
        
        # *prac_image* updates
        if prac_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_image.frameNStart = frameN  # exact frame index
            prac_image.tStart = t  # local t and not account for scr refresh
            prac_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_image, 'tStartRefresh')  # time at next scr refresh
            prac_image.setAutoDraw(True)
        
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
            win.callOnFlip(prac_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
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
                # a response ends the routine
                continueRoutine = False
        
        # *prac_fix_resp_2* updates
        waitOnFlip = False
        if prac_fix_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_fix_resp_2.frameNStart = frameN  # exact frame index
            prac_fix_resp_2.tStart = t  # local t and not account for scr refresh
            prac_fix_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_fix_resp_2, 'tStartRefresh')  # time at next scr refresh
            prac_fix_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(prac_fix_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(prac_fix_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if prac_fix_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = prac_fix_resp_2.getKeys(keyList=['space'], waitRelease=False)
            _prac_fix_resp_2_allKeys.extend(theseKeys)
            if len(_prac_fix_resp_2_allKeys):
                prac_fix_resp_2.keys = _prac_fix_resp_2_allKeys[-1].name  # just the last key pressed
                prac_fix_resp_2.rt = _prac_fix_resp_2_allKeys[-1].rt
        
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
    prac_trials_run1.addData('text_5.started', text_5.tStartRefresh)
    prac_trials_run1.addData('text_5.stopped', text_5.tStopRefresh)
    prac_trials_run1.addData('prac_image.started', prac_image.tStartRefresh)
    prac_trials_run1.addData('prac_image.stopped', prac_image.tStopRefresh)
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
    prac_trials_run1.addData('prac_resp.started', prac_resp.tStartRefresh)
    prac_trials_run1.addData('prac_resp.stopped', prac_resp.tStopRefresh)
    # check responses
    if prac_fix_resp_2.keys in ['', [], None]:  # No response was made
        prac_fix_resp_2.keys = None
    prac_trials_run1.addData('prac_fix_resp_2.keys',prac_fix_resp_2.keys)
    if prac_fix_resp_2.keys != None:  # we had a response
        prac_trials_run1.addData('prac_fix_resp_2.rt', prac_fix_resp_2.rt)
    prac_trials_run1.addData('prac_fix_resp_2.started', prac_fix_resp_2.tStartRefresh)
    prac_trials_run1.addData('prac_fix_resp_2.stopped', prac_fix_resp_2.tStopRefresh)
    # the Routine "prac_img" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Feedback"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    feedIM =''
    if prac_resp.keys == corr:
        feedIM = 'Stimuli/greenCheck.png'
        
    elif prac_resp.keys != corr:
        feedIM = 'Stimuli/redWrong.png'
    
    imFeedback.setImage(feedIM)
    # keep track of which components have finished
    FeedbackComponents = [imFeedback]
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
            if tThisFlipGlobal > imFeedback.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                imFeedback.tStop = t  # not accounting for scr refresh
                imFeedback.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imFeedback, 'tStopRefresh')  # time at next scr refresh
                imFeedback.setAutoDraw(False)
        
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
    prac_trials_run1.addData('imFeedback.started', imFeedback.tStartRefresh)
    prac_trials_run1.addData('imFeedback.stopped', imFeedback.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'prac_trials_run1'


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
thisExp.addData('instructions_imageR1.started', instructions_imageR1.tStartRefresh)
thisExp.addData('instructions_imageR1.stopped', instructions_imageR1.tStopRefresh)
# the Routine "trial_instr_run1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_run1 = data.TrialHandler(nReps=12, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(cond_file_run1),
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
        elif currFix == 'pink':
            currFix = 'orange'
        elif currFix == 'orange':
            currFix = 'pink'
    
    a = 1.25 # min ITI
    b = 1.75 # max ITI
    fixDur = (b-a) * random()+a
    
    if expInfo['position'] == '0':
        xPosition = 0
    elif expInfo['position'] == '1':
        if side == 'left':
            xPosition = -(width*x_scale)
        elif side == 'right':
            xPosition = width*x_scale
    
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
    
# completed 12 repeats of 'trials_run1'


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
thisExp.addData('Pinstructions_imageR2.started', Pinstructions_imageR2.tStartRefresh)
thisExp.addData('Pinstructions_imageR2.stopped', Pinstructions_imageR2.tStopRefresh)
# the Routine "prac_instr_run2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
prac_trials_run2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(cond_file_run2, selection=rand4rows_run2),
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
    else:
        if prac2_fixColSwitch[pTrial_run2-1] == 0:
            currFix = currFix
        elif  currFix == 'pink':
            currFix = 'orange'
        elif currFix == 'orange':
            currFix = 'pink'
    a = 1.25 # min ITI
    b = 1.75 # max ITI
    fixDur = (b-a) * random()+a
    
    if expInfo['position'] == '0':
        xPosition = 0
    elif expInfo['position'] == '1':
        if side == 'left':
            xPosition = -(width*x_scale)
        elif side == 'right':
            xPosition = width*x_scale
    
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
    prac_trials_run2.addData('text_3.started', text_3.tStartRefresh)
    prac_trials_run2.addData('text_3.stopped', text_3.tStopRefresh)
    # check responses
    if fix_respP2_1.keys in ['', [], None]:  # No response was made
        fix_respP2_1.keys = None
    prac_trials_run2.addData('fix_respP2_1.keys',fix_respP2_1.keys)
    if fix_respP2_1.keys != None:  # we had a response
        prac_trials_run2.addData('fix_respP2_1.rt', fix_respP2_1.rt)
    prac_trials_run2.addData('fix_respP2_1.started', fix_respP2_1.tStartRefresh)
    prac_trials_run2.addData('fix_respP2_1.stopped', fix_respP2_1.tStopRefresh)
    # the Routine "pracFixR2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "prac_img"-------
    continueRoutine = True
    # update component parameters for each repeat
    text_5.setColor(currFix, colorSpace='rgb')
    prac_image.setPos((xPosition, 0))
    prac_image.setSize((width*x_scale, height*y_scale))
    prac_image.setImage(imFile)
    prac_resp.keys = []
    prac_resp.rt = []
    _prac_resp_allKeys = []
    prac_fix_resp_2.keys = []
    prac_fix_resp_2.rt = []
    _prac_fix_resp_2_allKeys = []
    # keep track of which components have finished
    prac_imgComponents = [text_5, prac_image, prac_resp, prac_fix_resp_2]
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
    while continueRoutine:
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
        
        # *prac_image* updates
        if prac_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_image.frameNStart = frameN  # exact frame index
            prac_image.tStart = t  # local t and not account for scr refresh
            prac_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_image, 'tStartRefresh')  # time at next scr refresh
            prac_image.setAutoDraw(True)
        
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
            win.callOnFlip(prac_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
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
                # a response ends the routine
                continueRoutine = False
        
        # *prac_fix_resp_2* updates
        waitOnFlip = False
        if prac_fix_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_fix_resp_2.frameNStart = frameN  # exact frame index
            prac_fix_resp_2.tStart = t  # local t and not account for scr refresh
            prac_fix_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_fix_resp_2, 'tStartRefresh')  # time at next scr refresh
            prac_fix_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(prac_fix_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(prac_fix_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if prac_fix_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = prac_fix_resp_2.getKeys(keyList=['space'], waitRelease=False)
            _prac_fix_resp_2_allKeys.extend(theseKeys)
            if len(_prac_fix_resp_2_allKeys):
                prac_fix_resp_2.keys = _prac_fix_resp_2_allKeys[-1].name  # just the last key pressed
                prac_fix_resp_2.rt = _prac_fix_resp_2_allKeys[-1].rt
        
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
    prac_trials_run2.addData('text_5.started', text_5.tStartRefresh)
    prac_trials_run2.addData('text_5.stopped', text_5.tStopRefresh)
    prac_trials_run2.addData('prac_image.started', prac_image.tStartRefresh)
    prac_trials_run2.addData('prac_image.stopped', prac_image.tStopRefresh)
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
    prac_trials_run2.addData('prac_resp.started', prac_resp.tStartRefresh)
    prac_trials_run2.addData('prac_resp.stopped', prac_resp.tStopRefresh)
    # check responses
    if prac_fix_resp_2.keys in ['', [], None]:  # No response was made
        prac_fix_resp_2.keys = None
    prac_trials_run2.addData('prac_fix_resp_2.keys',prac_fix_resp_2.keys)
    if prac_fix_resp_2.keys != None:  # we had a response
        prac_trials_run2.addData('prac_fix_resp_2.rt', prac_fix_resp_2.rt)
    prac_trials_run2.addData('prac_fix_resp_2.started', prac_fix_resp_2.tStartRefresh)
    prac_trials_run2.addData('prac_fix_resp_2.stopped', prac_fix_resp_2.tStopRefresh)
    # the Routine "prac_img" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Feedback"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    feedIM =''
    if prac_resp.keys == corr:
        feedIM = 'Stimuli/greenCheck.png'
        
    elif prac_resp.keys != corr:
        feedIM = 'Stimuli/redWrong.png'
    
    imFeedback.setImage(feedIM)
    # keep track of which components have finished
    FeedbackComponents = [imFeedback]
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
            if tThisFlipGlobal > imFeedback.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                imFeedback.tStop = t  # not accounting for scr refresh
                imFeedback.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imFeedback, 'tStopRefresh')  # time at next scr refresh
                imFeedback.setAutoDraw(False)
        
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
    prac_trials_run2.addData('imFeedback.started', imFeedback.tStartRefresh)
    prac_trials_run2.addData('imFeedback.stopped', imFeedback.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'prac_trials_run2'


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
thisExp.addData('instructions_imageR2.started', instructions_imageR2.tStartRefresh)
thisExp.addData('instructions_imageR2.stopped', instructions_imageR2.tStopRefresh)
# the Routine "trial_instr_run2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_run2 = data.TrialHandler(nReps=12, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(cond_file_run2),
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
        elif currFix == 'pink':
            currFix = 'orange'
        elif currFix == 'orange':
            currFix = 'pink'
            
    a = 1.25 # min ITI
    b = 1.75 # max ITI
    fixDur = (b-a) * random()+a
    
    if expInfo['position'] == '0':
        xPosition = 0
    elif expInfo['position'] == '1':
        if side == 'left':
            xPosition = -(width*x_scale)
        elif side == 'right':
            xPosition = width*x_scale
    
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
    
# completed 12 repeats of 'trials_run2'


# ------Prepare to start Routine "EndScreen"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
EndScreenComponents = [allDone]
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
    
    # *allDone* updates
    if allDone.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        allDone.frameNStart = frameN  # exact frame index
        allDone.tStart = t  # local t and not account for scr refresh
        allDone.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(allDone, 'tStartRefresh')  # time at next scr refresh
        allDone.setAutoDraw(True)
    if allDone.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > allDone.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            allDone.tStop = t  # not accounting for scr refresh
            allDone.frameNStop = frameN  # exact frame index
            win.timeOnFlip(allDone, 'tStopRefresh')  # time at next scr refresh
            allDone.setAutoDraw(False)
    
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
thisExp.addData('allDone.started', allDone.tStartRefresh)
thisExp.addData('allDone.stopped', allDone.tStopRefresh)

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
