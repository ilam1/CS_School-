globals [level thoughtBubblesCollected lowestpatch point thoughtbubbleleft notendgame g obstaclespatches]
breed [thoughtBubbles thoughtBubble]
breed [endgoals endgoal]
breed [steams steam]
breed [water onewater]
breed [danger onedanger]
thoughtBubbles-own [water-in]
endgoals-own [water-in dangerpoints]
patches-own [origColor nextcolor]
water-own [xspeed yspeed nextxcor nextycor]


to setup
  ca
  reset-ticks
  set-default-shape thoughtBubbles "circle"
  choose-this-level
  correctColor
  set notendgame true
  ask patches [set origColor pcolor]
  ask patches [set nextcolor pcolor]
end

to play
  while [notendgame]
  [
    debris
    broccoli
    lava
    steaming
    poison
    ice
    collectThoughts
    if any? patches with [pcolor = blue or pcolor = violet]
    [move-water]
    ;pipe
    ;water-turtle-properties
    winlose
    tick
  ]
end

to collectThoughts
  ask thoughtBubbles with [water-in >= 15]
  [
    set point (point + 1)
    set thoughtbubbleleft (thoughtbubbleleft - 1)
    die
    ]
end

to winlose
  if count thoughtBubbles < 3 [
    ask endgoals with [water-in >= 25]
    [die]
  ]
  if count thoughtBubbles < 3 and count danger < (3 - count thoughtBubbles) and count endgoals = 0 [
    if level = 0
    [set chooseLevel "Level 1"]
    if level = 1
    [set chooseLevel "Level 2"]
    if level = 2
    [ifelse "Restart" = user-one-of "Congratulations!! You've cleared the game!!"
      ["Restart" "Quit :("]
      [set level 0]
      [set notendgame false ct cp]]
;    if level = 3
;    [set chooseLevel "Level 3"]
;    if level = 4
;    [set chooseLevel "Level 4"]
    set level level + 1
    choose-this-level
  ]
  if ticks > 50 and count patches with [pcolor = blue] < 1
  or count danger = 3
  [
    ifelse "Try Again?" = user-one-of "Better luck next time" ["Try Again?" "Quit :("]
    [setup]
    [set notendgame false ct cp]
  ]
  if any? endgoals [
    if [dangerpoints] of one-of endgoals > 0
    [
      ifelse "Try Again?" = user-one-of "Better luck next time" ["Try Again?" "Quit :("]
      [setup]
      [set notendgame false ct cp]
    ]
  ]
end

to correctColor
  ask patches with [pcolor > 120 and pcolor < 130]
  [set pcolor 125]
  ask patches with [pcolor > 111 and pcolor < 119]
  [set pcolor violet]
  ask patches with [pcolor > 50 and pcolor < 60]
  [set pcolor 54]
  ask patches with [pcolor = 2.7]
  [set pcolor black]
  ask patches with [pcolor < 109 and pcolor > 90]
  [set pcolor blue]
  ask patches with [pcolor < 4] [set pcolor black]
  ask patches with [pcolor = blue and pycor > 25] [
    ask neighbors with [pcolor != black or pcolor != white][
      set pcolor blue
      ask neighbors with [pcolor != black or pcolor != white]
      [set pcolor blue]
    ]
  ]
  ask patches with [pcolor = 114.9]
    [set pcolor magenta]
  ask patches with [pcolor = magenta]
    [if pxcor mod 5 = 0 and pycor mod 5 = 0
      [sprout 1 [
        set size 2
        set color one-of [red blue lime yellow violet]
        set shape "circle"
      ]
      ]
    ]
  ask patches with [pcolor < 9.9]
  [set pcolor black]
end

