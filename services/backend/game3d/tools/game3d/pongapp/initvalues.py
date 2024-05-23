## Field dimensions

FIELD_WIDTH = 400
FIELD_HEIGHT = 200

## Ball initial values

BALL_POSITION_X = 0
BALL_POSITION_Y = 0
BALL_DIR_X = 1
BALL_DIR_Y = 1
BALL_SPEED = 4

## Paddle1 initial values

PADDLE1_WIDTH = 10
PADDLE1_HEIGHT = 30
PADDLE1_DIMINISHED_HEIGHT = 20;
PADDLE1_AUGMENTED_HEIGHT = 40;
PADDLE1_POSITION_X = -FIELD_WIDTH / 2 + PADDLE1_WIDTH
PADDLE1_DIR_Y = 0
PADDLE1_SPEED = 8
PADDLE1_SCORE = 0

## Paddle2 initial values

PADDLE2_WIDTH = 10
PADDLE2_HEIGHT = 30
PADDLE2_DIMINISHED_HEIGHT = 20;
PADDLE2_AUGMENTED_HEIGHT = 40;
PADDLE2_POSITION_X = FIELD_WIDTH / 2 - PADDLE2_WIDTH
PADDLE2_DIR_Y = 0
PADDLE2_SPEED = 8
PADDLE2_SCORE = 0

## Party settings

SMALL_LIMIT_SCORE = 4
MID_LIMIT_SCORE = 7
LONG_LIMIT_SCORE = 11

## Power-Ups

PU_NO = 0
PU_ON_FIELD = 1 
PU_ON_PLAYER = 2 

SELF_BALL_ACCEL = 0 
OTHER_SMALL_PADDLE = 1 
SELF_BIG_PADDLE = 2 
OTHER_UP_VIEW = 3
NONE_PU = 4

## Power-Ups Locations

NORTH_WEST = '0'
NORTH = '1'
NORTH_EAST = '2' 
WEST = '3' 
CENTER = '4' 
EAST = '5'
SOUTH_WEST = '6' 
SOUTH = '7' 
SOUTH_EAST = '8'

DEFAULT_PU_LOC = 1000 
PU_OFFSET = 15
