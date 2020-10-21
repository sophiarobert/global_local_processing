/********************* 
 * Global_Local Test *
 *********************/

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'global_local';  // from the Builder filename that created this script
let expInfo = {'participant': 'SR', 'design': '1', 'position': '0'};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(screen_scaleRoutineBegin());
flowScheduler.add(screen_scaleRoutineEachFrame());
flowScheduler.add(screen_scaleRoutineEnd());
flowScheduler.add(pracInstructRoutineBegin());
flowScheduler.add(pracInstructRoutineEachFrame());
flowScheduler.add(pracInstructRoutineEnd());
flowScheduler.add(prac_instr_run1RoutineBegin());
flowScheduler.add(prac_instr_run1RoutineEachFrame());
flowScheduler.add(prac_instr_run1RoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'bankcard.png', 'path': 'bankcard.png'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.DEBUG);


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.2.4';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var screen_scaleClock;
var thisExp;
var win;
var event;
var shuffle;
var webbrowser;
var random;
var randint;
var round;
var oldt;
var x_size;
var y_size;
var screen_height;
var x_scale;
var y_scale;
var dbase;
var unittext;
var vsize;
var height;
var width;
var text_top;
var text_bottom;
var ccimage;
var pracInstructClock;
var fixColor_opts;
var prac1_fixColSwitch;
var prac2_fixColSwitch;
var fixColorIdx_Run1;
var fixColorIdx_Run2;
var start_exp_text;
var start_exp_press;
var prac_instr_run1Clock;
var instructions_run1;
var cond_file_run1;
var rand8Idx;
var rand4rows_run1;
var instructions_imageR1;
var key_resp;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "screen_scale"
  screen_scaleClock = new util.Clock();
  thisExp=psychoJS.experiment;
  win=psychoJS.window;
  event=psychoJS.eventManager;
  Array.prototype.append = [].push;
  shuffle = util.shuffle;
  webbrowser=window;
  
  random=Math.random;
  randint=function(min, maxplusone) {
      return Math.floor(Math.random() * (maxplusone - min) ) + min;
  }
  
  round = function(num, n=0) {    
      return +(Math.round(num + ("e+" + n))  + ("e-" + n));
  }
  
  psychoJS.downloadResources([{name: ("Stimuli/greenCheck.png"), path:("Stimuli/greenCheck.png")},
  {name: ("Stimuli/redWrong.png"), path:("Stimuli/redWrong.png")},
  {name: ("Stimuli/HofH2.bmp"), path:("Stimuli/HofH2.bmp")},
  {name: ("Stimuli/HofS2.bmp"), path:("Stimuli/HofS2.bmp")},
  {name: ("Stimuli/SofH2.bmp"), path:("Stimuli/SofH2.bmp")},
  {name: ("Stimuli/SofS2.bmp"), path:("Stimuli/SofS2.bmp")},
  {name: ("Designs/design1_run1.png"), path:("Designs/design1_run1.png")},
  {name: ("Designs/design2_run1.png"), path:("Designs/design2_run1.png")},
  {name: ("Designs/design3_run1.png"), path:("Designs/design3_run1.png")},
  {name: ("Designs/design4_run1.png"), path:("Designs/design4_run1.png")},
  {name: ("Designs/design1_run2.png"), path:("Designs/design1_run2.png")},
  {name: ("Designs/design2_run2.png"), path:("Designs/design2_run2.png")},
  {name: ("Designs/design3_run2.png"), path:("Designs/design3_run2.png")},
  {name: ("Designs/design4_run2.png"), path:("Designs/design4_run2.png")},
  {name: ("Designs/design1_run1.csv"), path:("Designs/design1_run1.csv")},
  {name: ("Designs/design2_run1.csv"), path:("Designs/design2_run1.csv")},
  {name: ("Designs/design3_run1.csv"), path:("Designs/design3_run1.csv")},
  {name: ("Designs/design4_run1.csv"), path:("Designs/design4_run1.csv")},
  {name: ("Designs/design1_run2.csv"), path:("Designs/design1_run2.csv")},
  {name: ("Designs/design2_run2.csv"), path:("Designs/design2_run2.csv")},
  {name: ("Designs/design3_run2.csv"), path:("Designs/design3_run2.csv")},
  {name: ("Designs/design4_run2.csv"), path:("Designs/design4_run2.csv")}]);
  
  expInfo['OS'] = window.navigator.platform;
  expInfo['xResolution'] = screen.width;
  expInfo['yResolution'] = screen.height;
  oldt = 0;
  x_size = 8.56;
  y_size = 5.398;
  screen_height = 0;
  if ((win.units === "norm")) {
      x_scale = 0.05;
      y_scale = 0.1;
      dbase = 0.0001;
      unittext = " norm units";
      vsize = 2;
  } else {
      if ((win.units === "pix")) {
          x_scale = 60;
          y_scale = 40;
          dbase = 0.1;
          unittext = " pixels";
          vsize = win.size[1];
      } else {
          x_scale = 0.05;
          y_scale = 0.05;
          dbase = 0.0001;
          unittext = " height units";
          vsize = 1;
      }
  }
  height = 3.459;
  width = 3.459;
  
  text_top = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_top',
    text: 'Resize this image to match the size of a credit card with arrow keys',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  text_bottom = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_bottom',
    text: 'Press Space when you’re finished',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  ccimage = new visual.ImageStim({
    win : psychoJS.window,
    name : 'ccimage', units : undefined, 
    image : 'bankcard.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [(x_size * x_scale), (y_size * y_scale)],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -4.0 
  });
  // Initialize components for Routine "pracInstruct"
  pracInstructClock = new util.Clock();
  fixColor_opts = ["orange", "pink"];
  shuffle(fixColor_opts);
  prac1_fixColSwitch = [0, 0, 0, 1];
  shuffle(prac1_fixColSwitch);
  prac2_fixColSwitch = [0, 0, 0, 1];
  shuffle(prac2_fixColSwitch);
  fixColorIdx_Run1 = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1];
  shuffle(fixColorIdx_Run1);
  fixColorIdx_Run2 = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1];
  shuffle(fixColorIdx_Run2);
  thisExp.addData("fixpR1", prac1_fixColSwitch);
  thisExp.addData("fixR1", fixColorIdx_Run1);
  thisExp.addData("fixpR2", prac2_fixColSwitch);
  thisExp.addData("fixR2", fixColorIdx_Run2);
  
  start_exp_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'start_exp_text',
    text: 'You will play two games. \nBefore you start, let’s do some practice!\n\nAre you ready? \nPress Space to start practice!',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  start_exp_press = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "prac_instr_run1"
  prac_instr_run1Clock = new util.Clock();
  if ((expInfo["design"] === "1")) {
      instructions_run1 = "Designs/design1_run1.png";
      cond_file_run1 = "Designs/design1_run1.csv";
  } else {
      if ((expInfo["design"] === "2")) {
          instructions_run1 = "Designs/design2_run1.png";
          cond_file_run1 = "Designs/design2_run1.csv";
      } else {
          if ((expInfo["design"] === "3")) {
              instruction_run1 = "Designs/design3_run1.png";
              cond_file_run1 = "Designs/design3_run1.csv";
          } else {
              if ((expInfo["design"] === "4")) {
                  instructions_run1 = "Designs/design4_run1.png";
                  cond_file_run1 = "Designs/design4_run1.csv";
              }
          }
      }
  }
  rand8Idx = [0, 1, 2, 3, 4, 5, 6, 7];
  shuffle(rand8Idx);
  rand4rows_run1 = rand8Idx.slice(0, 4);
  
  instructions_imageR1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'instructions_imageR1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [(0.75 * 1.5), 0.75],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -1.0 
  });
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var screen_scaleComponents;
function screen_scaleRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'screen_scale'-------
    t = 0;
    screen_scaleClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // keep track of which components have finished
    screen_scaleComponents = [];
    screen_scaleComponents.push(text_top);
    screen_scaleComponents.push(text_bottom);
    screen_scaleComponents.push(ccimage);
    
    screen_scaleComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