to choose-this-level
  if level = 1 or chooseLevel = "Level 1"
  [
    ct cp
    set notendgame true
    reset-ticks
    set level 1
    set chooseLevel "Level 1"
    set thoughtbubbleleft 3
    import-pcolors "Level 1.png"
    correctColor
    ask patch -30 29 [
      sprout-thoughtBubbles 1 [
        set color sky
        set size 10
      ]
    ]
    ask patch -30 8 [
      sprout-thoughtBubbles 1 [
        set color yellow
        set size 10
      ]
    ]
    ask patch 24 -47 [
      sprout-thoughtBubbles 1 [
        set color green
        set size 10
      ]
    ]
    create-endgoals 1 [
      setxy 26 -68
      set shape "bing bong's bag"
      set size 19
      set heading 0
    ]
  ]
  if level = 2 or chooseLevel = "Level 2"
  [
    ca
    set notendgame true
    reset-ticks
    set level 2
    set chooseLevel "Level 2"
    import-pcolors "Level 2.png"
    set thoughtbubbleleft 3
    correctColor
;    ask patch -60 78 [
;      ask neighbors [set pcolor white]
;      set pcolor white]
    ask patches with [pycor = 28 and pxcor > -66 and pxcor < -50]
    [set pcolor one-of [21 24 13 15]]
    ask patches with [pxcor < -52 and pxcor > -66 and pycor = -32]
    [set pcolor cyan]
    ask patches with [pycor = 40 and pxcor > -40 and pxcor < -30]
    [set pcolor cyan]
    ask patch -39 56 [
      sprout-thoughtBubbles 1 [
        set color sky
        set size 10
      ]
    ]
    ask patch 52 50 [
      sprout-thoughtBubbles 1 [
        set color red
        set size 10
      ]
    ]
    ask patch -46 3 [
      sprout-thoughtBubbles 1 [
        set color green
        set size 10
      ]
    ]
    create-endgoals 1 [
      setxy 12 -78
      set shape "bing bong's bag"
      set size 14
      set heading 0
    ]
  ]
  if chooseLevel = "Tutorial"
  [
    reset-ticks
    set chooseLevel "Tutorial"
    set level 0
    set thoughtbubbleleft 3
    import-pcolors "tutorial.png"
    ask patch 1 -17 [
      sprout-thoughtBubbles 1 [
        set color red
        set size 13
      ]
    ]
    ask patch 46 -42 [
      sprout-thoughtBubbles 1 [
        set color yellow
        set size 13
      ]
    ]
    ask patch -33 -55 [
      sprout-thoughtBubbles 1 [
        set color green
        set size 13
      ]
    ]
    create-endgoals 1 [
      setxy 6 -76
      set shape "bing bong's bag"
      set size 17
      set heading 0
    ]
    ]
end

to surfaceTension
set nextcolor pcolor
if [pcolor] of patch-at -1 -1 = white
[set nextcolor white
  ask patch-at -1 -1
  [set pcolor [pcolor] of myself
    ]
  ]
if [pcolor] of patch-at 1 -1 = white
[set nextcolor white
  ask patch-at 1 -1
  [set pcolor [pcolor] of myself
    ]
  ]
set pcolor nextcolor
end

to debris
  if mouse-down? and mouse-inside?
  [
    ask patch round mouse-xcor round mouse-ycor
    [
      if pcolor = black or pcolor = white
      [
        set pcolor white
        ask patches in-radius 5 with [pcolor = black]
        [set pcolor white]
      ]
    ]
  ]
end

to moveleft
  if pycor != -110 and nextcolor = blue or nextcolor = 115 and [nextcolor] of patch-at -1 0 = white
  [
    ask patch-at -1 0
    [set nextcolor [nextcolor] of myself]
    set nextcolor white
  ]
end

to moveright
  if pycor != -110 and nextcolor = blue or nextcolor = 115 and [nextcolor] of patch-at 1 0 = white
  [
    ask patch-at 1 0
    [set nextcolor [nextcolor] of myself]
    set nextcolor white
  ]
end

to moveWater
  set nextcolor pcolor
  if pycor = -88 or pxcor = 118 or pxcor = -118
  [set nextcolor white]
  if pycor != -88 and nextcolor = blue or nextcolor = violet and [nextcolor] of patch-at 0 -1 = white
  [
    ask patch-at 0 -1
    [set nextcolor [nextcolor] of myself]
    set nextcolor white
  ]
  ifelse random 2 = 0
  [moveleft]
  [moveright]
  ifelse pxcor > lowestpatch
  [moveleft]
  [moveright]
  if pcolor = blue and any? thoughtBubbles in-radius 5
  [
    set pcolor white
    ask min-one-of thoughtBubbles [distance myself]
    [set water-in (water-in + 1)]
  ]
  if pcolor = blue and any? endgoals in-radius 5
  [
    set pcolor white
    ask endgoals
    [set water-in (water-in + 1)]
  ]
end

to execute [agents]
end

to-report psetHue [hue]
  set pcolor hue
  report false
end

to-report psetnextHue [hue]
  set nextcolor hue
  report false
end

to move-water
  let watar patches with [pcolor = blue or pcolor = violet]
  let lowestpatchycor min [pycor] of watar
  let highestpatchycor max [pycor] of watar
  set lowestpatch one-of [pxcor] of watar with [pycor = lowestpatchycor]
  execute patches with [psetnextHue pcolor]
  repeat highestpatchycor - lowestpatchycor + 1
  [
    ask watar with [pycor = lowestpatchycor]
    [moveWater]
    set lowestpatchycor lowestpatchycor + 1
  ]
  execute patches with [(nextcolor = blue or nextcolor = white or nextcolor = violet) and psetHue nextcolor]
  tick
end

to broccoli
  ask patches with [pcolor = 54] [
    if any? neighbors with [pcolor = blue] [
      ask one-of neighbors with [pcolor = blue]
      [set pcolor 54]
    ]
  ]
end

