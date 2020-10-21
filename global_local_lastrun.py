#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.4),
    on Wed Oct 21 13:07:59 2020
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
expInfo = {'participant': '', 'design': '1', 'position': '0'}
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


thisExp.addData('fixpR1', prac1_fixColSwitch)
thisExp.addData('fixR1', fixColorIdx_Run1)
thisExp.addData('fixpR2', prac2_fixColSwitch)
thisExp.addData('fixR2', fixColorIdx_Run2)
start_exp_text = visual.TextStim(win=win, name='start_exp_text',
    text='You will play two games. \nBefore you start, let’s do some practice!\n\nAre you ready? \nPress ’Space’ to start practice!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
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
    instruction_run1 = 'Designs/design3_run1.png'
    cond_file_run1 = 'Designs/design3_run1.csv'
elif expInfo['design']=='4':
    instructions_run1 = 'Designs/design4_run1.png'
    cond_file_run1 = 'Designs/design4_run1.csv'

rand8Idx = [0,1,2,3,4,5,6,7];
shuffle(rand8Idx)
rand4rows_run1 = rand8Idx[0:4]
instructions_imageR1 = visual.ImageStim(
    win=win,
    name='instructions_imageR1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.75*1.5, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
key_resp = keyboard.Keyboard()

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
instructions_imageR1.setImage(instructions_run1)
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
prac_instr_run1Components = [instructions_imageR1, key_resp]
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
    
    # *instructions_imageR1* updates
    if instructions_imageR1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_imageR1.frameNStart = frameN  # exact frame index
        instructions_imageR1.tStart = t  # local t and not account for scr refresh
        instructions_imageR1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_imageR1, 'tStartRefresh')  # time at next scr refresh
        instructions_imageR1.setAutoDraw(True)
    
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
thisExp.addData('instructions_imageR1.started', instructions_imageR1.tStartRefresh)
thisExp.addData('instructions_imageR1.stopped', instructions_imageR1.tStopRefresh)
# the Routine "prac_instr_run1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
