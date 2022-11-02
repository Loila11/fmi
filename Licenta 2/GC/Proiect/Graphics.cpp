#ifdef __APPLE__
#include <GLUT/glut.h>
#include <iostream>
#else
#include <GL/glut.h>
#endif

#include "Graphics.h"
#include <cmath>

double PI = acos(-1.0);
double ANGLE_STEP      = PI/180.0;

void setColor(double red, double green, double blue) {
     glColor3d(red, green, blue);
}

void quitKey(unsigned char key, int x, int y) {
#ifdef __APPLE__
     if (key == 'q') std::exit(0);
#else
     if (key == 'q') exit(0);
#endif
}

void graphicsSetup(int argc, char **argv) {
     glutInit(&argc, argv);
     glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA);
	 glutInitWindowPosition(WINDOW_X,WINDOW_Y);
	 glutInitWindowSize(WINDOW_HEIGHT,WINDOW_WIDTH);
	 glutCreateWindow("COSC1315 - Graphics Lab");
	 glClearColor(WHITE,0.0);
	 gluOrtho2D(0,WINDOW_WIDTH, 0,WINDOW_HEIGHT);
     glutKeyboardFunc(quitKey);
  }

void clearWindow() {
     glClear(GL_COLOR_BUFFER_BIT);
}

void drawTriangle(double x1, double y1, double x2, double y2, double x3, double y3) {
     glBegin(GL_LINE_STRIP);
     glVertex2i(x1,y1);
     glVertex2i(x2,y2);
     glVertex2i(x3,y3);
     glVertex2i(x1,y1);
     glEnd();
     glFlush();
}

void drawFilledTriangle(double x1, double y1, double x2, double y2, double x3, double y3) {
     glBegin(GL_POLYGON);
     glVertex2i(x1,y1);
     glVertex2i(x2,y2);
     glVertex2i(x3,y3);
     glVertex2i(x1,y1);
     glEnd();
     glFlush();
}

void drawLine(double x1, double y1, double x2, double y2) {
     glBegin(GL_LINE_STRIP);
     glVertex2i(x1,y1);
     glVertex2i(x2,y2);
     glEnd();
     glFlush();
}

void drawBox(double x1, double y1, double x2, double y2) {
     glBegin(GL_LINE_STRIP);
     glVertex2i(x1,y1);
     glVertex2i(x2,y1);
     glVertex2i(x2,y2);
     glVertex2i(x1,y2);
     glVertex2i(x1,y1);
     glEnd();
     glFlush();
}

void drawFilledBox(double x1, double y1, double x2, double y2) {
     glBegin(GL_POLYGON);
     glVertex2i(x1,y1);
     glVertex2i(x2,y1);
     glVertex2i(x2,y2);
     glVertex2i(x1,y2);
     glVertex2i(x1,y1);
     glEnd();
     glFlush();
}

void drawCircle(double x1, double y1, double radius) {
     double angle;
     double X, Y;
     glBegin(GL_LINE_STRIP);
     for (angle=0;angle< 2.0*PI + ANGLE_STEP; angle += ANGLE_STEP) {
         X = x1 + double(double(radius) * cos(angle));
         Y = y1 + double(double(radius) * sin(angle));
         glVertex2i(X,Y);
     }
     glEnd();
     glFlush();
}         

void drawFilledCircle(double x1, double y1, double radius) {
     double angle;
     double X0, Y0, X1, Y1;
     glBegin(GL_TRIANGLES);
     X1 = x1 + radius;
     Y1 = y1;
     for (angle=0;angle< 2.0*PI + ANGLE_STEP; angle += ANGLE_STEP) {
         X0 = X1;
         Y0 = Y1;
         X1 = x1 + double(double(radius) * cos(angle));
         Y1 = y1 + double(double(radius) * sin(angle));
         glVertex2i(x1,y1);
         glVertex2i(X0,Y0);
         glVertex2i(X1,Y1);
     }
     glEnd();
     glFlush();
}         