to lava
  ask patches with [pcolor = 15 or pcolor = 21 or pcolor = 24 or pcolor = 13] [
    set nextcolor pcolor
    if [pcolor] of patch-at 0 -1 = white
    [ask patch-at 0 -1
      [set pcolor [nextcolor] of myself]
    set nextcolor white
    set pcolor nextcolor]
    if any? neighbors4 with [pcolor = blue] [
      ask neighbors4 with [pcolor = blue]
      [
        sprout-steams 1 [
          set shape "circle"
          set size 2
          set color 5
          set heading 0
        ]
      set pcolor white      ]

    ]
    if any? neighbors with [pcolor = 54] [
      ask neighbors with [pcolor = 54] [
        if any? neighbors with [pcolor = 54]
        [ask neighbors with [pcolor = 54] [
          if any? neighbors with [pcolor = 54]
          [ask neighbors with [pcolor = 54] [
            if any? neighbors with [pcolor = 54]
            [ask neighbors with [pcolor = 54] [
              if any? neighbors with [pcolor = 54]
              [ask neighbors with [pcolor = 54] [
                set pcolor 52]]
              set pcolor 52]]
            set pcolor 52]]
          set pcolor 52]]
        set pcolor 52]
      ask patches with [pcolor = 52]
      [set pcolor white]
    ]
  ]
end

to poison
  ask patches with [pcolor = violet] [
    if any? neighbors4 with [pcolor = blue] [
      ask one-of neighbors4 with [pcolor = blue]
      [set pcolor 115]
    ]
    if any? thoughtBubbles in-radius 5 [
      set thoughtbubbleleft (thoughtbubbleleft - 1)
      ask min-one-of thoughtBubbles [distance myself]
      [hatch-danger 1 [
          set shape "face sad"
          set color sky]
      die]
    ]
    if any? endgoals in-radius 5 [
      ask endgoals
      [set dangerpoints (dangerpoints + 1)]
    ]
  ]
end

to ice
  ask patches with [pcolor = cyan] [
    if any? neighbors4 with [pcolor = blue] [
      ask one-of neighbors4 with [pcolor = blue]
      [set pcolor cyan]
    ]
    if any? steams in-radius 2 [
      ask one-of steams in-radius 2
      [set pcolor blue
        die]
    ]
    if [pcolor] of patch-at 0 1 = 15 or [pcolor] of patch-at 0 1 = 21 or
    [pcolor] of patch-at 0 1 = 24 or [pcolor] of patch-at 0 1 = 13
    [ask patch-at 0 1 [
    set pcolor white]
    set pcolor white]
  ]
end

to steaming
  ask steams [
    every 1 / 30 [
      if ycor > 87 or xcor > 118 or xcor < -118 [die]
      if [pcolor] of patch-at 0 1 = 9.9 or [pcolor] of patch-at 0 1 = blue
      [fd 1]
      ifelse [pcolor] of patch-at 1 1 = 9.9 or [pcolor] of patch-at 0 1 = blue
        [rt 90 fd 1 lt 90 fd 1]
        [ifelse [pcolor] of patch-at -1 1 = 9.9 or [pcolor] of patch-at 0 1 = blue
          [lt 90 fd 1 rt 90 fd 1]
          [if [pcolor] of patch-at 0 1 = 9.9 and [pcolor] of patch-at 1 0 = 9.9
            or [pcolor] of patch-at 0 1 = blue
            [rt random 21 - 10
              fd 1
              set heading 0]
          ]
        ]
      ]
    ]
end

to pipe
 ask patches with [pcolor = 4.7]
  [if [pcolor] of patch-at 0 1 = white [
      sprout-water random 5
      [
        set color cyan
        set xspeed -7
        set yspeed 3.5 + random-float 1
        set shape "circle"
        set size 1
      ]
    ]
  ]
end

to water-turtle-properties
  ask water [
    set nextycor (ycor + yspeed)
    set nextxcor (xcor + xspeed)
    set yspeed (yspeed - g)
    checkGround
    setxy nextxcor nextycor
  ]
end

to checkGround
  if nextycor > 90 or abs nextxcor > 120[
      ask patch-here
      [set pcolor cyan]
      die
  ]

  if [pcolor] of patch nextxcor nextycor = black or [pcolor] of patch nextxcor nextycor = magenta
    [
      ask patch-here
      [set pcolor cyan]
      die
    ]

end
@#$#@#$#@
GRAPHICS-WINDOW
210
10
702
403
120
90
2.0
1
10
1
1
1
0
0
0
1
-120
120
-90
90
1
1
1
ticks
30.0

BUTTON
10
28
84
61
Setup
setup
NIL
1
T
OBSERVER
NIL
S
NIL
NIL
1

BUTTON
94
28
174
61
PLAY :)
play
NIL
1
T
OBSERVER
NIL
NIL
NIL
NIL
1

CHOOSER
13
66
151
111
chooseLevel
chooseLevel
"Tutorial" "Level 1" "Level 2"
1

MONITOR
5
121
207
174
Total Thought Bubbles Collected
point
0
1
13

MONITOR
5
178
206
231
Thought Bubbles Left
thoughtbubbleleft
0
1
13

@#$#@#$#@
# Features and Directions
## Story:

