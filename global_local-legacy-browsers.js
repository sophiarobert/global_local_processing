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
flowScheduler.add(pracInstruct2RoutineBegin());
flowScheduler.add(pracInstruct2RoutineEachFrame());
flowScheduler.add(pracInstruct2RoutineEnd());
flowScheduler.add(pracInstruct3RoutineBegin());
flowScheduler.add(pracInstruct3RoutineEachFrame());
flowScheduler.add(pracInstruct3RoutineEnd());
flowScheduler.add(hand_hold_instrRoutineBegin());
flowScheduler.add(hand_hold_instrRoutineEachFrame());
flowScheduler.add(hand_hold_instrRoutineEnd());
flowScheduler.add(hand_hold_trialRoutineBegin());
flowScheduler.add(hand_hold_trialRoutineEachFrame());
flowScheduler.add(hand_hold_trialRoutineEnd());
flowScheduler.add(hand_hold_feedbackRoutineBegin());
flowScheduler.add(hand_hold_feedbackRoutineEachFrame());
flowScheduler.add(hand_hold_feedbackRoutineEnd());
flowScheduler.add(prac_instr_run1RoutineBegin());
flowScheduler.add(prac_instr_run1RoutineEachFrame());
flowScheduler.add(prac_instr_run1RoutineEnd());
const repeatsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(repeatsLoopBegin, repeatsLoopScheduler);
flowScheduler.add(repeatsLoopScheduler);
flowScheduler.add(repeatsLoopEnd);
flowScheduler.add(trial_instr_run1RoutineBegin());
flowScheduler.add(trial_instr_run1RoutineEachFrame());
flowScheduler.add(trial_instr_run1RoutineEnd());
const trials_run1LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_run1LoopBegin, trials_run1LoopScheduler);
flowScheduler.add(trials_run1LoopScheduler);
flowScheduler.add(trials_run1LoopEnd);
flowScheduler.add(btwn_trial_GJRoutineBegin());
flowScheduler.add(btwn_trial_GJRoutineEachFrame());
flowScheduler.add(btwn_trial_GJRoutineEnd());
flowScheduler.add(hand_hold_instrRoutineBegin());
flowScheduler.add(hand_hold_instrRoutineEachFrame());
flowScheduler.add(hand_hold_instrRoutineEnd());
flowScheduler.add(hand_hold_trialRoutineBegin());
flowScheduler.add(hand_hold_trialRoutineEachFrame());
flowScheduler.add(hand_hold_trialRoutineEnd());
flowScheduler.add(hand_hold_feedbackRoutineBegin());
flowScheduler.add(hand_hold_feedbackRoutineEachFrame());
flowScheduler.add(hand_hold_feedbackRoutineEnd());
flowScheduler.add(prac_instr_run2RoutineBegin());
flowScheduler.add(prac_instr_run2RoutineEachFrame());
flowScheduler.add(prac_instr_run2RoutineEnd());
const repeats2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(repeats2LoopBegin, repeats2LoopScheduler);
flowScheduler.add(repeats2LoopScheduler);
flowScheduler.add(repeats2LoopEnd);
flowScheduler.add(trial_instr_run2RoutineBegin());
flowScheduler.add(trial_instr_run2RoutineEachFrame());
flowScheduler.add(trial_instr_run2RoutineEnd());
const trials_run2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_run2LoopBegin, trials_run2LoopScheduler);
flowScheduler.add(trials_run2LoopScheduler);
flowScheduler.add(trials_run2LoopEnd);
flowScheduler.add(btwn_trial_GJRoutineBegin());
flowScheduler.add(btwn_trial_GJRoutineEachFrame());
flowScheduler.add(btwn_trial_GJRoutineEnd());
flowScheduler.add(trial_instr_run1RoutineBegin());
flowScheduler.add(trial_instr_run1RoutineEachFrame());
flowScheduler.add(trial_instr_run1RoutineEnd());
const trials_run3LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_run3LoopBegin, trials_run3LoopScheduler);
flowScheduler.add(trials_run3LoopScheduler);
flowScheduler.add(trials_run3LoopEnd);
flowScheduler.add(btwn_trial_GJRoutineBegin());
flowScheduler.add(btwn_trial_GJRoutineEachFrame());
flowScheduler.add(btwn_trial_GJRoutineEnd());
flowScheduler.add(trial_instr_run2RoutineBegin());
flowScheduler.add(trial_instr_run2RoutineEachFrame());
flowScheduler.add(trial_instr_run2RoutineEnd());
const trials_run4LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_run4LoopBegin, trials_run4LoopScheduler);
flowScheduler.add(trials_run4LoopScheduler);
flowScheduler.add(trials_run4LoopEnd);
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
    {'name': 'Designs/prac_instr3.png', 'path': 'Designs/prac_instr3.png'},
    {'name': 'Designs/prac_instr1.png', 'path': 'Designs/prac_instr1.png'},
    {'name': 'bankcard.png', 'path': 'bankcard.png'},
    {'name': 'Designs/baby_dory_GJ.png', 'path': 'Designs/baby_dory_GJ.png'},
    {'name': 'Designs/prac_instr2.png', 'path': 'Designs/prac_instr2.png'},
    {'name': 'Designs/baby_squirt_GJ.png', 'path': 'Designs/baby_squirt_GJ.png'}
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
var width3deg;
var width4deg;
var text_top;
var text_bottom;
var ccimage;
var pracInstructClock;
var fixColor_opts;
var pfS1;
var prac1_fixColSwitch;
var pfS2;
var prac2_fixColSwitch;
var fixColorIdx_Run1;
var fixColorIdx_Run2;
var prac_instr1;
var start_exp_press;
var pracInstruct2Clock;
var prac_instr2;
var key_resp_6;
var pracInstruct3Clock;
var prac_instr3;
var key_resp_7;
var hand_hold_instrClock;
var hand_hold_ex1;
var handHoldCorr1;
var hold_hand_R1_img;
var hand_hold_ex2;
var handHoldCorr2;
var hold_hand_R2_img;
var hand_hold_feedback1corr;
var hand_hold_feedback1incorr;
var hand_hold_feedback2corr;
var hand_hold_feedback2incorr;
var image_2;
var key_resp_9;
var hand_hold_trialClock;
var text_8;
var image;
var hand_hold_resp;
var hand_hold_feedbackClock;
var image_3;
var key_resp_8;
var prac_instr_run1Clock;
var instructions_run1;
var cond_file_run1;
var Pinstructions_imageR1;
var key_resp;
var startPracClock;
var pracFixR1Clock;
var text;
var prac_imgClock;
var text_5;
var prac_image;
var prac_resp;
var prac_fix_resp;
var FeedbackClock;
var imFeedback;
var feedback_msg;
var checkPrac1Clock;
var text_7;
var key_resp_5;
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
var btwn_trial_GJClock;
var text_10;
var image_4;
var prac_instr_run2Clock;
var instructions_run2;
var cond_file_run2;
var Pinstructions_imageR2;
var key_resp_3;
var pracFixR2Clock;
var text_3;
var fix_respP2_1;
var checkPrac2Clock;
var text_9;
var key_resp_10;
var trial_instr_run2Clock;
var instructions_imageR2;
var key_resp_4;
var trialFixR2Clock;
var text_4;
var fix_resp2_1;
var EndScreenClock;
var image_5;
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
  {name: ("Stimuli/HofH2.jpg"), path:("Stimuli/HofH2.jpg")},
  {name: ("Stimuli/HofS2.jpg"), path:("Stimuli/HofS2.jpg")},
  {name: ("Stimuli/SofH2.jpg"), path:("Stimuli/SofH2.jpg")},
  {name: ("Stimuli/SofS2.jpg"), path:("Stimuli/SofS2.jpg")},
  {name: ("Designs/design1_run1.png"), path:("Designs/design1_run1.png")},
  {name: ("Designs/design2_run1.png"), path:("Designs/design2_run1.png")},
  {name: ("Designs/design3_run1.png"), path:("Designs/design3_run1.png")},
  {name: ("Designs/design4_run1.png"), path:("Designs/design4_run1.png")},
  {name: ("Designs/design1_run2.png"), path:("Designs/design1_run2.png")},
  {name: ("Designs/design2_run2.png"), path:("Designs/design2_run2.png")},
  {name: ("Designs/design3_run2.png"), path:("Designs/design3_run2.png")},
  {name: ("Designs/design4_run2.png"), path:("Designs/design4_run2.png")},
  {name: ("Designs/design1_run1_ex.png"), path:("Designs/design1_run1_ex.png")},
  {name: ("Designs/design2_run1_ex.png"), path:("Designs/design2_run1_ex.png")},
  {name: ("Designs/design3_run1_ex.png"), path:("Designs/design3_run1_ex.png")},
  {name: ("Designs/design4_run1_ex.png"), path:("Designs/design4_run1_ex.png")},
  {name: ("Designs/design1_run2_ex.png"), path:("Designs/design1_run2_ex.png")},
  {name: ("Designs/design2_run2_ex.png"), path:("Designs/design2_run2_ex.png")},
  {name: ("Designs/design3_run2_ex.png"), path:("Designs/design3_run2_ex.png")},
  {name: ("Designs/design4_run2_ex.png"), path:("Designs/design4_run2_ex.png")},
  {name: ("Designs/design1_run1.csv"), path:("Designs/design1_run1.csv")},
  {name: ("Designs/design2_run1.csv"), path:("Designs/design2_run1.csv")},
  {name: ("Designs/design3_run1.csv"), path:("Designs/design3_run1.csv")},
  {name: ("Designs/design4_run1.csv"), path:("Designs/design4_run1.csv")},
  {name: ("Designs/design1_run2.csv"), path:("Designs/design1_run2.csv")},
  {name: ("Designs/design2_run2.csv"), path:("Designs/design2_run2.csv")},
  {name: ("Designs/design3_run2.csv"), path:("Designs/design3_run2.csv")},
  {name: ("Designs/design4_run2.csv"), path:("Designs/design4_run2.csv")},
  {name: ("Designs/hand_hold_global_corr.png"), path:("Designs/hand_hold_global_corr.png")},
  {name: ("Designs/hand_hold_global_incorr.png"), path:("Designs/hand_hold_global_incorr.png")},
  {name: ("Designs/hand_hold_local_corr.png"), path:("Designs/hand_hold_local_corr.png")},
  {name: ("Designs/hand_hold_local_incorr.png"), path:("Designs/hand_hold_local_incorr.png")}]);
  
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
  height = (1.7296 * 2);
  width = (1.7296 * 2);
  width3deg = 3.47618705978;
  width4deg = 3.47618705978;
  
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
  function shuffle_array(array) {
      for (let i = array.length - 1; i > 0; i--) {
          let j = Math.floor(Math.random() * (i + 1)); // random index from 0 to i
  
              // swap elements array[i] and array[j]
              // we use "destructuring assignment" syntax to achieve that
              // you'll find more details about that syntax in later chapters
              // same can be written as:
              // let t = array[i]; array[i] = array[j]; array[j] = t
          [array[i], array[j]] = [array[j], array[i]];
      }
      return array
  }
  fixColor_opts = shuffle_array(["black", "white"]);
  pfS1 = [0, 1, 0, 1];
  prac1_fixColSwitch = [0, shuffle_array(pfS1), 0].flat();
  pfS2 = [0, 1, 0, 1];
  prac2_fixColSwitch = [0, shuffle_array(pfS2), 0].flat();
  console.log(prac2_fixColSwitch)
  if ((Number.parseInt(expInfo["position"]) === 2)) {
      fixColorIdx_Run1 = [shuffle_array([1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1]), shuffle_array([1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1])].flat();
      fixColorIdx_Run2 = [shuffle_array([1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1]), shuffle_array([1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1])].flat();
  } else {
      fixColorIdx_Run1 = [shuffle_array([1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]), shuffle_array([1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0])].flat();
      fixColorIdx_Run2 = [shuffle_array([1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]), shuffle_array([1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0])].flat();
  }
  
  prac_instr1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'prac_instr1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [(0.75 * 1.77), 0.75],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -1.0 
  });
  start_exp_press = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "pracInstruct2"
  pracInstruct2Clock = new util.Clock();
  prac_instr2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'prac_instr2', units : undefined, 
    image : 'Designs/prac_instr2.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [(0.75 * 1.77), 0.75],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : 0.0 
  });
  key_resp_6 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "pracInstruct3"
  pracInstruct3Clock = new util.Clock();
  prac_instr3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'prac_instr3', units : undefined, 
    image : 'Designs/prac_instr3.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [(0.75 * 1.77), 0.75],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : 0.0 
  });
  key_resp_7 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "hand_hold_instr"
  hand_hold_instrClock = new util.Clock();
  if ((expInfo["design"] === "1")) {
      hand_hold_ex1 = "Designs/design1_run1_ex.png";
      handHoldCorr1 = "j";
      hold_hand_R1_img = "Stimuli/HofS2.jpg";
      hand_hold_ex2 = "Designs/design1_run2_ex.png";
      handHoldCorr2 = "j";
      hold_hand_R2_img = "Stimuli/SofH2.jpg";
      hand_hold_feedback1corr = "Designs/hand_hold_local_corr.png";
      hand_hold_feedback1incorr = "Designs/hand_hold_local_incorr.png";
      hand_hold_feedback2corr = "Designs/hand_hold_global_corr.png";
      hand_hold_feedback2incorr = "Designs/hand_hold_global_incorr.png";
  } else {
      if ((expInfo["design"] === "2")) {
          hand_hold_ex1 = "Designs/design2_run1_ex.png";
          handHoldCorr1 = "j";
          hold_hand_R1_img = "Stimuli/SofH2.jpg";
          hand_hold_ex2 = "Designs/design2_run2_ex.png";
          handHoldCorr2 = "j";
          hold_hand_R2_img = "Stimuli/HofS2.jpg";
          hand_hold_feedback1corr = "Designs/hand_hold_global_corr.png";
          hand_hold_feedback1incorr = "Designs/hand_hold_global_incorr.png";
          hand_hold_feedback2corr = "Designs/hand_hold_local_corr.png";
          hand_hold_feedback2incorr = "Designs/hand_hold_local_incorr.png";
      } else {
          if ((expInfo["design"] === "3")) {
              hand_hold_ex1 = "Designs/design3_run1_ex.png";
              handHoldCorr1 = "f";
              hold_hand_R1_img = "Stimuli/SofH2.jpg";
              hand_hold_ex2 = "Designs/design3_run2_ex.png";
              handHoldCorr2 = "f";
              hold_hand_R2_img = "Stimuli/HofS2.jpg";
              hand_hold_feedback1corr = "Designs/hand_hold_global_corr.png";
              hand_hold_feedback1incorr = "Designs/hand_hold_global_incorr.png";
              hand_hold_feedback2corr = "Designs/hand_hold_local_corr.png";
              hand_hold_feedback2incorr = "Designs/hand_hold_local_incorr.png";
          } else {
              if ((expInfo["design"] === "4")) {
                  hand_hold_ex1 = "Designs/design4_run1_ex.png";
                  handHoldCorr1 = "f";
                  hold_hand_R1_img = "Stimuli/HofS2.jpg";
                  hand_hold_ex2 = "Designs/design4_run2_ex.png";
                  handHoldCorr2 = "f";
                  hold_hand_R2_img = "Stimuli/SofH2.jpg";
                  hand_hold_feedback1corr = "Designs/hand_hold_local_corr.png";
                  hand_hold_feedback1incorr = "Designs/hand_hold_local_incorr.png";
                  hand_hold_feedback2corr = "Designs/hand_hold_global_corr.png";
                  hand_hold_feedback2incorr = "Designs/hand_hold_global_incorr.png";
              }
          }
      }
  }
  
  image_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [(0.75 * 1.77), 0.75],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -1.0 
  });
  key_resp_9 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "hand_hold_trial"
  hand_hold_trialClock = new util.Clock();
  text_8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_8',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -1.0 
  });
  hand_hold_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "hand_hold_feedback"
  hand_hold_feedbackClock = new util.Clock();
  image_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_3', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [(0.75 * 1.77), 0.75],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -1.0 
  });
  key_resp_8 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "prac_instr_run1"
  prac_instr_run1Clock = new util.Clock();
  if ((Number.parseInt(expInfo["design"]) === 1)) {
      instructions_run1 = "Designs/design1_run1.png";
      cond_file_run1 = "Designs/design1_run1.csv";
  } else {
      if ((Number.parseInt(expInfo["design"]) === 2)) {
          instructions_run1 = "Designs/design2_run1.png";
          cond_file_run1 = "Designs/design2_run1.csv";
      } else {
          if ((Number.parseInt(expInfo["design"]) === 3)) {
              instructions_run1 = "Designs/design3_run1.png";
              cond_file_run1 = "Designs/design3_run1.csv";
          } else {
              if ((Number.parseInt(expInfo["design"]) === 4)) {
                  instructions_run1 = "Designs/design4_run1.png";
                  cond_file_run1 = "Designs/design4_run1.csv";
              }
          }
      }
  }
  
  Pinstructions_imageR1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Pinstructions_imageR1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [(0.75 * 1.75), 0.75],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -1.0 
  });
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "startPrac"
  startPracClock = new util.Clock();
  // Initialize components for Routine "pracFixR1"
  pracFixR1Clock = new util.Clock();
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
  
  prac_fix_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Feedback"
  FeedbackClock = new util.Clock();
  imFeedback = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imFeedback', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -1.0 
  });
  feedback_msg = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_msg',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.25)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "checkPrac1"
  checkPrac1Clock = new util.Clock();
  text_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_7',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "trial_instr_run1"
  trial_instr_run1Clock = new util.Clock();
  if ((Number.parseInt(expInfo["design"]) === 1)) {
      instructions_run1 = "Designs/design1_run1.png";
      cond_file_run1 = "Designs/design1_run1.csv";
  } else {
      if ((Number.parseInt(expInfo["design"]) === 2)) {
          instructions_run1 = "Designs/design2_run1.png";
          cond_file_run1 = "Designs/design2_run1.csv";
      } else {
          if ((Number.parseInt(expInfo["design"]) === 3)) {
              instructions_run1 = "Designs/design3_run1.png";
              cond_file_run1 = "Designs/design3_run1.csv";
          } else {
              if ((Number.parseInt(expInfo["design"]) === 4)) {
                  instructions_run1 = "Designs/design4_run1.png";
                  cond_file_run1 = "Designs/design4_run1.csv";
              }
          }
      }
  }
  if ((Number.parseInt(expInfo["position"]) === 2)) {
      Trial_run1 = 1;
      Total_run1 = 96;
      Trial_run2 = 1;
      Total_run2 = 96;
      positionRows = [0, 1, 2, 3, 4, 5, 6, 7];
  } else {
      if ((Number.parseInt(expInfo["position"]) === 1)) {
          Trial_run1 = 1;
          Total_run1 = (96 / 2);
          Trial_run2 = 1;
          Total_run2 = (96 / 2);
          positionRows = [0, 1, 2, 3];
      } else {
          if ((Number.parseInt(expInfo["position"]) === 3)) {
              Trial_run1 = 1;
              Total_run1 = (96 / 2);
              Trial_run2 = 1;
              Total_run2 = (96 / 2);
              positionRows = [4, 5, 6, 7];
          }
      }
  }
  
  instructions_imageR1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'instructions_imageR1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [(0.75 * 1.77), 0.75],
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
  
  // Initialize components for Routine "btwn_trial_GJ"
  btwn_trial_GJClock = new util.Clock();
  text_10 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_10',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  image_4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_4', units : undefined, 
    image : 'Designs/baby_dory_GJ.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.4, (0.4 * 1.83)],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "hand_hold_instr"
  hand_hold_instrClock = new util.Clock();
  if ((expInfo["design"] === "1")) {
      hand_hold_ex1 = "Designs/design1_run1_ex.png";
      handHoldCorr1 = "j";
      hold_hand_R1_img = "Stimuli/HofS2.jpg";
      hand_hold_ex2 = "Designs/design1_run2_ex.png";
      handHoldCorr2 = "j";
      hold_hand_R2_img = "Stimuli/SofH2.jpg";
      hand_hold_feedback1corr = "Designs/hand_hold_local_corr.png";
      hand_hold_feedback1incorr = "Designs/hand_hold_local_incorr.png";
      hand_hold_feedback2corr = "Designs/hand_hold_global_corr.png";
      hand_hold_feedback2incorr = "Designs/hand_hold_global_incorr.png";
  } else {
      if ((expInfo["design"] === "2")) {
          hand_hold_ex1 = "Designs/design2_run1_ex.png";
          handHoldCorr1 = "j";
          hold_hand_R1_img = "Stimuli/SofH2.jpg";
          hand_hold_ex2 = "Designs/design2_run2_ex.png";
          handHoldCorr2 = "j";
          hold_hand_R2_img = "Stimuli/HofS2.jpg";
          hand_hold_feedback1corr = "Designs/hand_hold_global_corr.png";
          hand_hold_feedback1incorr = "Designs/hand_hold_global_incorr.png";
          hand_hold_feedback2corr = "Designs/hand_hold_local_corr.png";
          hand_hold_feedback2incorr = "Designs/hand_hold_local_incorr.png";
      } else {
          if ((expInfo["design"] === "3")) {
              hand_hold_ex1 = "Designs/design3_run1_ex.png";
              handHoldCorr1 = "f";
              hold_hand_R1_img = "Stimuli/SofH2.jpg";
              hand_hold_ex2 = "Designs/design3_run2_ex.png";
              handHoldCorr2 = "f";
              hold_hand_R2_img = "Stimuli/HofS2.jpg";
              hand_hold_feedback1corr = "Designs/hand_hold_global_corr.png";
              hand_hold_feedback1incorr = "Designs/hand_hold_global_incorr.png";
              hand_hold_feedback2corr = "Designs/hand_hold_local_corr.png";
              hand_hold_feedback2incorr = "Designs/hand_hold_local_incorr.png";
          } else {
              if ((expInfo["design"] === "4")) {
                  hand_hold_ex1 = "Designs/design4_run1_ex.png";
                  handHoldCorr1 = "f";
                  hold_hand_R1_img = "Stimuli/HofS2.jpg";
                  hand_hold_ex2 = "Designs/design4_run2_ex.png";
                  handHoldCorr2 = "f";
                  hold_hand_R2_img = "Stimuli/SofH2.jpg";
                  hand_hold_feedback1corr = "Designs/hand_hold_local_corr.png";
                  hand_hold_feedback1incorr = "Designs/hand_hold_local_incorr.png";
                  hand_hold_feedback2corr = "Designs/hand_hold_global_corr.png";
                  hand_hold_feedback2incorr = "Designs/hand_hold_global_incorr.png";
              }
          }
      }
  }
  
  image_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [(0.75 * 1.77), 0.75],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -1.0 
  });
  key_resp_9 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "hand_hold_trial"
  hand_hold_trialClock = new util.Clock();
  text_8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_8',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -1.0 
  });
  hand_hold_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "hand_hold_feedback"
  hand_hold_feedbackClock = new util.Clock();
  image_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_3', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [(0.75 * 1.77), 0.75],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -1.0 
  });
  key_resp_8 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
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
  
  Pinstructions_imageR2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Pinstructions_imageR2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [(0.75 * 1.77), 0.75],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -1.0 
  });
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "startPrac"
  startPracClock = new util.Clock();
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
  
  prac_fix_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Feedback"
  FeedbackClock = new util.Clock();
  imFeedback = new visual.ImageStim({
    win : psychoJS.window,
    name : 'imFeedback', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -1.0 
  });
  feedback_msg = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_msg',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.25)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "checkPrac2"
  checkPrac2Clock = new util.Clock();
  text_9 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_9',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp_10 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "trial_instr_run2"
  trial_instr_run2Clock = new util.Clock();
  if ((Number.parseInt(expInfo["design"]) === 1)) {
      instructions_run2 = "Designs/design1_run2.png";
      cond_file_run2 = "Designs/design1_run2.csv";
  } else {
      if ((Number.parseInt(expInfo["design"]) === 2)) {
          instructions_run2 = "Designs/design2_run2.png";
          cond_file_run2 = "Designs/design2_run2.csv";
      } else {
          if ((Number.parseInt(expInfo["design"]) === 3)) {
              instructions_run2 = "Designs/design3_run2.png";
              cond_file_run2 = "Designs/design3_run2.csv";
          } else {
              if ((Number.parseInt(expInfo["design"]) === 4)) {
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
    ori : 0, pos : [0, 0], size : [(0.75 * 1.77), 0.75],
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
  
  // Initialize components for Routine "btwn_trial_GJ"
  btwn_trial_GJClock = new util.Clock();
  text_10 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_10',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  image_4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_4', units : undefined, 
    image : 'Designs/baby_dory_GJ.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.4, (0.4 * 1.83)],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "trial_instr_run1"
  trial_instr_run1Clock = new util.Clock();
  if ((Number.parseInt(expInfo["design"]) === 1)) {
      instructions_run1 = "Designs/design1_run1.png";
      cond_file_run1 = "Designs/design1_run1.csv";
  } else {
      if ((Number.parseInt(expInfo["design"]) === 2)) {
          instructions_run1 = "Designs/design2_run1.png";
          cond_file_run1 = "Designs/design2_run1.csv";
      } else {
          if ((Number.parseInt(expInfo["design"]) === 3)) {
              instructions_run1 = "Designs/design3_run1.png";
              cond_file_run1 = "Designs/design3_run1.csv";
          } else {
              if ((Number.parseInt(expInfo["design"]) === 4)) {
                  instructions_run1 = "Designs/design4_run1.png";
                  cond_file_run1 = "Designs/design4_run1.csv";
              }
          }
      }
  }
  if ((Number.parseInt(expInfo["position"]) === 2)) {
      Trial_run1 = 1;
      Total_run1 = 96;
      Trial_run2 = 1;
      Total_run2 = 96;
      positionRows = [0, 1, 2, 3, 4, 5, 6, 7];
  } else {
      if ((Number.parseInt(expInfo["position"]) === 1)) {
          Trial_run1 = 1;
          Total_run1 = (96 / 2);
          Trial_run2 = 1;
          Total_run2 = (96 / 2);
          positionRows = [0, 1, 2, 3];
      } else {
          if ((Number.parseInt(expInfo["position"]) === 3)) {
              Trial_run1 = 1;
              Total_run1 = (96 / 2);
              Trial_run2 = 1;
              Total_run2 = (96 / 2);
              positionRows = [4, 5, 6, 7];
          }
      }
  }
  
  instructions_imageR1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'instructions_imageR1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [(0.75 * 1.77), 0.75],
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
  
  // Initialize components for Routine "btwn_trial_GJ"
  btwn_trial_GJClock = new util.Clock();
  text_10 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_10',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  image_4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_4', units : undefined, 
    image : 'Designs/baby_dory_GJ.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.4, (0.4 * 1.83)],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "trial_instr_run2"
  trial_instr_run2Clock = new util.Clock();
  if ((Number.parseInt(expInfo["design"]) === 1)) {
      instructions_run2 = "Designs/design1_run2.png";
      cond_file_run2 = "Designs/design1_run2.csv";
  } else {
      if ((Number.parseInt(expInfo["design"]) === 2)) {
          instructions_run2 = "Designs/design2_run2.png";
          cond_file_run2 = "Designs/design2_run2.csv";
      } else {
          if ((Number.parseInt(expInfo["design"]) === 3)) {
              instructions_run2 = "Designs/design3_run2.png";
              cond_file_run2 = "Designs/design3_run2.csv";
          } else {
              if ((Number.parseInt(expInfo["design"]) === 4)) {
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
    ori : 0, pos : [0, 0], size : [(0.75 * 1.77), 0.75],
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
  image_5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_5', units : undefined, 
    image : 'Designs/baby_squirt_GJ.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [(0.5 * 1.6), 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 512, interpolate : true, depth : 0.0 
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


var hand_hold_run;
var _start_exp_press_allKeys;
var pracInstructComponents;
function pracInstructRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'pracInstruct'-------
    t = 0;
    pracInstructClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    hand_hold_run = 1;
    
    prac_instr1.setImage('Designs/prac_instr1.png');
    start_exp_press.keys = undefined;
    start_exp_press.rt = undefined;
    _start_exp_press_allKeys = [];
    // keep track of which components have finished
    pracInstructComponents = [];
    pracInstructComponents.push(prac_instr1);
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
    
    // *prac_instr1* updates
    if (t >= 0.0 && prac_instr1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_instr1.tStart = t;  // (not accounting for frame time here)
      prac_instr1.frameNStart = frameN;  // exact frame index
      
      prac_instr1.setAutoDraw(true);
    }

    
    // *start_exp_press* updates
    if (t >= 0.3 && start_exp_press.status === PsychoJS.Status.NOT_STARTED) {
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


var _key_resp_6_allKeys;
var pracInstruct2Components;
function pracInstruct2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'pracInstruct2'-------
    t = 0;
    pracInstruct2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_6.keys = undefined;
    key_resp_6.rt = undefined;
    _key_resp_6_allKeys = [];
    // keep track of which components have finished
    pracInstruct2Components = [];
    pracInstruct2Components.push(prac_instr2);
    pracInstruct2Components.push(key_resp_6);
    
    pracInstruct2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function pracInstruct2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'pracInstruct2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = pracInstruct2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *prac_instr2* updates
    if (t >= 0.0 && prac_instr2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_instr2.tStart = t;  // (not accounting for frame time here)
      prac_instr2.frameNStart = frameN;  // exact frame index
      
      prac_instr2.setAutoDraw(true);
    }

    
    // *key_resp_6* updates
    if (t >= 0.3 && key_resp_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_6.tStart = t;  // (not accounting for frame time here)
      key_resp_6.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_6.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.clearEvents(); });
    }

    if (key_resp_6.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_6.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_6_allKeys = _key_resp_6_allKeys.concat(theseKeys);
      if (_key_resp_6_allKeys.length > 0) {
        key_resp_6.keys = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].name;  // just the last key pressed
        key_resp_6.rt = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].rt;
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
    pracInstruct2Components.forEach( function(thisComponent) {
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


function pracInstruct2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'pracInstruct2'-------
    pracInstruct2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "pracInstruct2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_7_allKeys;
var pracInstruct3Components;
function pracInstruct3RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'pracInstruct3'-------
    t = 0;
    pracInstruct3Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_7.keys = undefined;
    key_resp_7.rt = undefined;
    _key_resp_7_allKeys = [];
    // keep track of which components have finished
    pracInstruct3Components = [];
    pracInstruct3Components.push(prac_instr3);
    pracInstruct3Components.push(key_resp_7);
    
    pracInstruct3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function pracInstruct3RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'pracInstruct3'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = pracInstruct3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *prac_instr3* updates
    if (t >= 0.0 && prac_instr3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_instr3.tStart = t;  // (not accounting for frame time here)
      prac_instr3.frameNStart = frameN;  // exact frame index
      
      prac_instr3.setAutoDraw(true);
    }

    
    // *key_resp_7* updates
    if (t >= 0.3 && key_resp_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_7.tStart = t;  // (not accounting for frame time here)
      key_resp_7.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_7.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_7.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_7.clearEvents(); });
    }

    if (key_resp_7.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_7.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_7_allKeys = _key_resp_7_allKeys.concat(theseKeys);
      if (_key_resp_7_allKeys.length > 0) {
        key_resp_7.keys = _key_resp_7_allKeys[_key_resp_7_allKeys.length - 1].name;  // just the last key pressed
        key_resp_7.rt = _key_resp_7_allKeys[_key_resp_7_allKeys.length - 1].rt;
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
    pracInstruct3Components.forEach( function(thisComponent) {
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


function pracInstruct3RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'pracInstruct3'-------
    pracInstruct3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "pracInstruct3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var left_right;
var rand_side;
var xPosition;
var hand_hold_ex;
var handHoldCorr;
var hold_hand_img;
var hand_hold_feedbackcorr;
var hand_hold_feedbackincorr;
var _key_resp_9_allKeys;
var hand_hold_instrComponents;
function hand_hold_instrRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'hand_hold_instr'-------
    t = 0;
    hand_hold_instrClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    left_right = "";
    rand_side = "";
    if ((expInfo["position"] === "0")) {
        xPosition = 0;
    } else {
        if ((expInfo["position"] === "2")) {
            left_right = [0, 1];
            shuffle(left_right);
            rand_side = [0];
            if ((rand_side === 0)) {
                xPosition = (- (width4deg * x_scale));
            } else {
                xPosition = (width4deg * x_scale);
            }
        } else {
            if ((expInfo["position"] === "1")) {
                xPosition = (- (width4deg * x_scale));
            } else {
                if ((expInfo["position"] === "3")) {
                    xPosition = (width4deg * x_scale);
                }
            }
        }
    }
    if ((hand_hold_run === 1)) {
        hand_hold_ex = hand_hold_ex1;
        handHoldCorr = handHoldCorr1;
        hold_hand_img = hold_hand_R1_img;
        hand_hold_feedbackcorr = hand_hold_feedback1corr;
        hand_hold_feedbackincorr = hand_hold_feedback1incorr;
    } else {
        hand_hold_ex = hand_hold_ex2;
        handHoldCorr = handHoldCorr2;
        hold_hand_img = hold_hand_R2_img;
        hand_hold_feedbackcorr = hand_hold_feedback2corr;
        hand_hold_feedbackincorr = hand_hold_feedback2incorr;
    }
    
    image_2.setImage(hand_hold_ex);
    key_resp_9.keys = undefined;
    key_resp_9.rt = undefined;
    _key_resp_9_allKeys = [];
    // keep track of which components have finished
    hand_hold_instrComponents = [];
    hand_hold_instrComponents.push(image_2);
    hand_hold_instrComponents.push(key_resp_9);
    
    hand_hold_instrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function hand_hold_instrRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'hand_hold_instr'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = hand_hold_instrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_2* updates
    if (t >= 0.0 && image_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_2.tStart = t;  // (not accounting for frame time here)
      image_2.frameNStart = frameN;  // exact frame index
      
      image_2.setAutoDraw(true);
    }

    
    // *key_resp_9* updates
    if (t >= 0.0 && key_resp_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_9.tStart = t;  // (not accounting for frame time here)
      key_resp_9.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_9.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_9.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_9.clearEvents(); });
    }

    if (key_resp_9.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_9.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_9_allKeys = _key_resp_9_allKeys.concat(theseKeys);
      if (_key_resp_9_allKeys.length > 0) {
        key_resp_9.keys = _key_resp_9_allKeys[_key_resp_9_allKeys.length - 1].name;  // just the last key pressed
        key_resp_9.rt = _key_resp_9_allKeys[_key_resp_9_allKeys.length - 1].rt;
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
    hand_hold_instrComponents.forEach( function(thisComponent) {
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


function hand_hold_instrRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'hand_hold_instr'-------
    hand_hold_instrComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "hand_hold_instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _hand_hold_resp_allKeys;
var hand_hold_trialComponents;
function hand_hold_trialRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'hand_hold_trial'-------
    t = 0;
    hand_hold_trialClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    image.setPos([xPosition, 0]);
    image.setSize([(width * x_scale), (height * y_scale)]);
    image.setImage(hold_hand_img);
    hand_hold_resp.keys = undefined;
    hand_hold_resp.rt = undefined;
    _hand_hold_resp_allKeys = [];
    // keep track of which components have finished
    hand_hold_trialComponents = [];
    hand_hold_trialComponents.push(text_8);
    hand_hold_trialComponents.push(image);
    hand_hold_trialComponents.push(hand_hold_resp);
    
    hand_hold_trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function hand_hold_trialRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'hand_hold_trial'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = hand_hold_trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_8* updates
    if (t >= 0.0 && text_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_8.tStart = t;  // (not accounting for frame time here)
      text_8.frameNStart = frameN;  // exact frame index
      
      text_8.setAutoDraw(true);
    }

    
    // *image* updates
    if (t >= 0.0 && image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image.tStart = t;  // (not accounting for frame time here)
      image.frameNStart = frameN;  // exact frame index
      
      image.setAutoDraw(true);
    }

    
    // *hand_hold_resp* updates
    if (t >= 0.0 && hand_hold_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      hand_hold_resp.tStart = t;  // (not accounting for frame time here)
      hand_hold_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { hand_hold_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { hand_hold_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { hand_hold_resp.clearEvents(); });
    }

    if (hand_hold_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = hand_hold_resp.getKeys({keyList: ['f', 'j'], waitRelease: false});
      _hand_hold_resp_allKeys = _hand_hold_resp_allKeys.concat(theseKeys);
      if (_hand_hold_resp_allKeys.length > 0) {
        hand_hold_resp.keys = _hand_hold_resp_allKeys[_hand_hold_resp_allKeys.length - 1].name;  // just the last key pressed
        hand_hold_resp.rt = _hand_hold_resp_allKeys[_hand_hold_resp_allKeys.length - 1].rt;
        // was this correct?
        if (hand_hold_resp.keys == handHoldCorr) {
            hand_hold_resp.corr = 1;
        } else {
            hand_hold_resp.corr = 0;
        }
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
    hand_hold_trialComponents.forEach( function(thisComponent) {
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


function hand_hold_trialRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'hand_hold_trial'-------
    hand_hold_trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // was no response the correct answer?!
    if (hand_hold_resp.keys === undefined) {
      if (['None','none',undefined].includes(handHoldCorr)) {
         hand_hold_resp.corr = 1;  // correct non-response
      } else {
         hand_hold_resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('hand_hold_resp.keys', hand_hold_resp.keys);
    psychoJS.experiment.addData('hand_hold_resp.corr', hand_hold_resp.corr);
    if (typeof hand_hold_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('hand_hold_resp.rt', hand_hold_resp.rt);
        routineTimer.reset();
        }
    
    hand_hold_resp.stop();
    // the Routine "hand_hold_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var feedHHim;
var _key_resp_8_allKeys;
var hand_hold_feedbackComponents;
function hand_hold_feedbackRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'hand_hold_feedback'-------
    t = 0;
    hand_hold_feedbackClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    feedHHim = "";
    if ((hand_hold_run === 1)) {
        if ((hand_hold_resp.keys === handHoldCorr)) {
            feedHHim = hand_hold_feedback1corr;
        } else {
            feedHHim = hand_hold_feedback1incorr;
        }
    } else {
        if ((hand_hold_resp.keys === handHoldCorr)) {
            feedHHim = hand_hold_feedback2corr;
        } else {
            feedHHim = hand_hold_feedback2incorr;
        }
    }
    
    image_3.setImage(feedHHim);
    key_resp_8.keys = undefined;
    key_resp_8.rt = undefined;
    _key_resp_8_allKeys = [];
    // keep track of which components have finished
    hand_hold_feedbackComponents = [];
    hand_hold_feedbackComponents.push(image_3);
    hand_hold_feedbackComponents.push(key_resp_8);
    
    hand_hold_feedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function hand_hold_feedbackRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'hand_hold_feedback'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = hand_hold_feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_3* updates
    if (t >= 0.0 && image_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_3.tStart = t;  // (not accounting for frame time here)
      image_3.frameNStart = frameN;  // exact frame index
      
      image_3.setAutoDraw(true);
    }

    
    // *key_resp_8* updates
    if (t >= 1 && key_resp_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_8.tStart = t;  // (not accounting for frame time here)
      key_resp_8.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_8.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_8.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_8.clearEvents(); });
    }

    if (key_resp_8.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_8.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_8_allKeys = _key_resp_8_allKeys.concat(theseKeys);
      if (_key_resp_8_allKeys.length > 0) {
        key_resp_8.keys = _key_resp_8_allKeys[_key_resp_8_allKeys.length - 1].name;  // just the last key pressed
        key_resp_8.rt = _key_resp_8_allKeys[_key_resp_8_allKeys.length - 1].rt;
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
    hand_hold_feedbackComponents.forEach( function(thisComponent) {
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


function hand_hold_feedbackRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'hand_hold_feedback'-------
    hand_hold_feedbackComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "hand_hold_feedback" was not non-slip safe, so reset the non-slip timer
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


var repeats;
var currentLoop;
function repeatsLoopBegin(repeatsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  repeats = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 4, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'repeats'
  });
  psychoJS.experiment.addLoop(repeats); // add the loop to the experiment
  currentLoop = repeats;  // we're now the current loop

  // Schedule all the trials in the trialList:
  repeats.forEach(function() {
    const snapshot = repeats.getSnapshot();

    repeatsLoopScheduler.add(importConditions(snapshot));
    repeatsLoopScheduler.add(startPracRoutineBegin(snapshot));
    repeatsLoopScheduler.add(startPracRoutineEachFrame(snapshot));
    repeatsLoopScheduler.add(startPracRoutineEnd(snapshot));
    const prac_trials_run1LoopScheduler = new Scheduler(psychoJS);
    repeatsLoopScheduler.add(prac_trials_run1LoopBegin, prac_trials_run1LoopScheduler);
    repeatsLoopScheduler.add(prac_trials_run1LoopScheduler);
    repeatsLoopScheduler.add(prac_trials_run1LoopEnd);
    repeatsLoopScheduler.add(checkPrac1RoutineBegin(snapshot));
    repeatsLoopScheduler.add(checkPrac1RoutineEachFrame(snapshot));
    repeatsLoopScheduler.add(checkPrac1RoutineEnd(snapshot));
    repeatsLoopScheduler.add(endLoopIteration(repeatsLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


var prac_trials_run1;
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
  prac_trials_run1.forEach(function() {
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
  });

  return Scheduler.Event.NEXT;
}


function prac_trials_run1LoopEnd() {
  psychoJS.experiment.removeLoop(prac_trials_run1);

  return Scheduler.Event.NEXT;
}


function repeatsLoopEnd() {
  psychoJS.experiment.removeLoop(repeats);

  return Scheduler.Event.NEXT;
}


var trials_run1;
function trials_run1LoopBegin(trials_run1LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_run1 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 6, method: TrialHandler.Method.FULLRANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, cond_file_run1, positionRows),
    seed: undefined, name: 'trials_run1'
  });
  psychoJS.experiment.addLoop(trials_run1); // add the loop to the experiment
  currentLoop = trials_run1;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials_run1.forEach(function() {
    const snapshot = trials_run1.getSnapshot();

    trials_run1LoopScheduler.add(importConditions(snapshot));
    trials_run1LoopScheduler.add(trialFixR1RoutineBegin(snapshot));
    trials_run1LoopScheduler.add(trialFixR1RoutineEachFrame(snapshot));
    trials_run1LoopScheduler.add(trialFixR1RoutineEnd(snapshot));
    trials_run1LoopScheduler.add(trial_imgRoutineBegin(snapshot));
    trials_run1LoopScheduler.add(trial_imgRoutineEachFrame(snapshot));
    trials_run1LoopScheduler.add(trial_imgRoutineEnd(snapshot));
    trials_run1LoopScheduler.add(endLoopIteration(trials_run1LoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function trials_run1LoopEnd() {
  psychoJS.experiment.removeLoop(trials_run1);

  return Scheduler.Event.NEXT;
}


var repeats2;
function repeats2LoopBegin(repeats2LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  repeats2 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 4, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'repeats2'
  });
  psychoJS.experiment.addLoop(repeats2); // add the loop to the experiment
  currentLoop = repeats2;  // we're now the current loop

  // Schedule all the trials in the trialList:
  repeats2.forEach(function() {
    const snapshot = repeats2.getSnapshot();

    repeats2LoopScheduler.add(importConditions(snapshot));
    repeats2LoopScheduler.add(startPracRoutineBegin(snapshot));
    repeats2LoopScheduler.add(startPracRoutineEachFrame(snapshot));
    repeats2LoopScheduler.add(startPracRoutineEnd(snapshot));
    const prac_trials_run2LoopScheduler = new Scheduler(psychoJS);
    repeats2LoopScheduler.add(prac_trials_run2LoopBegin, prac_trials_run2LoopScheduler);
    repeats2LoopScheduler.add(prac_trials_run2LoopScheduler);
    repeats2LoopScheduler.add(prac_trials_run2LoopEnd);
    repeats2LoopScheduler.add(checkPrac2RoutineBegin(snapshot));
    repeats2LoopScheduler.add(checkPrac2RoutineEachFrame(snapshot));
    repeats2LoopScheduler.add(checkPrac2RoutineEnd(snapshot));
    repeats2LoopScheduler.add(endLoopIteration(repeats2LoopScheduler, snapshot));
  });

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
  prac_trials_run2.forEach(function() {
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
  });

  return Scheduler.Event.NEXT;
}


function prac_trials_run2LoopEnd() {
  psychoJS.experiment.removeLoop(prac_trials_run2);

  return Scheduler.Event.NEXT;
}


function repeats2LoopEnd() {
  psychoJS.experiment.removeLoop(repeats2);

  return Scheduler.Event.NEXT;
}


var trials_run2;
function trials_run2LoopBegin(trials_run2LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_run2 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 6, method: TrialHandler.Method.FULLRANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, cond_file_run2, positionRows),
    seed: undefined, name: 'trials_run2'
  });
  psychoJS.experiment.addLoop(trials_run2); // add the loop to the experiment
  currentLoop = trials_run2;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials_run2.forEach(function() {
    const snapshot = trials_run2.getSnapshot();

    trials_run2LoopScheduler.add(importConditions(snapshot));
    trials_run2LoopScheduler.add(trialFixR2RoutineBegin(snapshot));
    trials_run2LoopScheduler.add(trialFixR2RoutineEachFrame(snapshot));
    trials_run2LoopScheduler.add(trialFixR2RoutineEnd(snapshot));
    trials_run2LoopScheduler.add(trial_imgRoutineBegin(snapshot));
    trials_run2LoopScheduler.add(trial_imgRoutineEachFrame(snapshot));
    trials_run2LoopScheduler.add(trial_imgRoutineEnd(snapshot));
    trials_run2LoopScheduler.add(endLoopIteration(trials_run2LoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function trials_run2LoopEnd() {
  psychoJS.experiment.removeLoop(trials_run2);

  return Scheduler.Event.NEXT;
}


var trials_run3;
function trials_run3LoopBegin(trials_run3LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_run3 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 6, method: TrialHandler.Method.FULLRANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, cond_file_run1, positionRows),
    seed: undefined, name: 'trials_run3'
  });
  psychoJS.experiment.addLoop(trials_run3); // add the loop to the experiment
  currentLoop = trials_run3;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials_run3.forEach(function() {
    const snapshot = trials_run3.getSnapshot();

    trials_run3LoopScheduler.add(importConditions(snapshot));
    trials_run3LoopScheduler.add(trialFixR1RoutineBegin(snapshot));
    trials_run3LoopScheduler.add(trialFixR1RoutineEachFrame(snapshot));
    trials_run3LoopScheduler.add(trialFixR1RoutineEnd(snapshot));
    trials_run3LoopScheduler.add(trial_imgRoutineBegin(snapshot));
    trials_run3LoopScheduler.add(trial_imgRoutineEachFrame(snapshot));
    trials_run3LoopScheduler.add(trial_imgRoutineEnd(snapshot));
    trials_run3LoopScheduler.add(endLoopIteration(trials_run3LoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function trials_run3LoopEnd() {
  psychoJS.experiment.removeLoop(trials_run3);

  return Scheduler.Event.NEXT;
}


var trials_run4;
function trials_run4LoopBegin(trials_run4LoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_run4 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 6, method: TrialHandler.Method.FULLRANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, cond_file_run2, positionRows),
    seed: undefined, name: 'trials_run4'
  });
  psychoJS.experiment.addLoop(trials_run4); // add the loop to the experiment
  currentLoop = trials_run4;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials_run4.forEach(function() {
    const snapshot = trials_run4.getSnapshot();

    trials_run4LoopScheduler.add(importConditions(snapshot));
    trials_run4LoopScheduler.add(trialFixR2RoutineBegin(snapshot));
    trials_run4LoopScheduler.add(trialFixR2RoutineEachFrame(snapshot));
    trials_run4LoopScheduler.add(trialFixR2RoutineEnd(snapshot));
    trials_run4LoopScheduler.add(trial_imgRoutineBegin(snapshot));
    trials_run4LoopScheduler.add(trial_imgRoutineEachFrame(snapshot));
    trials_run4LoopScheduler.add(trial_imgRoutineEnd(snapshot));
    trials_run4LoopScheduler.add(endLoopIteration(trials_run4LoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function trials_run4LoopEnd() {
  psychoJS.experiment.removeLoop(trials_run4);

  return Scheduler.Event.NEXT;
}


var numIncorr_fix;
var numIncorr_miss;
var numIncorr_img;
var rand4Idx;
var rand8Idx;
var randRows_run1;
var randRows_run2;
var pTrial_run1;
var pracTotal_run1;
var pTrial_run2;
var pracTotal_run2;
var startPracComponents;
function startPracRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'startPrac'-------
    t = 0;
    startPracClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    numIncorr_fix = 0;
    numIncorr_miss = 0;
    numIncorr_img = 0;
    rand4Idx = "";
    rand8Idx = "";
    if ((Number.parseInt(expInfo["position"]) === 2)) {
        rand8Idx = [0, 1, 2, 3, 4, 5, 6, 7];
        shuffle(rand8Idx);
        randRows_run1 = rand8Idx.slice(0, 6);
        shuffle(rand8Idx);
        randRows_run2 = rand8Idx.slice(0, 6);
    } else {
        if ((Number.parseInt(expInfo["position"]) === 1)) {
            rand4Idx = [0, 1, 2, 3, 0, 1];
            shuffle(rand4Idx);
            randRows_run1 = rand4Idx;
            shuffle(rand4Idx);
            randRows_run2 = rand4Idx;
        } else {
            if ((Number.parseInt(expInfo["position"]) === 3)) {
                rand4Idx = [4, 5, 6, 7, 4, 5];
                shuffle(rand4Idx);
                randRows_run1 = rand4Idx;
                shuffle(rand4Idx);
                randRows_run2 = rand4Idx;
            }
        }
    }
    pTrial_run1 = 1;
    pracTotal_run1 = 6;
    pTrial_run2 = 1;
    pracTotal_run2 = 6;
    
    // keep track of which components have finished
    startPracComponents = [];
    
    startPracComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function startPracRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'startPrac'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = startPracClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    startPracComponents.forEach( function(thisComponent) {
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


function startPracRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'startPrac'-------
    startPracComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "startPrac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var trialMsg;
var currFix;
var corrfixResp;
var a;
var b;
var fixDur;
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
        corrfixResp = undefined;
    } else {
        if ((prac1_fixColSwitch[(pTrial_run1 - 1)] === 1)) {
            if ((currFix === "white")) {
                currFix = "black";
                corrfixResp = "space";
            } else {
                if ((currFix === "black")) {
                    currFix = "white";
                    corrfixResp = "space";
                }
            }
        } else {
            currFix = currFix;
            corrfixResp = undefined;
        }
    }
    a = 1.25;
    b = 1.75;
    fixDur = (((b - a) * random()) + a);
    if ((Number.parseInt(expInfo["position"]) === 0)) {
        xPosition = 0;
    } else {
        if ((Number.parseInt(expInfo["position"]) === 2)) {
            if ((side === "left")) {
                xPosition = (- (width4deg * x_scale));
            } else {
                if ((side === "right")) {
                    xPosition = (width4deg * x_scale);
                }
            }
        } else {
            if ((Number.parseInt(expInfo["position"]) === 1)) {
                xPosition = (- (width4deg * x_scale));
            } else {
                if ((Number.parseInt(expInfo["position"]) === 3)) {
                    xPosition = (width4deg * x_scale);
                }
            }
        }
    }
    thisExp.addData("fixpR1", prac1_fixColSwitch[(pTrial_run1 - 1)]);
    
    text.setColor(new util.Color(currFix));
    // keep track of which components have finished
    pracFixR1Components = [];
    pracFixR1Components.push(text);
    
    pracFixR1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
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
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    pracFixR1Components.forEach( function(thisComponent) {
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


function pracFixR1RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'pracFixR1'-------
    pracFixR1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    pTrial_run1 = (pTrial_run1 + 1);
    
    // the Routine "pracFixR1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _prac_resp_allKeys;
var _prac_fix_resp_allKeys;
var prac_imgComponents;
function prac_imgRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'prac_img'-------
    t = 0;
    prac_imgClock.reset(); // clock
    frameN = -1;
    routineTimer.add(4.000000);
    // update component parameters for each repeat
    text_5.setColor(new util.Color(currFix));
    prac_image.setPos([xPosition, 0]);
    prac_image.setSize([(width * x_scale), (height * y_scale)]);
    prac_image.setImage(imFile);
    prac_resp.keys = undefined;
    prac_resp.rt = undefined;
    _prac_resp_allKeys = [];
    prac_fix_resp.keys = undefined;
    prac_fix_resp.rt = undefined;
    _prac_fix_resp_allKeys = [];
    // keep track of which components have finished
    prac_imgComponents = [];
    prac_imgComponents.push(text_5);
    prac_imgComponents.push(prac_image);
    prac_imgComponents.push(prac_resp);
    prac_imgComponents.push(prac_fix_resp);
    
    prac_imgComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
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

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_5.setAutoDraw(false);
    }
    
    // *prac_image* updates
    if (t >= 0.0 && prac_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_image.tStart = t;  // (not accounting for frame time here)
      prac_image.frameNStart = frameN;  // exact frame index
      
      prac_image.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (prac_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      prac_image.setAutoDraw(false);
    }
    
    // *prac_resp* updates
    if (t >= 0.0 && prac_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_resp.tStart = t;  // (not accounting for frame time here)
      prac_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { prac_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { prac_resp.start(); }); // start on screen flip
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (prac_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      prac_resp.status = PsychoJS.Status.FINISHED;
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
      }
    }
    
    
    // *prac_fix_resp* updates
    if (t >= 0.0 && prac_fix_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_fix_resp.tStart = t;  // (not accounting for frame time here)
      prac_fix_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { prac_fix_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { prac_fix_resp.start(); }); // start on screen flip
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (prac_fix_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      prac_fix_resp.status = PsychoJS.Status.FINISHED;
  }

    if (prac_fix_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = prac_fix_resp.getKeys({keyList: ['space'], waitRelease: false});
      _prac_fix_resp_allKeys = _prac_fix_resp_allKeys.concat(theseKeys);
      if (_prac_fix_resp_allKeys.length > 0) {
        prac_fix_resp.keys = _prac_fix_resp_allKeys[_prac_fix_resp_allKeys.length - 1].name;  // just the last key pressed
        prac_fix_resp.rt = _prac_fix_resp_allKeys[_prac_fix_resp_allKeys.length - 1].rt;
        // was this correct?
        if (prac_fix_resp.keys == corrfixResp) {
            prac_fix_resp.corr = 1;
        } else {
            prac_fix_resp.corr = 0;
        }
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
    prac_imgComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function prac_imgRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'prac_img'-------
    prac_imgComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
        }
    
    prac_resp.stop();
    // was no response the correct answer?!
    if (prac_fix_resp.keys === undefined) {
      if (['None','none',undefined].includes(corrfixResp)) {
         prac_fix_resp.corr = 1;  // correct non-response
      } else {
         prac_fix_resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('prac_fix_resp.keys', prac_fix_resp.keys);
    psychoJS.experiment.addData('prac_fix_resp.corr', prac_fix_resp.corr);
    if (typeof prac_fix_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('prac_fix_resp.rt', prac_fix_resp.rt);
        }
    
    prac_fix_resp.stop();
    return Scheduler.Event.NEXT;
  };
}


var feedIM;
var prac_msg;
var FeedbackComponents;
function FeedbackRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Feedback'-------
    t = 0;
    FeedbackClock.reset(); // clock
    frameN = -1;
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    feedIM = "";
    if ((prac_resp.keys === corr)) {
        if ((prac_fix_resp.corr === 1)) {
            feedIM = "Stimuli/greenCheck.png";
            prac_msg = "Well done!";
        } else {
            numIncorr_fix = (numIncorr_fix + 1);
            feedIM = "Stimuli/redWrong.png";
            if ((corrfixResp === "space")) {
                prac_msg = "Oops, you missed the cross change.";
            } else {
                prac_msg = "Oops, you pressed space when the cross didn't change.";
            }
        }
    } else {
        if ((prac_resp.keys !== corr)) {
            if ((prac_resp.keys === undefined)) {
                feedIM = "Stimuli/redWrong.png";
                numIncorr_miss = (numIncorr_miss + 1);
                if ((corrfixResp === "space")) {
                    numIncorr_fix = (numIncorr_fix + 1);
                }
                prac_msg = "Oops, time ran out. That's ok, try again!";
            } else {
                if ((prac_fix_resp.corr === 1)) {
                    feedIM = "Stimuli/redWrong.png";
                    numIncorr_img = (numIncorr_img + 1);
                    if ((corrfixResp === "space")) {
                        prac_msg = "Good job! You got pressed space when the cross changed! But the picture response was wrong.";
                    } else {
                        prac_msg = "Oops, the picture response was wrong.";
                    }
                } else {
                    numIncorr_img = (numIncorr_img + 1);
                    numIncorr_fix = (numIncorr_fix + 1);
                    feedIM = "Stimuli/redWrong.png";
                    if ((corrfixResp === "space")) {
                        prac_msg = "Oops, you missed the cross change and the picture response was wrong.";
                    } else {
                        prac_msg = "Oops, you press space when the cross didn't change and the picture response was wrong.";
                    }
                }
            }
        }
    }
    
    imFeedback.setImage(feedIM);
    feedback_msg.setText(prac_msg);
    // keep track of which components have finished
    FeedbackComponents = [];
    FeedbackComponents.push(imFeedback);
    FeedbackComponents.push(feedback_msg);
    
    FeedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
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

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (imFeedback.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      imFeedback.setAutoDraw(false);
    }
    
    // *feedback_msg* updates
    if (t >= 0.0 && feedback_msg.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_msg.tStart = t;  // (not accounting for frame time here)
      feedback_msg.frameNStart = frameN;  // exact frame index
      
      feedback_msg.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (feedback_msg.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedback_msg.setAutoDraw(false);
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
    FeedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    FeedbackComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var prac_feedback;
var _key_resp_5_allKeys;
var checkPrac1Components;
function checkPrac1RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'checkPrac1'-------
    t = 0;
    checkPrac1Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    if (((((numIncorr_fix + numIncorr_miss) + numIncorr_img) < 3) && (numIncorr_fix !== 2))) {
        prac_feedback = "Great job! You are now ready for the real game. \nPress Space to see the instructions again.";
        repeats.finished = true;
    } else {
        if ((((numIncorr_fix > 1) && (numIncorr_img < 2)) && (numIncorr_miss < 2))) {
            prac_feedback = (("Good job with the pictures! \n You missed " + numIncorr_fix.toString()) + " of the two fix changes. \n In the real game, make sure you press Space as soon as you see it change!\n\n Let's try some more practice. \n Press Space to start.");
        } else {
            if ((((numIncorr_fix < 2) && (numIncorr_img > 1)) && (numIncorr_miss < 2))) {
                prac_feedback = (((("Good job, you got " + (2 - numIncorr_fix).toString()) + " of the 2 fix changes! \nYou missed ") + numIncorr_img.toString()) + " of the pictures. \n Sometimes the big letter and the little letters are different. \nMake sure you focus on the right ones and press the right keys! \n\nLet's try some more practice. \n Press Space to start.");
            } else {
                if ((((numIncorr_fix < 2) && (numIncorr_img < 2)) && (numIncorr_miss > 1))) {
                    prac_feedback = (("You missed " + numIncorr_miss.toString()) + " of the trials because the time was up. That's ok, in the real game the pictures will stay on, but try to go as fast as you can. \n\n Press Space to practice more.");
                } else {
                    prac_feedback = (((((("Nice try! You missed " + numIncorr_img.toString()) + " of the picture responses, ") + numIncorr_fix.toString()) + " of the two fix changes, and ") + numIncorr_miss.toString()) + " trials went by too fast. \n\nLet's try another round of practice. \nPress Space to start.");
                }
            }
        }
    }
    
    text_7.setText(prac_feedback);
    key_resp_5.keys = undefined;
    key_resp_5.rt = undefined;
    _key_resp_5_allKeys = [];
    // keep track of which components have finished
    checkPrac1Components = [];
    checkPrac1Components.push(text_7);
    checkPrac1Components.push(key_resp_5);
    
    checkPrac1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function checkPrac1RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'checkPrac1'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = checkPrac1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_7* updates
    if (t >= 0.0 && text_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_7.tStart = t;  // (not accounting for frame time here)
      text_7.frameNStart = frameN;  // exact frame index
      
      text_7.setAutoDraw(true);
    }

    
    // *key_resp_5* updates
    if (t >= 1 && key_resp_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_5.tStart = t;  // (not accounting for frame time here)
      key_resp_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.clearEvents(); });
    }

    if (key_resp_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_5.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_5_allKeys = _key_resp_5_allKeys.concat(theseKeys);
      if (_key_resp_5_allKeys.length > 0) {
        key_resp_5.keys = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].name;  // just the last key pressed
        key_resp_5.rt = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].rt;
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
    checkPrac1Components.forEach( function(thisComponent) {
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


function checkPrac1RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'checkPrac1'-------
    checkPrac1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "checkPrac1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var incorr_fix;
var runType;
var _key_resp_2_allKeys;
var trial_instr_run1Components;
function trial_instr_run1RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'trial_instr_run1'-------
    t = 0;
    trial_instr_run1Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    incorr_fix = 0;
    runType = 1;
    
    instructions_imageR1.setImage(instructions_run1);
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // keep track of which components have finished
    trial_instr_run1Components = [];
    trial_instr_run1Components.push(instructions_imageR1);
    trial_instr_run1Components.push(key_resp_2);
    
    trial_instr_run1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
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
    trial_instr_run1Components.forEach( function(thisComponent) {
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


function trial_instr_run1RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'trial_instr_run1'-------
    trial_instr_run1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "trial_instr_run1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var corrResp;
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
        corrResp = undefined;
    } else {
        if ((fixColorIdx_Run1[(Trial_run1 - 1)] === 0)) {
            currFix = currFix;
            corrResp = undefined;
        } else {
            if ((fixColorIdx_Run1[(Trial_run1 - 1)] === 1)) {
                corrResp = "space";
                if ((currFix === "white")) {
                    currFix = "black";
                } else {
                    if ((currFix === "black")) {
                        currFix = "white";
                    }
                }
            }
        }
    }
    a = 1.25;
    b = 1.75;
    fixDur = (((b - a) * random()) + a);
    if ((Number.parseInt(expInfo["position"]) === 0)) {
        xPosition = 0;
    } else {
        if ((Number.parseInt(expInfo["position"]) === 2)) {
            if ((runType === 1)) {
                xPosition = (- (width4deg * x_scale));
            } else {
                xPosition = (width4deg * x_scale);
            }
        } else {
            if ((Number.parseInt(expInfo["position"]) === 1)) {
                xPosition = (- (width4deg * x_scale));
            } else {
                if ((Number.parseInt(expInfo["position"]) === 3)) {
                    xPosition = (width4deg * x_scale);
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
    
    trialFixR1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
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
        // was this correct?
        if (fix_resp1_1.keys == corrResp) {
            fix_resp1_1.corr = 1;
        } else {
            fix_resp1_1.corr = 0;
        }
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
    trialFixR1Components.forEach( function(thisComponent) {
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


function trialFixR1RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'trialFixR1'-------
    trialFixR1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    Trial_run1 = (Trial_run1 + 1);
    
    // was no response the correct answer?!
    if (fix_resp1_1.keys === undefined) {
      if (['None','none',undefined].includes(corrResp)) {
         fix_resp1_1.corr = 1;  // correct non-response
      } else {
         fix_resp1_1.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('fix_resp1_1.keys', fix_resp1_1.keys);
    psychoJS.experiment.addData('fix_resp1_1.corr', fix_resp1_1.corr);
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
    if ((runType === 1)) {
        if ((corrResp === "space")) {
            if ((fix_resp1_1.corr !== 1)) {
                incorr_fix = (incorr_fix + 1);
            }
        }
    } else {
        if ((corrResp === "space")) {
            if ((fix_resp2_1.corr !== 1)) {
                incorr_fix = (incorr_fix + 1);
            }
        }
    }
    
    // keep track of which components have finished
    trial_imgComponents = [];
    trial_imgComponents.push(text_6);
    trial_imgComponents.push(trial_image);
    trial_imgComponents.push(trial_resp);
    trial_imgComponents.push(fix_resp_2);
    
    trial_imgComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
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
    trial_imgComponents.forEach( function(thisComponent) {
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


function trial_imgRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'trial_img'-------
    trial_imgComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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


var sum;
var total_fix;
var btwn_trial_GJComponents;
function btwn_trial_GJRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'btwn_trial_GJ'-------
    t = 0;
    btwn_trial_GJClock.reset(); // clock
    frameN = -1;
    routineTimer.add(4.000000);
    // update component parameters for each repeat
    feedback_msg = "";
    sum = function (arr) {
    return arr.reduce((a,b)=>a+b)
    }
    
    hand_hold_run = 2;
    total_fix = Number.parseInt((sum(fixColorIdx_Run1) / 2));
    feedback_msg = (((("You caught " + (total_fix - incorr_fix).toString()) + " of the ") + total_fix.toString()) + " cross changes.");
    
    text_10.setText(feedback_msg);
    // keep track of which components have finished
    btwn_trial_GJComponents = [];
    btwn_trial_GJComponents.push(text_10);
    btwn_trial_GJComponents.push(image_4);
    
    btwn_trial_GJComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function btwn_trial_GJRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'btwn_trial_GJ'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = btwn_trial_GJClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_10* updates
    if (t >= 0.0 && text_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_10.tStart = t;  // (not accounting for frame time here)
      text_10.frameNStart = frameN;  // exact frame index
      
      text_10.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_10.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_10.setAutoDraw(false);
    }
    
    // *image_4* updates
    if (t >= 2 && image_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_4.tStart = t;  // (not accounting for frame time here)
      image_4.frameNStart = frameN;  // exact frame index
      
      image_4.setAutoDraw(true);
    }

    frameRemains = 2 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_4.setAutoDraw(false);
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
    btwn_trial_GJComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function btwn_trial_GJRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'btwn_trial_GJ'-------
    btwn_trial_GJComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    
    prac_instr_run2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
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
    prac_instr_run2Components.forEach( function(thisComponent) {
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


function prac_instr_run2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'prac_instr_run2'-------
    prac_instr_run2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
        corrfixResp = undefined;
    } else {
        if ((prac2_fixColSwitch[(pTrial_run2 - 1)] === 0)) {
            currFix = currFix;
            corrfixResp = undefined;
        } else {
            if ((prac2_fixColSwitch[(pTrial_run2 - 1)] === 1)) {
                if ((currFix === "white")) {
                    currFix = "black";
                    corrfixResp = "space";
                } else {
                    if ((currFix === "black")) {
                        currFix = "white";
                        corrfixResp = "space";
                    }
                }
            }
        }
    }
    a = 1.25;
    b = 1.75;
    fixDur = (((b - a) * random()) + a);
    if ((expInfo["position"] === 0)) {
        xPosition = 0;
    } else {
        if ((Number.parseInt(expInfo["position"]) === 2)) {
            if ((side === "left")) {
                xPosition = (- (width4deg * x_scale));
            } else {
                if ((side === "right")) {
                    xPosition = (width4deg * x_scale);
                }
            }
        } else {
            if ((Number.parseInt(expInfo["position"]) === 1)) {
                xPosition = (- (width4deg * x_scale));
            } else {
                if ((Number.parseInt(expInfo["position"]) === 3)) {
                    xPosition = (width4deg * x_scale);
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
    
    pracFixR2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
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
    pracFixR2Components.forEach( function(thisComponent) {
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


function pracFixR2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'pracFixR2'-------
    pracFixR2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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


var _key_resp_10_allKeys;
var checkPrac2Components;
function checkPrac2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'checkPrac2'-------
    t = 0;
    checkPrac2Clock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    if (((((numIncorr_fix + numIncorr_miss) + numIncorr_img) < 3) && (numIncorr_fix !== 2))) {
        prac_feedback = "Great job! You are now ready for the real game. \nPress Space to see the instructions again.";
        repeats2.finished = true;
    } else {
        if ((((numIncorr_fix > 1) && (numIncorr_img < 2)) && (numIncorr_miss < 2))) {
            prac_feedback = (("Good job with the pictures! \n You missed " + numIncorr_fix.toString()) + " of the two fix changes. \n In the real game, make sure you press Space as soon as you see it change!\n\n Let's try some more practice. \n Press Space to start.");
        } else {
            if ((((numIncorr_fix < 2) && (numIncorr_img > 1)) && (numIncorr_miss < 2))) {
                prac_feedback = (((("Good job, you got " + (2 - numIncorr_fix).toString()) + " of the 2 fix changes! \nYou missed ") + numIncorr_img.toString()) + " of the pictures. \n Sometimes the big letter and the little letters are different. \nMake sure you focus on the right ones and press the right keys! \n\nLet's try some more practice. \n Press Space to start.");
            } else {
                if ((((numIncorr_fix < 2) && (numIncorr_img < 2)) && (numIncorr_miss > 1))) {
                    prac_feedback = (("You missed " + numIncorr_miss.toString()) + " of the trials because the time was up. That's ok, in the real game the pictures will stay on, but try to go as fast as you can. \n\n Press Space to practice more.");
                } else {
                    prac_feedback = (((((("Nice try! You missed " + numIncorr_img.toString()) + " of the picture responses, ") + numIncorr_fix.toString()) + " of the two fix changes, and ") + numIncorr_miss.toString()) + " trials went by too fast. \n\nLet's try another round of practice. \nPress Space to start.");
                }
            }
        }
    }
    
    text_9.setText(prac_feedback);
    key_resp_10.keys = undefined;
    key_resp_10.rt = undefined;
    _key_resp_10_allKeys = [];
    // keep track of which components have finished
    checkPrac2Components = [];
    checkPrac2Components.push(text_9);
    checkPrac2Components.push(key_resp_10);
    
    checkPrac2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


function checkPrac2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'checkPrac2'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = checkPrac2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_9* updates
    if (t >= 0.0 && text_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_9.tStart = t;  // (not accounting for frame time here)
      text_9.frameNStart = frameN;  // exact frame index
      
      text_9.setAutoDraw(true);
    }

    
    // *key_resp_10* updates
    if (t >= 1 && key_resp_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_10.tStart = t;  // (not accounting for frame time here)
      key_resp_10.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_10.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_10.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_10.clearEvents(); });
    }

    if (key_resp_10.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_10.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_10_allKeys = _key_resp_10_allKeys.concat(theseKeys);
      if (_key_resp_10_allKeys.length > 0) {
        key_resp_10.keys = _key_resp_10_allKeys[_key_resp_10_allKeys.length - 1].name;  // just the last key pressed
        key_resp_10.rt = _key_resp_10_allKeys[_key_resp_10_allKeys.length - 1].rt;
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
    checkPrac2Components.forEach( function(thisComponent) {
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


function checkPrac2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'checkPrac2'-------
    checkPrac2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_10.keys', key_resp_10.keys);
    if (typeof key_resp_10.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_10.rt', key_resp_10.rt);
        routineTimer.reset();
        }
    
    key_resp_10.stop();
    // the Routine "checkPrac2" was not non-slip safe, so reset the non-slip timer
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
    incorr_fix = 0;
    runType = 2;
    
    instructions_imageR2.setImage(instructions_run2);
    key_resp_4.keys = undefined;
    key_resp_4.rt = undefined;
    _key_resp_4_allKeys = [];
    // keep track of which components have finished
    trial_instr_run2Components = [];
    trial_instr_run2Components.push(instructions_imageR2);
    trial_instr_run2Components.push(key_resp_4);
    
    trial_instr_run2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
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
    trial_instr_run2Components.forEach( function(thisComponent) {
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


function trial_instr_run2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'trial_instr_run2'-------
    trial_instr_run2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
            if ((fixColorIdx_Run2[(Trial_run2 - 1)] === 1)) {
                corrResp = "space";
                if ((currFix === "white")) {
                    currFix = "black";
                } else {
                    if ((currFix === "black")) {
                        currFix = "white";
                    }
                }
            }
        }
    }
    a = 1.25;
    b = 1.75;
    fixDur = (((b - a) * random()) + a);
    if ((Number.parseInt(expInfo["position"]) === 0)) {
        xPosition = 0;
    } else {
        if ((Number.parseInt(expInfo["position"]) === 2)) {
            if ((side === "left")) {
                xPosition = (- (width4deg * x_scale));
            } else {
                if ((side === "right")) {
                    xPosition = (width4deg * x_scale);
                }
            }
        } else {
            if ((Number.parseInt(expInfo["position"]) === 1)) {
                xPosition = (- (width4deg * x_scale));
            } else {
                if ((expInfo["position"] === 3)) {
                    xPosition = (width4deg * x_scale);
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
    
    trialFixR2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
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
        // was this correct?
        if (fix_resp2_1.keys == corrResp) {
            fix_resp2_1.corr = 1;
        } else {
            fix_resp2_1.corr = 0;
        }
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
    trialFixR2Components.forEach( function(thisComponent) {
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


function trialFixR2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'trialFixR2'-------
    trialFixR2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    Trial_run2 = (Trial_run2 + 1);
    
    // was no response the correct answer?!
    if (fix_resp2_1.keys === undefined) {
      if (['None','none',undefined].includes(corrResp)) {
         fix_resp2_1.corr = 1;  // correct non-response
      } else {
         fix_resp2_1.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('fix_resp2_1.keys', fix_resp2_1.keys);
    psychoJS.experiment.addData('fix_resp2_1.corr', fix_resp2_1.corr);
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
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    EndScreenComponents = [];
    EndScreenComponents.push(image_5);
    
    EndScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
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
    
    // *image_5* updates
    if (t >= 0.0 && image_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_5.tStart = t;  // (not accounting for frame time here)
      image_5.frameNStart = frameN;  // exact frame index
      
      image_5.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_5.setAutoDraw(false);
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
    EndScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    EndScreenComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
