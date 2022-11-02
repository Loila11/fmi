#ifndef GRAPHICS_H
#define GRAPHICS_H

// set the drawing screen dimensions and position
#define WINDOW_HEIGHT    500.0
#define WINDOW_WIDTH    500.0
#define WINDOW_X        100.0
#define WINDOW_Y        100.0

// set the pre-defined colors
#define WHITE           1.0,1.0,1.0
#define BLACK           0.0,0.0,0.0
#define RED             1.0,0.0,0.0
#define BLUE            0.0,0.0,1.0
#define GREEN           0.0,1.0,0.0
#define GREY            1.0,0.5,0.0
#define PURPLE          0.5,0.0,0.5
#define FOREST_GREEN    0.0,0.25,0.0
#define MIDNIGHT_BLUE   0.0,0.0,0.25
#define CYAN            0.0,1.0,1.0
#define MAGENTA         1.0,0.0,1.0
#define YELLOW          1.0,0.5,0.0
#define BROWN           0.5,0.25,0.0

// initialization routine
void graphicsSetup(int argc, char **argv);
void drawScene(void);
void clearWindow(void);

// set line or fill color
void setColor(double red, double green, double blue);

// graphic object primatives
void drawTriangle(double x1, double y1,double x2,double y2,double x3,double y3);
void drawLine(double x1, double y1, double x2, double y2);
void drawBox(double x1, double y1, double x2, double y2);
void drawCircle(double x1, double y1, double radius);

// filled graphics primatives
void drawFilledTriangle(double x1, double y1,double x2,double y2,double x3,double y3);
void drawFilledBox(double x1, double y1, double x2, double y2);
void drawFilledCircle(double x1, double y1, double radius);


#endif