Single player puzzle game dedicated to Stuyvesant High School’s Computer Science Department 2015 Halloween collaboration on Inside Out.

The game is staged in Memory Dump. The objective of the game is to move a sufficient amount of water to the end goal (Riley’s mind), based on a path created by moving debris away (by clicking on the debris). Three thought bubbles will be dispersed in each level. Each thought bubble will require a certain amount of water to retrieve, and at least one thought must be collected to proceed to the next level. The game will involve a tutorial and multiple levels, each with progressing difficulty.

Warning: Due to netlogo's slow capabilities when faced with wide patches and long code (and the programmers' inability to make the code any faster), this game will require A LOT of patience. (There is no map for pipe) Best of luck!

## Directions:
1. Press Setup
2. Press PLAY :)
3. Click on the debris (black patches) and bring water to at least one thought bubble, then to the end goal in order to clear the level. Collect as many thought bubbles as you can!

## Rules:
*Clearing the level requires collecting at least one thought bubble and clearing the end goal
>*10 drops of water are required to collect a thought bubble
>*25 drops of water are required to clear the end goal

*Water cannot pass through the hippocampus, and is affected by gravity and surface tension (has a tendancy to fall and takes the shape of its container).
*Debris will clear upon clicking it
*Be careful of each element: some are helpful, some are harmful (see Features below)

## References Explained

*Thought bubbles are memory orbs, where red is Anger, green is Disgust, sky is Sadness, and yellow is Joy
*End goal is Bing Bong's bag
*Green thing (with pcolor of 54) that changes water into it, aka broccoli, is one of the main foods that Riley dislikes (careful!)
*Lava (pcolor 13,15,21,24) is part of Riley's imagination as a child, where she jumps on top of chairs, tables, sofas, etc. to avoid the lava floor

## Features:
*Debris (black patch)
*Hippocampus (magenta patch)
*Thought bubbles (red, blue, green, or yellow turtle)
*End goal (star shaped turtle)

Elements:
*Water (blue patch) :
-able to move
-takes the shape of the container underneath it
-becomes ice when in contact with ice
-becomes broccoli when in contact with broccoli
-becomes steam when in contact with lava
-becomes poison when in contact with poison

*Broccoli (greenish (pcolor 54) patch) :
-unable to move
-changes any water it comes in contact with to broccoli
-burns (dies/ becomes white) when in contact with lava

*Lava (patch with pcolor 13, 15, 21, or 24)
-unable to move
-when in contact with water, changes the water it comes in contact to to steam
-when in contact with broccoli, burns the broccoli (the broccoli patches become white, lava does not increase)
-will move down if the patch underneath it is white
-when in contact with ice, evaporates the ice (set ice pcolor to white), but is simultaneously drowned by ice (pcolor of myself becomes white)

*Steam (gray turtle)
-able to move
-created when water comes into contact with lava (or alternatively can show up in the level as coded by the programmers)
-becomes water when in contact with ice

*Poison (violet patch) :
-able to move
-takes the shape of the container underneath it
-when in contact with water, changes the water it comes in contact to to poison
-when in contact with a thought bubble, automatically kills the bubble
-automatically causes the user to lose the game if poison comes into contact with the endgoal

*Ice (cyan patch):
-unable to move
-when in contact with steam, changes the steam it comes in contact to to liquid water
-when in contact with water, changes the water it comes in contact to to ice (and increases the amount of ice)
-when in contact with lava, drowns the lava (set lava pcolor to white) but is simultaneously evaporated (pcolor of myself becomes white)

## Development Log
## 01-11-2016
>Added Features
*Water
*thoughtBubbles
*endgoal

####Together
*Created the Setup and Play buttons
*Created breeds for water, thoughtBubbles, and endgoals
*Started setWater (turtle context)

## 01-12-2016
####Together
*Created tutorial map
*Created setEndgoal command

## 01-13-2016
>Added Features
*Debris

####Lydia
*Finished debris command (clears the debris upon clicking it)
*Began the appearance of thought bubbles (setThoughtBubbles command)

####Irene
*Began water surfaceTension (with water as turtles)
*Began setWater commands (with water as turtles)

###Known Bugs
*Moving the mouse too fast creates squares througout the debris with large gaps in between, largely attributed to the commands (and Netlogo) being unable to keep up with the speed of the mouse (Netlogo does not have a function to continuously hold the mouse down, thus there is a pause in time after each click)

## 01-14-2016
####Lydia
*Began collectThoughts command (only for when water is a turtle)
*Began win conditions (only for when water is a turtle)
*Created commands to set the next level (choose-this-level chooser, nextLevel and import-this-level)

####Irene
*Changed water from turtle context to patche context (based on the Netlogo sand model)
*Revised surfaceTension (gravity) allowing the "water" to level
*Added preliminary conditions for water under Setup and Play
*Added ticks

###Known Bugs
*Circles are created throughout if the mouse is moved too fast bug still present

