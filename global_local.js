/********************* 
 * Global_Local Test *
 *********************/

import { PsychoJS } from './lib/core-2020.2.js';
import * as core from './lib/core-2020.2.js';
import { TrialHandler } from './lib/data-2020.2.js';
import { Scheduler } from './lib/util-2020.2.js';
import * as visual from './lib/visual-2020.2.js';
import * as sound from './lib/sound-2020.2.js';
import * as util from './lib/util-2020.2.js';
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;

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
let expInfo = {'participant': '', 'design': '1', 'position': '2'};

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
const prac_trials_run1LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(prac_trials_run1LoopBegin, prac_trials_run1LoopScheduler);
flowScheduler.add(prac_trials_run1LoopScheduler);
flowScheduler.add(prac_trials_run1LoopEnd);
flowScheduler.add(trial_instr_run1RoutineBegin());
flowScheduler.add(trial_instr_run1RoutineEachFrame());
flowScheduler.add(trial_instr_run1RoutineEnd());
const trials_run1LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_run1LoopBegin, trials_run1LoopScheduler);
flowScheduler.add(trials_run1LoopScheduler);
flowScheduler.add(trials_run1LoopEnd);
flowScheduler.add(prac_instr_run2RoutineBegin());
flowScheduler.add(prac_instr_run2RoutineEachFrame());
flowScheduler.add(prac_instr_run2RoutineEnd());
const prac_trials_run2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(prac_trials_run2LoopBegin, prac_trials_run2LoopScheduler);
flowScheduler.add(prac_trials_run2LoopScheduler);
flowScheduler.add(prac_trials_run2LoopEnd);
flowScheduler.add(trial_instr_run2RoutineBegin());
flowScheduler.add(trial_instr_run2RoutineEachFrame());
flowScheduler.add(trial_instr_run2RoutineEnd());
const trials_run2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_run2LoopBegin, trials_run2LoopScheduler);
flowScheduler.add(trials_run2LoopScheduler);
flowScheduler.add(trials_run2LoopEnd);
flowScheduler.add(EndScreenRoutineBegin());
flowScheduler.add(EndScreenRoutineEachFrame());
flowScheduler.add(EndScreenRoutineEnd());
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
var randRows_run1;
var Pinstructions_imageR1;
var key_resp;
var pracFixR1Clock;
var pTrial_run1;
var pracTotal_run1;
var pTrial_run2;
var pracTotal_run2;
var text;
var fix_respP1_1;
var prac_imgClock;
var text_5;
var prac_image;
var prac_resp;
var prac_fix_resp_2;
var FeedbackClock;
var imFeedback;
var trial_instr_run1Clock;
var Trial_run1;
var Total_run1;
var Trial_run2;
var Total_run2;
var positionRows;
var instructions_imageR1;
var key_resp_2;
var trialFixR1Clock;
var text_2;
var fix_resp1_1;
var trial_imgClock;
var text_6;
var trial_image;
var trial_resp;
var fix_resp_2;
var prac_instr_run2Clock;
var instructions_run2;
var cond_file_run2;
var randRows_run2;
var Pinstructions_imageR2;
var key_resp_3;
var pracFixR2Clock;
var text_3;
var fix_respP2_1;
var trial_instr_run2Clock;
var instructions_imageR2;
var key_resp_4;
var trialFixR2Clock;
var text_4;
var fix_resp2_1;
var EndScreenClock;
var allDone;
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
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  text_bottom = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_bottom',
    text: 'Press Space when you’re finished',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
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
  
  start_exp_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'start_exp_text',
    text: 'You will play two games. \nBefore you start, let’s do some practice!\n\nAre you ready? \nPress Space to start practice!',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  start_exp_press = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "prac_instr_run1"
  prac_instr_run1Clock = new util.Clock();
  var rand4Idx;
  if ((expInfo["design"] === "1")) {
      instructions_run1 = "Designs/design1_run1.png";
      cond_file_run1 = "Designs/design1_run1.csv";
  } else {
      if ((expInfo["design"] === "2")) {
          instructions_run1 = "Designs/design2_run1.png";
          cond_file_run1 = "Designs/design2_run1.csv";
      } else {
          if ((expInfo["design"] === "3")) {
              instructions_run1 = "Designs/design3_run1.png";
              cond_file_run1 = "Designs/design3_run1.csv";
          } else {
              if ((expInfo["design"] === "4")) {
                  instructions_run1 = "Designs/design4_run1.png";
                  cond_file_run1 = "Designs/design4_run1.csv";
              }
          }
      }
  }
  if ((expInfo["position"] === "2")) {
      rand8Idx = [0, 1, 2, 3, 4, 5, 6, 7];
      shuffle(rand8Idx);
      randRows_run1 = rand8Idx.slice(0, 4);
  } else {
      if ((expInfo["position"] === "1")) {
          rand4Idx = [0, 1, 2, 3];
          shuffle(rand4Idx);
          randRows_run1 = rand4Idx.slice(0, 2);
      } else {
          if ((expInfo["position"] === "3")) {
              rand4Idx = [4, 5, 6, 7];
              shuffle(rand4Idx);
              randRows_run1 = rand4Idx.slice(0, 2);
          }
      }
  }
  
  Pinstructions_imageR1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Pinstructions_imageR1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [(0.75 * 1.5), 0.75],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -2.0 
  });
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "pracFixR1"
  pracFixR1Clock = new util.Clock();
  pTrial_run1 = 1;
  pracTotal_run1 = 4;
  pTrial_run2 = 1;
  pracTotal_run2 = 4;
  
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  fix_respP1_1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "prac_img"
  prac_imgClock = new util.Clock();
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  prac_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'prac_image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -1.0 
  });
  prac_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  prac_fix_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Feedback"
  FeedbackClock = new util.Clock();
  imFeedback = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imFeedback', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -1.0 
  });
  // Initialize components for Routine "trial_instr_run1"
  trial_instr_run1Clock = new util.Clock();
  if ((expInfo["design"] === "1")) {
      instructions_run1 = "Designs/design1_run1.png";
      cond_file_run1 = "Designs/design1_run1.csv";
  } else {
      if ((expInfo["design"] === "2")) {
          instructions_run1 = "Designs/design2_run1.png";
          cond_file_run1 = "Designs/design2_run1.csv";
      } else {
          if ((expInfo["design"] === "3")) {
              instructions_run1 = "Designs/design3_run1.png";
              cond_file_run1 = "Designs/design3_run1.csv";
          } else {
              if ((expInfo["design"] === "4")) {
                  instructions_run1 = "Designs/design4_run1.png";
                  cond_file_run1 = "Designs/design4_run1.csv";
              }
          }
      }
  }
  Trial_run1 = 1;
  Total_run1 = 96;
  Trial_run2 = 1;
  Total_run2 = 96;
  if ((expInfo["position"] === "2")) {
      positionRows = [0, 1, 2, 3, 4, 5, 6, 7];
  }
  if ((expInfo["position"] === "1")) {
      positionRows = [0, 1, 2, 3];
  }
  if ((expInfo["position"] === "3")) {
      positionRows = [4, 5, 6, 7];
  }
  
  instructions_imageR1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'instructions_imageR1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [(0.75 * 1.5), 0.75],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -1.0 
  });
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "trialFixR1"
  trialFixR1Clock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  fix_resp1_1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "trial_img"
  trial_imgClock = new util.Clock();
  text_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_6',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  trial_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial_image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -1.0 
  });
  trial_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  fix_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "prac_instr_run2"
  prac_instr_run2Clock = new util.Clock();
  if ((expInfo["design"] === "1")) {
      instructions_run2 = "Designs/design1_run2.png";
      cond_file_run2 = "Designs/design1_run2.csv";
  } else {
      if ((expInfo["design"] === "2")) {
          instructions_run2 = "Designs/design2_run2.png";
          cond_file_run2 = "Designs/design2_run2.csv";
      } else {
          if ((expInfo["design"] === "3")) {
              instructions_run2 = "Designs/design3_run2.png";
              cond_file_run2 = "Designs/design3_run2.csv";
          } else {
              if ((expInfo["design"] === "4")) {
                  instructions_run2 = "Designs/design4_run2.png";
                  cond_file_run2 = "Designs/design4_run2.csv";
              }
          }
      }
  }
  if ((expInfo["position"] === "2")) {
      rand8Idx = [0, 1, 2, 3, 4, 5, 6, 7];
      shuffle(rand8Idx);
      randRows_run2 = rand8Idx.slice(0, 4);
  } else {
      if ((expInfo["position"] === "1")) {
          rand4Idx = [0, 1, 2, 3];
          shuffle(rand4Idx);
          randRows_run2 = rand4Idx.slice(0, 2);
      } else {
          if ((expInfo["position"] === "3")) {
              rand4Idx = [4, 5, 6, 7];
              shuffle(rand4Idx);
              randRows_run2 = rand4Idx.slice(0, 2);
          }
      }
  }
  
  Pinstructions_imageR2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Pinstructions_imageR2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [(0.75 * 1.5), 0.75],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -1.0 
  });
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "pracFixR2"
  pracFixR2Clock = new util.Clock();
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  fix_respP2_1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "prac_img"
  prac_imgClock = new util.Clock();
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  prac_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'prac_image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -1.0 
  });
  prac_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  prac_fix_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Feedback"
  FeedbackClock = new util.Clock();
  imFeedback = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imFeedback', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -1.0 
  });
  // Initialize components for Routine "trial_instr_run2"
  trial_instr_run2Clock = new util.Clock();
  if ((expInfo["design"] === "1")) {
      instructions_run2 = "Designs/design1_run2.png";
      cond_file_run2 = "Designs/design1_run2.csv";
  } else {
      if ((expInfo["design"] === "2")) {
          instructions_run2 = "Designs/design2_run2.png";
          cond_file_run2 = "Designs/design2_run2.csv";
      } else {
          if ((expInfo["design"] === "3")) {
              instructions_run2 = "Designs/design3_run2.png";
              cond_file_run2 = "Designs/design3_run2.csv";
          } else {
              if ((expInfo["design"] === "4")) {
                  instructions_run2 = "Designs/design4_run2.png";
                  cond_file_run2 = "Designs/design4_run2.csv";
              }
          }
      }
  }
  
  instructions_imageR2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'instructions_imageR2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [(0.75 * 1.5), 0.75],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -1.0 
  });
  key_resp_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "trialFixR2"
  trialFixR2Clock = new util.Clock();
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  fix_resp2_1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "trial_img"
  trial_imgClock = new util.Clock();
  text_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_6',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  trial_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial_image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -1.0 
  });
  trial_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  fix_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "EndScreen"
  EndScreenClock = new util.Clock();
  allDone = new visual.TextStim({
    win: psychoJS.window,
    name: 'allDone',
    text: 'You are all done. Thank you!',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
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
    
    for (const thisComponent of screen_scaleComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
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
    for (const thisComponent of screen_scaleComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
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
    for (const thisComponent of screen_scaleComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
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
    
    for (const thisComponent of pracInstructComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
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
    for (const thisComponent of pracInstructComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
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
    for (const thisComponent of pracInstructComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
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
    Pinstructions_imageR1.setImage(instructions_run1);
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    prac_instr_run1Components = [];
    prac_instr_run1Components.push(Pinstructions_imageR1);
    prac_instr_run1Components.push(key_resp);
    
    for (const thisComponent of prac_instr_run1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
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
    
    // *Pinstructions_imageR1* updates
    if (t >= 0.0 && Pinstructions_imageR1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Pinstructions_imageR1.tStart = t;  // (not accounting for frame time here)
      Pinstructions_imageR1.frameNStart = frameN;  // exact frame index
      
      Pinstructions_imageR1.setAutoDraw(true);
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
    for (const thisComponent of prac_instr_run1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
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
    for (const thisComponent of prac_instr_run1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "prac_instr_run1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var prac_trials_run1;
var currentLoop;
function prac_trials_run1LoopBegin(prac_trials_run1LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  prac_trials_run1 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, cond_file_run1, randRows_run1),
    seed: undefined, name: 'prac_trials_run1'
  });
  psychoJS.experiment.addLoop(prac_trials_run1); // add the loop to the experiment
  currentLoop = prac_trials_run1;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisPrac_trials_run1 of prac_trials_run1) {
    const snapshot = prac_trials_run1.getSnapshot();
    prac_trials_run1LoopScheduler.add(importConditions(snapshot));
    prac_trials_run1LoopScheduler.add(pracFixR1RoutineBegin(snapshot));
    prac_trials_run1LoopScheduler.add(pracFixR1RoutineEachFrame(snapshot));
    prac_trials_run1LoopScheduler.add(pracFixR1RoutineEnd(snapshot));
    prac_trials_run1LoopScheduler.add(prac_imgRoutineBegin(snapshot));
    prac_trials_run1LoopScheduler.add(prac_imgRoutineEachFrame(snapshot));
    prac_trials_run1LoopScheduler.add(prac_imgRoutineEnd(snapshot));
    prac_trials_run1LoopScheduler.add(FeedbackRoutineBegin(snapshot));
    prac_trials_run1LoopScheduler.add(FeedbackRoutineEachFrame(snapshot));
    prac_trials_run1LoopScheduler.add(FeedbackRoutineEnd(snapshot));
    prac_trials_run1LoopScheduler.add(endLoopIteration(prac_trials_run1LoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function prac_trials_run1LoopEnd() {
  psychoJS.experiment.removeLoop(prac_trials_run1);

  return Scheduler.Event.NEXT;
}


var trials_run1;
function trials_run1LoopBegin(trials_run1LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_run1 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 12, method: TrialHandler.Method.FULLRANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, cond_file_run1, positionRows),
    seed: undefined, name: 'trials_run1'
  });
  psychoJS.experiment.addLoop(trials_run1); // add the loop to the experiment
  currentLoop = trials_run1;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrials_run1 of trials_run1) {
    const snapshot = trials_run1.getSnapshot();
    trials_run1LoopScheduler.add(importConditions(snapshot));
    trials_run1LoopScheduler.add(trialFixR1RoutineBegin(snapshot));
    trials_run1LoopScheduler.add(trialFixR1RoutineEachFrame(snapshot));
    trials_run1LoopScheduler.add(trialFixR1RoutineEnd(snapshot));
    trials_run1LoopScheduler.add(trial_imgRoutineBegin(snapshot));
    trials_run1LoopScheduler.add(trial_imgRoutineEachFrame(snapshot));
    trials_run1LoopScheduler.add(trial_imgRoutineEnd(snapshot));
    trials_run1LoopScheduler.add(endLoopIteration(trials_run1LoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function trials_run1LoopEnd() {
  psychoJS.experiment.removeLoop(trials_run1);

  return Scheduler.Event.NEXT;
}


var prac_trials_run2;
function prac_trials_run2LoopBegin(prac_trials_run2LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  prac_trials_run2 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, cond_file_run2, randRows_run2),
    seed: undefined, name: 'prac_trials_run2'
  });
  psychoJS.experiment.addLoop(prac_trials_run2); // add the loop to the experiment
  currentLoop = prac_trials_run2;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisPrac_trials_run2 of prac_trials_run2) {
    const snapshot = prac_trials_run2.getSnapshot();
    prac_trials_run2LoopScheduler.add(importConditions(snapshot));
    prac_trials_run2LoopScheduler.add(pracFixR2RoutineBegin(snapshot));
    prac_trials_run2LoopScheduler.add(pracFixR2RoutineEachFrame(snapshot));
    prac_trials_run2LoopScheduler.add(pracFixR2RoutineEnd(snapshot));
    prac_trials_run2LoopScheduler.add(prac_imgRoutineBegin(snapshot));
    prac_trials_run2LoopScheduler.add(prac_imgRoutineEachFrame(snapshot));
    prac_trials_run2LoopScheduler.add(prac_imgRoutineEnd(snapshot));
    prac_trials_run2LoopScheduler.add(FeedbackRoutineBegin(snapshot));
    prac_trials_run2LoopScheduler.add(FeedbackRoutineEachFrame(snapshot));
    prac_trials_run2LoopScheduler.add(FeedbackRoutineEnd(snapshot));
    prac_trials_run2LoopScheduler.add(endLoopIteration(prac_trials_run2LoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function prac_trials_run2LoopEnd() {
  psychoJS.experiment.removeLoop(prac_trials_run2);

  return Scheduler.Event.NEXT;
}


var trials_run2;
function trials_run2LoopBegin(trials_run2LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_run2 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 12, method: TrialHandler.Method.FULLRANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, cond_file_run2, positionRows),
    seed: undefined, name: 'trials_run2'
  });
  psychoJS.experiment.addLoop(trials_run2); // add the loop to the experiment
  currentLoop = trials_run2;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrials_run2 of trials_run2) {
    const snapshot = trials_run2.getSnapshot();
    trials_run2LoopScheduler.add(importConditions(snapshot));
    trials_run2LoopScheduler.add(trialFixR2RoutineBegin(snapshot));
    trials_run2LoopScheduler.add(trialFixR2RoutineEachFrame(snapshot));
    trials_run2LoopScheduler.add(trialFixR2RoutineEnd(snapshot));
    trials_run2LoopScheduler.add(trial_imgRoutineBegin(snapshot));
    trials_run2LoopScheduler.add(trial_imgRoutineEachFrame(snapshot));
    trials_run2LoopScheduler.add(trial_imgRoutineEnd(snapshot));
    trials_run2LoopScheduler.add(endLoopIteration(trials_run2LoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function trials_run2LoopEnd() {
  psychoJS.experiment.removeLoop(trials_run2);

  return Scheduler.Event.NEXT;
}


var trialMsg;
var currFix;
var a;
var b;
var fixDur;
var xPosition;
var _fix_respP1_1_allKeys;
var pracFixR1Components;
function pracFixR1RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'pracFixR1'-------
    t = 0;
    pracFixR1Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    trialMsg = ((("Practice: " + pTrial_run1.toString()) + " of ") + pracTotal_run1.toString());
    if (((pTrial_run1 - 1) === 0)) {
        currFix = fixColor_opts[0];
    } else {
        if ((prac1_fixColSwitch[(pTrial_run1 - 1)] === 0)) {
            currFix = currFix;
        } else {
            if ((currFix === "pink")) {
                currFix = "orange";
            } else {
                if ((currFix === "orange")) {
                    currFix = "pink";
                }
            }
        }
    }
    a = 1.25;
    b = 1.75;
    fixDur = (((b - a) * random()) + a);
    if ((expInfo["position"] === "0")) {
        xPosition = 0;
    } else {
        if ((expInfo["position"] === "2")) {
            if ((side === "left")) {
                xPosition = (- (width * x_scale));
            } else {
                if ((side === "right")) {
                    xPosition = (width * x_scale);
                }
            }
        } else {
            if ((expInfo["position"] === "1")) {
                xPosition = (- (width * x_scale));
            } else {
                if ((expInfo["position"] === "3")) {
                    xPosition = (width * x_scale);
                }
            }
        }
    }
    thisExp.addData("fixpR1", prac1_fixColSwitch[(pTrial_run1 - 1)]);
    
    text.setColor(new util.Color(currFix));
    fix_respP1_1.keys = undefined;
    fix_respP1_1.rt = undefined;
    _fix_respP1_1_allKeys = [];
    // keep track of which components have finished
    pracFixR1Components = [];
    pracFixR1Components.push(text);
    pracFixR1Components.push(fix_respP1_1);
    
    for (const thisComponent of pracFixR1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


var frameRemains;
function pracFixR1RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'pracFixR1'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = pracFixR1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    frameRemains = 0.0 + fixDur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text.setAutoDraw(false);
    }
    
    // *fix_respP1_1* updates
    if (t >= 0.0 && fix_respP1_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fix_respP1_1.tStart = t;  // (not accounting for frame time here)
      fix_respP1_1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { fix_respP1_1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { fix_respP1_1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { fix_respP1_1.clearEvents(); });
    }

    frameRemains = 0.0 + fixDur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fix_respP1_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fix_respP1_1.status = PsychoJS.Status.FINISHED;
  }

    if (fix_respP1_1.status === PsychoJS.Status.STARTED) {
      let theseKeys = fix_respP1_1.getKeys({keyList: ['space'], waitRelease: false});
      _fix_respP1_1_allKeys = _fix_respP1_1_allKeys.concat(theseKeys);
      if (_fix_respP1_1_allKeys.length > 0) {
        fix_respP1_1.keys = _fix_respP1_1_allKeys[_fix_respP1_1_allKeys.length - 1].name;  // just the last key pressed
        fix_respP1_1.rt = _fix_respP1_1_allKeys[_fix_respP1_1_allKeys.length - 1].rt;
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
    for (const thisComponent of pracFixR1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function pracFixR1RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'pracFixR1'-------
    for (const thisComponent of pracFixR1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    pTrial_run1 = (pTrial_run1 + 1);
    
    psychoJS.experiment.addData('fix_respP1_1.keys', fix_respP1_1.keys);
    if (typeof fix_respP1_1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('fix_respP1_1.rt', fix_respP1_1.rt);
        }
    
    fix_respP1_1.stop();
    // the Routine "pracFixR1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _prac_resp_allKeys;
var _prac_fix_resp_2_allKeys;
var prac_imgComponents;
function prac_imgRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'prac_img'-------
    t = 0;
    prac_imgClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    text_5.setColor(new util.Color(currFix));
    prac_image.setPos([xPosition, 0]);
    prac_image.setSize([(width * x_scale), (height * y_scale)]);
    prac_image.setImage(imFile);
    prac_resp.keys = undefined;
    prac_resp.rt = undefined;
    _prac_resp_allKeys = [];
    prac_fix_resp_2.keys = undefined;
    prac_fix_resp_2.rt = undefined;
    _prac_fix_resp_2_allKeys = [];
    // keep track of which components have finished
    prac_imgComponents = [];
    prac_imgComponents.push(text_5);
    prac_imgComponents.push(prac_image);
    prac_imgComponents.push(prac_resp);
    prac_imgComponents.push(prac_fix_resp_2);
    
    for (const thisComponent of prac_imgComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function prac_imgRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'prac_img'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = prac_imgClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_5* updates
    if (t >= 0.0 && text_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_5.tStart = t;  // (not accounting for frame time here)
      text_5.frameNStart = frameN;  // exact frame index
      
      text_5.setAutoDraw(true);
    }

    
    // *prac_image* updates
    if (t >= 0.0 && prac_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_image.tStart = t;  // (not accounting for frame time here)
      prac_image.frameNStart = frameN;  // exact frame index
      
      prac_image.setAutoDraw(true);
    }

    
    // *prac_resp* updates
    if (t >= 0.0 && prac_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_resp.tStart = t;  // (not accounting for frame time here)
      prac_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { prac_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { prac_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { prac_resp.clearEvents(); });
    }

    if (prac_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = prac_resp.getKeys({keyList: ['f', 'j'], waitRelease: false});
      _prac_resp_allKeys = _prac_resp_allKeys.concat(theseKeys);
      if (_prac_resp_allKeys.length > 0) {
        prac_resp.keys = _prac_resp_allKeys[_prac_resp_allKeys.length - 1].name;  // just the last key pressed
        prac_resp.rt = _prac_resp_allKeys[_prac_resp_allKeys.length - 1].rt;
        // was this correct?
        if (prac_resp.keys == corr) {
            prac_resp.corr = 1;
        } else {
            prac_resp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *prac_fix_resp_2* updates
    if (t >= 0.0 && prac_fix_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_fix_resp_2.tStart = t;  // (not accounting for frame time here)
      prac_fix_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { prac_fix_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { prac_fix_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { prac_fix_resp_2.clearEvents(); });
    }

    if (prac_fix_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = prac_fix_resp_2.getKeys({keyList: ['space'], waitRelease: false});
      _prac_fix_resp_2_allKeys = _prac_fix_resp_2_allKeys.concat(theseKeys);
      if (_prac_fix_resp_2_allKeys.length > 0) {
        prac_fix_resp_2.keys = _prac_fix_resp_2_allKeys[_prac_fix_resp_2_allKeys.length - 1].name;  // just the last key pressed
        prac_fix_resp_2.rt = _prac_fix_resp_2_allKeys[_prac_fix_resp_2_allKeys.length - 1].rt;
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
    for (const thisComponent of prac_imgComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function prac_imgRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'prac_img'-------
    for (const thisComponent of prac_imgComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (prac_resp.keys === undefined) {
      if (['None','none',undefined].includes(corr)) {
         prac_resp.corr = 1;  // correct non-response
      } else {
         prac_resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('prac_resp.keys', prac_resp.keys);
    psychoJS.experiment.addData('prac_resp.corr', prac_resp.corr);
    if (typeof prac_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('prac_resp.rt', prac_resp.rt);
        routineTimer.reset();
        }
    
    prac_resp.stop();
    psychoJS.experiment.addData('prac_fix_resp_2.keys', prac_fix_resp_2.keys);
    if (typeof prac_fix_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('prac_fix_resp_2.rt', prac_fix_resp_2.rt);
        }
    
    prac_fix_resp_2.stop();
    // the Routine "prac_img" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var feedIM;
var FeedbackComponents;
function FeedbackRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Feedback'-------
    t = 0;
    FeedbackClock.reset(); // clock
    frameN = -1;
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    feedIM = "";
    if ((prac_resp.keys === corr)) {
        feedIM = "Stimuli/greenCheck.png";
    } else {
        if ((prac_resp.keys !== corr)) {
            feedIM = "Stimuli/redWrong.png";
        }
    }
    
    imFeedback.setImage(feedIM);
    // keep track of which components have finished
    FeedbackComponents = [];
    FeedbackComponents.push(imFeedback);
    
    for (const thisComponent of FeedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function FeedbackRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Feedback'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = FeedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *imFeedback* updates
    if (t >= 0.0 && imFeedback.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      imFeedback.tStart = t;  // (not accounting for frame time here)
      imFeedback.frameNStart = frameN;  // exact frame index
      
      imFeedback.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imFeedback.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imFeedback.setAutoDraw(false);
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
    for (const thisComponent of FeedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function FeedbackRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Feedback'-------
    for (const thisComponent of FeedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_2_allKeys;
var trial_instr_run1Components;
function trial_instr_run1RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'trial_instr_run1'-------
    t = 0;
    trial_instr_run1Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    instructions_imageR1.setImage(instructions_run1);
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // keep track of which components have finished
    trial_instr_run1Components = [];
    trial_instr_run1Components.push(instructions_imageR1);
    trial_instr_run1Components.push(key_resp_2);
    
    for (const thisComponent of trial_instr_run1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function trial_instr_run1RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'trial_instr_run1'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = trial_instr_run1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instructions_imageR1* updates
    if (t >= 0.0 && instructions_imageR1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructions_imageR1.tStart = t;  // (not accounting for frame time here)
      instructions_imageR1.frameNStart = frameN;  // exact frame index
      
      instructions_imageR1.setAutoDraw(true);
    }

    
    // *key_resp_2* updates
    if (t >= 1 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }

    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
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
    for (const thisComponent of trial_instr_run1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trial_instr_run1RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'trial_instr_run1'-------
    for (const thisComponent of trial_instr_run1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "trial_instr_run1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _fix_resp1_1_allKeys;
var trialFixR1Components;
function trialFixR1RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'trialFixR1'-------
    t = 0;
    trialFixR1Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    if (((Trial_run1 - 1) === 0)) {
        currFix = fixColor_opts[0];
    } else {
        if ((fixColorIdx_Run1[(Trial_run1 - 1)] === 0)) {
            currFix = currFix;
        } else {
            if ((currFix === "pink")) {
                currFix = "orange";
            } else {
                if ((currFix === "orange")) {
                    currFix = "pink";
                }
            }
        }
    }
    a = 1.25;
    b = 1.75;
    fixDur = (((b - a) * random()) + a);
    if ((expInfo["position"] === "0")) {
        xPosition = 0;
    } else {
        if ((expInfo["position"] === "2")) {
            if ((side === "left")) {
                xPosition = (- (width * x_scale));
            } else {
                if ((side === "right")) {
                    xPosition = (width * x_scale);
                }
            }
        } else {
            if ((expInfo["position"] === "1")) {
                xPosition = (- (width * x_scale));
            } else {
                if ((expInfo["position"] === "3")) {
                    xPosition = (width * x_scale);
                }
            }
        }
    }
    thisExp.addData("fixR1", fixColorIdx_Run1[(Trial_run1 - 1)]);
    
    text_2.setColor(new util.Color(currFix));
    fix_resp1_1.keys = undefined;
    fix_resp1_1.rt = undefined;
    _fix_resp1_1_allKeys = [];
    // keep track of which components have finished
    trialFixR1Components = [];
    trialFixR1Components.push(text_2);
    trialFixR1Components.push(fix_resp1_1);
    
    for (const thisComponent of trialFixR1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function trialFixR1RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'trialFixR1'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = trialFixR1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + fixDur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_2.setAutoDraw(false);
    }
    
    // *fix_resp1_1* updates
    if (t >= 0.0 && fix_resp1_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fix_resp1_1.tStart = t;  // (not accounting for frame time here)
      fix_resp1_1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { fix_resp1_1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { fix_resp1_1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { fix_resp1_1.clearEvents(); });
    }

    frameRemains = 0.0 + fixDur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fix_resp1_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fix_resp1_1.status = PsychoJS.Status.FINISHED;
  }

    if (fix_resp1_1.status === PsychoJS.Status.STARTED) {
      let theseKeys = fix_resp1_1.getKeys({keyList: ['space'], waitRelease: false});
      _fix_resp1_1_allKeys = _fix_resp1_1_allKeys.concat(theseKeys);
      if (_fix_resp1_1_allKeys.length > 0) {
        fix_resp1_1.keys = _fix_resp1_1_allKeys[_fix_resp1_1_allKeys.length - 1].name;  // just the last key pressed
        fix_resp1_1.rt = _fix_resp1_1_allKeys[_fix_resp1_1_allKeys.length - 1].rt;
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
    for (const thisComponent of trialFixR1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trialFixR1RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'trialFixR1'-------
    for (const thisComponent of trialFixR1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    Trial_run1 = (Trial_run1 + 1);
    
    psychoJS.experiment.addData('fix_resp1_1.keys', fix_resp1_1.keys);
    if (typeof fix_resp1_1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('fix_resp1_1.rt', fix_resp1_1.rt);
        }
    
    fix_resp1_1.stop();
    // the Routine "trialFixR1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _trial_resp_allKeys;
var _fix_resp_2_allKeys;
var trial_imgComponents;
function trial_imgRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'trial_img'-------
    t = 0;
    trial_imgClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    text_6.setColor(new util.Color(currFix));
    trial_image.setPos([xPosition, 0]);
    trial_image.setSize([(width * x_scale), (height * y_scale)]);
    trial_image.setImage(imFile);
    trial_resp.keys = undefined;
    trial_resp.rt = undefined;
    _trial_resp_allKeys = [];
    fix_resp_2.keys = undefined;
    fix_resp_2.rt = undefined;
    _fix_resp_2_allKeys = [];
    // keep track of which components have finished
    trial_imgComponents = [];
    trial_imgComponents.push(text_6);
    trial_imgComponents.push(trial_image);
    trial_imgComponents.push(trial_resp);
    trial_imgComponents.push(fix_resp_2);
    
    for (const thisComponent of trial_imgComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function trial_imgRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'trial_img'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = trial_imgClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_6* updates
    if (t >= 0.0 && text_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_6.tStart = t;  // (not accounting for frame time here)
      text_6.frameNStart = frameN;  // exact frame index
      
      text_6.setAutoDraw(true);
    }

    
    // *trial_image* updates
    if (t >= 0.0 && trial_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial_image.tStart = t;  // (not accounting for frame time here)
      trial_image.frameNStart = frameN;  // exact frame index
      
      trial_image.setAutoDraw(true);
    }

    
    // *trial_resp* updates
    if (t >= 0.0 && trial_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial_resp.tStart = t;  // (not accounting for frame time here)
      trial_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { trial_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { trial_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { trial_resp.clearEvents(); });
    }

    if (trial_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = trial_resp.getKeys({keyList: ['f', 'j'], waitRelease: false});
      _trial_resp_allKeys = _trial_resp_allKeys.concat(theseKeys);
      if (_trial_resp_allKeys.length > 0) {
        trial_resp.keys = _trial_resp_allKeys[_trial_resp_allKeys.length - 1].name;  // just the last key pressed
        trial_resp.rt = _trial_resp_allKeys[_trial_resp_allKeys.length - 1].rt;
        // was this correct?
        if (trial_resp.keys == corr) {
            trial_resp.corr = 1;
        } else {
            trial_resp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *fix_resp_2* updates
    if (t >= 0.0 && fix_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fix_resp_2.tStart = t;  // (not accounting for frame time here)
      fix_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { fix_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { fix_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { fix_resp_2.clearEvents(); });
    }

    if (fix_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = fix_resp_2.getKeys({keyList: ['space'], waitRelease: false});
      _fix_resp_2_allKeys = _fix_resp_2_allKeys.concat(theseKeys);
      if (_fix_resp_2_allKeys.length > 0) {
        fix_resp_2.keys = _fix_resp_2_allKeys[_fix_resp_2_allKeys.length - 1].name;  // just the last key pressed
        fix_resp_2.rt = _fix_resp_2_allKeys[_fix_resp_2_allKeys.length - 1].rt;
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
    for (const thisComponent of trial_imgComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trial_imgRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'trial_img'-------
    for (const thisComponent of trial_imgComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (trial_resp.keys === undefined) {
      if (['None','none',undefined].includes(corr)) {
         trial_resp.corr = 1;  // correct non-response
      } else {
         trial_resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('trial_resp.keys', trial_resp.keys);
    psychoJS.experiment.addData('trial_resp.corr', trial_resp.corr);
    if (typeof trial_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('trial_resp.rt', trial_resp.rt);
        routineTimer.reset();
        }
    
    trial_resp.stop();
    psychoJS.experiment.addData('fix_resp_2.keys', fix_resp_2.keys);
    if (typeof fix_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('fix_resp_2.rt', fix_resp_2.rt);
        }
    
    fix_resp_2.stop();
    // the Routine "trial_img" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_3_allKeys;
var prac_instr_run2Components;
function prac_instr_run2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'prac_instr_run2'-------
    t = 0;
    prac_instr_run2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    Pinstructions_imageR2.setImage(instructions_run2);
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    // keep track of which components have finished
    prac_instr_run2Components = [];
    prac_instr_run2Components.push(Pinstructions_imageR2);
    prac_instr_run2Components.push(key_resp_3);
    
    for (const thisComponent of prac_instr_run2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function prac_instr_run2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'prac_instr_run2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = prac_instr_run2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Pinstructions_imageR2* updates
    if (t >= 0.0 && Pinstructions_imageR2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Pinstructions_imageR2.tStart = t;  // (not accounting for frame time here)
      Pinstructions_imageR2.frameNStart = frameN;  // exact frame index
      
      Pinstructions_imageR2.setAutoDraw(true);
    }

    
    // *key_resp_3* updates
    if (t >= 1 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
    }

    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
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
    for (const thisComponent of prac_instr_run2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function prac_instr_run2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'prac_instr_run2'-------
    for (const thisComponent of prac_instr_run2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "prac_instr_run2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _fix_respP2_1_allKeys;
var pracFixR2Components;
function pracFixR2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'pracFixR2'-------
    t = 0;
    pracFixR2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    trialMsg = ((("Practice: " + pTrial_run2.toString()) + " of ") + pracTotal_run2.toString());
    if (((pTrial_run2 - 1) === 0)) {
        currFix = fixColor_opts[0];
    } else {
        if ((prac2_fixColSwitch[(pTrial_run2 - 1)] === 0)) {
            currFix = currFix;
        } else {
            if ((currFix === "pink")) {
                currFix = "orange";
            } else {
                if ((currFix === "orange")) {
                    currFix = "pink";
                }
            }
        }
    }
    a = 1.25;
    b = 1.75;
    fixDur = (((b - a) * random()) + a);
    if ((expInfo["position"] === "0")) {
        xPosition = 0;
    } else {
        if ((expInfo["position"] === "2")) {
            if ((side === "left")) {
                xPosition = (- (width * x_scale));
            } else {
                if ((side === "right")) {
                    xPosition = (width * x_scale);
                }
            }
        } else {
            if ((expInfo["position"] === "1")) {
                xPosition = (- (width * x_scale));
            } else {
                if ((expInfo["position"] === "3")) {
                    xPosition = (width * x_scale);
                }
            }
        }
    }
    thisExp.addData("fixpR2", prac2_fixColSwitch[(pTrial_run2 - 1)]);
    
    text_3.setColor(new util.Color(currFix));
    fix_respP2_1.keys = undefined;
    fix_respP2_1.rt = undefined;
    _fix_respP2_1_allKeys = [];
    // keep track of which components have finished
    pracFixR2Components = [];
    pracFixR2Components.push(text_3);
    pracFixR2Components.push(fix_respP2_1);
    
    for (const thisComponent of pracFixR2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function pracFixR2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'pracFixR2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = pracFixR2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_3* updates
    if (t >= 0.0 && text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_3.tStart = t;  // (not accounting for frame time here)
      text_3.frameNStart = frameN;  // exact frame index
      
      text_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + fixDur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_3.setAutoDraw(false);
    }
    
    // *fix_respP2_1* updates
    if (t >= 0.0 && fix_respP2_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fix_respP2_1.tStart = t;  // (not accounting for frame time here)
      fix_respP2_1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { fix_respP2_1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { fix_respP2_1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { fix_respP2_1.clearEvents(); });
    }

    frameRemains = 0.0 + fixDur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fix_respP2_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fix_respP2_1.status = PsychoJS.Status.FINISHED;
  }

    if (fix_respP2_1.status === PsychoJS.Status.STARTED) {
      let theseKeys = fix_respP2_1.getKeys({keyList: ['space'], waitRelease: false});
      _fix_respP2_1_allKeys = _fix_respP2_1_allKeys.concat(theseKeys);
      if (_fix_respP2_1_allKeys.length > 0) {
        fix_respP2_1.keys = _fix_respP2_1_allKeys[_fix_respP2_1_allKeys.length - 1].name;  // just the last key pressed
        fix_respP2_1.rt = _fix_respP2_1_allKeys[_fix_respP2_1_allKeys.length - 1].rt;
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
    for (const thisComponent of pracFixR2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function pracFixR2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'pracFixR2'-------
    for (const thisComponent of pracFixR2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    pTrial_run2 = (pTrial_run2 + 1);
    
    psychoJS.experiment.addData('fix_respP2_1.keys', fix_respP2_1.keys);
    if (typeof fix_respP2_1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('fix_respP2_1.rt', fix_respP2_1.rt);
        }
    
    fix_respP2_1.stop();
    // the Routine "pracFixR2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_4_allKeys;
var trial_instr_run2Components;
function trial_instr_run2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'trial_instr_run2'-------
    t = 0;
    trial_instr_run2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    instructions_imageR2.setImage(instructions_run2);
    key_resp_4.keys = undefined;
    key_resp_4.rt = undefined;
    _key_resp_4_allKeys = [];
    // keep track of which components have finished
    trial_instr_run2Components = [];
    trial_instr_run2Components.push(instructions_imageR2);
    trial_instr_run2Components.push(key_resp_4);
    
    for (const thisComponent of trial_instr_run2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function trial_instr_run2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'trial_instr_run2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = trial_instr_run2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instructions_imageR2* updates
    if (t >= 0.0 && instructions_imageR2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructions_imageR2.tStart = t;  // (not accounting for frame time here)
      instructions_imageR2.frameNStart = frameN;  // exact frame index
      
      instructions_imageR2.setAutoDraw(true);
    }

    
    // *key_resp_4* updates
    if (t >= 1 && key_resp_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_4.tStart = t;  // (not accounting for frame time here)
      key_resp_4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.clearEvents(); });
    }

    if (key_resp_4.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_4.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_4_allKeys = _key_resp_4_allKeys.concat(theseKeys);
      if (_key_resp_4_allKeys.length > 0) {
        key_resp_4.keys = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].name;  // just the last key pressed
        key_resp_4.rt = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].rt;
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
    for (const thisComponent of trial_instr_run2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trial_instr_run2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'trial_instr_run2'-------
    for (const thisComponent of trial_instr_run2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "trial_instr_run2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _fix_resp2_1_allKeys;
var trialFixR2Components;
function trialFixR2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'trialFixR2'-------
    t = 0;
    trialFixR2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    if (((Trial_run2 - 1) === 0)) {
        currFix = fixColor_opts[0];
    } else {
        if ((fixColorIdx_Run2[(Trial_run2 - 1)] === 0)) {
            currFix = currFix;
        } else {
            if ((currFix === "pink")) {
                currFix = "orange";
            } else {
                if ((currFix === "orange")) {
                    currFix = "pink";
                }
            }
        }
    }
    a = 1.25;
    b = 1.75;
    fixDur = (((b - a) * random()) + a);
    if ((expInfo["position"] === "0")) {
        xPosition = 0;
    } else {
        if ((expInfo["position"] === "2")) {
            if ((side === "left")) {
                xPosition = (- (width * x_scale));
            } else {
                if ((side === "right")) {
                    xPosition = (width * x_scale);
                }
            }
        } else {
            if ((expInfo["position"] === "1")) {
                xPosition = (- (width * x_scale));
            } else {
                if ((expInfo["position"] === "3")) {
                    xPosition = (width * x_scale);
                }
            }
        }
    }
    thisExp.addData("fixR2", fixColorIdx_Run2[(Trial_run2 - 1)]);
    
    text_4.setColor(new util.Color(currFix));
    fix_resp2_1.keys = undefined;
    fix_resp2_1.rt = undefined;
    _fix_resp2_1_allKeys = [];
    // keep track of which components have finished
    trialFixR2Components = [];
    trialFixR2Components.push(text_4);
    trialFixR2Components.push(fix_resp2_1);
    
    for (const thisComponent of trialFixR2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function trialFixR2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'trialFixR2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = trialFixR2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_4* updates
    if (t >= 0.0 && text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_4.tStart = t;  // (not accounting for frame time here)
      text_4.frameNStart = frameN;  // exact frame index
      
      text_4.setAutoDraw(true);
    }

    frameRemains = 0.0 + fixDur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_4.setAutoDraw(false);
    }
    
    // *fix_resp2_1* updates
    if (t >= 0.0 && fix_resp2_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fix_resp2_1.tStart = t;  // (not accounting for frame time here)
      fix_resp2_1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { fix_resp2_1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { fix_resp2_1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { fix_resp2_1.clearEvents(); });
    }

    frameRemains = 0.0 + fixDur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fix_resp2_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fix_resp2_1.status = PsychoJS.Status.FINISHED;
  }

    if (fix_resp2_1.status === PsychoJS.Status.STARTED) {
      let theseKeys = fix_resp2_1.getKeys({keyList: ['space'], waitRelease: false});
      _fix_resp2_1_allKeys = _fix_resp2_1_allKeys.concat(theseKeys);
      if (_fix_resp2_1_allKeys.length > 0) {
        fix_resp2_1.keys = _fix_resp2_1_allKeys[_fix_resp2_1_allKeys.length - 1].name;  // just the last key pressed
        fix_resp2_1.rt = _fix_resp2_1_allKeys[_fix_resp2_1_allKeys.length - 1].rt;
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
    for (const thisComponent of trialFixR2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trialFixR2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'trialFixR2'-------
    for (const thisComponent of trialFixR2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    Trial_run2 = (Trial_run2 + 1);
    
    psychoJS.experiment.addData('fix_resp2_1.keys', fix_resp2_1.keys);
    if (typeof fix_resp2_1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('fix_resp2_1.rt', fix_resp2_1.rt);
        }
    
    fix_resp2_1.stop();
    // the Routine "trialFixR2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var EndScreenComponents;
function EndScreenRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'EndScreen'-------
    t = 0;
    EndScreenClock.reset(); // clock
    frameN = -1;
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    EndScreenComponents = [];
    EndScreenComponents.push(allDone);
    
    for (const thisComponent of EndScreenComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function EndScreenRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'EndScreen'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = EndScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *allDone* updates
    if (t >= 0.0 && allDone.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      allDone.tStart = t;  // (not accounting for frame time here)
      allDone.frameNStart = frameN;  // exact frame index
      
      allDone.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (allDone.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      allDone.setAutoDraw(false);
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
    for (const thisComponent of EndScreenComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function EndScreenRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'EndScreen'-------
    for (const thisComponent of EndScreenComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
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