var _pj;
var keys;
var dscale;
var continueRoutine;
function screen_scaleRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'screen_scale'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = screen_scaleClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    keys = event.getKeys();
    if (keys.length) {
        if (((t - oldt) < 0.5)) {
            dscale = (5 * dbase);
            oldt = t;
        } else {
            dscale = dbase;
            oldt = t;
        }
        if (_pj.in_es6("space", keys)) {
            continueRoutine = false;
        } else {
            if (_pj.in_es6("up", keys)) {
                y_scale = (round(((y_scale + dscale) * 10000)) / 10000);
            } else {
                if (_pj.in_es6("down", keys)) {
                    y_scale = (round(((y_scale - dscale) * 10000)) / 10000);
                } else {
                    if (_pj.in_es6("left", keys)) {
                        x_scale = (round(((x_scale - dscale) * 10000)) / 10000);
                    } else {
                        if (_pj.in_es6("right", keys)) {
                            x_scale = (round(((x_scale + dscale) * 10000)) / 10000);
                        }
                    }
                }
            }
        }
        screen_height = (round(((vsize * 10) / y_scale)) / 10);
        ccimage.size = [(x_size * x_scale), (y_size * y_scale)];
    }
    
    
    // *text_top* updates
    if (t >= 0.0 && text_top.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_top.tStart = t;  // (not accounting for frame time here)
      text_top.frameNStart = frameN;  // exact frame index
      
      text_top.setAutoDraw(true);
    }

    
    // *text_bottom* updates
    if (t >= 0.0 && text_bottom.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_bottom.tStart = t;  // (not accounting for frame time here)
      text_bottom.frameNStart = frameN;  // exact frame index
      
      text_bottom.setAutoDraw(true);
    }

    
    // *ccimage* updates
    if (t >= 0.0 && ccimage.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ccimage.tStart = t;  // (not accounting for frame time here)
      ccimage.frameNStart = frameN;  // exact frame index
      
      ccimage.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    screen_scaleComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function screen_scaleRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'screen_scale'-------
    screen_scaleComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    thisExp.addData("X Scale", x_scale);
    thisExp.addData("Y Scale", y_scale);
    
    // the Routine "screen_scale" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _start_exp_press_allKeys;
var pracInstructComponents;
function pracInstructRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'pracInstruct'-------
    t = 0;
    pracInstructClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    start_exp_press.keys = undefined;
    start_exp_press.rt = undefined;
    _start_exp_press_allKeys = [];
    // keep track of which components have finished
    pracInstructComponents = [];
    pracInstructComponents.push(start_exp_text);
    pracInstructComponents.push(start_exp_press);
    
    pracInstructComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function pracInstructRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'pracInstruct'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = pracInstructClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *start_exp_text* updates
    if (t >= 0.0 && start_exp_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      start_exp_text.tStart = t;  // (not accounting for frame time here)
      start_exp_text.frameNStart = frameN;  // exact frame index
      
      start_exp_text.setAutoDraw(true);
    }

    
    // *start_exp_press* updates
    if (t >= 1 && start_exp_press.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      start_exp_press.tStart = t;  // (not accounting for frame time here)
      start_exp_press.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { start_exp_press.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { start_exp_press.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { start_exp_press.clearEvents(); });
    }

    if (start_exp_press.status === PsychoJS.Status.STARTED) {
      let theseKeys = start_exp_press.getKeys({keyList: ['space'], waitRelease: false});
      _start_exp_press_allKeys = _start_exp_press_allKeys.concat(theseKeys);
      if (_start_exp_press_allKeys.length > 0) {
        start_exp_press.keys = _start_exp_press_allKeys[_start_exp_press_allKeys.length - 1].name;  // just the last key pressed
        start_exp_press.rt = _start_exp_press_allKeys[_start_exp_press_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    pracInstructComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function pracInstructRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'pracInstruct'-------
    pracInstructComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "pracInstruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_allKeys;
var prac_instr_run1Components;
function prac_instr_run1RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'prac_instr_run1'-------
    t = 0;
    prac_instr_run1Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    instructions_imageR1.setImage(instructions_run1);
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    prac_instr_run1Components = [];
    prac_instr_run1Components.push(instructions_imageR1);
    prac_instr_run1Components.push(key_resp);
    
    prac_instr_run1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function prac_instr_run1RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'prac_instr_run1'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = prac_instr_run1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instructions_imageR1* updates
    if (t >= 0.0 && instructions_imageR1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructions_imageR1.tStart = t;  // (not accounting for frame time here)
      instructions_imageR1.frameNStart = frameN;  // exact frame index
      
      instructions_imageR1.setAutoDraw(true);
    }

    
    // *key_resp* updates
    if (t >= 1 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    prac_instr_run1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function prac_instr_run1RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'prac_instr_run1'-------
    prac_instr_run1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "prac_instr_run1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