## 01-15-2016
####Lydia
*Modified thought bubble properties to clear when water are patches

####Irene
*Set conditions for tutorial (location of thoughtBubbles, endgoal)
*Made the code more readable (removed import-this-level, revised setup)

###Known Bugs
*Circles are created throughout if the mouse is moved too fast bug still present
*Water patches appear more like sand, will not splash and has a tendancy to stick to the container edges made by dragging the mouse through the debris

## 01-18-2016
####Together
*Modified end goal properties to clear when water are patches
*Set thought bubble tutorial location, and conditions for disappearing
*Set end goal tutorial location and conditions for disappearing

## 01-19-2016
>Added Features
*Broccoli

####Irene
*Finalized conditions for when end goal will die
*Revised the code to automatically continue to the next level upon clearing the previous level
*Added monitors for Total Thought Bubbles Collected and Thought Bubbles Left
*Began and finished conditions for broccoli
*Tested conditions for broccoli

###Known Bugs
*Run time error on min [pxcor] of targets after clearing tutorial and attempting to import Level 1
*Water sand similarites bug is still present
*Circles are created throughout if the mouse is moved too fast bug still present

## 01-20-2016
>Added Features
*Lava
*Steam
*Pipe

####Lydia
*Began making maps for broccoli and pipes
*Used Mr. K's code on website for parabolic motion for pipes (changed variables to work)

####Irene
*Set conditions for lava when in contact with water and broccoli (untested)
*Began code for steam

###Known Bugs
*Pipe command does not work (water is motionless)
*Water sprouts and just stays static
*Water sand similarites bug is still present
*Circles are created throughout if the mouse is moved too fast bug still present

## 01-21-2016
####Lydia
*Updated pipe code so there is movement for the water (xspeed and yspeed were 0)

####Irene
*Set conditions for steam (sprouting as turtles)
*Added user message in winlose command
*Tested lava and steam

###Known Bugs
*Steam will attempt to move around the water patches
*Water goes outside of the window when running pipe
*Water sand similarites bug is still present
*Circles are created throughout if the mouse is moved too fast bug still present

## 01-22-2016
####Lydia
*Changed numbers to make pipe water look more realistic

####Irene
*Adjusted image size and colors to correspond with code
*Began poison command (in patch context)
*Hippocampus is now magenta (poison is violet)
*Tested code (see Known Bugs)

###Known Bugs
*Same pipe problem as 01-21-2016
*Try again does not work properly (i.e. some water patches have a color not cyan, preventing them from being affected by the water commands)
*Tutorial causes an error when completing the level to move to level 1
*Steam will attempt to move around the water patches bug still present
*Water sand similarites bug is still present
*Circles are created throughout if the mouse is moved too fast bug still present

##01-23-2016
>Added Features
*Poison

####Irene
*Finished poison command and conditions (ex: all blue patches in contact with poison becomes poison)
*Changed code in regards to poison (modified winlose conditions, water movement command, thoughtbubble conditions, endgoal conditions, correctColor)

###Known Bugs
*Same pipe problem as 01-21-2016
*Try again does not work properly (i.e. some water patches have a color not cyan, preventing them from being affected by the water commands)
*Tutorial causes an error when completing the level to move to level 1
*Steam will attempt to move around the water patches
*Water sand similarites bug is still present
*Circles are created throughout if the mouse is moved too fast bug still present

##01-24-2016
>Added Features
*Ice

####Lydia
*Added orb decoration to magenta walls

####Irene
*Finished ice command conditions (adjusted all of the code to make water blue and ice cyan)
*Added conditions to lava, broccoli, and steam in accordance with ice
*Added more conditions to lava and steam (ex: lava will move down if the patch underneath it is white)
*Wrote explanations on the info tab (story, direction, references, features, things to try, related models, credits)
*Designed end goal/ Bing Bong's bag
*Adjusted image pictures, and location of thoughtBubbles and endgoal in relation to map size
*Designed Level 1 and Level 2, created map in Paint, set thoughtBubble positions, endgoal position
*Added congratulations user message upon finishing the last level
*Fixed bug on try again
*Fixed bug preventing tutorial from moving to level 1
*Final testing on game

###Known Bugs
*Steam will attempt to move around the water patches
*Water sand similarites bug is still present
*Circles are created throughout if the mouse is moved too fast bug still present

## THINGS TO TRY
*Pipes will shoot a certain substance (i.e. water, lava, broccoli) depending on the pipe. The amount of the substance from pipes is infinite.
*Store that allows the user to purchase more backgrounds using the thought bubbles they collected (ex: the color of concrete, the pipes, and mud), purchase a skip-level (that allows the user to skip one level), etc
*More elements
Wind: pushes steam to a certain direction, doesn’t affect the other elements
Mud: becomes debris if not in contact with water for 7 seconds; when in contact with water, changes the water it comes in contact to to mud
*Barriers that open if water reaches the key (a block located elsewhere on the screen that is able to sense when water touches the key)
*Reversing gravity (ex: water floats up, steam sinks)

## RELATED MODELS

*Sand (Under the Chemistry & Physics folder)

## CREDITS AND REFERENCES

Brought to you by Bubbles (Irene Lam and Lydia Zhang)
*Huge thanks to Patrick Chan for his hours of advice and contributions to the water function, making the general code faster, and technical difficulties (i.e. user-message)

*Special thanks to the CS Dojo for moral support :)
@#$#@#$#@
default
true
0
Polygon -7500403 true true 150 5 40 250 150 205 260 250

airplane
true
0
Polygon -7500403 true true 150 0 135 15 120 60 120 105 15 165 15 195 120 180 135 240 105 270 120 285 150 270 180 285 210 270 165 240 180 180 285 195 285 165 180 105 180 60 165 15

arrow
true
0
Polygon -7500403 true true 150 0 0 150 105 150 105 293 195 293 195 150 300 150

bing bong's bag
true
15
Polygon -8630108 true false 15 90 60 135 105 150 195 150 255 120 285 90 300 120 300 180 270 240 240 270 195 300 165 300 120 300 60 270 30 240 15 210 0 180 0 120 15 90
Polygon -7500403 false false 0 105 15 90
Circle -2674135 true false 210 180 30
Line -7500403 false 240 195 270 210
Rectangle -13791810 true false 45 195 90 210
Polygon -7500403 true false 45 195 30 195 30 210 45 210
Polygon -7500403 true false 105 195 90 195 90 210 105 210
Circle -955883 true false 60 225 30
Polygon -7500403 true false 90 240 105 240 105 225 90 240 105 255 105 240
Polygon -7500403 true false 60 240 45 240 45 255 60 240 45 225 45 240
Circle -13840069 true false 15 135 30
Polygon -7500403 true false 15 150 0 150 0 165 15 150 0 135 0 150
Polygon -7500403 true false 45 150 60 150 60 135 45 150 60 165 60 150
Rectangle -2064490 true false 165 240 180 285
Polygon -7500403 true false 180 285 165 285 165 300 180 300
Polygon -7500403 true false 180 225 165 225 165 240 180 240
Line -7500403 false 120 270 150 240
Circle -14835848 true false 105 255 30
Circle -1184463 true false 240 135 30
Polygon -7500403 true false 270 150 285 135 285 165 270 150
Polygon -7500403 true false 240 150 225 150 225 165 240 150 225 135 225 150
Polygon -955883 true false 210 255 210 240 240 255 210 270 210 240
Polygon -2674135 true false 30 180 15 180 15 195 30 180
Polygon -11221820 true false 255 180 270 165 285 195
Polygon -2064490 true false 120 210 135 240 135 210
Polygon -5825686 true false 75 270 90 255 90 285
Circle -11221820 true false 135 165 30
Polygon -7500403 true false 165 180 180 180 180 165 165 180 180 195 180 180
Polygon -7500403 true false 135 180 120 180 120 195 135 180 120 165 120 180
Polygon -14835848 true false 75 180 90 180 90 165

box
false
0
Polygon -7500403 true true 150 285 285 225 285 75 150 135
Polygon -7500403 true true 150 135 15 75 150 15 285 75
Polygon -7500403 true true 15 75 15 225 150 285 150 135
Line -16777216 false 150 285 150 135
Line -16777216 false 150 135 15 75
Line -16777216 false 150 135 285 75

bug
true
0
Circle -7500403 true true 96 182 108
Circle -7500403 true true 110 127 80
Circle -7500403 true true 110 75 80
Line -7500403 true 150 100 80 30
Line -7500403 true 150 100 220 30

butterfly
true
0
Polygon -7500403 true true 150 165 209 199 225 225 225 255 195 270 165 255 150 240
Polygon -7500403 true true 150 165 89 198 75 225 75 255 105 270 135 255 150 240
Polygon -7500403 true true 139 148 100 105 55 90 25 90 10 105 10 135 25 180 40 195 85 194 139 163
Polygon -7500403 true true 162 150 200 105 245 90 275 90 290 105 290 135 275 180 260 195 215 195 162 165
Polygon -16777216 true false 150 255 135 225 120 150 135 120 150 105 165 120 180 150 165 225
Circle -16777216 true false 135 90 30
Line -16777216 false 150 105 195 60
Line -16777216 false 150 105 105 60

car
false
0
Polygon -7500403 true true 300 180 279 164 261 144 240 135 226 132 213 106 203 84 185 63 159 50 135 50 75 60 0 150 0 165 0 225 300 225 300 180
Circle -16777216 true false 180 180 90
Circle -16777216 true false 30 180 90
Polygon -16777216 true false 162 80 132 78 134 135 209 135 194 105 189 96 180 89
Circle -7500403 true true 47 195 58
Circle -7500403 true true 195 195 58

circle
false
0
Circle -7500403 true true 0 0 300

circle 2
false
0
Circle -7500403 true true 0 0 300
Circle -16777216 true false 30 30 240

cow
false
0
Polygon -7500403 true true 200 193 197 249 179 249 177 196 166 187 140 189 93 191 78 179 72 211 49 209 48 181 37 149 25 120 25 89 45 72 103 84 179 75 198 76 252 64 272 81 293 103 285 121 255 121 242 118 224 167
Polygon -7500403 true true 73 210 86 251 62 249 48 208
Polygon -7500403 true true 25 114 16 195 9 204 23 213 25 200 39 123

cylinder
false
0
Circle -7500403 true true 0 0 300

dot
false
0
Circle -7500403 true true 90 90 120

face happy
false
0
Circle -7500403 true true 8 8 285
Circle -16777216 true false 60 75 60
Circle -16777216 true false 180 75 60
Polygon -16777216 true false 150 255 90 239 62 213 47 191 67 179 90 203 109 218 150 225 192 218 210 203 227 181 251 194 236 217 212 240

face neutral
false
0
Circle -7500403 true true 8 7 285
Circle -16777216 true false 60 75 60
Circle -16777216 true false 180 75 60
Rectangle -16777216 true false 60 195 240 225

face sad
false
0
Circle -7500403 true true 8 8 285
Circle -16777216 true false 60 75 60
Circle -16777216 true false 180 75 60
Polygon -16777216 true false 150 168 90 184 62 210 47 232 67 244 90 220 109 205 150 198 192 205 210 220 227 242 251 229 236 206 212 183

fish
false
0
Polygon -1 true false 44 131 21 87 15 86 0 120 15 150 0 180 13 214 20 212 45 166
Polygon -1 true false 135 195 119 235 95 218 76 210 46 204 60 165
Polygon -1 true false 75 45 83 77 71 103 86 114 166 78 135 60
Polygon -7500403 true true 30 136 151 77 226 81 280 119 292 146 292 160 287 170 270 195 195 210 151 212 30 166
Circle -16777216 true false 215 106 30

flag
false
0
Rectangle -7500403 true true 60 15 75 300
Polygon -7500403 true true 90 150 270 90 90 30
Line -7500403 true 75 135 90 135
Line -7500403 true 75 45 90 45

flower
false
0
Polygon -10899396 true false 135 120 165 165 180 210 180 240 150 300 165 300 195 240 195 195 165 135
Circle -7500403 true true 85 132 38
Circle -7500403 true true 130 147 38
Circle -7500403 true true 192 85 38
Circle -7500403 true true 85 40 38
Circle -7500403 true true 177 40 38
Circle -7500403 true true 177 132 38
Circle -7500403 true true 70 85 38
Circle -7500403 true true 130 25 38
Circle -7500403 true true 96 51 108
Circle -16777216 true false 113 68 74
Polygon -10899396 true false 189 233 219 188 249 173 279 188 234 218
Polygon -10899396 true false 180 255 150 210 105 210 75 240 135 240

house
false
0
Rectangle -7500403 true true 45 120 255 285
Rectangle -16777216 true false 120 210 180 285
Polygon -7500403 true true 15 120 150 15 285 120
Line -16777216 false 30 120 270 120

leaf
false
0
Polygon -7500403 true true 150 210 135 195 120 210 60 210 30 195 60 180 60 165 15 135 30 120 15 105 40 104 45 90 60 90 90 105 105 120 120 120 105 60 120 60 135 30 150 15 165 30 180 60 195 60 180 120 195 120 210 105 240 90 255 90 263 104 285 105 270 120 285 135 240 165 240 180 270 195 240 210 180 210 165 195
Polygon -7500403 true true 135 195 135 240 120 255 105 255 105 285 135 285 165 240 165 195

line
true
0
Line -7500403 true 150 0 150 300

line half
true
0
Line -7500403 true 150 0 150 150

pentagon
false
0
Polygon -7500403 true true 150 15 15 120 60 285 240 285 285 120

person
false
0
Circle -7500403 true true 110 5 80
Polygon -7500403 true true 105 90 120 195 90 285 105 300 135 300 150 225 165 300 195 300 210 285 180 195 195 90
Rectangle -7500403 true true 127 79 172 94
Polygon -7500403 true true 195 90 240 150 225 180 165 105
Polygon -7500403 true true 105 90 60 150 75 180 135 105

plant
false
0
Rectangle -7500403 true true 135 90 165 300
Polygon -7500403 true true 135 255 90 210 45 195 75 255 135 285
Polygon -7500403 true true 165 255 210 210 255 195 225 255 165 285
Polygon -7500403 true true 135 180 90 135 45 120 75 180 135 210
Polygon -7500403 true true 165 180 165 210 225 180 255 120 210 135
Polygon -7500403 true true 135 105 90 60 45 45 75 105 135 135
Polygon -7500403 true true 165 105 165 135 225 105 255 45 210 60
Polygon -7500403 true true 135 90 120 45 150 15 180 45 165 90

poison
false
0
Circle -16777216 true false 0 0 300

sheep
false
15
Circle -1 true true 203 65 88
Circle -1 true true 70 65 162
Circle -1 true true 150 105 120
Polygon -7500403 true false 218 120 240 165 255 165 278 120
Circle -7500403 true false 214 72 67
Rectangle -1 true true 164 223 179 298
Polygon -1 true true 45 285 30 285 30 240 15 195 45 210
Circle -1 true true 3 83 150
Rectangle -1 true true 65 221 80 296
Polygon -1 true true 195 285 210 285 210 240 240 210 195 210
Polygon -7500403 true false 276 85 285 105 302 99 294 83
Polygon -7500403 true false 219 85 210 105 193 99 201 83

square
false
0
Rectangle -7500403 true true 30 30 270 270

square 2
false
0
Rectangle -7500403 true true 30 30 270 270
Rectangle -16777216 true false 60 60 240 240

star
false
0
Polygon -7500403 true true 151 1 185 108 298 108 207 175 242 282 151 216 59 282 94 175 3 108 116 108

target
false
0
Circle -7500403 true true 0 0 300
Circle -16777216 true false 30 30 240
Circle -7500403 true true 60 60 180
Circle -16777216 true false 90 90 120
Circle -7500403 true true 120 120 60

tree
false
0
Circle -7500403 true true 118 3 94
Rectangle -6459832 true false 120 195 180 300
Circle -7500403 true true 65 21 108
Circle -7500403 true true 116 41 127
Circle -7500403 true true 45 90 120
Circle -7500403 true true 104 74 152

triangle
false
0
Polygon -7500403 true true 150 30 15 255 285 255

triangle 2
false
0
Polygon -7500403 true true 150 30 15 255 285 255
Polygon -16777216 true false 151 99 225 223 75 224

truck
false
0
Rectangle -7500403 true true 4 45 195 187
Polygon -7500403 true true 296 193 296 150 259 134 244 104 208 104 207 194
Rectangle -1 true false 195 60 195 105
Polygon -16777216 true false 238 112 252 141 219 141 218 112
Circle -16777216 true false 234 174 42
Rectangle -7500403 true true 181 185 214 194
Circle -16777216 true false 144 174 42
Circle -16777216 true false 24 174 42
Circle -7500403 false true 24 174 42
Circle -7500403 false true 144 174 42
Circle -7500403 false true 234 174 42

turtle
true
0
Polygon -10899396 true false 215 204 240 233 246 254 228 266 215 252 193 210
Polygon -10899396 true false 195 90 225 75 245 75 260 89 269 108 261 124 240 105 225 105 210 105
Polygon -10899396 true false 105 90 75 75 55 75 40 89 31 108 39 124 60 105 75 105 90 105
Polygon -10899396 true false 132 85 134 64 107 51 108 17 150 2 192 18 192 52 169 65 172 87
Polygon -10899396 true false 85 204 60 233 54 254 72 266 85 252 107 210
Polygon -7500403 true true 119 75 179 75 209 101 224 135 220 225 175 261 128 261 81 224 74 135 88 99

wheel
false
0
Circle -7500403 true true 3 3 294
Circle -16777216 true false 30 30 240
Line -7500403 true 150 285 150 15
Line -7500403 true 15 150 285 150
Circle -7500403 true true 120 120 60
Line -7500403 true 216 40 79 269
Line -7500403 true 40 84 269 221
Line -7500403 true 40 216 269 79
Line -7500403 true 84 40 221 269

wolf
false
0
Polygon -16777216 true false 253 133 245 131 245 133
Polygon -7500403 true true 2 194 13 197 30 191 38 193 38 205 20 226 20 257 27 265 38 266 40 260 31 253 31 230 60 206 68 198 75 209 66 228 65 243 82 261 84 268 100 267 103 261 77 239 79 231 100 207 98 196 119 201 143 202 160 195 166 210 172 213 173 238 167 251 160 248 154 265 169 264 178 247 186 240 198 260 200 271 217 271 219 262 207 258 195 230 192 198 210 184 227 164 242 144 259 145 284 151 277 141 293 140 299 134 297 127 273 119 270 105
Polygon -7500403 true true -1 195 14 180 36 166 40 153 53 140 82 131 134 133 159 126 188 115 227 108 236 102 238 98 268 86 269 92 281 87 269 103 269 113

x
false
0
Polygon -7500403 true true 270 75 225 30 30 225 75 270
Polygon -7500403 true true 30 75 75 30 270 225 225 270

@#$#@#$#@
NetLogo 5.0.2
@#$#@#$#@
@#$#@#$#@
@#$#@#$#@
@#$#@#$#@
@#$#@#$#@
default
0.0
-0.2 0 0.0 1.0
0.0 1 1.0 0.0
0.2 0 0.0 1.0
link direction
true
0
Line -7500403 true 150 150 90 180
Line -7500403 true 150 150 210 180

@#$#@#$#@
0
@#$#@#$#@
