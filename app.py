"""
Created on Sat Aug 10 12:10:40 2019

@author: Minixtrator@gmail.com
         ADMINIXTRATOR @Aang Studios
"""

import matplotlib.pyplot as plt
import matplotlib.tri as tri
import matplotlib.cm as cm
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

plt.style.use('default')

#   lOOP pOINT-----------------
while True:
    print('''\n\t -----------------------\n\t| MATPLOTLIB CARDINATOR |
\t -----------------------\n\n
****This is an evaluation build of the Matplotlib Cardinator v1.0****\n\n''')

    print('''\n Created by: ADMINIXTRATOR             Date: 28th August, 2019
 Twitter: Adminixtrator                Email: minixtrator@gmail.com\n\n''')

    print('''[1.] Random Graph\n[2.] Line Graph \n[3.] Pie Chart\n[4.] Bar Chart\n[5.] Histogram\n[6.] Scatter plot\n[7.] Box plot
[8.] Triangulation Plot\n\n****Coming Soon****\n[9.] 3D Plot\n[10.] Plot from File\n''')
    #   QUERY-----------------
    asd = str(input('Please select an operation:\n'))
    #   CONDITIONS-----------
#   OPERATION 01 - rANDOM gRAPH-------------
    if asd == '1':
        #   cHECH iNPUT---------------
        asd = str(input('''Please select a type:\n\nA. Line Graph\nB. Pie Chart\nC. Bar Chart\nD. Histogram\nE. Scatter plot\nF. Box plot\nG. Triangulation plot\nH. 3D plot\n
Type:\n'''))
        #   PLOTTER-------------
        #   lINE gRAPH-------------
        if asd == 'A' or asd == 'a':
            data = np.random.rand(10)*100; plt.scatter(range(len(data)),data); plt.plot(range(len(data)),data); plt.show()
        #   pIE cHART---------------
        elif asd == 'B' or asd == 'b':
            data = np.random.randn(100); plt.pie(data); plt.show()
        #   bAR cHART---------------
        elif asd == 'C' or asd == 'c':
            #   cHECH iNPUT---------------
            asd = str(input('''Please select a type:\n\nA. Vertical Bar Chart\nB. Horizontal Bar Chart\nC. Multiple Bar Chart\nD. Stacked Bar Chart from Top\n\nType:\n'''))
            #   pLOTTER-----------------
            #   vERTICAL bAR cHART---------------
            if asd == 'A' or asd == 'a':
                data = np.random.rand(5)*100; plt.bar(range(len(data)),data); plt.show()
            #   hORIZONTAL bAR cHART---------------
            elif asd == 'B' or asd == 'b':
                data = np.random.rand(5)*100; plt.barh(range(len(data)),data); plt.show()
            #   mULTIPLE bAR cHART---------------
            elif asd == 'C' or asd == 'c':
                data = np.random.rand(5)*100; x = np.arange(4); plt.bar(x + 0.00, data[0], width = 0.25) ;plt.bar(x + 0.25, data[1], width = 0.25)
                plt.bar(x + 0.50, data[2], width = 0.25); plt.show()
            #   sTACKED bAR cHART fROM tOP---------------
            elif asd == 'D' or asd == 'd':
                A = np.linspace(0, 15, 4)  
                B = np.linspace(0, 12, 4) 
                C = np.linspace(0, 10, 4) 
                X = np.arange(4)
                plt.bar(X, A, color = 'g') 
                plt.bar(X, B, bottom = A) 
                plt.bar(X, C, color = 'teal', bottom = A + B)
                plt.show()
            #   eXCEPTION---------------
            else:
                print('''\n Invalid type-----------
-------------Please check your input and try again.''')
        #   hISTOGRAM---------------
        elif asd == 'D' or asd == 'd':
            x = np.random.randn(1000); plt.style.use('classic'); plt.hist(x, bins = 10); plt.show()
#   __________________________________________________________________________
            plt.style.use('default')    #   cHANGE gRAPH pLOT tYPE------------
#   __________________________________________________________________________
        #   sCATTER pLOT-------------
        elif asd == 'E' or asd == 'e':
            data = np.random.rand(500)*100; plt.scatter(range(len(data)),data); plt.show()
        #   bOX pLOT-------------
        elif asd == 'F' or asd == 'f':
            x = np.random.randn(100,3); plt.boxplot(x); plt.show()
        #   tRIANGULATION pLOT-------------
        elif asd == 'G' or asd == 'g':
            data = np.random.rand(7)*100; plttri = tri.Triangulation(range(len(data)),data); plt.triplot(plttri); plt.show()
        #   eXCEPTION-------------------
        elif asd == 'H' or asd == 'h':
            x = np.linspace(-3, 3, 256); y = np.linspace(-3, 3, 256); X, Y = np.meshgrid(x, y); Z = np.sinc(np.sqrt(X ** 2 + Y ** 2)); fig = plt.figure(); ax = fig.gca(projection = '3d') 
            ax.plot_surface(X, Y, Z, cmap=cm.gray); plt.show()
        else:
            print('''\n Invalid type----------
-----------Please check your input and try again.\n''')
#   _____________________________________________________________________________________________________       
#   _____________________________________________________________________________________________________        
#   OPERATION 02 - lINE gRAPH---------------
    elif asd == '2':
        #   cHECH iNPUT---------------
        asd = str(input('''Please select a type:\nA. Single Plot from points\nB. Multiple Plots from points\n\nType:\n'''))
        title = str(input('Please enter the title of the Plot:\n')); xlabel = str(input('Please the title of the X-Axis:\n')); ylabel = str(input('Please the title of the Y-Axis:\n'))
        if asd == 'A' or asd == 'a':
            asd = int(input('Please enter the amount of points to be plotted, maximum of 20.\n'))
            if asd == 5:
                x1 = int(input('''Please enter the points for the X-Axis--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input())
                y1 = int(input('''Please enter the points for the Y-Axis--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input())
                plt.plot([x1,x2,x3,x4,x5],[y1,y2,y3,y4,y5]); plt.scatter([x1,x2,x3,x4,x5],[y1,y2,y3,y4,y5]); plt.plot(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
            elif asd == 6:
                x1 = int(input('''Please enter the points for the X-Axis--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                y1 = int(input('''Please enter the points for the Y-Axis--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                plt.plot([x1,x2,x3,x4,x5,x6],[y1,y2,y3,y4,y5,y6]); plt.scatter([x1,x2,x3,x4,x5,x5],[y1,y2,y3,y4,y5,y6]); plt.plot(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
            elif asd == 7:
                x1 = int(input('''Please enter the points for the X-Axis--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input()); x7 = int(input())
                y1 = int(input('''Please enter the points for the Y-Axis--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input()); y7 = int(input())
                plt.plot([x1,x2,x3,x4,x5,x6,x7],[y1,y2,y3,y4,y5,y6,y7]); plt.scatter([x1,x2,x3,x4,x5,x6,x7],[y1,y2,y3,y4,y5,y6,y7]); plt.plot(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
            elif asd == 8:
                x1 = int(input('''Please enter the points for the X-Axis--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input()); x7 = int(input()); x8 = int(input())
                y1 = int(input('''Please enter the points for the Y-Axis--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input()); y7 = int(input()); y8 = int(input())
                plt.plot([x1,x2,x3,x4,x5,x6,x7,x8],[y1,y2,y3,y4,y5,y6,y7,y8]); plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8],[y1,y2,y3,y4,y5,y6,y7,y8]); plt.plot(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
            elif asd == 9:
                x1 = int(input('''Please enter the points for the X-Axis--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input()); x7 = int(input()); x8 = int(input()); x9 = int(input())
                y1 = int(input('''Please enter the points for the Y-Axis--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input()); y7 = int(input()); y8 = int(input()); y9 = int(input())
                plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9],[y1,y2,y3,y4,y5,y6,y7,y8,y9]); plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9],[y1,y2,y3,y4,y5,y6,y7,y8,y9]); plt.plot(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
            elif asd == 10:
                x1 = int(input('''Please enter the points for the X-Axis--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input()); x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input())
                y1 = int(input('''Please enter the points for the Y-Axis--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input()) ;y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input())
                plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10]); plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10]); plt.plot(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
            elif asd == 11:
                x1 = int(input('''Please enter the points for the X-Axis--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input())
                y1 = int(input('''Please enter the points for the Y-Axis--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input())
                plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11]); plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11]); plt.plot(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
            elif asd == 12:
                x1 = int(input('''Please enter the points for the X-Axis--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input())
                y1 = int(input('''Please enter the points for the Y-Axis--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input())
                plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12]); plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12]); plt.plot(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
            elif asd == 13:
                x1 = int(input('''Please enter the points for the X-Axis--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input())
                y1 = int(input('''Please enter the points for the Y-Axis--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input())
                plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13]); plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13]); plt.plot(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
            elif asd == 14:
                x1 = int(input('''Please enter the points for the X-Axis--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input()); x14 = int(input())
                y1 = int(input('''Please enter the points for the Y-Axis--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input()); y14 = int(input())
                plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14]); plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14]); plt.plot(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
            elif asd == 15:
                x1 = int(input('''Please enter the points for the X-Axis--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input()); x14 = int(input()); x15 = int(input())
                y1 = int(input('''Please enter the points for the Y-Axis--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input()); y14 = int(input()); y15 = int(input())
                plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15]); plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15]); plt.plot(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
            elif asd == 16:
                x1 = int(input('''Please enter the points for the X-Axis--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input()); x14 = int(input()); x15 = int(input()); x16 = int(input())
                y1 = int(input('''Please enter the points for the Y-Axis--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input()); y14 = int(input()); y15 = int(input()); y16 = int(input())
                plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16]); plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16]); plt.plot(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
            elif asd == 17:
                x1 = int(input('''Please enter the points for the X-Axis--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input())
                x14 = int(input()); x15 = int(input()); x16 = int(input()); x17 = int(input())
                y1 = int(input('''Please enter the points for the Y-Axis--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input())
                y14 = int(input()); y15 = int(input()); y16 = int(input()); y17 = int(input())
                plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17]) 
                plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17]); plt.plot(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
            elif asd == 18:
                x1 = int(input('''Please enter the points for the X-Axis--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input())
                x14 = int(input()); x15 = int(input()); x16 = int(input()); x17 = int(input()); x18 = int(input())
                y1 = int(input('''Please enter the points for the Y-Axis--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input())
                y14 = int(input()); y15 = int(input()); y16 = int(input()); y17 = int(input()); y18 = int(input())
                plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18]) 
                plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18]); plt.plot(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()   
            elif asd == 19:
                x1 = int(input('''Please enter the points for the X-Axis--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input())
                x14 = int(input()); x15 = int(input()); x16 = int(input()); x17 = int(input()); x18 = int(input()); x19 = int(input())
                y1 = int(input('''Please enter the points for the Y-Axis--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input())
                y14 = int(input()); y15 = int(input()); y16 = int(input()); y17 = int(input()); y18 = int(input()); y19 = int(input())
                plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19]) 
                plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19]); plt.plot(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
            elif asd == 20:
                x1 = int(input('''Please enter the points for the X-Axis--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input())
                x14 = int(input()); x15 = int(input()); x16 = int(input()); x17 = int(input()); x18 = int(input()); x19 = int(input()); x20 = int(input())
                y1 = int(input('''Please enter the points for the Y-Axis--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input())
                y14 = int(input()); y15 = int(input()); y16 = int(input()); y17 = int(input()); y18 = int(input()); y19 = int(input()); y20 = int(input())
                plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19,y20]) 
                plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19,y20]); plt.plot(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
            elif asd < 5:
                print('plot plot starts from 5 points.\n')
            else:
                print('''Invalid amount-----------
------------Please check your input and try again.\n''')
        elif asd == 'B' or asd == 'b':
            asd = int(input('Please enter the amount of plots to be created, maximum of 4.\n'))
            if asd == 2:
                asd = int(input('Please enter the amount of points to be plotted, maximum of 20.\n'))
                v1 = str(input('''Please enter the names for each plot-------
----------Pressing enter after each input.\n''')); v2 = str(input())
                if asd == 5:
                    x1 = int(input('''Please enter the points for the X-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input())
                    plt.plot([x1,x2,x3,x4,x5],[y1,y2,y3,y4,y5]); plt.plot([a1,a2,a3,a4,a5],[b1,b2,b3,b4,b5]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2]); plt.show()
                elif asd == 6:
                    x1 = int(input('''Please enter the points for the X-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    plt.plot([x1,x2,x3,x4,x5,x6],[y1,y2,y3,y4,y5,y6]); plt.plot([a1,a2,a3,a4,a5,a6],[b1,b2,b3,b4,b5,b6]); plt.title(title); plt.xlabel(xlabel)
                    plt.ylabel(ylabel); plt.legend([v1,v2]); plt.show()
                elif asd == 7:
                    x1 = int(input('''Please enter the points for the X-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input()); x7 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input()); y7 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input()); a7 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input()); b7 = int(input())
                    plt.plot([x1,x2,x3,x4,x5,x6,x7],[y1,y2,y3,y4,y5,y6,y7]); plt.plot([a1,a2,a3,a4,a5,a6,a7],[b1,b2,b3,b4,b5,b6,b7]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2]); plt.show()
                elif asd == 8:
                    x1 = int(input('''Please enter the points for the X-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input()); x7 = int(input()); x8 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input()); y7 = int(input()); y8 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input()); a7 = int(input()); a8 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input()); b7 = int(input()); b8 = int(input())
                    plt.plot([x1,x2,x3,x4,x5,x6,x7,x8],[y1,y2,y3,y4,y5,y6,y7,y8]); plt.plot([a1,a2,a3,a4,a5,a6,a7,a8],[b1,b2,b3,b4,b5,b6,b7,b8]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2]); plt.show()
                elif asd == 9:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input()); x7 = int(input()); x8 = int(input()); x9 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input()); y7 = int(input()); y8 = int(input()); y9 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input()); a7 = int(input()); a8 = int(input()); a9 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input()); b7 = int(input()); b8 = int(input()); b9 = int(input())
                    plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9],[y1,y2,y3,y4,y5,y6,y7,y8,y9]); plt.plot([a1,a2,a3,a4,a5,a6,a7,a8,a9],[b1,b2,b3,b4,b5,b6,b7,b8,b9]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2]); plt.show()
                elif asd == 10:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input()); x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input()); y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input()); a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input()); b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input())
                    plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10]); plt.plot([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2]); plt.show()
                elif asd == 11:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input())
                    plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11]); plt.plot([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2]); plt.show()
                elif asd == 12:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input())
                    plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12]); plt.plot([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2]); plt.show()
                elif asd == 13:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input())
                    plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13]); plt.plot([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2]); plt.show()
                elif asd == 14:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input()); x14 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input()); y14 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input()); a14 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input()); b14 = int(input())
                    plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14]); plt.plot([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2]); plt.show()
                elif asd == 15:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input()); x14 = int(input()); x15 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input()); y14 = int(input()); y15 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); x5 = int(input()); x6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input()); a14 = int(input()); a15 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input()); b14 = int(input()); b15 = int(input())
                    plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15]); plt.plot([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2]); plt.show()
                elif asd == 16:
                    x1 = int(input('''Please enter the points for the X-Axis for the first data--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input()); x14 = int(input()); x15 = int(input()); x16 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first data--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input()); y14 = int(input()); y15 = int(input()); y16 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second data--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input()); a14 = int(input()); a15 = int(input()); a16 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second data--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input()); b14 = int(input()); b15 = int(input()); b16 = int(input())
                    plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16]); plt.plot([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16]); plt.title(title)
                    plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2]); plt.show()
                elif asd == 17:
                    x1 = int(input('''Please enter the points for the X-Axis of the first data--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input())
                    x14 = int(input()); x15 = int(input()); x16 = int(input()); x17 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis of the first data--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input())
                    y14 = int(input()); y15 = int(input()); y16 = int(input()); y17 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis of the second data--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); x5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input())
                    a14 = int(input()); a15 = int(input()); a16 = int(input()); a17 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis of the second datas\--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    y7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input())
                    b14 = int(input()); b15 = int(input()); b16 = int(input()); b17 = int(input())
                    plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17]); plt.plot([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17]) 
                    plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2]); plt.show()
                elif asd == 18:
                    x1 = int(input('''Please enter the points for the X-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input())
                    x14 = int(input()); x15 = int(input()); x16 = int(input()); x17 = int(input()); x18 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input())
                    y14 = int(input()); y15 = int(input()); y16 = int(input()); y17 = int(input()); y18 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input())
                    a14 = int(input()); a15 = int(input()); a16 = int(input()); a17 = int(input()); a18 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input())
                    b14 = int(input()); b15 = int(input()); b16 = int(input()); b17 = int(input()); b18 = int(input())
                    plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18]); plt.plot([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18]) 
                    plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2]); plt.show()   
                elif asd == 19:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input())
                    x14 = int(input()); x15 = int(input()); x16 = int(input()); x17 = int(input()); x18 = int(input()); x19 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input())
                    y14 = int(input()); y15 = int(input()); y16 = int(input()); y17 = int(input()); y18 = int(input()); y19 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input())
                    a14 = int(input()); a15 = int(input()); a16 = int(input()); a17 = int(input()); a18 = int(input()); a19 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input())
                    b14 = int(input()); b15 = int(input()); b16 = int(input()); b17 = int(input()); b18 = int(input()); b19 = int(input())
                    plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19]); plt.plot([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19]) 
                    plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2]); plt.show()
                elif asd == 20:
                    x1 = int(input('''Please enter the points for the X-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input())
                    x14 = int(input()); x15 = int(input()); x16 = int(input()); x17 = int(input()); x18 = int(input()); x19 = int(input()); x20 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input())
                    y14 = int(input()); y15 = int(input()); y16 = int(input()); y17 = int(input()); y18 = int(input()); y19 = int(input()); y20 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input())
                    a14 = int(input()); a15 = int(input()); a16 = int(input()); a17 = int(input()); a18 = int(input()); a19 = int(input()); a20 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input())
                    b14 = int(input()); b15 = int(input()); b16 = int(input()); b17 = int(input()); b18 = int(input()); b19 = int(input()); b20 = int(input())
                    plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19,y20]); plt.plot([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20]) 
                    plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2]); plt.show()
                elif asd < 5:
                    print('plot plot starts from 5 points.\n')
                else:
                    print('''Invalid amount-----------
------------Please check your input and try again.\n''')
            elif asd == 3:
                asd = int(input('Please enter the amount of points to be plotted, maximum of 20.\n'))
                v1 = str(input('''Please enter the names for each plot-------
----------Pressing enter after each input.\n''')); v3 = str(input());
                if asd == 5:
                    x1 = int(input('''Please enter the points for the X-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input())
                    plt.plot([x1,x2,x3,x4,x5],[y1,y2,y3,y4,y5]); plt.plot([a1,a2,a3,a4,a5],[b1,b2,b3,b4,b5]); plt.plot([c1,c2,c3,c4,c5],[d1,d2,d3,d4,d5]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3]); plt.show()
                elif asd == 6:
                    x1 = int(input('''Please enter the points for the X-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input())
                    plt.plot([x1,x2,x3,x4,x5,x6],[y1,y2,y3,y4,y5,y6]); plt.plot([a1,a2,a3,a4,a5,a6],[b1,b2,b3,b4,b5,b6]); plt.plot([c1,c2,c3,c4,c5,c6],[d1,d2,d3,d4,d5,d6]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3]); plt.show()
                elif asd == 7:
                    x1 = int(input('''Please enter the points for the X-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input()); x7 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input()); y7 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input()); a7 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input()); b7 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input()); c7 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input()); d7 = int(input())
                    plt.plot([x1,x2,x3,x4,x5,x6,x7],[y1,y2,y3,y4,y5,y6,y7]); plt.plot([a1,a2,a3,a4,a5,a6,a7],[b1,b2,b3,b4,b5,b6,b7]); plt.plot([c1,c2,c3,c4,c5,c6,c7],[d1,d2,d3,d4,d5,d6,d7]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3]); plt.show()
                elif asd == 8:
                    x1 = int(input('''Please enter the points for the X-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input()); x7 = int(input()); x8 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input()); y7 = int(input()); y8 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input()); a7 = int(input()); a8 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input()); b7 = int(input()); b8 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input()); c7 = int(input()); c8 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input()); d7 = int(input()); d8 = int(input())
                    plt.plot([x1,x2,x3,x4,x5,x6,x7,x8],[y1,y2,y3,y4,y5,y6,y7,y8]); plt.plot([a1,a2,a3,a4,a5,a6,a7,a8],[b1,b2,b3,b4,b5,b6,b7,b8]); plt.plot([c1,c2,c3,c4,c5,c6,c7,c8],[d1,d2,d3,d4,d5,d6,d7,d8]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3]); plt.show()
                elif asd == 9:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input()); x7 = int(input()); x8 = int(input()); x9 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input()); y7 = int(input()); y8 = int(input()); y9 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input()); a7 = int(input()); a8 = int(input()); a9 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input()); b7 = int(input()); b8 = int(input()); b9 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input()); c7 = int(input()); c8 = int(input()); c9 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input()); d7 = int(input()); d8 = int(input()); d9 = int(input())
                    plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9],[y1,y2,y3,y4,y5,y6,y7,y8,y9]); plt.plot([a1,a2,a3,a4,a5,a6,a7,a8,a9],[b1,b2,b3,b4,b5,b6,b7,b8,b9]); plt.plot([c1,c2,c3,c4,c5,c6,c7,c8,c9],[d1,d2,d3,d4,d5,d6,d7,d8,d9]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3]); plt.show()
                elif asd == 10:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input()); x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input()); y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input()); a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input()); b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input()); c7 = int(input()); c8 = int(input()); c9 = int(input()); c10 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input()); d7 = int(input()); d8 = int(input()); d9 = int(input()); d10 = int(input())
                    plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10]); plt.plot([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10]); plt.plot([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10],[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3]); plt.show()
                elif asd == 11:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input())
                    c7 = int(input()); c8 = int(input()); c9 = int(input()); c10 = int(input()); c11 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input())
                    d7 = int(input()); d8 = int(input()); d9 = int(input()); d10 = int(input()); d11 = int(input())
                    plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11]); plt.plot([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11]); plt.plot([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,11],[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3]); plt.show()
                elif asd == 12:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input())
                    c7 = int(input()); c8 = int(input()); c9 = int(input()); c10 = int(input()); c11 = int(input()); c12 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input())
                    d7 = int(input()); d8 = int(input()); d9 = int(input()); d10 = int(input()); d11 = int(input()); d12 = int(input())
                    plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12]); plt.plot([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12]); plt.plot([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12],[d1,d2,d3,d4,d5,d6,d7,d8,d9,b10,d11,d12]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3]); plt.show()
                elif asd == 13:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input())
                    c7 = int(input()); c8 = int(input()); c9 = int(input()); c10 = int(input()); c11 = int(input()); c12 = int(input()); c13 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input())
                    d7 = int(input()); d8 = int(input()); d9 = int(input()); d10 = int(input()); d11 = int(input()); d12 = int(input()); d13 = int(input())
                    plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13]); plt.plot([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13]); plt.plot([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13],[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3]); plt.show()
                elif asd == 14:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input()); x14 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input()); y14 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input()); a14 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input()); b14 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input())
                    c7 = int(input()); c8 = int(input()); c9 = int(input()); c10 = int(input()); c11 = int(input()); c12 = int(input()); c13 = int(input())
                    c14 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input())
                    d7 = int(input()); d8 = int(input()); d9 = int(input()); d10 = int(input()); d11 = int(input()); d12 = int(input()); d13 = int(input())
                    d14 = int(input())
                    plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14]); plt.plot([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14]); plt.plot([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14],[d1,d2,d3,d4,b5,d6,d7,d8,d9,d10,d11,d12,d13,d14]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3]); plt.show()
                elif asd == 15:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input()); x14 = int(input()); x15 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input()); y14 = int(input()); y15 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); x5 = int(input()); x6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input()); a14 = int(input()); a15 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input()); b14 = int(input()); b15 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input())
                    c7 = int(input()); c8 = int(input()); c9 = int(input()); c10 = int(input()); c11 = int(input()); c12 = int(input()); c13 = int(input())
                    c14 = int(input()); c15 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input())
                    d7 = int(input()); d8 = int(input()); d9 = int(input()); d10 = int(input()); d11 = int(input()); d12 = int(input()); d13 = int(input())
                    d14 = int(input()); d15 = int(input())
                    plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15]); plt.plot([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15]); plt.xlabel(xlabel); plt.plot([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15],[d1,d2,d3,d4,b5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15]); plt.ylabel(ylabel); plt.legend([v1,v2,v3]); plt.show()
                elif asd == 16:
                    x1 = int(input('''Please enter the points for the X-Axis for the first data--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input()); x14 = int(input()); x15 = int(input()); x16 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first data--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input()); y14 = int(input()); y15 = int(input()); y16 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second data--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input()); a14 = int(input()); a15 = int(input()); a16 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second data--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input()); b14 = int(input()); b15 = int(input()); b16 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input())
                    c7 = int(input()); c8 = int(input()); c9 = int(input()); c10 = int(input()); c11 = int(input()); c12 = int(input()); c13 = int(input())
                    c14 = int(input()); c15 = int(input()); c16 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input())
                    d7 = int(input()); d8 = int(input()); d9 = int(input()); d10 = int(input()); d11 = int(input()); d12 = int(input()); d13 = int(input())
                    d14 = int(input()); d15 = int(input()); d16 = int(input())
                    plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16]); plt.plot([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16]); plt.plot([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16],[d1,d2,d3,d4,b5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16]); plt.title(title)
                    plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3]); plt.show()
                elif asd == 17:
                    x1 = int(input('''Please enter the points for the X-Axis of the first data--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input())
                    x14 = int(input()); x15 = int(input()); x16 = int(input()); x17 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis of the first data--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input())
                    y14 = int(input()); y15 = int(input()); y16 = int(input()); y17 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis of the second data--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); x5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input())
                    a14 = int(input()); a15 = int(input()); a16 = int(input()); a17 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis of the second datas\--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    y7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input())
                    b14 = int(input()); b15 = int(input()); b16 = int(input()); b17 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input())
                    c7 = int(input()); c8 = int(input()); c9 = int(input()); c10 = int(input()); c11 = int(input()); c12 = int(input()); c13 = int(input())
                    c14 = int(input()); c15 = int(input()); c16 = int(input()); c17 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input())
                    d7 = int(input()); d8 = int(input()); d9 = int(input()); d10 = int(input()); d11 = int(input()); d12 = int(input()); d13 = int(input())
                    d14 = int(input()); d15 = int(input()); d16 = int(input()); d17 = int(input())
                    plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17]); plt.plot([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17]); plt.plot([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17],[d1,d2,d3,d4,b5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17])
                    plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3]); plt.show()
                elif asd == 18:
                    x1 = int(input('''Please enter the points for the X-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input())
                    x14 = int(input()); x15 = int(input()); x16 = int(input()); x17 = int(input()); x18 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input())
                    y14 = int(input()); y15 = int(input()); y16 = int(input()); y17 = int(input()); y18 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input())
                    a14 = int(input()); a15 = int(input()); a16 = int(input()); a17 = int(input()); a18 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input())
                    b14 = int(input()); b15 = int(input()); b16 = int(input()); b17 = int(input()); b18 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input())
                    c7 = int(input()); c8 = int(input()); c9 = int(input()); c10 = int(input()); c11 = int(input()); c12 = int(input()); c13 = int(input())
                    c14 = int(input()); c15 = int(input()); c16 = int(input()); c17 = int(input()); c18 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input())
                    d7 = int(input()); d8 = int(input()); d9 = int(input()); d10 = int(input()); d11 = int(input()); d12 = int(input()); d13 = int(input())
                    d14 = int(input()); d15 = int(input()); d16 = int(input()); d17 = int(input()); d18 = int(input())
                    plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18]); plt.plot([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18]); plt.plot([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18],[d1,d2,d3,d4,b5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18])
                    plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3]); plt.show()   
                elif asd == 19:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input())
                    x14 = int(input()); x15 = int(input()); x16 = int(input()); x17 = int(input()); x18 = int(input()); x19 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input())
                    y14 = int(input()); y15 = int(input()); y16 = int(input()); y17 = int(input()); y18 = int(input()); y19 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input())
                    a14 = int(input()); a15 = int(input()); a16 = int(input()); a17 = int(input()); a18 = int(input()); a19 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input())
                    b14 = int(input()); b15 = int(input()); b16 = int(input()); b17 = int(input()); b18 = int(input()); b19 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input())
                    c7 = int(input()); c8 = int(input()); c9 = int(input()); c10 = int(input()); c11 = int(input()); c12 = int(input()); c13 = int(input())
                    c14 = int(input()); c15 = int(input()); c16 = int(input()); c17 = int(input()); c18 = int(input()); c19 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input())
                    d7 = int(input()); d8 = int(input()); d9 = int(input()); d10 = int(input()); d11 = int(input()); d12 = int(input()); d13 = int(input())
                    d14 = int(input()); d15 = int(input()); d16 = int(input()); d17 = int(input()); d18 = int(input()); d19 = int(input())
                    plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19]); plt.plot([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19]); plt.plot([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19],[d1,d2,d3,d4,b5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19])
                    plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3]); plt.show()
                elif asd == 20:
                    x1 = int(input('''Please enter the points for the X-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input())
                    x14 = int(input()); x15 = int(input()); x16 = int(input()); x17 = int(input()); x18 = int(input()); x19 = int(input()); x20 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input())
                    y14 = int(input()); y15 = int(input()); y16 = int(input()); y17 = int(input()); y18 = int(input()); y19 = int(input()); y20 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input())
                    a14 = int(input()); a15 = int(input()); a16 = int(input()); a17 = int(input()); a18 = int(input()); a19 = int(input()); a20 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input())
                    b14 = int(input()); b15 = int(input()); b16 = int(input()); b17 = int(input()); b18 = int(input()); b19 = int(input()); b20 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input())
                    c7 = int(input()); c8 = int(input()); c9 = int(input()); c10 = int(input()); c11 = int(input()); c12 = int(input()); c13 = int(input())
                    c14 = int(input()); c15 = int(input()); c16 = int(input()); c17 = int(input()); c18 = int(input()); c19 = int(input()); c20 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input())
                    d7 = int(input()); d8 = int(input()); d9 = int(input()); d10 = int(input()); d11 = int(input()); d12 = int(input()); d13 = int(input())
                    d14 = int(input()); d15 = int(input()); d16 = int(input()); d17 = int(input()); d18 = int(input()); d19 = int(input()); d20 = int(input())
                    plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19,y20]); plt.plot([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20]); plt.plot([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20],[d1,d2,d3,d4,b5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,d20]) 
                    plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3]); plt.show()
                elif asd < 5:
                    print('plot plot starts from 5 points.\n')
                else:
                    print('''Invalid amount-----------
------------Please check your input and try again.\n''')
            elif asd == 4:
                asd = int(input('Please enter the amount of points to be plotted, maximum of 20.\n'))
                v1 = str(input('''Please enter the names for each plot-------
----------Pressing enter after each input.\n''')); v3 = str(input()); v4 = str(input())
                if asd == 5:
                    x1 = int(input('''Please enter the points for the X-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input())
                    e1 = int(input('''Please enter the points for the X-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); e2 = int(input()); e3 = int(input()); e4 = int(input()); e5 = int(input())
                    f1 = int(input('''Please enter the points for the Y-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); f2 = int(input()); f3 = int(input()); f4 = int(input()); f5 = int(input())
                    plt.plot([x1,x2,x3,x4,x5],[y1,y2,y3,y4,y5]); plt.plot([a1,a2,a3,a4,a5],[b1,b2,b3,b4,b5]); plt.plot([c1,c2,c3,c4,c5],[d1,d2,d3,d4,d5]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3,v4]); plt.plot([e1,e2,e3,e4,e5],[f1,f2,f3,f4,f5]); plt.show()
                elif asd == 6:
                    x1 = int(input('''Please enter the points for the X-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input())
                    e1 = int(input('''Please enter the points for the X-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); e2 = int(input()); e3 = int(input()); e4 = int(input()); e5 = int(input()); e6 = int(input())
                    f1 = int(input('''Please enter the points for the Y-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); f2 = int(input()); f3 = int(input()); f4 = int(input()); f5 = int(input()); f6 = int(input())
                    plt.plot([x1,x2,x3,x4,x5,x6],[y1,y2,y3,y4,y5,y6]); plt.plot([a1,a2,a3,a4,a5,a6],[b1,b2,b3,b4,b5,b6]); plt.plot([c1,c2,c3,c4,c5,c6],[d1,d2,d3,d4,d5,d6]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3,v4]); plt.plot([e1,e2,e3,e4,e5,e6],[f1,f2,f3,f4,f5,f6]); plt.show()
                elif asd == 7:
                    x1 = int(input('''Please enter the points for the X-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input()); x7 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input()); y7 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input()); a7 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input()); b7 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input()); c7 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input()); d7 = int(input())
                    e1 = int(input('''Please enter the points for the X-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); e2 = int(input()); e3 = int(input()); e4 = int(input()); e5 = int(input()); e6 = int(input()); e7 = int(input())
                    f1 = int(input('''Please enter the points for the Y-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); f2 = int(input()); f3 = int(input()); f4 = int(input()); f5 = int(input()); f6 = int(input()); f7 = int(input())
                    plt.plot([x1,x2,x3,x4,x5,x6,x7],[y1,y2,y3,y4,y5,y6,y7]); plt.plot([a1,a2,a3,a4,a5,a6,a7],[b1,b2,b3,b4,b5,b6,b7]); plt.plot([c1,c2,c3,c4,c5,c6,c7],[d1,d2,d3,d4,d5,d6,d7]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3,v4]); plt.plot([e1,e2,e3,e4,e5,e6,e7],[f1,f2,f3,f4,f5,f6,f7]); plt.show()
                elif asd == 8:
                    x1 = int(input('''Please enter the points for the X-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input()); x7 = int(input()); x8 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input()); y7 = int(input()); y8 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input()); a7 = int(input()); a8 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input()); b7 = int(input()); b8 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input()); c7 = int(input()); c8 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input()); d7 = int(input()); d8 = int(input())
                    e1 = int(input('''Please enter the points for the X-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); e2 = int(input()); e3 = int(input()); e4 = int(input()); e5 = int(input()); e6 = int(input()); e7 = int(input()); e8 = int(input())
                    f1 = int(input('''Please enter the points for the Y-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); f2 = int(input()); f3 = int(input()); f4 = int(input()); f5 = int(input()); f6 = int(input()); f7 = int(input()); f8 = int(input())
                    plt.plot([x1,x2,x3,x4,x5,x6,x7,x8],[y1,y2,y3,y4,y5,y6,y7,y8]); plt.plot([a1,a2,a3,a4,a5,a6,a7,a8],[b1,b2,b3,b4,b5,b6,b7,b8]); plt.plot([c1,c2,c3,c4,c5,c6,c7,c8],[d1,d2,d3,d4,d5,d6,d7,d8]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3,v4]); plt.plot([e1,e2,e3,e4,e5,e6,e7,e8],[f1,f2,f3,f4,f5,f6,f7,f8]); plt.show()
                elif asd == 9:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input()); x7 = int(input()); x8 = int(input()); x9 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input()); y7 = int(input()); y8 = int(input()); y9 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input()); a7 = int(input()); a8 = int(input()); a9 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input()); b7 = int(input()); b8 = int(input()); b9 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input()); c7 = int(input()); c8 = int(input()); c9 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input()); d7 = int(input()); d8 = int(input()); d9 = int(input())
                    e1 = int(input('''Please enter the points for the X-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); e2 = int(input()); e3 = int(input()); e4 = int(input()); e5 = int(input()); e6 = int(input()); e7 = int(input()); e8 = int(input()); e9 = int(input())
                    f1 = int(input('''Please enter the points for the Y-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); f2 = int(input()); f3 = int(input()); f4 = int(input()); f5 = int(input()); f6 = int(input()); f7 = int(input()); f8 = int(input()); f9 = int(input())
                    plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9],[y1,y2,y3,y4,y5,y6,y7,y8,y9]); plt.plot([a1,a2,a3,a4,a5,a6,a7,a8,a9],[b1,b2,b3,b4,b5,b6,b7,b8,b9]); plt.plot([c1,c2,c3,c4,c5,c6,c7,c8,c9],[d1,d2,d3,d4,d5,d6,d7,d8,d9]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3,v4]); plt.plot([e1,e2,e3,e4,e5,e6,e7,e8,e9],[f1,f2,f3,f4,f5,f6,f7,f8,f9]); plt.show()
                elif asd == 10:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input()); x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input()); y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input()); a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input()); b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input()); c7 = int(input()); c8 = int(input()); c9 = int(input()); c10 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input()); d7 = int(input()); d8 = int(input()); d9 = int(input()); d10 = int(input())
                    e1 = int(input('''Please enter the points for the X-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); e2 = int(input()); e3 = int(input()); e4 = int(input()); e5 = int(input()); e6 = int(input()); e7 = int(input()); e8 = int(input()); e9 = int(input()); e10 = int(input())
                    f1 = int(input('''Please enter the points for the Y-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); f2 = int(input()); f3 = int(input()); f4 = int(input()); f5 = int(input()); f6 = int(input()); f7 = int(input()); f8 = int(input()); f9 = int(input()); f10 = int(input())
                    plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10]); plt.plot([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10]); plt.plot([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10],[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3,v4]); plt.plot([e1,e2,e3,e4,e5,e6,e7,e8,e9,e10],[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10]); plt.show()
                elif asd == 11:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input())
                    c7 = int(input()); c8 = int(input()); c9 = int(input()); c10 = int(input()); c11 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input())
                    d7 = int(input()); d8 = int(input()); d9 = int(input()); d10 = int(input()); d11 = int(input())
                    e1 = int(input('''Please enter the points for the X-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); e2 = int(input()); e3 = int(input()); e4 = int(input()); e5 = int(input()); e6 = int(input())
                    e7 = int(input()); e8 = int(input()); e9 = int(input()); e10 = int(input()); e11 = int(input())
                    f1 = int(input('''Please enter the points for the Y-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); f2 = int(input()); f3 = int(input()); f4 = int(input()); f5 = int(input()); f6 = int(input())
                    f7 = int(input()); f8 = int(input()); f9 = int(input()); f10 = int(input()); f11 = int(input())
                    plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11]); plt.plot([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11]); plt.plot([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,11],[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3,v4]); plt.plot([e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11],[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11]); plt.show()
                elif asd == 12:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input())
                    c7 = int(input()); c8 = int(input()); c9 = int(input()); c10 = int(input()); c11 = int(input()); c12 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input())
                    d7 = int(input()); d8 = int(input()); d9 = int(input()); d10 = int(input()); d11 = int(input()); d12 = int(input())
                    e1 = int(input('''Please enter the points for the X-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); e2 = int(input()); e3 = int(input()); e4 = int(input()); e5 = int(input()); e6 = int(input())
                    e7 = int(input()); e8 = int(input()); e9 = int(input()); e10 = int(input()); e11 = int(input()); e12 = int(input())
                    f1 = int(input('''Please enter the points for the Y-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); f2 = int(input()); f3 = int(input()); f4 = int(input()); f5 = int(input()); f6 = int(input())
                    f7 = int(input()); f8 = int(input()); f9 = int(input()); f10 = int(input()); f11 = int(input());f12 = int(input())
                    plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12]); plt.plot([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12]); plt.plot([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12],[d1,d2,d3,d4,d5,d6,d7,d8,d9,b10,d11,d12]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3,v4]); plt.plot([e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12],[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12]); plt.show()
                elif asd == 13:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input())
                    c7 = int(input()); c8 = int(input()); c9 = int(input()); c10 = int(input()); c11 = int(input()); c12 = int(input()); c13 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input())
                    d7 = int(input()); d8 = int(input()); d9 = int(input()); d10 = int(input()); d11 = int(input()); d12 = int(input()); d13 = int(input())
                    e1 = int(input('''Please enter the points for the X-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); e2 = int(input()); e3 = int(input()); e4 = int(input()); e5 = int(input()); e6 = int(input())
                    e7 = int(input()); e8 = int(input()); e9 = int(input()); e10 = int(input()); e11 = int(input()); e12 = int(input()); e13 = int(input())
                    f1 = int(input('''Please enter the points for the Y-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); f2 = int(input()); f3 = int(input()); f4 = int(input()); f5 = int(input()); f6 = int(input())
                    f7 = int(input()); f8 = int(input()); f9 = int(input()); f10 = int(input()); f11 = int(input());f12 = int(input()); f13 = int(input())
                    plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13]); plt.plot([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13]); plt.plot([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13],[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3,v4]); plt.plot([e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13],[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13]); plt.show()
                elif asd == 14:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input()); x14 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input()); y14 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input()); a14 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input()); b14 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input())
                    c7 = int(input()); c8 = int(input()); c9 = int(input()); c10 = int(input()); c11 = int(input()); c12 = int(input()); c13 = int(input())
                    c14 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input())
                    d7 = int(input()); d8 = int(input()); d9 = int(input()); d10 = int(input()); d11 = int(input()); d12 = int(input()); d13 = int(input())
                    d14 = int(input())
                    e1 = int(input('''Please enter the points for the X-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); e2 = int(input()); e3 = int(input()); e4 = int(input()); e5 = int(input()); e6 = int(input())
                    e7 = int(input()); e8 = int(input()); e9 = int(input()); e10 = int(input()); e11 = int(input()); e12 = int(input()); e13 = int(input()); e14 = int(input())
                    f1 = int(input('''Please enter the points for the Y-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); f2 = int(input()); f3 = int(input()); f4 = int(input()); f5 = int(input()); f6 = int(input())
                    f7 = int(input()); f8 = int(input()); f9 = int(input()); f10 = int(input()); f11 = int(input());f12 = int(input()); f13 = int(input()); f14 = int(input())
                    plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14]); plt.plot([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14]); plt.plot([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14],[d1,d2,d3,d4,b5,d6,d7,d8,d9,d10,d11,d12,d13,d14]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3,v4]); plt.plot([e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14],[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14]); plt.show()
                elif asd == 15:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input()); x14 = int(input()); x15 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input()); y14 = int(input()); y15 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); x5 = int(input()); x6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input()); a14 = int(input()); a15 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input()); b14 = int(input()); b15 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input())
                    c7 = int(input()); c8 = int(input()); c9 = int(input()); c10 = int(input()); c11 = int(input()); c12 = int(input()); c13 = int(input())
                    c14 = int(input()); c15 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input())
                    d7 = int(input()); d8 = int(input()); d9 = int(input()); d10 = int(input()); d11 = int(input()); d12 = int(input()); d13 = int(input())
                    d14 = int(input()); d15 = int(input())
                    e1 = int(input('''Please enter the points for the X-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); e2 = int(input()); e3 = int(input()); e4 = int(input()); e5 = int(input()); e6 = int(input())
                    e7 = int(input()); e8 = int(input()); e9 = int(input()); e10 = int(input()); e11 = int(input()); e12 = int(input()); e13 = int(input()); e14 = int(input()); e15 = int(input())
                    f1 = int(input('''Please enter the points for the Y-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); f2 = int(input()); f3 = int(input()); f4 = int(input()); f5 = int(input()); f6 = int(input())
                    f7 = int(input()); f8 = int(input()); f9 = int(input()); f10 = int(input()); f11 = int(input());f12 = int(input()); f13 = int(input()); f14 = int(input()); f15 = int(input())
                    plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15]); plt.plot([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15]); plt.xlabel(xlabel); plt.plot([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15],[d1,d2,d3,d4,b5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15]); plt.ylabel(ylabel); plt.legend([v1,v2,v3,v4]); plt.plot([e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15],[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15]); plt.show()
                elif asd == 16:
                    x1 = int(input('''Please enter the points for the X-Axis for the first data--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input()); x14 = int(input()); x15 = int(input()); x16 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first data--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input()); y14 = int(input()); y15 = int(input()); y16 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second data--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input()); a14 = int(input()); a15 = int(input()); a16 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second data--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input()); b14 = int(input()); b15 = int(input()); b16 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input())
                    c7 = int(input()); c8 = int(input()); c9 = int(input()); c10 = int(input()); c11 = int(input()); c12 = int(input()); c13 = int(input())
                    c14 = int(input()); c15 = int(input()); c16 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input())
                    d7 = int(input()); d8 = int(input()); d9 = int(input()); d10 = int(input()); d11 = int(input()); d12 = int(input()); d13 = int(input())
                    d14 = int(input()); d15 = int(input()); d16 = int(input())
                    e1 = int(input('''Please enter the points for the X-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); e2 = int(input()); e3 = int(input()); e4 = int(input()); e5 = int(input()); e6 = int(input())
                    e7 = int(input()); e8 = int(input()); e9 = int(input()); e10 = int(input()); e11 = int(input()); e12 = int(input()); e13 = int(input()); e14 = int(input()); e15 = int(input()); e16 = int(input())
                    f1 = int(input('''Please enter the points for the Y-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); f2 = int(input()); f3 = int(input()); f4 = int(input()); f5 = int(input()); f6 = int(input())
                    f7 = int(input()); f8 = int(input()); f9 = int(input()); f10 = int(input()); f11 = int(input());f12 = int(input()); f13 = int(input()); f14 = int(input()); f15 = int(input()); f16 = int(input())
                    plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16]); plt.plot([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16]); plt.plot([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16],[d1,d2,d3,d4,b5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16]); plt.title(title); plt.plot([e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16],[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16])
                    plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3,v4]); plt.show()
                elif asd == 17:
                    x1 = int(input('''Please enter the points for the X-Axis of the first data--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input())
                    x14 = int(input()); x15 = int(input()); x16 = int(input()); x17 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis of the first data--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input())
                    y14 = int(input()); y15 = int(input()); y16 = int(input()); y17 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis of the second data--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); x5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input())
                    a14 = int(input()); a15 = int(input()); a16 = int(input()); a17 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis of the second datas\--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    y7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input())
                    b14 = int(input()); b15 = int(input()); b16 = int(input()); b17 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input())
                    c7 = int(input()); c8 = int(input()); c9 = int(input()); c10 = int(input()); c11 = int(input()); c12 = int(input()); c13 = int(input())
                    c14 = int(input()); c15 = int(input()); c16 = int(input()); c17 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input())
                    d7 = int(input()); d8 = int(input()); d9 = int(input()); d10 = int(input()); d11 = int(input()); d12 = int(input()); d13 = int(input())
                    d14 = int(input()); d15 = int(input()); d16 = int(input()); d17 = int(input())
                    e1 = int(input('''Please enter the points for the X-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); e2 = int(input()); e3 = int(input()); e4 = int(input()); e5 = int(input()); e6 = int(input())
                    e7 = int(input()); e8 = int(input()); e9 = int(input()); e10 = int(input()); e11 = int(input()); e12 = int(input()); e13 = int(input()); e14 = int(input()); e15 = int(input()); e16 = int(input()); e17 = int(input())
                    f1 = int(input('''Please enter the points for the Y-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); f2 = int(input()); f3 = int(input()); f4 = int(input()); f5 = int(input()); f6 = int(input())
                    f7 = int(input()); f8 = int(input()); f9 = int(input()); f10 = int(input()); f11 = int(input());f12 = int(input()); f13 = int(input()); f14 = int(input()); f15 = int(input()); f16 = int(input()); f17 = int(input())
                    plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17]); plt.plot([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17]); plt.plot([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17],[d1,d2,d3,d4,b5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17]); plt.plot([e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17],[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17])
                    plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3,v4]); plt.show()
                elif asd == 18:
                    x1 = int(input('''Please enter the points for the X-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input())
                    x14 = int(input()); x15 = int(input()); x16 = int(input()); x17 = int(input()); x18 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input())
                    y14 = int(input()); y15 = int(input()); y16 = int(input()); y17 = int(input()); y18 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input())
                    a14 = int(input()); a15 = int(input()); a16 = int(input()); a17 = int(input()); a18 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input())
                    b14 = int(input()); b15 = int(input()); b16 = int(input()); b17 = int(input()); b18 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input())
                    c7 = int(input()); c8 = int(input()); c9 = int(input()); c10 = int(input()); c11 = int(input()); c12 = int(input()); c13 = int(input())
                    c14 = int(input()); c15 = int(input()); c16 = int(input()); c17 = int(input()); c18 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input())
                    d7 = int(input()); d8 = int(input()); d9 = int(input()); d10 = int(input()); d11 = int(input()); d12 = int(input()); d13 = int(input())
                    d14 = int(input()); d15 = int(input()); d16 = int(input()); d17 = int(input()); d18 = int(input())
                    e1 = int(input('''Please enter the points for the X-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); e2 = int(input()); e3 = int(input()); e4 = int(input()); e5 = int(input()); e6 = int(input())
                    e7 = int(input()); e8 = int(input()); e9 = int(input()); e10 = int(input()); e11 = int(input()); e12 = int(input()); e13 = int(input())
                    e14 = int(input()); e15 = int(input()); e16 = int(input()); e17 = int(input()); e18 = int(input())
                    f1 = int(input('''Please enter the points for the Y-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); f2 = int(input()); f3 = int(input()); f4 = int(input()); f5 = int(input()); f6 = int(input())
                    f7 = int(input()); f8 = int(input()); f9 = int(input()); f10 = int(input()); f11 = int(input());f12 = int(input()); f13 = int(input())
                    f14 = int(input()); f15 = int(input()); f16 = int(input()); f17 = int(input()); f18 = int(input())
                    plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18]); plt.plot([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18]); plt.plot([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18],[d1,d2,d3,d4,b5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18]); plt.plot([e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18],[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18])
                    plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3,v4]); plt.show()   
                elif asd == 19:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input())
                    x14 = int(input()); x15 = int(input()); x16 = int(input()); x17 = int(input()); x18 = int(input()); x19 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input())
                    y14 = int(input()); y15 = int(input()); y16 = int(input()); y17 = int(input()); y18 = int(input()); y19 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input())
                    a14 = int(input()); a15 = int(input()); a16 = int(input()); a17 = int(input()); a18 = int(input()); a19 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input())
                    b14 = int(input()); b15 = int(input()); b16 = int(input()); b17 = int(input()); b18 = int(input()); b19 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input())
                    c7 = int(input()); c8 = int(input()); c9 = int(input()); c10 = int(input()); c11 = int(input()); c12 = int(input()); c13 = int(input())
                    c14 = int(input()); c15 = int(input()); c16 = int(input()); c17 = int(input()); c18 = int(input()); c19 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input())
                    d7 = int(input()); d8 = int(input()); d9 = int(input()); d10 = int(input()); d11 = int(input()); d12 = int(input()); d13 = int(input())
                    d14 = int(input()); d15 = int(input()); d16 = int(input()); d17 = int(input()); d18 = int(input()); d19 = int(input())
                    e1 = int(input('''Please enter the points for the X-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); e2 = int(input()); e3 = int(input()); e4 = int(input()); e5 = int(input()); e6 = int(input())
                    e7 = int(input()); e8 = int(input()); e9 = int(input()); e10 = int(input()); e11 = int(input()); e12 = int(input()); e13 = int(input())
                    e14 = int(input()); e15 = int(input()); e16 = int(input()); e17 = int(input()); e18 = int(input()); e19 = int(input())
                    f1 = int(input('''Please enter the points for the Y-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); f2 = int(input()); f3 = int(input()); f4 = int(input()); f5 = int(input()); f6 = int(input())
                    f7 = int(input()); f8 = int(input()); f9 = int(input()); f10 = int(input()); f11 = int(input());f12 = int(input()); f13 = int(input())
                    f14 = int(input()); f15 = int(input()); f16 = int(input()); f17 = int(input()); f18 = int(input()); f19 = int(input())
                    plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19]); plt.plot([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19]); plt.plot([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19],[d1,d2,d3,d4,b5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19]); plt.plot([e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19],[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19])
                    plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3,v4]); plt.show()
                elif asd == 20:
                    x1 = int(input('''Please enter the points for the X-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input())
                    x14 = int(input()); x15 = int(input()); x16 = int(input()); x17 = int(input()); x18 = int(input()); x19 = int(input()); x20 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input())
                    y14 = int(input()); y15 = int(input()); y16 = int(input()); y17 = int(input()); y18 = int(input()); y19 = int(input()); y20 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input())
                    a14 = int(input()); a15 = int(input()); a16 = int(input()); a17 = int(input()); a18 = int(input()); a19 = int(input()); a20 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input())
                    b14 = int(input()); b15 = int(input()); b16 = int(input()); b17 = int(input()); b18 = int(input()); b19 = int(input()); b20 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input())
                    c7 = int(input()); c8 = int(input()); c9 = int(input()); c10 = int(input()); c11 = int(input()); c12 = int(input()); c13 = int(input())
                    c14 = int(input()); c15 = int(input()); c16 = int(input()); c17 = int(input()); c18 = int(input()); c19 = int(input()); c20 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input())
                    d7 = int(input()); d8 = int(input()); d9 = int(input()); d10 = int(input()); d11 = int(input()); d12 = int(input()); d13 = int(input())
                    d14 = int(input()); d15 = int(input()); d16 = int(input()); d17 = int(input()); d18 = int(input()); d19 = int(input()); d20 = int(input())
                    e1 = int(input('''Please enter the points for the X-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); e2 = int(input()); e3 = int(input()); e4 = int(input()); e5 = int(input()); e6 = int(input())
                    e7 = int(input()); e8 = int(input()); e9 = int(input()); e10 = int(input()); e11 = int(input()); e12 = int(input()); e13 = int(input())
                    e14 = int(input()); e15 = int(input()); e16 = int(input()); e17 = int(input()); e18 = int(input()); e19 = int(input()); e20 = int(input())
                    f1 = int(input('''Please enter the points for the Y-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); f2 = int(input()); f3 = int(input()); f4 = int(input()); f5 = int(input()); f6 = int(input())
                    f7 = int(input()); f8 = int(input()); f9 = int(input()); f10 = int(input()); f11 = int(input());f12 = int(input()); f13 = int(input())
                    f14 = int(input()); f15 = int(input()); f16 = int(input()); f17 = int(input()); f18 = int(input()); f19 = int(input()); f20 = int(input())
                    plt.plot([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19,y20]); plt.plot([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20]); plt.plot([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20],[d1,d2,d3,d4,b5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,d20]); plt.plot([e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20],[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20]) 
                    plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3,v4]); plt.show()
                elif asd < 5:
                    print('plot plot starts from 5 points.\n')
                else:
                    print('''Invalid amount-----------
------------Please check your input and try again.\n''')
            else:
                print('''Invalid amount-----------
-------------Please check your input and try again.\n''') 
    
#   _____________________________________________________________________________________________________       
#   _____________________________________________________________________________________________________
#   OPERATION 03 - pIE cHART----------------
    elif asd == '3':
        #   cHECK iNPUT------------
        title = str(input('Please enter the title of the Chart:\n'))
        asd = str(input('Please enter the amount of sections in the chart, maximum of 10\n'))
        #   2 sECTIONS------------
        if asd == '2':
            #   INPUT------------
            l1 = str(input('''Please enter the labels with respective values-------
----------Pressing enter after each input. E.g\nKenya\n15\nTokyo\n35\ne.t.c\n\nInput:\n''')); d1 = int(input()); l2 = str(input()); d2 = int(input())
            #   PLOTTER----------
            data = [d1,d2]; plt.pie(data); plt.title(title); plt.legend([l1,l2]); plt.show()
        #   3 sECTIONS---------------
        elif asd == '3':
            #   INPUT------------
            l1 = str(input('''Please enter the labels with respective values-------
----------Pressing enter after each input. E.g\nKenya\n15\nTokyo\n35\ne.t.c\n\nInput:\n''')); d1 = int(input()); l2 = str(input()); d2 = int(input()); l3 = str(input()); d3 = int(input())
            #   PLOTTER----------
            data = [d1,d2,d3]; plt.pie(data); plt.title(title); plt.legend([l1,l2,l3]); plt.show()
        #   4 sECTIONS-------------
        elif asd == '4':
            #   INPUT------------
            l1 = str(input('''Please enter the labels with respective values-------
----------Pressing enter after each input. E.g\nKenya\n15\nTokyo\n35\ne.t.c\n\nInput:\n''')); d1 = int(input()); l2 = str(input()); d2 = int(input()); l3 = str(input()); d3 = int(input())
            l4 = str(input()); d4 = int(input())
            #   PLOTTER----------
            data = [d1,d2,d3,d4]; plt.pie(data); plt.title(title); plt.legend([l1,l2,l3,l4]); plt.show()
        #   5 sECTIONS--------------
        elif asd == '5':
            #   INPUT------------
            l1 = str(input('''Please enter the labels with respective values-------
----------Pressing enter after each input. E.g\nKenya\n15\nTokyo\n35\ne.t.c\n\nInput:\n''')); d1 = int(input()); l2 = str(input()); d2 = int(input()); l3 = str(input()); d3 = int(input())
            l4 = str(input()); d4 = int(input()); l5 = str(input()); d5 = int(input())
            #   PLOTTER----------
            data = [d1,d2,d3,d4,d5]; plt.pie(data); plt.title(title); plt.legend([l1,l2,l3,l4,l5]); plt.show()
        #   6 sECTIONS----------------
        elif asd == '6':
            #   INPUT------------
            l1 = str(input('''Please enter the labels with respective values-------
----------Pressing enter after each input. E.g\nKenya\n15\nTokyo\n35\ne.t.c\n\nInput:\n''')); d1 = int(input()); l2 = str(input()); d2 = int(input()); l3 = str(input()); d3 = int(input());
            l4 = str(input()); d4 = int(input()); l5 = str(input()); d5 = int(input()); l6 = str(input()); d6 = int(input())
            #   PLOTTER----------
            data = [d1,d2,d3,d4,d5,d6]; plt.pie(data); plt.title(title); plt.legend([l1,l2,l3,l4,l5,l6]); plt.show()
        #   7 sECTIONS---------------
        elif asd == '7':
            #   INPUT------------
            l1 = str(input('''Please enter the labels with respective values-------
----------Pressing enter after each input. E.g\nKenya\n15\nTokyo\n35\ne.t.c\n\nInput:\n''')); d1 = int(input()); l2 = str(input()); d2 = int(input()); l3 = str(input()); d3 = int(input())
            l4 = str(input()); d4 = int(input()); l5 = str(input()); d5 = int(input()); l6 = str(input()); d6 = int(input()); l7 = str(input()); d7 = int(input())
            #   PLOTTER----------
            data = [d1,d2,d3,d4,d5,d6,d7]; plt.pie(data); plt.title(title); plt.legend([l1,l2,l3,l4,l5,l6,l7]); plt.show()
        #   8 sECTIONS---------------
        elif asd == '8':
            #   INPUT------------
            l1 = str(input('''Please enter the labels with respective values-------
----------Pressing enter after each input. E.g\nKenya\n15\nTokyo\n35\ne.t.c\n\nInput:\n''')); d1 = int(input()); l2 = str(input()); d2 = int(input()); l3 = str(input()); d3 = int(input())
            l4 = str(input()); d4 = int(input()); l5 = str(input()); d5 = int(input()); l6 = str(input()); d6 = int(input()); l7 = str(input()); d7 = int(input()); l8 = str(input()); d8 = int(input())
            #   PLOTTER----------
            data = [d1,d2,d3,d4,d5,d6,d7,d8]; plt.pie(data); plt.title(title); plt.legend([l1,l2,l3,l4,l5,l6,l7,l8]); plt.show()
        #   9 sECTIONS---------------
        elif asd == '9':
            #   INPUT------------
            l1 = str(input('''Please enter the labels with respective values-------
----------Pressing enter after each input. E.g\nKenya\n15\nTokyo\n35\ne.t.c\n\nInput:\n''')); d1 = int(input()); l2 = str(input()); d2 = int(input()); l3 = str(input()); d3 = int(input())
            l4 = str(input()); d4 = int(input()); l5 = str(input()); d5 = int(input()); l6 = str(input()); d6 = int(input()); l7 = str(input()); d7 = int(input()); l8 = str(input()); d8 = int(input())
            l9 = str(input()); d9 = int(input())
            #   PLOTTER----------
            data = [d1,d2,d3,d4,d5,d6,d7,d8,d9]; plt.pie(data); plt.title(title); plt.legend([l1,l2,l3,l4,l5,l6,l7,l8,l9]); plt.show()
        #   10 sECTIONS--------------
        elif asd == '10':
            #   INPUT------------
            l1 = str(input('''Please enter the labels with respective values-------
----------Pressing enter after each input. E.g\nKenya\n15\nTokyo\n35\ne.t.c\n\nInput:\n''')); d1 = int(input()); l2 = str(input()); d2 = int(input()); l3 = str(input()); d3 = int(input())
            l4 = str(input()); d4 = int(input()); l5 = str(input()); d5 = int(input()); l6 = str(input()); d6 = int(input()); l7 = str(input()); d7 = int(input()); l8 = str(input()); d8 = int(input())
            l9 = str(input()); d9 = int(input()); l10 = str(input()); d10 = int(input())
            #   PLOTTER----------
            data = [d1,d2,d2,d3,d4,d5,d6,d7,d8,d9,d10]; plt.pie(data); plt.title(title); plt.legend([l1,l2,l3,l4,l5,l6,l7,l8,l9,l10]); plt.show()
        #   eXCEPTION---------------
        else:
            print('''\n Invalid amount-----------
-----------Please check your input and try again.\n''')
    
    
#   _____________________________________________________________________________________________________       
#   _____________________________________________________________________________________________________    
#   OPERATION 04 - bAR cHART-----------
    elif asd == '4':
        #   cHECH iNPUT---------------
        asd = str(input('''Please select a type:\n\nA. Vertical Bar Chart\nB. Horizontal Bar Chart\nC. Multiple Bar Chart\nD. Stacked Bar Chart from Top\nE. Stacked Bar Chart from bottom\n\nType:\n'''))
        #   PLOTTER--------------
        #   vERTICAL bAR cHART-------------
        if asd == 'A' or asd == 'a':
            #   cHECK iNPUT----------------
            asd = int(input('Please enter the amount of data to be plotted, maximum of 10.\n'))
            title = str(input('Please enter the title of the Chart:\n')); xlabel = str(input('Please the title of the X-Axis:\n')); ylabel = str(input('Please the title of the Y-Axis:\n'))
            #   dATA = 2-------------
            if asd == 2:
                #   iNPUT------------
                l1 = str(input('''Please enter the y-labels with respective values-------
----------Pressing enter after each input. E.g\nSilk\n500\nCotton\n350\ne.t.c\n\nInput:\n''')); v1 = int(input()); l2 = str(input()); v2 = int(input())
                #   pLOTTER-----------
                labels = np.array([l1,l2]); data = np.array([v1,v2]); plt.bar(labels, data); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
            #   dATA = 3-------------
            elif asd == 3:
                #   iNPUT-------------
                l1 = str(input('''Please enter the y-labels with respective values-------
----------Pressing enter after each input. E.g\nSilk\n500\nCotton\n350\ne.t.c\n\nInput:\n''')); v1 = int(input()); l2 = str(input()); v2 = int(input()); l3 = str(input()); v3 = int(input())
                #   pLOTTER-----------
                labels = np.array([l1,l2,l3]); data = np.array([v1,v2,v3]); plt.bar(labels, data); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
            #   dATA = 4----------------
            elif asd == 4:
                #   iNPUT-----------
                l1 = str(input('''Please enter the y-labels with respective values-------
----------Pressing enter after each input. E.g\nSilk\n500\nCotton\n350\ne.t.c\n\nInput:\n''')); v1 = int(input()); l2 = str(input()); v2 = int(input()); l3 = str(input()); v3 = int(input()); l4 = str(input()); v4 = int(input())
                #   pLOTTER-----------
                labels = np.array([l1,l2,l3,l4]); data = np.array([v1,v2,v3,v4]) ;plt.bar(labels, data); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
            #   dATA = 5--------------
            elif asd == 5:
                #   iNPUT-------------
                l1 = str(input('''Please enter the y-labels with respective values-------
----------Pressing enter after each input. E.g\nSilk\n500\nCotton\n350\ne.t.c\n\nInput:\n''')); v1 = int(input()); l2 = str(input()); v2 = int(input()); l3 = str(input()); v3 = int(input()); l4 = str(input())
                v4 = int(input()); l5 = str(input()); v5 = int(input())
                #   pLOTTER-----------
                labels = np.array([l1,l2,l3,l4,l5]); data = np.array([v1,v2,v3,v4,v5]); plt.bar(labels, data); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
            # dATA = 6---------------
            elif asd == 6:
                #   iNPUT-----------
                l1 = str(input('''Please enter the y-labels with respective values-------
----------Pressing enter after each input. E.g\nSilk\n500\nCotton\n350\ne.t.c\n\nInput:\n''')); v1 = int(input()) ;l2 = str(input()); v2 = int(input()); l3 = str(input()); v3 = int(input()); l4 = str(input())
                v4 = int(input()); l5 = str(input()); v5 = int(input()); l6 = str(input()); v6 = int(input())
                #   pLOTTER-----------
                labels = np.array([l1,l2,l3,l4,l5,l6]); data = np.array([v1,v2,v3,v4,v5,v6]); plt.bar(labels, data); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
            #   dATA = 7-------------
            elif asd == 7:
                #   iNPUT-----------
                l1 = str(input('''Please enter the y-labels with respective values-------
----------Pressing enter after each input. E.g\nSilk\n500\nCotton\n350\ne.t.c\n\nInput:\n''')); v1 = int(input()); l2 = str(input()); v2 = int(input()); l3 = str(input()); v3 = int(input()) ;l4 = str(input())
                v4 = int(input()); l5 = str(input()); v5 = int(input()); l6 = str(input()); v6 = int(input()); l7 = str(input()); v7 = int(input())
                #   pLOTTER-----------
                labels = np.array([l1,l2,l3,l4,l5,l6,l7]) ;data = np.array([v1,v2,v3,v4,v5,v6,v7]); plt.bar(labels, data); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
            #   dATA = 8--------------
            elif asd == 8:
                #   iNPUT-------------
                l1 = str(input('''Please enter the y-labels with respective values-------
----------Pressing enter after each input. E.g\nSilk\n500\nCotton\n350\ne.t.c\n\nInput:\n''')); v1 = int(input()); l2 = str(input()); v2 = int(input()); l3 = str(input()); v3 = int(input()); l4 = str(input())
                v4 = int(input()); l5 = str(input()); v5 = int(input()); l6 = str(input()); v6 = int(input()); l7 = str(input()); v7 = int(input()); l8 = str(input()); v8 = int(input())
                #   pLOTTER-----------
                labels = np.array([l1,l2,l3,l4,l5,l6,l7,l8]); data = np.array([v1,v2,v3,v4,v5,v6,v7,v8]); plt.bar(labels, data); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
            #   dATA = 9------------
            elif asd == 9:
                #   iNPUT-----------
                l1 = str(input('''Please enter the y-labels with respective values-------
----------Pressing enter after each input. E.g\nSilk\n500\nCotton\n350\ne.t.c\n\nInput:\n''')); v1 = int(input()); l2 = str(input()); v2 = int(input()); l3 = str(input()); v3 = int(input()); l4 = str(input())
                v4 = int(input()); l5 = str(input()); v5 = int(input()); l6 = str(input()); v6 = int(input()); l7 = str(input()); v7 = int(input()); l8 = str(input()); v8 = int(input()); l9 = str(input()); v9 = int(input())
                #   pLOTTER-----------
                labels = np.array([l1,l2,l3,l4,l5,l6,l7,l8,l9]); data = np.array([v1,v2,v3,v4,v5,v6,v7,v8,v9]); plt.bar(labels, data); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
            #   dATA = 10------------------
            elif asd == 10:
                #   iNPUT-------------
                l1 = str(input('''Please enter the y-labels with respective values-------
----------Pressing enter after each input. E.g\nSilk\n500\nCotton\n350\ne.t.c\n\nInput:\n''')); v1 = int(input()); l2 = str(input()); v2 = int(input()); l3 = str(input()); v3 = int(input())
                l4 = str(input()); v4 = int(input()); l5 = str(input()); v5 = int(input()); l6 = str(input()); v6 = int(input()); l7 = str(input()); v7 = int(input()); l8 = str(input()); v8 = int(input())
                l9 = str(input()); v9 = int(input()); l10 = str(input()); v10 = int(input())
                #   pLOTTER-----------
                labels = np.array([l1,l2,l3,l4,l5,l6,l7,l8,l9,l10]); data = np.array([v1,v2,v3,v4,v5,v6,v7,v8,v9,v10]); plt.bar(labels, data); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
            else:
                print('''\n Invalid amount---------------
-------------Please check your input and try again.''')
        #   hORIZONTAL bAR cHART----------------
        elif asd == 'B' or asd == 'b':
            #   cHECK iNPUT----------------
            asd = int(input('Please enter the amount of data to be plotted, maximum of 10.\n'))
            #   dATA = 2-------------
            if asd == 2:
                #   iNPUT------------
                l1 = str(input('''Please enter the y-labels with respective values-------
----------Pressing enter after each input. E.g\nSilk\n500\nCotton\n350\ne.t.c\n\nInput:\n''')); v1 = int(input()); l2 = str(input()); v2 = int(input())
                #   pLOTTER-----------
                labels = np.array([l1,l2]); data = np.array([v1,v2]); plt.barh(labels, data); plt.show()
            #   dATA = 3-------------
            elif asd == 3:
                #   iNPUT-------------
                l1 = str(input('''Please enter the y-labels with respective values-------
----------Pressing enter after each input. E.g\nSilk\n500\nCotton\n350\ne.t.c\n\nInput:\n''')); v1 = int(input()); l2 = str(input()); v2 = int(input()); l3 = str(input()); v3 = int(input())
                #   pLOTTER-----------
                labels = np.array([l1,l2,l3]); data = np.array([v1,v2,v3]); plt.barh(labels, data); plt.show()
            #   dATA = 4----------------
            elif asd == 4:
                #   iNPUT-----------
                l1 = str(input('''Please enter the y-labels with respective values-------
----------Pressing enter after each input. E.g\nSilk\n500\nCotton\n350\ne.t.c\n\nInput:\n''')); v1 = int(input()); l2 = str(input()); v2 = int(input()); l3 = str(input()); v3 = int(input()); l4 = str(input()); v4 = int(input())
                #   pLOTTER-----------
                labels = np.array([l1,l2,l3,l4]); data = np.array([v1,v2,v3,v4]) ;plt.barh(labels, data); plt.show()
            #   dATA = 5--------------
            elif asd == 5:
                #   iNPUT-------------
                l1 = str(input('''Please enter the y-labels with respective values-------
----------Pressing enter after each input. E.g\nSilk\n500\nCotton\n350\ne.t.c\n\nInput:\n''')); v1 = int(input()); l2 = str(input()); v2 = int(input()); l3 = str(input()); v3 = int(input()); l4 = str(input())
                v4 = int(input()); l5 = str(input()); v5 = int(input())
                #   pLOTTER-----------
                labels = np.array([l1,l2,l3,l4,l5]); data = np.array([v1,v2,v3,v4,v5]); plt.barh(labels, data); plt.show()
            # dATA = 6---------------
            elif asd == 6:
                #   iNPUT-----------
                l1 = str(input('''Please enter the y-labels with respective values-------
----------Pressing enter after each input. E.g\nSilk\n500\nCotton\n350\ne.t.c\n\nInput:\n''')); v1 = int(input()) ;l2 = str(input()); v2 = int(input()); l3 = str(input()); v3 = int(input()); l4 = str(input())
                v4 = int(input()); l5 = str(input()); v5 = int(input()); l6 = str(input()); v6 = int(input())
                #   pLOTTER-----------
                labels = np.array([l1,l2,l3,l4,l5,l6]); data = np.array([v1,v2,v3,v4,v5,v6]); plt.barh(labels, data); plt.show()
            #   dATA = 7-------------
            elif asd == 7:
                #   iNPUT-----------
                l1 = str(input('''Please enter the y-labels with respective values-------
----------Pressing enter after each input. E.g\nSilk\n500\nCotton\n350\ne.t.c\n\nInput:\n''')); v1 = int(input()); l2 = str(input()); v2 = int(input()); l3 = str(input()); v3 = int(input()) ;l4 = str(input())
                v4 = int(input()); l5 = str(input()); v5 = int(input()); l6 = str(input()); v6 = int(input()); l7 = str(input()); v7 = int(input())
                #   pLOTTER-----------
                labels = np.array([l1,l2,l3,l4,l5,l6,l7]) ;data = np.array([v1,v2,v3,v4,v5,v6,v7]); plt.barh(labels, data); plt.show()
            #   dATA = 8--------------
            elif asd == 8:
                #   iNPUT-------------
                l1 = str(input('''Please enter the y-labels with respective values-------
----------Pressing enter after each input. E.g\nSilk\n500\nCotton\n350\ne.t.c\n\nInput:\n''')); v1 = int(input()); l2 = str(input()); v2 = int(input()); l3 = str(input()); v3 = int(input()); l4 = str(input())
                v4 = int(input()); l5 = str(input()); v5 = int(input()); l6 = str(input()); v6 = int(input()); l7 = str(input()); v7 = int(input()); l8 = str(input()); v8 = int(input())
                #   pLOTTER-----------
                labels = np.array([l1,l2,l3,l4,l5,l6,l7,l8]); data = np.array([v1,v2,v3,v4,v5,v6,v7,v8]); plt.barh(labels, data); plt.show()
            #   dATA = 9------------
            elif asd == 9:
                #   iNPUT-----------
                l1 = str(input('''Please enter the y-labels with respective values-------
----------Pressing enter after each input. E.g\nSilk\n500\nCotton\n350\ne.t.c\n\nInput:\n''')); v1 = int(input()); l2 = str(input()); v2 = int(input()); l3 = str(input()); v3 = int(input()); l4 = str(input())
                v4 = int(input()); l5 = str(input()); v5 = int(input()); l6 = str(input()); v6 = int(input()); l7 = str(input()); v7 = int(input()); l8 = str(input()); v8 = int(input()); l9 = str(input()); v9 = int(input())
                #   pLOTTER-----------
                labels = np.array([l1,l2,l3,l4,l5,l6,l7,l8,l9]); data = np.array([v1,v2,v3,v4,v5,v6,v7,v8,v9]); plt.barh(labels, data); plt.show()
            #   dATA = 10------------------
            elif asd == 10:
                #   iNPUT-------------
                l1 = str(input('''Please enter the y-labels with respective values-------
----------Pressing enter after each input. E.g\nSilk\n500\nCotton\n350\ne.t.c\n\nInput:\n''')); v1 = int(input()); l2 = str(input()); v2 = int(input()); l3 = str(input()); v3 = int(input())
                l4 = str(input()); v4 = int(input()); l5 = str(input()); v5 = int(input()); l6 = str(input()); v6 = int(input()); l7 = str(input()); v7 = int(input()); l8 = str(input()); v8 = int(input())
                l9 = str(input()); v9 = int(input()); l10 = str(input()); v10 = int(input())
                #   pLOTTER-----------
                labels = np.array([l1,l2,l3,l4,l5,l6,l7,l8,l9,l10]); data = np.array([v1,v2,v3,v4,v5,v6,v7,v8,v9,v10]); plt.barh(labels, data); plt.show()
            else:
                print('''\n Invalid amount---------------
-------------Please check your input and try again.''')
                
        #   mULTIPLE bAR cHART-----------------
        elif asd == 'C' or asd == 'c':
            #   cHECK iNPUT----------------
            title = str(input('Please enter the title of the Chart:\n')); xlabel = str(input('Please the title of the X-Axis:\n')); ylabel = str(input('Please the title of the Y-Axis:\n'))
            asd = int(input('Please enter the amount of stacked bars to be plotted, maximum of 5.\n'))
            #   dATA = 2-------------
            if asd == 2:
                #   iNPUT------------
                asd = int(input('Please the amount of data to be plotted in the multiple bars, maximum of 5.\n'))
                #   dATA aMOUNT-------------
                if asd == 2:
                    #   iNPUT-----------
                    l1 = str(input('''Please enter the data name for each multiple bar-------
----------Pressing enter after each input. E.g\n2017\n2018\ne.t.c\n\nInput:\n''')); l2 = str(input())
                    v1 = str(input('''Please enter the data names for each bar in the multiple bar-------
----------Pressing enter after each input. E.g\nSilk\nCotton\ne.t.c\n\nInput:\n''')); v2 = str(input())
                    A1 = int(input('''Please enter the values for the first multiple bar respectively-------
----------Pressing enter after each input. E.g\n500\n350\ne.t.c\n\nInput:\n''')); A2 = int(input())
                    B1 = int(input('''Please enter the values for the second multiple bar respectively-------
----------Pressing enter after each input. E.g\n820\n550\ne.t.c\n\nInput:\n''')); B2 = int(input())
                    #   pLOTTER-----------
                    x = np.arange(2); data = [[A1,B1],[A2,B2]]; plt.bar(x + 0.00,data[0],width=0.25); plt.bar(x + 0.25,data[1],width=0.25)
                    plt.legend([v1,v2]); plt.xticks(x + 0.25/2,[l1,l2]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
                elif asd == 3:
                    #   iNPUT------------
                    l1 = str(input('''Please enter the data name for each multiple bar-------
----------Pressing enter after each input. E.g\n2017\n2018\ne.t.c\n\nInput:\n''')); l2 = str(input())
                    v1 = str(input('''Please enter the data names for each bar in the multiple bar-------
----------Pressing enter after each input. E.g\nSilk\nCotton\ne.t.c\n\nInput:\n''')); v2 = str(input()); v3 = str(input())
                    A1 = int(input('''Please enter the values for the first multiple bar respectively-------
----------Pressing enter after each input. E.g\n500\n350\ne.t.c\n\nInput:\n''')); A2 = int(input()); A3 = int(input())
                    B1 = int(input('''Please enter the values for the second multiple bar respectively-------
----------Pressing enter after each input. E.g\n820\n550\ne.t.c\n\nInput:\n''')); B2 = int(input()); B3 = int(input())
                    #   pLOTTER-----------
                    x = np.arange(2); data = [[A1,B1],[A2,B2],[A3,B3]]; plt.bar(x + 0.00,data[0],width=0.25); plt.bar(x + 0.25,data[1],width=0.25)
                    plt.bar(x + 0.50,data[2],width=0.25); plt.legend([v1,v2,v3]); plt.xticks(x + 0.50/2,[l1,l2]); plt.title(title); plt.xlabel(xlabel)
                    plt.ylabel(ylabel); plt.show()
                elif asd == 4:
                    #   iNPUT------------
                    l1 = str(input('''Please enter the data name for each multiple bar-------
----------Pressing enter after each input. E.g\n2017\n2018\ne.t.c\n\nInput:\n''')); l2 = str(input())
                    v1 = str(input('''Please enter the data names for each bar in the multiple bar-------
----------Pressing enter after each input. E.g\nSilk\nCotton\ne.t.c\n\nInput:\n''')); v2 = str(input()); v3 = str(input()); v4 = str(input())
                    A1 = int(input('''Please enter the values for the first multiple bar respectively-------
----------Pressing enter after each input. E.g\n500\n350\ne.t.c\n\nInput:\n''')); A2 = int(input()); A3 = int(input()); A4 = int(input())
                    B1 = int(input('''Please enter the values for the second multiple bar respectively-------
----------Pressing enter after each input. E.g\n820\n550\ne.t.c\n\nInput:\n''')); B2 = int(input()); B3 = int(input()); B4 = int(input())
                    #   pLOTTER-----------
                    x = np.arange(2); data = [[A1,B1],[A2,B2],[A3,B3],[A4,B4]]; plt.bar(x + 0.00,data[0],width=0.20); plt.bar(x + 0.20,data[1],width=0.20)
                    plt.bar(x + 0.40,data[2],width=0.20); plt.bar(x + 0.60,data[3],width=0.20); plt.legend([v1,v2,v3,v4]); plt.xticks(x + 0.60/2,[l1,l2]); plt.title(title)
                    plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
                elif asd == 5:
                     #   iNPUT------------
                    l1 = str(input('''Please enter the data name for each multiple bar-------
----------Pressing enter after each input. E.g\n2017\n2018\ne.t.c\n\nInput:\n''')); l2 = str(input())
                    v1 = str(input('''Please enter the data names for each bar in the multiple bar-------
----------Pressing enter after each input. E.g\nSilk\nCotton\ne.t.c\n\nInput:\n''')); v2 = str(input()); v3 = str(input()); v4 = str(input()); v5 = str(input())
                    A1 = int(input('''Please enter the values for the first multiple bar respectively-------
----------Pressing enter after each input. E.g\n500\n350\ne.t.c\n\nInput:\n''')); A2 = int(input()); A3 = int(input()); A4 = int(input()); A5 = int(input())
                    B1 = int(input('''Please enter the values for the second multiple bar respectively-------
----------Pressing enter after each input. E.g\n820\n550\ne.t.c\n\nInput:\n''')); B2 = int(input()); B3 = int(input()); B4 = int(input()); B5 = int(input())  
                    #   pLOTTER-----------
                    x = np.arange(2); data = [[A1,B1],[A2,B2],[A3,B3],[A4,B4],[A5,B5]]; plt.bar(x + 0.00,data[0],width=0.15); plt.bar(x + 0.15,data[1],width=0.15)
                    plt.bar(x + 0.30,data[2],width=0.15); plt.bar(x + 0.45,data[3],width=0.15); plt.bar(x + 0.60,data[4],width=0.15); plt.legend([v1,v2,v3,v4,v5])
                    plt.xticks(x + 0.60/2,[l1,l2]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
                else:
                    print('''Invalid amount-----------
-------------Please check your input and try again.\n''')
            #   dATA = 3-------------
            elif asd == 3:
                #   iNPUT------------
                asd = int(input('Please the amount of data to be plotted in the multiple bars, maximum of 5.\n'))
                #   dATA aMOUNT-------------
                if asd == 2:
                    #   iNPUT-----------
                    l1 = str(input('''Please enter the data name for each multiple bar-------
----------Pressing enter after each input. E.g\n2017\n2018\ne.t.c\n\nInput:\n''')); l2 = str(input()); l3 = str(input())
                    v1 = str(input('''Please enter the data names for each bar in the multiple bar-------
----------Pressing enter after each input. E.g\nSilk\nCotton\ne.t.c\n\nInput:\n''')); v2 = str(input())
                    A1 = int(input('''Please enter the values for the first multiple bar respectively-------
----------Pressing enter after each input. E.g\n500\n350\ne.t.c\n\nInput:\n''')); A2 = int(input())
                    B1 = int(input('''Please enter the values for the second multiple bar respectively-------
----------Pressing enter after each input. E.g\n820\n550\ne.t.c\n\nInput:\n''')); B2 = int(input())
                    C1 = int(input('''Please enter the values for the third multiple bar respectively-------
----------Pressing enter after each input. E.g\n820\n550\ne.t.c\n\nInput:\n''')); C2 = int(input())                    
                    #   pLOTTER-----------
                    x = np.arange(3); data = [[A1,B1,C1],[A2,B2,C2]]; plt.bar(x + 0.00,data[0],width=0.25); plt.bar(x + 0.25,data[1],width=0.25)
                    plt.legend([v1,v2]); plt.xticks(x + 0.25/2,[l1,l2,l3]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
                elif asd == 3:
                    #   iNPUT------------
                    l1 = str(input('''Please enter the data name for each multiple bar-------
----------Pressing enter after each input. E.g\n2017\n2018\ne.t.c\n\nInput:\n''')); l2 = str(input()); l3 = str(input())
                    v1 = str(input('''Please enter the data names for each bar in the multiple bar-------
----------Pressing enter after each input. E.g\nSilk\nCotton\ne.t.c\n\nInput:\n''')); v2 = str(input()); v3 = str(input())
                    A1 = int(input('''Please enter the values for the first multiple bar respectively-------
----------Pressing enter after each input. E.g\n500\n350\ne.t.c\n\nInput:\n''')); A2 = int(input()); A3 = int(input())
                    B1 = int(input('''Please enter the values for the second multiple bar respectively-------
----------Pressing enter after each input. E.g\n820\n550\ne.t.c\n\nInput:\n''')); B2 = int(input()); B3 = int(input())
                    C1 = int(input('''Please enter the values for the third multiple bar respectively-------
----------Pressing enter after each input. E.g\n820\n550\ne.t.c\n\nInput:\n''')); C2 = int(input()); C3 = int(input())                 
                    #   pLOTTER-----------
                    x = np.arange(3); data = [[A1,B1,C1],[A2,B2,C2],[A3,B3,C3]]; plt.bar(x + 0.00,data[0],width=0.25); plt.bar(x + 0.25,data[1],width=0.25)
                    plt.bar(x + 0.50,data[2],width=0.25); plt.legend([v1,v2,v3]); plt.xticks(x + 0.50/2,[l1,l2,l3]); plt.title(title); plt.xlabel(xlabel)
                    plt.ylabel(ylabel); plt.show()
                elif asd == 4:
                    #   iNPUT------------
                    l1 = str(input('''Please enter the data name for each multiple bar-------
----------Pressing enter after each input. E.g\n2017\n2018\ne.t.c\n\nInput:\n''')); l2 = str(input()); l3 = str(input())
                    v1 = str(input('''Please enter the data names for each bar in the multiple bar-------
----------Pressing enter after each input. E.g\nSilk\nCotton\ne.t.c\n\nInput:\n''')); v2 = str(input()); v3 = str(input()); v4 = str(input())
                    A1 = int(input('''Please enter the values for the first multiple bar respectively-------
----------Pressing enter after each input. E.g\n500\n350\ne.t.c\n\nInput:\n''')); A2 = int(input()); A3 = int(input()); A4 = int(input())
                    B1 = int(input('''Please enter the values for the second multiple bar respectively-------
----------Pressing enter after each input. E.g\n820\n550\ne.t.c\n\nInput:\n''')); B2 = int(input()); B3 = int(input()); B4 = int(input())
                    C1 = int(input('''Please enter the values for the third multiple bar respectively-------
----------Pressing enter after each input. E.g\n820\n550\ne.t.c\n\nInput:\n''')); C2 = int(input()); C3 = int(input()); C4 = int(input()) 
                    #   pLOTTER-----------
                    x = np.arange(3); data = [[A1,B1,C1],[A2,B2,C2],[A3,B3,C3],[A4,B4,C4]]; plt.bar(x + 0.00,data[0],width=0.20); plt.bar(x + 0.20,data[1],width=0.20)
                    plt.bar(x + 0.40,data[2],width=0.20); plt.bar(x + 0.60,data[3],width=0.20); plt.legend([v1,v2,v3,v4]); plt.xticks(x + 0.60/2,[l1,l2,l3]); plt.title(title)
                    plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
                elif asd == 5:
                     #   iNPUT------------
                    l1 = str(input('''Please enter the data name for each multiple bar-------
----------Pressing enter after each input. E.g\n2017\n2018\ne.t.c\n\nInput:\n''')); l2 = str(input()); l3 = str(input())
                    v1 = str(input('''Please enter the data names for each bar in the multiple bar-------
----------Pressing enter after each input. E.g\nSilk\nCotton\ne.t.c\n\nInput:\n''')); v2 = str(input()); v3 = str(input()); v4 = str(input()); v5 = str(input())
                    A1 = int(input('''Please enter the values for the first multiple bar respectively-------
----------Pressing enter after each input. E.g\n500\n350\ne.t.c\n\nInput:\n''')); A2 = int(input()); A3 = int(input()); A4 = int(input()); A5 = int(input())
                    B1 = int(input('''Please enter the values for the second multiple bar respectively-------
----------Pressing enter after each input. E.g\n820\n550\ne.t.c\n\nInput:\n''')); B2 = int(input()); B3 = int(input()); B4 = int(input()); B5 = int(input())
                    C1 = int(input('''Please enter the values for the third multiple bar respectively-------
----------Pressing enter after each input. E.g\n820\n550\ne.t.c\n\nInput:\n''')); C2 = int(input()); C3 = int(input()); C4 = int(input()); C5 = int(input())
                    
                    #   pLOTTER-----------
                    x = np.arange(3); data = [[A1,B1,C1],[A2,B2,C2],[A3,B3,C3],[A4,B4,C4],[A5,B5,C5]]; plt.bar(x + 0.00,data[0],width=0.15); plt.bar(x + 0.15,data[1],width=0.15)
                    plt.bar(x + 0.30,data[2],width=0.15); plt.bar(x + 0.45,data[3],width=0.15); plt.bar(x + 0.60,data[4],width=0.15); plt.legend([v1,v2,v3,v4,v5])
                    plt.xticks(x + 0.60/2,[l1,l2,l3]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
                else:
                    print('''Invalid amount-----------
-------------Please check your input and try again.\n''')
                
            #   dATA = 4----------------
            elif asd == 4:
                #   iNPUT------------
                asd = int(input('Please the amount of data to be plotted in the multiple bars, maximum of 5.\n'))
                #   dATA aMOUNT-------------
                if asd == 2:
                    #   iNPUT-----------
                    l1 = str(input('''Please enter the data name for each multiple bar-------
----------Pressing enter after each input. E.g\n2017\n2018\ne.t.c\n\nInput:\n''')); l2 = str(input()); l3 = str(input()); l4 = str(input())
                    v1 = str(input('''Please enter the data names for each bar in the multiple bar-------
----------Pressing enter after each input. E.g\nSilk\nCotton\ne.t.c\n\nInput:\n''')); v2 = str(input())
                    A1 = int(input('''Please enter the values for the first multiple bar respectively-------
----------Pressing enter after each input. E.g\n500\n350\ne.t.c\n\nInput:\n''')); A2 = int(input())
                    B1 = int(input('''Please enter the values for the second multiple bar respectively-------
----------Pressing enter after each input. E.g\n820\n550\ne.t.c\n\nInput:\n''')); B2 = int(input())
                    C1 = int(input('''Please enter the values for the third multiple bar respectively-------
----------Pressing enter after each input. E.g\n820\n550\ne.t.c\n\nInput:\n''')); C2 = int(input()) 
                    D1 = int(input('''Please enter the values for the fourth multiple bar respectively-------
----------Pressing enter after each input. E.g\n820\n550\ne.t.c\n\nInput:\n''')); D2 = int(input()) 
                    #   pLOTTER-----------
                    x = np.arange(4); data = [[A1,B1,C1,D1],[A2,B2,C2,D2]]; plt.bar(x + 0.00,data[0],width=0.25); plt.bar(x + 0.25,data[1],width=0.25)
                    plt.legend([v1,v2]); plt.xticks(x + 0.25/2,[l1,l2,l3,l4]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
                elif asd == 3:
                    #   iNPUT------------
                    l1 = str(input('''Please enter the data name for each multiple bar-------
----------Pressing enter after each input. E.g\n2017\n2018\ne.t.c\n\nInput:\n''')); l2 = str(input()); l3 = str(input()); l4 = str(input())
                    v1 = str(input('''Please enter the data names for each bar in the multiple bar-------
----------Pressing enter after each input. E.g\nSilk\nCotton\ne.t.c\n\nInput:\n''')); v2 = str(input()); v3 = str(input())
                    A1 = int(input('''Please enter the values for the first multiple bar respectively-------
----------Pressing enter after each input. E.g\n500\n350\ne.t.c\n\nInput:\n''')); A2 = int(input()); A3 = int(input())
                    B1 = int(input('''Please enter the values for the second multiple bar respectively-------
----------Pressing enter after each input. E.g\n820\n550\ne.t.c\n\nInput:\n''')); B2 = int(input()); B3 = int(input())
                    C1 = int(input('''Please enter the values for the third multiple bar respectively-------
----------Pressing enter after each input. E.g\n820\n550\ne.t.c\n\nInput:\n''')); C2 = int(input()); C3 = int(input())  
                    D1 = int(input('''Please enter the values for the fourth multiple bar respectively-------
----------Pressing enter after each input. E.g\n820\n550\ne.t.c\n\nInput:\n''')); D2 = int(input()); D3 = int(input())  
                    #   pLOTTER-----------
                    x = np.arange(4); data = [[A1,B1,C1,D1],[A2,B2,C2,D2],[A3,B3,C3,D3]]; plt.bar(x + 0.00,data[0],width=0.25); plt.bar(x + 0.25,data[1],width=0.25)
                    plt.bar(x + 0.50,data[2],width=0.25); plt.legend([v1,v2,v3]); plt.xticks(x + 0.50/2,[l1,l2,l3,l4]); plt.title(title); plt.xlabel(xlabel)
                    plt.ylabel(ylabel); plt.show()
                elif asd == 4:
                    #   iNPUT------------
                    l1 = str(input('''Please enter the data name for each multiple bar-------
----------Pressing enter after each input. E.g\n2017\n2018\ne.t.c\n\nInput:\n''')); l2 = str(input()); l3 = str(input()); l4 = str(input())
                    v1 = str(input('''Please enter the data names for each bar in the multiple bar-------
----------Pressing enter after each input. E.g\nSilk\nCotton\ne.t.c\n\nInput:\n''')); v2 = str(input()); v3 = str(input()); v4 = str(input())
                    A1 = int(input('''Please enter the values for the first multiple bar respectively-------
----------Pressing enter after each input. E.g\n500\n350\ne.t.c\n\nInput:\n''')); A2 = int(input()); A3 = int(input()); A4 = int(input())
                    B1 = int(input('''Please enter the values for the second multiple bar respectively-------
----------Pressing enter after each input. E.g\n820\n550\ne.t.c\n\nInput:\n''')); B2 = int(input()); B3 = int(input()); B4 = int(input())
                    C1 = int(input('''Please enter the values for the third multiple bar respectively-------
----------Pressing enter after each input. E.g\n820\n550\ne.t.c\n\nInput:\n''')); C2 = int(input()); C3 = int(input()); C4 = int(input())
                    D1 = int(input('''Please enter the values for the fourth multiple bar respectively-------
----------Pressing enter after each input. E.g\n820\n550\ne.t.c\n\nInput:\n''')); D2 = int(input()); D3 = int(input()); D4 = int(input())
                    #   pLOTTER-----------
                    x = np.arange(4); data = [[A1,B1,C1,D1],[A2,B2,C2,D2],[A3,B3,C3,D3],[A4,B4,C4,D4]]; plt.bar(x + 0.00,data[0],width=0.20); plt.bar(x + 0.20,data[1],width=0.20)
                    plt.bar(x + 0.40,data[2],width=0.20); plt.bar(x + 0.60,data[3],width=0.20); plt.legend([v1,v2,v3,v4]); plt.xticks(x + 0.60/2,[l1,l2,l3,l4]); plt.title(title)
                    plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
                elif asd == 5:
                     #   iNPUT------------
                    l1 = str(input('''Please enter the data name for each multiple bar-------
----------Pressing enter after each input. E.g\n2017\n2018\ne.t.c\n\nInput:\n''')); l2 = str(input()); l3 = str(input()); l4 = str(input())
                    v1 = str(input('''Please enter the data names for each bar in the multiple bar-------
----------Pressing enter after each input. E.g\nSilk\nCotton\ne.t.c\n\nInput:\n''')); v2 = str(input()); v3 = str(input()); v4 = str(input()); v5 = str(input())
                    A1 = int(input('''Please enter the values for the first multiple bar respectively-------
----------Pressing enter after each input. E.g\n500\n350\ne.t.c\n\nInput:\n''')); A2 = int(input()); A3 = int(input()); A4 = int(input()); A5 = int(input())
                    B1 = int(input('''Please enter the values for the second multiple bar respectively-------
----------Pressing enter after each input. E.g\n820\n550\ne.t.c\n\nInput:\n''')); B2 = int(input()); B3 = int(input()); B4 = int(input()); B5 = int(input())
                    C1 = int(input('''Please enter the values for the third multiple bar respectively-------
----------Pressing enter after each input. E.g\n820\n550\ne.t.c\n\nInput:\n''')); C2 = int(input()); C3 = int(input()); C4 = int(input()); C5 = int(input())
                    D1 = int(input('''Please enter the values for the fourth multiple bar respectively-------
----------Pressing enter after each input. E.g\n820\n550\ne.t.c\n\nInput:\n''')); D2 = int(input()); D3 = int(input()); D4 = int(input()); D5 = int(input())               
                    #   pLOTTER-----------
                    x = np.arange(4); data = [[A1,B1,C1,D1],[A2,B2,C2,D2],[A3,B3,C3,D3],[A4,B4,C4,D4],[A5,B5,C5,D5]]; plt.bar(x + 0.00,data[0],width=0.15); plt.bar(x + 0.15,data[1],width=0.15)
                    plt.bar(x + 0.30,data[2],width=0.15); plt.bar(x + 0.45,data[3],width=0.15); plt.bar(x + 0.60,data[4],width=0.15); plt.legend([v1,v2,v3,v4,v5])
                    plt.xticks(x + 0.60/2,[l1,l2,l3,l4]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
                else:
                    print('''Invalid amount-----------
-------------Please check your input and try again.\n''')
                    
            #   dATA = 5--------------
            elif asd == 5:
                #   iNPUT------------
                asd = int(input('Please the amount of data to be plotted in the multiple bars, maximum of 5.\n'))
                #   dATA aMOUNT-------------
                if asd == 2:
                    #   iNPUT-----------
                    l1 = str(input('''Please enter the data name for each multiple bar-------
----------Pressing enter after each input. E.g\n2017\n2018\ne.t.c\n\nInput:\n''')); l2 = str(input()); l3 = str(input()); l4 = str(input()); l5 = str(input())
                    v1 = str(input('''Please enter the data names for each bar in the multiple bar-------
----------Pressing enter after each input. E.g\nSilk\nCotton\ne.t.c\n\nInput:\n''')); v2 = str(input())
                    A1 = int(input('''Please enter the values for the first multiple bar respectively-------
----------Pressing enter after each input. E.g\n500\n350\ne.t.c\n\nInput:\n''')); A2 = int(input())
                    B1 = int(input('''Please enter the values for the second multiple bar respectively-------
----------Pressing enter after each input. E.g\n820\n550\ne.t.c\n\nInput:\n''')); B2 = int(input())
                    C1 = int(input('''Please enter the values for the third multiple bar respectively-------
----------Pressing enter after each input. E.g\n820\n550\ne.t.c\n\nInput:\n''')); C2 = int(input()) 
                    D1 = int(input('''Please enter the values for the fourth multiple bar respectively-------
----------Pressing enter after each input. E.g\n820\n550\ne.t.c\n\nInput:\n''')); D2 = int(input()) 
                    E1 = int(input('''Please enter the values for the fifth multiple bar respectively-------
----------Pressing enter after each input. E.g\n820\n550\ne.t.c\n\nInput:\n''')); E2 = int(input()) 
                    #   pLOTTER-----------
                    x = np.arange(5); data = [[A1,B1,C1,D1,E1],[A2,B2,C2,D2,E2]]; plt.bar(x + 0.00,data[0],width=0.25); plt.bar(x + 0.25,data[1],width=0.25)
                    plt.legend([v1,v2]); plt.xticks(x + 0.25/2,[l1,l2,l3,l4,l5]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
                elif asd == 3:
                    #   iNPUT------------
                    l1 = str(input('''Please enter the data name for each multiple bar-------
----------Pressing enter after each input. E.g\n2017\n2018\ne.t.c\n\nInput:\n''')); l2 = str(input()); l3 = str(input()); l4 = str(input()); l5 = str(input())
                    v1 = str(input('''Please enter the data names for each bar in the multiple bar-------
----------Pressing enter after each input. E.g\nSilk\nCotton\ne.t.c\n\nInput:\n''')); v2 = str(input()); v3 = str(input())
                    A1 = int(input('''Please enter the values for the first multiple bar respectively-------
----------Pressing enter after each input. E.g\n500\n350\ne.t.c\n\nInput:\n''')); A2 = int(input()); A3 = int(input())
                    B1 = int(input('''Please enter the values for the second multiple bar respectively-------
----------Pressing enter after each input. E.g\n820\n550\ne.t.c\n\nInput:\n''')); B2 = int(input()); B3 = int(input())
                    C1 = int(input('''Please enter the values for the third multiple bar respectively-------
----------Pressing enter after each input. E.g\n820\n550\ne.t.c\n\nInput:\n''')); C2 = int(input()); C3 = int(input())  
                    D1 = int(input('''Please enter the values for the fourth multiple bar respectively-------
----------Pressing enter after each input. E.g\n820\n550\ne.t.c\n\nInput:\n''')); D2 = int(input()); D3 = int(input())
                    E1 = int(input('''Please enter the values for the fifth multiple bar respectively-------
----------Pressing enter after each input. E.g\n820\n550\ne.t.c\n\nInput:\n''')); E2 = int(input()); E3 = int(input())
                    #   pLOTTER-----------
                    x = np.arange(5); data = [[A1,B1,C1,D1,E1],[A2,B2,C2,D2,E2],[A3,B3,C3,D3,E3]]; plt.bar(x + 0.00,data[0],width=0.25); plt.bar(x + 0.25,data[1],width=0.25)
                    plt.bar(x + 0.50,data[2],width=0.25); plt.legend([v1,v2,v3]); plt.xticks(x + 0.50/2,[l1,l2,l3,l4,l5]); plt.title(title); plt.xlabel(xlabel)
                    plt.ylabel(ylabel); plt.show()
                elif asd == 4:
                    #   iNPUT------------
                    l1 = str(input('''Please enter the data name for each multiple bar-------
----------Pressing enter after each input. E.g\n2017\n2018\ne.t.c\n\nInput:\n''')); l2 = str(input()); l3 = str(input()); l4 = str(input()); l5 = str(input())
                    v1 = str(input('''Please enter the data names for each bar in the multiple bar-------
----------Pressing enter after each input. E.g\nSilk\nCotton\ne.t.c\n\nInput:\n''')); v2 = str(input()); v3 = str(input()); v4 = str(input())
                    A1 = int(input('''Please enter the values for the first multiple bar respectively-------
----------Pressing enter after each input. E.g\n500\n350\ne.t.c\n\nInput:\n''')); A2 = int(input()); A3 = int(input()); A4 = int(input())
                    B1 = int(input('''Please enter the values for the second multiple bar respectively-------
----------Pressing enter after each input. E.g\n820\n550\ne.t.c\n\nInput:\n''')); B2 = int(input()); B3 = int(input()); B4 = int(input())
                    C1 = int(input('''Please enter the values for the third multiple bar respectively-------
----------Pressing enter after each input. E.g\n820\n550\ne.t.c\n\nInput:\n''')); C2 = int(input()); C3 = int(input()); C4 = int(input())
                    D1 = int(input('''Please enter the values for the fourth multiple bar respectively-------
----------Pressing enter after each input. E.g\n820\n550\ne.t.c\n\nInput:\n''')); D2 = int(input()); D3 = int(input()); D4 = int(input())
                    E1 = int(input('''Please enter the values for the fifth multiple bar respectively-------
----------Pressing enter after each input. E.g\n820\n550\ne.t.c\n\nInput:\n''')); E2 = int(input()); E3 = int(input()); E4 = int(input())
                    #   pLOTTER-----------
                    x = np.arange(5); data = [[A1,B1,C1,D1,E1],[A2,B2,C2,D2,E2],[A3,B3,C3,D3,E3],[A4,B4,C4,D4,E4]]; plt.bar(x + 0.00,data[0],width=0.20); plt.bar(x + 0.20,data[1],width=0.20)
                    plt.bar(x + 0.40,data[2],width=0.20); plt.bar(x + 0.60,data[3],width=0.20); plt.legend([v1,v2,v3,v4]); plt.xticks(x + 0.60/2,[l1,l2,l3,l4,l5]); plt.title(title)
                    plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
                elif asd == 5:
                     #   iNPUT------------
                    l1 = str(input('''Please enter the data name for each multiple bar-------
----------Pressing enter after each input. E.g\n2017\n2018\ne.t.c\n\nInput:\n''')); l2 = str(input()); l3 = str(input()); l4 = str(input()); l5 = str(input())
                    v1 = str(input('''Please enter the data names for each bar in the multiple bar-------
----------Pressing enter after each input. E.g\nSilk\nCotton\ne.t.c\n\nInput:\n''')); v2 = str(input()); v3 = str(input()); v4 = str(input()); v5 = str(input())
                    A1 = int(input('''Please enter the values for the first multiple bar respectively-------
----------Pressing enter after each input. E.g\n500\n350\ne.t.c\n\nInput:\n''')); A2 = int(input()); A3 = int(input()); A4 = int(input()); A5 = int(input())
                    B1 = int(input('''Please enter the values for the second multiple bar respectively-------
----------Pressing enter after each input. E.g\n820\n550\ne.t.c\n\nInput:\n''')); B2 = int(input()); B3 = int(input()); B4 = int(input()); B5 = int(input())
                    C1 = int(input('''Please enter the values for the third multiple bar respectively-------
----------Pressing enter after each input. E.g\n820\n550\ne.t.c\n\nInput:\n''')); C2 = int(input()); C3 = int(input()); C4 = int(input()); C5 = int(input())
                    D1 = int(input('''Please enter the values for the fourth multiple bar respectively-------
----------Pressing enter after each input. E.g\n820\n550\ne.t.c\n\nInput:\n''')); D2 = int(input()); D3 = int(input()); D4 = int(input()); D5 = int(input())
                    E1 = int(input('''Please enter the values for the fifth multiple bar respectively-------
----------Pressing enter after each input. E.g\n820\n550\ne.t.c\n\nInput:\n''')); E2 = int(input()); E3 = int(input()); E4 = int(input()); E5 = int(input())
                    #   pLOTTER-----------
                    x = np.arange(5); data = [[A1,B1,C1,D1,E1],[A2,B2,C2,D2,E2],[A3,B3,C3,D3,E3],[A4,B4,C4,D4,E4],[A5,B5,C5,D5,E5]]; plt.bar(x + 0.00,data[0],width=0.15); plt.bar(x + 0.15,data[1],width=0.15)
                    plt.bar(x + 0.30,data[2],width=0.15); plt.bar(x + 0.45,data[3],width=0.15); plt.bar(x + 0.60,data[4],width=0.15); plt.legend([v1,v2,v3,v4,v5])
                    plt.xticks(x + 0.60/2,[l1,l2,l3,l4,l5]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
                else:
                    print('''Invalid amount-----------
-------------Please check your input and try again.\n''')
                    
        #   sTACKED bAR cHART FROM tOP-------------
        elif asd == 'D' or asd == 'd':
            print('''This is the first build of the Matplotlib Cardinator. The major challenge is the input pattern. A better defined pattern of input has not be determined for this operation.
Please bear with us.''')
        #   eXCEPTION-----------
        else:
            print('''\n Invalid type-----------
-----------Please check your input and try again.''')
#   _____________________________________________________________________________________________________       
#   _____________________________________________________________________________________________________    
#   OPERATION 05 - hISTOGRAM PLOT-----------
    elif asd == '5':
        print('Complex mode of input made it undescided to build this operation. Please bear with us as this issue will be fixed with any coming update.')
#   _____________________________________________________________________________________________________       
#   _____________________________________________________________________________________________________    
#   OPERATION 06 - sCATTER pLOT-----------
    elif asd == '6':
        #   cHECH iNPUT---------------
        asd = str(input('''Please select a type:\nA. Single Plot from points\nB. Multiple Plots from points\n\nType:\n'''))
        title = str(input('Please enter the title of the Plot:\n')); xlabel = str(input('Please the title of the X-Axis:\n')); ylabel = str(input('Please the title of the Y-Axis:\n'))
        if asd == 'A' or asd == 'a':
            asd = int(input('Please enter the amount of points to be plotted, maximum of 20.\n'))
            if asd == 5:
                x1 = int(input('''Please enter the points for the X-Axis--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input())
                y1 = int(input('''Please enter the points for the Y-Axis--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input())
                plt.scatter([x1,x2,x3,x4,x5],[y1,y2,y3,y4,y5]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
            elif asd == 6:
                x1 = int(input('''Please enter the points for the X-Axis--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                y1 = int(input('''Please enter the points for the Y-Axis--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                plt.scatter([x1,x2,x3,x4,x5,x6],[y1,y2,y3,y4,y5,y6]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
            elif asd == 7:
                x1 = int(input('''Please enter the points for the X-Axis--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input()); x7 = int(input())
                y1 = int(input('''Please enter the points for the Y-Axis--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input()); y7 = int(input())
                plt.scatter([x1,x2,x3,x4,x5,x6,x7],[y1,y2,y3,y4,y5,y6,y7]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
            elif asd == 8:
                x1 = int(input('''Please enter the points for the X-Axis--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input()); x7 = int(input()); x8 = int(input())
                y1 = int(input('''Please enter the points for the Y-Axis--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input()); y7 = int(input()); y8 = int(input())
                plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8],[y1,y2,y3,y4,y5,y6,y7,y8]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
            elif asd == 9:
                x1 = int(input('''Please enter the points for the X-Axis--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input()); x7 = int(input()); x8 = int(input()); x9 = int(input())
                y1 = int(input('''Please enter the points for the Y-Axis--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input()); y7 = int(input()); y8 = int(input()); y9 = int(input())
                plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9],[y1,y2,y3,y4,y5,y6,y7,y8,y9]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
            elif asd == 10:
                x1 = int(input('''Please enter the points for the X-Axis--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input()); x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input())
                y1 = int(input('''Please enter the points for the Y-Axis--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input()) ;y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input())
                plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
            elif asd == 11:
                x1 = int(input('''Please enter the points for the X-Axis--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input())
                y1 = int(input('''Please enter the points for the Y-Axis--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input())
                plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
            elif asd == 12:
                x1 = int(input('''Please enter the points for the X-Axis--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input())
                y1 = int(input('''Please enter the points for the Y-Axis--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input())
                plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
            elif asd == 13:
                x1 = int(input('''Please enter the points for the X-Axis--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input())
                y1 = int(input('''Please enter the points for the Y-Axis--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input())
                plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
            elif asd == 14:
                x1 = int(input('''Please enter the points for the X-Axis--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input()); x14 = int(input())
                y1 = int(input('''Please enter the points for the Y-Axis--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input()); y14 = int(input())
                plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
            elif asd == 15:
                x1 = int(input('''Please enter the points for the X-Axis--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input()); x14 = int(input()); x15 = int(input())
                y1 = int(input('''Please enter the points for the Y-Axis--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input()); y14 = int(input()); y15 = int(input())
                plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
            elif asd == 16:
                x1 = int(input('''Please enter the points for the X-Axis--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input()); x14 = int(input()); x15 = int(input()); x16 = int(input())
                y1 = int(input('''Please enter the points for the Y-Axis--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input()); y14 = int(input()); y15 = int(input()); y16 = int(input())
                plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
            elif asd == 17:
                x1 = int(input('''Please enter the points for the X-Axis--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input())
                x14 = int(input()); x15 = int(input()); x16 = int(input()); x17 = int(input())
                y1 = int(input('''Please enter the points for the Y-Axis--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input())
                y14 = int(input()); y15 = int(input()); y16 = int(input()); y17 = int(input())
                plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17]) 
                plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
            elif asd == 18:
                x1 = int(input('''Please enter the points for the X-Axis--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input())
                x14 = int(input()); x15 = int(input()); x16 = int(input()); x17 = int(input()); x18 = int(input())
                y1 = int(input('''Please enter the points for the Y-Axis--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input())
                y14 = int(input()); y15 = int(input()); y16 = int(input()); y17 = int(input()); y18 = int(input())
                plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18]) 
                plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()   
            elif asd == 19:
                x1 = int(input('''Please enter the points for the X-Axis--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input())
                x14 = int(input()); x15 = int(input()); x16 = int(input()); x17 = int(input()); x18 = int(input()); x19 = int(input())
                y1 = int(input('''Please enter the points for the Y-Axis--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input())
                y14 = int(input()); y15 = int(input()); y16 = int(input()); y17 = int(input()); y18 = int(input()); y19 = int(input())
                plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19]) 
                plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
            elif asd == 20:
                x1 = int(input('''Please enter the points for the X-Axis--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input())
                x14 = int(input()); x15 = int(input()); x16 = int(input()); x17 = int(input()); x18 = int(input()); x19 = int(input()); x20 = int(input())
                y1 = int(input('''Please enter the points for the Y-Axis--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input())
                y14 = int(input()); y15 = int(input()); y16 = int(input()); y17 = int(input()); y18 = int(input()); y19 = int(input()); y20 = int(input())
                plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19,y20]) 
                plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.show()
            elif asd < 5:
                print('Scatter plot starts from 5 points.\n')
            else:
                print('''Invalid amount-----------
------------Please check your input and try again.\n''')
        elif asd == 'B' or asd == 'b':
            asd = int(input('Please enter the amount of plots to be created, maximum of 4.\n'))
            if asd == 2:
                asd = int(input('Please enter the amount of points to be plotted, maximum of 20.\n'))
                v1 = str(input('''Please enter the names for each plot-------
----------Pressing enter after each input.\n''')); v2 = str(input()); 
                if asd == 5:
                    x1 = int(input('''Please enter the points for the X-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5],[y1,y2,y3,y4,y5]); plt.scatter([a1,a2,a3,a4,a5],[b1,b2,b3,b4,b5]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2]); plt.show()
                elif asd == 6:
                    x1 = int(input('''Please enter the points for the X-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5,x6],[y1,y2,y3,y4,y5,y6]); plt.scatter([a1,a2,a3,a4,a5,a6],[b1,b2,b3,b4,b5,b6]); plt.title(title); plt.xlabel(xlabel)
                    plt.ylabel(ylabel); plt.legend([v1,v2]); plt.show()
                elif asd == 7:
                    x1 = int(input('''Please enter the points for the X-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input()); x7 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input()); y7 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input()); a7 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input()); b7 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5,x6,x7],[y1,y2,y3,y4,y5,y6,y7]); plt.scatter([a1,a2,a3,a4,a5,a6,a7],[b1,b2,b3,b4,b5,b6,b7]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2]); plt.show()
                elif asd == 8:
                    x1 = int(input('''Please enter the points for the X-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input()); x7 = int(input()); x8 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input()); y7 = int(input()); y8 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input()); a7 = int(input()); a8 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input()); b7 = int(input()); b8 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8],[y1,y2,y3,y4,y5,y6,y7,y8]); plt.scatter([a1,a2,a3,a4,a5,a6,a7,a8],[b1,b2,b3,b4,b5,b6,b7,b8]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2]); plt.show()
                elif asd == 9:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input()); x7 = int(input()); x8 = int(input()); x9 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input()); y7 = int(input()); y8 = int(input()); y9 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input()); a7 = int(input()); a8 = int(input()); a9 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input()); b7 = int(input()); b8 = int(input()); b9 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9],[y1,y2,y3,y4,y5,y6,y7,y8,y9]); plt.scatter([a1,a2,a3,a4,a5,a6,a7,a8,a9],[b1,b2,b3,b4,b5,b6,b7,b8,b9]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2]); plt.show()
                elif asd == 10:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input()); x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input()); y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input()); a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input()); b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10]); plt.scatter([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2]); plt.show()
                elif asd == 11:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11]); plt.scatter([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2]); plt.show()
                elif asd == 12:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12]); plt.scatter([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2]); plt.show()
                elif asd == 13:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13]); plt.scatter([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2]); plt.show()
                elif asd == 14:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input()); x14 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input()); y14 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input()); a14 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input()); b14 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14]); plt.scatter([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2]); plt.show()
                elif asd == 15:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input()); x14 = int(input()); x15 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input()); y14 = int(input()); y15 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); x5 = int(input()); x6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input()); a14 = int(input()); a15 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input()); b14 = int(input()); b15 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15]); plt.scatter([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2]); plt.show()
                elif asd == 16:
                    x1 = int(input('''Please enter the points for the X-Axis for the first data--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input()); x14 = int(input()); x15 = int(input()); x16 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first data--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input()); y14 = int(input()); y15 = int(input()); y16 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second data--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input()); a14 = int(input()); a15 = int(input()); a16 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second data--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input()); b14 = int(input()); b15 = int(input()); b16 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16]); plt.scatter([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16]); plt.title(title)
                    plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2]); plt.show()
                elif asd == 17:
                    x1 = int(input('''Please enter the points for the X-Axis of the first data--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input())
                    x14 = int(input()); x15 = int(input()); x16 = int(input()); x17 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis of the first data--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input())
                    y14 = int(input()); y15 = int(input()); y16 = int(input()); y17 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis of the second data--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); x5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input())
                    a14 = int(input()); a15 = int(input()); a16 = int(input()); a17 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis of the second datas\--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    y7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input())
                    b14 = int(input()); b15 = int(input()); b16 = int(input()); b17 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17]); plt.scatter([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17]) 
                    plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2]); plt.show()
                elif asd == 18:
                    x1 = int(input('''Please enter the points for the X-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input())
                    x14 = int(input()); x15 = int(input()); x16 = int(input()); x17 = int(input()); x18 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input())
                    y14 = int(input()); y15 = int(input()); y16 = int(input()); y17 = int(input()); y18 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input())
                    a14 = int(input()); a15 = int(input()); a16 = int(input()); a17 = int(input()); a18 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input())
                    b14 = int(input()); b15 = int(input()); b16 = int(input()); b17 = int(input()); b18 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18]); plt.scatter([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18]) 
                    plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2]); plt.show()   
                elif asd == 19:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input())
                    x14 = int(input()); x15 = int(input()); x16 = int(input()); x17 = int(input()); x18 = int(input()); x19 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input())
                    y14 = int(input()); y15 = int(input()); y16 = int(input()); y17 = int(input()); y18 = int(input()); y19 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input())
                    a14 = int(input()); a15 = int(input()); a16 = int(input()); a17 = int(input()); a18 = int(input()); a19 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input())
                    b14 = int(input()); b15 = int(input()); b16 = int(input()); b17 = int(input()); b18 = int(input()); b19 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19]); plt.scatter([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19]) 
                    plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2]); plt.show()
                elif asd == 20:
                    x1 = int(input('''Please enter the points for the X-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input())
                    x14 = int(input()); x15 = int(input()); x16 = int(input()); x17 = int(input()); x18 = int(input()); x19 = int(input()); x20 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input())
                    y14 = int(input()); y15 = int(input()); y16 = int(input()); y17 = int(input()); y18 = int(input()); y19 = int(input()); y20 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input())
                    a14 = int(input()); a15 = int(input()); a16 = int(input()); a17 = int(input()); a18 = int(input()); a19 = int(input()); a20 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input())
                    b14 = int(input()); b15 = int(input()); b16 = int(input()); b17 = int(input()); b18 = int(input()); b19 = int(input()); b20 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19,y20]); plt.scatter([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20]) 
                    plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2]); plt.show()
                elif asd < 5:
                    print('Scatter plot starts from 5 points.\n')
                else:
                    print('''Invalid amount-----------
------------Please check your input and try again.\n''')
            elif asd == 3:
                asd = int(input('Please enter the amount of points to be plotted, maximum of 20.\n'))
                v1 = str(input('''Please enter the names for each plot-------
----------Pressing enter after each input.\n''')); v3 = str(input());
                if asd == 5:
                    x1 = int(input('''Please enter the points for the X-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5],[y1,y2,y3,y4,y5]); plt.scatter([a1,a2,a3,a4,a5],[b1,b2,b3,b4,b5]); plt.scatter([c1,c2,c3,c4,c5],[d1,d2,d3,d4,d5]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3]); plt.show()
                elif asd == 6:
                    x1 = int(input('''Please enter the points for the X-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5,x6],[y1,y2,y3,y4,y5,y6]); plt.scatter([a1,a2,a3,a4,a5,a6],[b1,b2,b3,b4,b5,b6]); plt.scatter([c1,c2,c3,c4,c5,c6],[d1,d2,d3,d4,d5,d6]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3]); plt.show()
                elif asd == 7:
                    x1 = int(input('''Please enter the points for the X-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input()); x7 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input()); y7 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input()); a7 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input()); b7 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input()); c7 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input()); d7 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5,x6,x7],[y1,y2,y3,y4,y5,y6,y7]); plt.scatter([a1,a2,a3,a4,a5,a6,a7],[b1,b2,b3,b4,b5,b6,b7]); plt.scatter([c1,c2,c3,c4,c5,c6,c7],[d1,d2,d3,d4,d5,d6,d7]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3]); plt.show()
                elif asd == 8:
                    x1 = int(input('''Please enter the points for the X-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input()); x7 = int(input()); x8 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input()); y7 = int(input()); y8 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input()); a7 = int(input()); a8 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input()); b7 = int(input()); b8 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input()); c7 = int(input()); c8 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input()); d7 = int(input()); d8 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8],[y1,y2,y3,y4,y5,y6,y7,y8]); plt.scatter([a1,a2,a3,a4,a5,a6,a7,a8],[b1,b2,b3,b4,b5,b6,b7,b8]); plt.scatter([c1,c2,c3,c4,c5,c6,c7,c8],[d1,d2,d3,d4,d5,d6,d7,d8]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3]); plt.show()
                elif asd == 9:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input()); x7 = int(input()); x8 = int(input()); x9 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input()); y7 = int(input()); y8 = int(input()); y9 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input()); a7 = int(input()); a8 = int(input()); a9 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input()); b7 = int(input()); b8 = int(input()); b9 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input()); c7 = int(input()); c8 = int(input()); c9 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input()); d7 = int(input()); d8 = int(input()); d9 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9],[y1,y2,y3,y4,y5,y6,y7,y8,y9]); plt.scatter([a1,a2,a3,a4,a5,a6,a7,a8,a9],[b1,b2,b3,b4,b5,b6,b7,b8,b9]); plt.scatter([c1,c2,c3,c4,c5,c6,c7,c8,c9],[d1,d2,d3,d4,d5,d6,d7,d8,d9]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3]); plt.show()
                elif asd == 10:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input()); x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input()); y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input()); a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input()); b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input()); c7 = int(input()); c8 = int(input()); c9 = int(input()); c10 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input()); d7 = int(input()); d8 = int(input()); d9 = int(input()); d10 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10]); plt.scatter([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10]); plt.scatter([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10],[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3]); plt.show()
                elif asd == 11:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input())
                    c7 = int(input()); c8 = int(input()); c9 = int(input()); c10 = int(input()); c11 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input())
                    d7 = int(input()); d8 = int(input()); d9 = int(input()); d10 = int(input()); d11 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11]); plt.scatter([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11]); plt.scatter([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,11],[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3]); plt.show()
                elif asd == 12:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input())
                    c7 = int(input()); c8 = int(input()); c9 = int(input()); c10 = int(input()); c11 = int(input()); c12 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input())
                    d7 = int(input()); d8 = int(input()); d9 = int(input()); d10 = int(input()); d11 = int(input()); d12 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12]); plt.scatter([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12]); plt.scatter([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12],[d1,d2,d3,d4,d5,d6,d7,d8,d9,b10,d11,d12]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3]); plt.show()
                elif asd == 13:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input())
                    c7 = int(input()); c8 = int(input()); c9 = int(input()); c10 = int(input()); c11 = int(input()); c12 = int(input()); c13 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input())
                    d7 = int(input()); d8 = int(input()); d9 = int(input()); d10 = int(input()); d11 = int(input()); d12 = int(input()); d13 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13]); plt.scatter([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13]); plt.scatter([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13],[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3]); plt.show()
                elif asd == 14:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input()); x14 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input()); y14 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input()); a14 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input()); b14 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input())
                    c7 = int(input()); c8 = int(input()); c9 = int(input()); c10 = int(input()); c11 = int(input()); c12 = int(input()); c13 = int(input())
                    c14 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input())
                    d7 = int(input()); d8 = int(input()); d9 = int(input()); d10 = int(input()); d11 = int(input()); d12 = int(input()); d13 = int(input())
                    d14 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14]); plt.scatter([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14]); plt.scatter([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14],[d1,d2,d3,d4,b5,d6,d7,d8,d9,d10,d11,d12,d13,d14]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3]); plt.show()
                elif asd == 15:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input()); x14 = int(input()); x15 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input()); y14 = int(input()); y15 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); x5 = int(input()); x6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input()); a14 = int(input()); a15 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input()); b14 = int(input()); b15 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input())
                    c7 = int(input()); c8 = int(input()); c9 = int(input()); c10 = int(input()); c11 = int(input()); c12 = int(input()); c13 = int(input())
                    c14 = int(input()); c15 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input())
                    d7 = int(input()); d8 = int(input()); d9 = int(input()); d10 = int(input()); d11 = int(input()); d12 = int(input()); d13 = int(input())
                    d14 = int(input()); d15 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15]); plt.scatter([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15]); plt.xlabel(xlabel); plt.scatter([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15],[d1,d2,d3,d4,b5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15]); plt.ylabel(ylabel); plt.legend([v1,v2,v3]); plt.show()
                elif asd == 16:
                    x1 = int(input('''Please enter the points for the X-Axis for the first data--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input()); x14 = int(input()); x15 = int(input()); x16 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first data--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input()); y14 = int(input()); y15 = int(input()); y16 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second data--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input()); a14 = int(input()); a15 = int(input()); a16 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second data--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input()); b14 = int(input()); b15 = int(input()); b16 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input())
                    c7 = int(input()); c8 = int(input()); c9 = int(input()); c10 = int(input()); c11 = int(input()); c12 = int(input()); c13 = int(input())
                    c14 = int(input()); c15 = int(input()); c16 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input())
                    d7 = int(input()); d8 = int(input()); d9 = int(input()); d10 = int(input()); d11 = int(input()); d12 = int(input()); d13 = int(input())
                    d14 = int(input()); d15 = int(input()); d16 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16]); plt.scatter([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16]); plt.scatter([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16],[d1,d2,d3,d4,b5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16]); plt.title(title)
                    plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3]); plt.show()
                elif asd == 17:
                    x1 = int(input('''Please enter the points for the X-Axis of the first data--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input())
                    x14 = int(input()); x15 = int(input()); x16 = int(input()); x17 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis of the first data--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input())
                    y14 = int(input()); y15 = int(input()); y16 = int(input()); y17 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis of the second data--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); x5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input())
                    a14 = int(input()); a15 = int(input()); a16 = int(input()); a17 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis of the second datas\--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    y7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input())
                    b14 = int(input()); b15 = int(input()); b16 = int(input()); b17 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input())
                    c7 = int(input()); c8 = int(input()); c9 = int(input()); c10 = int(input()); c11 = int(input()); c12 = int(input()); c13 = int(input())
                    c14 = int(input()); c15 = int(input()); c16 = int(input()); c17 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input())
                    d7 = int(input()); d8 = int(input()); d9 = int(input()); d10 = int(input()); d11 = int(input()); d12 = int(input()); d13 = int(input())
                    d14 = int(input()); d15 = int(input()); d16 = int(input()); d17 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17]); plt.scatter([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17]); plt.scatter([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17],[d1,d2,d3,d4,b5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17])
                    plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3]); plt.show()
                elif asd == 18:
                    x1 = int(input('''Please enter the points for the X-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input())
                    x14 = int(input()); x15 = int(input()); x16 = int(input()); x17 = int(input()); x18 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input())
                    y14 = int(input()); y15 = int(input()); y16 = int(input()); y17 = int(input()); y18 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input())
                    a14 = int(input()); a15 = int(input()); a16 = int(input()); a17 = int(input()); a18 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input())
                    b14 = int(input()); b15 = int(input()); b16 = int(input()); b17 = int(input()); b18 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input())
                    c7 = int(input()); c8 = int(input()); c9 = int(input()); c10 = int(input()); c11 = int(input()); c12 = int(input()); c13 = int(input())
                    c14 = int(input()); c15 = int(input()); c16 = int(input()); c17 = int(input()); c18 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input())
                    d7 = int(input()); d8 = int(input()); d9 = int(input()); d10 = int(input()); d11 = int(input()); d12 = int(input()); d13 = int(input())
                    d14 = int(input()); d15 = int(input()); d16 = int(input()); d17 = int(input()); d18 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18]); plt.scatter([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18]); plt.scatter([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18],[d1,d2,d3,d4,b5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18])
                    plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3]); plt.show()   
                elif asd == 19:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input())
                    x14 = int(input()); x15 = int(input()); x16 = int(input()); x17 = int(input()); x18 = int(input()); x19 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input())
                    y14 = int(input()); y15 = int(input()); y16 = int(input()); y17 = int(input()); y18 = int(input()); y19 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input())
                    a14 = int(input()); a15 = int(input()); a16 = int(input()); a17 = int(input()); a18 = int(input()); a19 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input())
                    b14 = int(input()); b15 = int(input()); b16 = int(input()); b17 = int(input()); b18 = int(input()); b19 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input())
                    c7 = int(input()); c8 = int(input()); c9 = int(input()); c10 = int(input()); c11 = int(input()); c12 = int(input()); c13 = int(input())
                    c14 = int(input()); c15 = int(input()); c16 = int(input()); c17 = int(input()); c18 = int(input()); c19 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input())
                    d7 = int(input()); d8 = int(input()); d9 = int(input()); d10 = int(input()); d11 = int(input()); d12 = int(input()); d13 = int(input())
                    d14 = int(input()); d15 = int(input()); d16 = int(input()); d17 = int(input()); d18 = int(input()); d19 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19]); plt.scatter([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19]); plt.scatter([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19],[d1,d2,d3,d4,b5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19])
                    plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3]); plt.show()
                elif asd == 20:
                    x1 = int(input('''Please enter the points for the X-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input())
                    x14 = int(input()); x15 = int(input()); x16 = int(input()); x17 = int(input()); x18 = int(input()); x19 = int(input()); x20 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input())
                    y14 = int(input()); y15 = int(input()); y16 = int(input()); y17 = int(input()); y18 = int(input()); y19 = int(input()); y20 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input())
                    a14 = int(input()); a15 = int(input()); a16 = int(input()); a17 = int(input()); a18 = int(input()); a19 = int(input()); a20 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input())
                    b14 = int(input()); b15 = int(input()); b16 = int(input()); b17 = int(input()); b18 = int(input()); b19 = int(input()); b20 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input())
                    c7 = int(input()); c8 = int(input()); c9 = int(input()); c10 = int(input()); c11 = int(input()); c12 = int(input()); c13 = int(input())
                    c14 = int(input()); c15 = int(input()); c16 = int(input()); c17 = int(input()); c18 = int(input()); c19 = int(input()); c20 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input())
                    d7 = int(input()); d8 = int(input()); d9 = int(input()); d10 = int(input()); d11 = int(input()); d12 = int(input()); d13 = int(input())
                    d14 = int(input()); d15 = int(input()); d16 = int(input()); d17 = int(input()); d18 = int(input()); d19 = int(input()); d20 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19,y20]); plt.scatter([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20]); plt.scatter([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20],[d1,d2,d3,d4,b5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,d20]) 
                    plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3]); plt.show()
                elif asd < 5:
                    print('Scatter plot starts from 5 points.\n')
                else:
                    print('''Invalid amount-----------
------------Please check your input and try again.\n''')
            elif asd == 4:
                asd = int(input('Please enter the amount of points to be plotted, maximum of 20.\n'))
                v1 = str(input('''Please enter the names for each plot-------
----------Pressing enter after each input.\n''')); v3 = str(input()); v4 = str(input())
                if asd == 5:
                    x1 = int(input('''Please enter the points for the X-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input())
                    e1 = int(input('''Please enter the points for the X-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); e2 = int(input()); e3 = int(input()); e4 = int(input()); e5 = int(input())
                    f1 = int(input('''Please enter the points for the Y-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); f2 = int(input()); f3 = int(input()); f4 = int(input()); f5 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5],[y1,y2,y3,y4,y5]); plt.scatter([a1,a2,a3,a4,a5],[b1,b2,b3,b4,b5]); plt.scatter([c1,c2,c3,c4,c5],[d1,d2,d3,d4,d5]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3,v4]); plt.scatter([e1,e2,e3,e4,e5],[f1,f2,f3,f4,f5]); plt.show()
                elif asd == 6:
                    x1 = int(input('''Please enter the points for the X-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input())
                    e1 = int(input('''Please enter the points for the X-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); e2 = int(input()); e3 = int(input()); e4 = int(input()); e5 = int(input()); e6 = int(input())
                    f1 = int(input('''Please enter the points for the Y-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); f2 = int(input()); f3 = int(input()); f4 = int(input()); f5 = int(input()); f6 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5,x6],[y1,y2,y3,y4,y5,y6]); plt.scatter([a1,a2,a3,a4,a5,a6],[b1,b2,b3,b4,b5,b6]); plt.scatter([c1,c2,c3,c4,c5,c6],[d1,d2,d3,d4,d5,d6]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3,v4]); plt.scatter([e1,e2,e3,e4,e5,e6],[f1,f2,f3,f4,f5,f6]); plt.show()
                elif asd == 7:
                    x1 = int(input('''Please enter the points for the X-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input()); x7 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input()); y7 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input()); a7 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input()); b7 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input()); c7 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input()); d7 = int(input())
                    e1 = int(input('''Please enter the points for the X-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); e2 = int(input()); e3 = int(input()); e4 = int(input()); e5 = int(input()); e6 = int(input()); e7 = int(input())
                    f1 = int(input('''Please enter the points for the Y-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); f2 = int(input()); f3 = int(input()); f4 = int(input()); f5 = int(input()); f6 = int(input()); f7 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5,x6,x7],[y1,y2,y3,y4,y5,y6,y7]); plt.scatter([a1,a2,a3,a4,a5,a6,a7],[b1,b2,b3,b4,b5,b6,b7]); plt.scatter([c1,c2,c3,c4,c5,c6,c7],[d1,d2,d3,d4,d5,d6,d7]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3,v4]); plt.scatter([e1,e2,e3,e4,e5,e6,e7],[f1,f2,f3,f4,f5,f6,f7]); plt.show()
                elif asd == 8:
                    x1 = int(input('''Please enter the points for the X-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input()); x7 = int(input()); x8 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input()); y7 = int(input()); y8 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input()); a7 = int(input()); a8 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input()); b7 = int(input()); b8 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input()); c7 = int(input()); c8 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input()); d7 = int(input()); d8 = int(input())
                    e1 = int(input('''Please enter the points for the X-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); e2 = int(input()); e3 = int(input()); e4 = int(input()); e5 = int(input()); e6 = int(input()); e7 = int(input()); e8 = int(input())
                    f1 = int(input('''Please enter the points for the Y-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); f2 = int(input()); f3 = int(input()); f4 = int(input()); f5 = int(input()); f6 = int(input()); f7 = int(input()); f8 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8],[y1,y2,y3,y4,y5,y6,y7,y8]); plt.scatter([a1,a2,a3,a4,a5,a6,a7,a8],[b1,b2,b3,b4,b5,b6,b7,b8]); plt.scatter([c1,c2,c3,c4,c5,c6,c7,c8],[d1,d2,d3,d4,d5,d6,d7,d8]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3,v4]); plt.scatter([e1,e2,e3,e4,e5,e6,e7,e8],[f1,f2,f3,f4,f5,f6,f7,f8]); plt.show()
                elif asd == 9:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input()); x7 = int(input()); x8 = int(input()); x9 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input()); y7 = int(input()); y8 = int(input()); y9 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input()); a7 = int(input()); a8 = int(input()); a9 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input()); b7 = int(input()); b8 = int(input()); b9 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input()); c7 = int(input()); c8 = int(input()); c9 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input()); d7 = int(input()); d8 = int(input()); d9 = int(input())
                    e1 = int(input('''Please enter the points for the X-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); e2 = int(input()); e3 = int(input()); e4 = int(input()); e5 = int(input()); e6 = int(input()); e7 = int(input()); e8 = int(input()); e9 = int(input())
                    f1 = int(input('''Please enter the points for the Y-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); f2 = int(input()); f3 = int(input()); f4 = int(input()); f5 = int(input()); f6 = int(input()); f7 = int(input()); f8 = int(input()); f9 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9],[y1,y2,y3,y4,y5,y6,y7,y8,y9]); plt.scatter([a1,a2,a3,a4,a5,a6,a7,a8,a9],[b1,b2,b3,b4,b5,b6,b7,b8,b9]); plt.scatter([c1,c2,c3,c4,c5,c6,c7,c8,c9],[d1,d2,d3,d4,d5,d6,d7,d8,d9]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3,v4]); plt.scatter([e1,e2,e3,e4,e5,e6,e7,e8,e9],[f1,f2,f3,f4,f5,f6,f7,f8,f9]); plt.show()
                elif asd == 10:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input()); x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input()); y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input()); a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input()); b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input()); c7 = int(input()); c8 = int(input()); c9 = int(input()); c10 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input()); d7 = int(input()); d8 = int(input()); d9 = int(input()); d10 = int(input())
                    e1 = int(input('''Please enter the points for the X-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); e2 = int(input()); e3 = int(input()); e4 = int(input()); e5 = int(input()); e6 = int(input()); e7 = int(input()); e8 = int(input()); e9 = int(input()); e10 = int(input())
                    f1 = int(input('''Please enter the points for the Y-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); f2 = int(input()); f3 = int(input()); f4 = int(input()); f5 = int(input()); f6 = int(input()); f7 = int(input()); f8 = int(input()); f9 = int(input()); f10 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10]); plt.scatter([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10]); plt.scatter([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10],[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3,v4]); plt.scatter([e1,e2,e3,e4,e5,e6,e7,e8,e9,e10],[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10]); plt.show()
                elif asd == 11:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input())
                    c7 = int(input()); c8 = int(input()); c9 = int(input()); c10 = int(input()); c11 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input())
                    d7 = int(input()); d8 = int(input()); d9 = int(input()); d10 = int(input()); d11 = int(input())
                    e1 = int(input('''Please enter the points for the X-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); e2 = int(input()); e3 = int(input()); e4 = int(input()); e5 = int(input()); e6 = int(input())
                    e7 = int(input()); e8 = int(input()); e9 = int(input()); e10 = int(input()); e11 = int(input())
                    f1 = int(input('''Please enter the points for the Y-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); f2 = int(input()); f3 = int(input()); f4 = int(input()); f5 = int(input()); f6 = int(input())
                    f7 = int(input()); f8 = int(input()); f9 = int(input()); f10 = int(input()); f11 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11]); plt.scatter([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11]); plt.scatter([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,11],[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3,v4]); plt.scatter([e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11],[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11]); plt.show()
                elif asd == 12:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input())
                    c7 = int(input()); c8 = int(input()); c9 = int(input()); c10 = int(input()); c11 = int(input()); c12 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input())
                    d7 = int(input()); d8 = int(input()); d9 = int(input()); d10 = int(input()); d11 = int(input()); d12 = int(input())
                    e1 = int(input('''Please enter the points for the X-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); e2 = int(input()); e3 = int(input()); e4 = int(input()); e5 = int(input()); e6 = int(input())
                    e7 = int(input()); e8 = int(input()); e9 = int(input()); e10 = int(input()); e11 = int(input()); e12 = int(input())
                    f1 = int(input('''Please enter the points for the Y-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); f2 = int(input()); f3 = int(input()); f4 = int(input()); f5 = int(input()); f6 = int(input())
                    f7 = int(input()); f8 = int(input()); f9 = int(input()); f10 = int(input()); f11 = int(input());f12 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12]); plt.scatter([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12]); plt.scatter([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12],[d1,d2,d3,d4,d5,d6,d7,d8,d9,b10,d11,d12]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3,v4]); plt.scatter([e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12],[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12]); plt.show()
                elif asd == 13:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input())
                    c7 = int(input()); c8 = int(input()); c9 = int(input()); c10 = int(input()); c11 = int(input()); c12 = int(input()); c13 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input())
                    d7 = int(input()); d8 = int(input()); d9 = int(input()); d10 = int(input()); d11 = int(input()); d12 = int(input()); d13 = int(input())
                    e1 = int(input('''Please enter the points for the X-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); e2 = int(input()); e3 = int(input()); e4 = int(input()); e5 = int(input()); e6 = int(input())
                    e7 = int(input()); e8 = int(input()); e9 = int(input()); e10 = int(input()); e11 = int(input()); e12 = int(input()); e13 = int(input())
                    f1 = int(input('''Please enter the points for the Y-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); f2 = int(input()); f3 = int(input()); f4 = int(input()); f5 = int(input()); f6 = int(input())
                    f7 = int(input()); f8 = int(input()); f9 = int(input()); f10 = int(input()); f11 = int(input());f12 = int(input()); f13 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13]); plt.scatter([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13]); plt.scatter([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13],[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3,v4]); plt.scatter([e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13],[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13]); plt.show()
                elif asd == 14:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input()); x14 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input()); y14 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input()); a14 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input()); b14 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input())
                    c7 = int(input()); c8 = int(input()); c9 = int(input()); c10 = int(input()); c11 = int(input()); c12 = int(input()); c13 = int(input())
                    c14 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input())
                    d7 = int(input()); d8 = int(input()); d9 = int(input()); d10 = int(input()); d11 = int(input()); d12 = int(input()); d13 = int(input())
                    d14 = int(input())
                    e1 = int(input('''Please enter the points for the X-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); e2 = int(input()); e3 = int(input()); e4 = int(input()); e5 = int(input()); e6 = int(input())
                    e7 = int(input()); e8 = int(input()); e9 = int(input()); e10 = int(input()); e11 = int(input()); e12 = int(input()); e13 = int(input()); e14 = int(input())
                    f1 = int(input('''Please enter the points for the Y-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); f2 = int(input()); f3 = int(input()); f4 = int(input()); f5 = int(input()); f6 = int(input())
                    f7 = int(input()); f8 = int(input()); f9 = int(input()); f10 = int(input()); f11 = int(input());f12 = int(input()); f13 = int(input()); f14 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14]); plt.scatter([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14]); plt.scatter([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14],[d1,d2,d3,d4,b5,d6,d7,d8,d9,d10,d11,d12,d13,d14]); plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3,v4]); plt.scatter([e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14],[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14]); plt.show()
                elif asd == 15:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input()); x14 = int(input()); x15 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input()); y14 = int(input()); y15 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); x5 = int(input()); x6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input()); a14 = int(input()); a15 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input()); b14 = int(input()); b15 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input())
                    c7 = int(input()); c8 = int(input()); c9 = int(input()); c10 = int(input()); c11 = int(input()); c12 = int(input()); c13 = int(input())
                    c14 = int(input()); c15 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input())
                    d7 = int(input()); d8 = int(input()); d9 = int(input()); d10 = int(input()); d11 = int(input()); d12 = int(input()); d13 = int(input())
                    d14 = int(input()); d15 = int(input())
                    e1 = int(input('''Please enter the points for the X-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); e2 = int(input()); e3 = int(input()); e4 = int(input()); e5 = int(input()); e6 = int(input())
                    e7 = int(input()); e8 = int(input()); e9 = int(input()); e10 = int(input()); e11 = int(input()); e12 = int(input()); e13 = int(input()); e14 = int(input()); e15 = int(input())
                    f1 = int(input('''Please enter the points for the Y-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); f2 = int(input()); f3 = int(input()); f4 = int(input()); f5 = int(input()); f6 = int(input())
                    f7 = int(input()); f8 = int(input()); f9 = int(input()); f10 = int(input()); f11 = int(input());f12 = int(input()); f13 = int(input()); f14 = int(input()); f15 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15]); plt.scatter([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15]); plt.xlabel(xlabel); plt.scatter([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15],[d1,d2,d3,d4,b5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15]); plt.ylabel(ylabel); plt.legend([v1,v2,v3,v4]); plt.scatter([e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15],[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15]); plt.show()
                elif asd == 16:
                    x1 = int(input('''Please enter the points for the X-Axis for the first data--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input()); x14 = int(input()); x15 = int(input()); x16 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first data--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input()); y14 = int(input()); y15 = int(input()); y16 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second data--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input()); a14 = int(input()); a15 = int(input()); a16 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second data--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input()); b14 = int(input()); b15 = int(input()); b16 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input())
                    c7 = int(input()); c8 = int(input()); c9 = int(input()); c10 = int(input()); c11 = int(input()); c12 = int(input()); c13 = int(input())
                    c14 = int(input()); c15 = int(input()); c16 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input())
                    d7 = int(input()); d8 = int(input()); d9 = int(input()); d10 = int(input()); d11 = int(input()); d12 = int(input()); d13 = int(input())
                    d14 = int(input()); d15 = int(input()); d16 = int(input())
                    e1 = int(input('''Please enter the points for the X-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); e2 = int(input()); e3 = int(input()); e4 = int(input()); e5 = int(input()); e6 = int(input())
                    e7 = int(input()); e8 = int(input()); e9 = int(input()); e10 = int(input()); e11 = int(input()); e12 = int(input()); e13 = int(input()); e14 = int(input()); e15 = int(input()); e16 = int(input())
                    f1 = int(input('''Please enter the points for the Y-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); f2 = int(input()); f3 = int(input()); f4 = int(input()); f5 = int(input()); f6 = int(input())
                    f7 = int(input()); f8 = int(input()); f9 = int(input()); f10 = int(input()); f11 = int(input());f12 = int(input()); f13 = int(input()); f14 = int(input()); f15 = int(input()); f16 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16]); plt.scatter([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16]); plt.scatter([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16],[d1,d2,d3,d4,b5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16]); plt.title(title); plt.scatter([e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16],[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16])
                    plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3,v4]); plt.show()
                elif asd == 17:
                    x1 = int(input('''Please enter the points for the X-Axis of the first data--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input())
                    x14 = int(input()); x15 = int(input()); x16 = int(input()); x17 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis of the first data--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input())
                    y14 = int(input()); y15 = int(input()); y16 = int(input()); y17 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis of the second data--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); x5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input())
                    a14 = int(input()); a15 = int(input()); a16 = int(input()); a17 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis of the second datas\--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    y7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input())
                    b14 = int(input()); b15 = int(input()); b16 = int(input()); b17 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input())
                    c7 = int(input()); c8 = int(input()); c9 = int(input()); c10 = int(input()); c11 = int(input()); c12 = int(input()); c13 = int(input())
                    c14 = int(input()); c15 = int(input()); c16 = int(input()); c17 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input())
                    d7 = int(input()); d8 = int(input()); d9 = int(input()); d10 = int(input()); d11 = int(input()); d12 = int(input()); d13 = int(input())
                    d14 = int(input()); d15 = int(input()); d16 = int(input()); d17 = int(input())
                    e1 = int(input('''Please enter the points for the X-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); e2 = int(input()); e3 = int(input()); e4 = int(input()); e5 = int(input()); e6 = int(input())
                    e7 = int(input()); e8 = int(input()); e9 = int(input()); e10 = int(input()); e11 = int(input()); e12 = int(input()); e13 = int(input()); e14 = int(input()); e15 = int(input()); e16 = int(input()); e17 = int(input())
                    f1 = int(input('''Please enter the points for the Y-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); f2 = int(input()); f3 = int(input()); f4 = int(input()); f5 = int(input()); f6 = int(input())
                    f7 = int(input()); f8 = int(input()); f9 = int(input()); f10 = int(input()); f11 = int(input());f12 = int(input()); f13 = int(input()); f14 = int(input()); f15 = int(input()); f16 = int(input()); f17 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17]); plt.scatter([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17]); plt.scatter([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17],[d1,d2,d3,d4,b5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17]); plt.scatter([e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17],[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17])
                    plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3,v4]); plt.show()
                elif asd == 18:
                    x1 = int(input('''Please enter the points for the X-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input())
                    x14 = int(input()); x15 = int(input()); x16 = int(input()); x17 = int(input()); x18 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input())
                    y14 = int(input()); y15 = int(input()); y16 = int(input()); y17 = int(input()); y18 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input())
                    a14 = int(input()); a15 = int(input()); a16 = int(input()); a17 = int(input()); a18 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input())
                    b14 = int(input()); b15 = int(input()); b16 = int(input()); b17 = int(input()); b18 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input())
                    c7 = int(input()); c8 = int(input()); c9 = int(input()); c10 = int(input()); c11 = int(input()); c12 = int(input()); c13 = int(input())
                    c14 = int(input()); c15 = int(input()); c16 = int(input()); c17 = int(input()); c18 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input())
                    d7 = int(input()); d8 = int(input()); d9 = int(input()); d10 = int(input()); d11 = int(input()); d12 = int(input()); d13 = int(input())
                    d14 = int(input()); d15 = int(input()); d16 = int(input()); d17 = int(input()); d18 = int(input())
                    e1 = int(input('''Please enter the points for the X-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); e2 = int(input()); e3 = int(input()); e4 = int(input()); e5 = int(input()); e6 = int(input())
                    e7 = int(input()); e8 = int(input()); e9 = int(input()); e10 = int(input()); e11 = int(input()); e12 = int(input()); e13 = int(input())
                    e14 = int(input()); e15 = int(input()); e16 = int(input()); e17 = int(input()); e18 = int(input())
                    f1 = int(input('''Please enter the points for the Y-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); f2 = int(input()); f3 = int(input()); f4 = int(input()); f5 = int(input()); f6 = int(input())
                    f7 = int(input()); f8 = int(input()); f9 = int(input()); f10 = int(input()); f11 = int(input());f12 = int(input()); f13 = int(input())
                    f14 = int(input()); f15 = int(input()); f16 = int(input()); f17 = int(input()); f18 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18]); plt.scatter([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18]); plt.scatter([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18],[d1,d2,d3,d4,b5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18]); plt.scatter([e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18],[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18])
                    plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3,v4]); plt.show()   
                elif asd == 19:
                    x1 = int(input('''Please enter the points for the X-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input())
                    x14 = int(input()); x15 = int(input()); x16 = int(input()); x17 = int(input()); x18 = int(input()); x19 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis for the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input())
                    y14 = int(input()); y15 = int(input()); y16 = int(input()); y17 = int(input()); y18 = int(input()); y19 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input())
                    a14 = int(input()); a15 = int(input()); a16 = int(input()); a17 = int(input()); a18 = int(input()); a19 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis for the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input())
                    b14 = int(input()); b15 = int(input()); b16 = int(input()); b17 = int(input()); b18 = int(input()); b19 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input())
                    c7 = int(input()); c8 = int(input()); c9 = int(input()); c10 = int(input()); c11 = int(input()); c12 = int(input()); c13 = int(input())
                    c14 = int(input()); c15 = int(input()); c16 = int(input()); c17 = int(input()); c18 = int(input()); c19 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input())
                    d7 = int(input()); d8 = int(input()); d9 = int(input()); d10 = int(input()); d11 = int(input()); d12 = int(input()); d13 = int(input())
                    d14 = int(input()); d15 = int(input()); d16 = int(input()); d17 = int(input()); d18 = int(input()); d19 = int(input())
                    e1 = int(input('''Please enter the points for the X-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); e2 = int(input()); e3 = int(input()); e4 = int(input()); e5 = int(input()); e6 = int(input())
                    e7 = int(input()); e8 = int(input()); e9 = int(input()); e10 = int(input()); e11 = int(input()); e12 = int(input()); e13 = int(input())
                    e14 = int(input()); e15 = int(input()); e16 = int(input()); e17 = int(input()); e18 = int(input()); e19 = int(input())
                    f1 = int(input('''Please enter the points for the Y-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); f2 = int(input()); f3 = int(input()); f4 = int(input()); f5 = int(input()); f6 = int(input())
                    f7 = int(input()); f8 = int(input()); f9 = int(input()); f10 = int(input()); f11 = int(input());f12 = int(input()); f13 = int(input())
                    f14 = int(input()); f15 = int(input()); f16 = int(input()); f17 = int(input()); f18 = int(input()); f19 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19]); plt.scatter([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19]); plt.scatter([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19],[d1,d2,d3,d4,b5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19]); plt.scatter([e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19],[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19])
                    plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3,v4]); plt.show()
                elif asd == 20:
                    x1 = int(input('''Please enter the points for the X-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); x2 = int(input()); x3 = int(input()); x4 = int(input()); x5 = int(input()); x6 = int(input())
                    x7 = int(input()); x8 = int(input()); x9 = int(input()); x10 = int(input()); x11 = int(input()); x12 = int(input()); x13 = int(input())
                    x14 = int(input()); x15 = int(input()); x16 = int(input()); x17 = int(input()); x18 = int(input()); x19 = int(input()); x20 = int(input())
                    y1 = int(input('''Please enter the points for the Y-Axis of the first plot--------
-----------Pressing enter after each input.\n''')); y2 = int(input()); y3 = int(input()); y4 = int(input()); y5 = int(input()); y6 = int(input())
                    y7 = int(input()); y8 = int(input()); y9 = int(input()); y10 = int(input()); y11 = int(input()); y12 = int(input()); y13 = int(input())
                    y14 = int(input()); y15 = int(input()); y16 = int(input()); y17 = int(input()); y18 = int(input()); y19 = int(input()); y20 = int(input())
                    a1 = int(input('''Please enter the points for the X-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); a2 = int(input()); a3 = int(input()); a4 = int(input()); a5 = int(input()); a6 = int(input())
                    a7 = int(input()); a8 = int(input()); a9 = int(input()); a10 = int(input()); a11 = int(input()); a12 = int(input()); a13 = int(input())
                    a14 = int(input()); a15 = int(input()); a16 = int(input()); a17 = int(input()); a18 = int(input()); a19 = int(input()); a20 = int(input())
                    b1 = int(input('''Please enter the points for the Y-Axis of the second plot--------
-----------Pressing enter after each input.\n''')); b2 = int(input()); b3 = int(input()); b4 = int(input()); b5 = int(input()); b6 = int(input())
                    b7 = int(input()); b8 = int(input()); b9 = int(input()); b10 = int(input()); b11 = int(input()); b12 = int(input()); b13 = int(input())
                    b14 = int(input()); b15 = int(input()); b16 = int(input()); b17 = int(input()); b18 = int(input()); b19 = int(input()); b20 = int(input())
                    c1 = int(input('''Please enter the points for the X-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); c2 = int(input()); c3 = int(input()); c4 = int(input()); c5 = int(input()); c6 = int(input())
                    c7 = int(input()); c8 = int(input()); c9 = int(input()); c10 = int(input()); c11 = int(input()); c12 = int(input()); c13 = int(input())
                    c14 = int(input()); c15 = int(input()); c16 = int(input()); c17 = int(input()); c18 = int(input()); c19 = int(input()); c20 = int(input())
                    d1 = int(input('''Please enter the points for the Y-Axis of the third plot--------
-----------Pressing enter after each input.\n''')); d2 = int(input()); d3 = int(input()); d4 = int(input()); d5 = int(input()); d6 = int(input())
                    d7 = int(input()); d8 = int(input()); d9 = int(input()); d10 = int(input()); d11 = int(input()); d12 = int(input()); d13 = int(input())
                    d14 = int(input()); d15 = int(input()); d16 = int(input()); d17 = int(input()); d18 = int(input()); d19 = int(input()); d20 = int(input())
                    e1 = int(input('''Please enter the points for the X-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); e2 = int(input()); e3 = int(input()); e4 = int(input()); e5 = int(input()); e6 = int(input())
                    e7 = int(input()); e8 = int(input()); e9 = int(input()); e10 = int(input()); e11 = int(input()); e12 = int(input()); e13 = int(input())
                    e14 = int(input()); e15 = int(input()); e16 = int(input()); e17 = int(input()); e18 = int(input()); e19 = int(input()); e20 = int(input())
                    f1 = int(input('''Please enter the points for the Y-Axis of the fourth plot--------
-----------Pressing enter after each input.\n''')); f2 = int(input()); f3 = int(input()); f4 = int(input()); f5 = int(input()); f6 = int(input())
                    f7 = int(input()); f8 = int(input()); f9 = int(input()); f10 = int(input()); f11 = int(input());f12 = int(input()); f13 = int(input())
                    f14 = int(input()); f15 = int(input()); f16 = int(input()); f17 = int(input()); f18 = int(input()); f19 = int(input()); f20 = int(input())
                    plt.scatter([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20],[y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19,y20]); plt.scatter([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20],[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20]); plt.scatter([c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20],[d1,d2,d3,d4,b5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,d20]); plt.scatter([e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20],[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20]) 
                    plt.title(title); plt.xlabel(xlabel); plt.ylabel(ylabel); plt.legend([v1,v2,v3,v4]); plt.show()
                elif asd < 5:
                    print('Scatter plot starts from 5 points.\n')
                else:
                    print('''Invalid amount-----------
------------Please check your input and try again.\n''')
            else:
                print('''Invalid amount-----------
-------------Please check your input and try again.\n''')
#   _____________________________________________________________________________________________________       
#   _____________________________________________________________________________________________________    
#   OPERATION 07 - bOX pLOT-----------
    elif asd == '7':
        print('Complex mode of input made it undescided to build this operation. Please bear with us as this issue will be fixed with any coming update.')
#   _____________________________________________________________________________________________________       
#   _____________________________________________________________________________________________________    
#   OPERATION 08 - tRIANGULATION pLOT-----------
    elif asd == '8':
        print('Complex mode of input has been a major challenge to making this funtion user friendly. Please bear as this issue will be fixed in coming updates.')
#   _____________________________________________________________________________________________________       
#   _____________________________________________________________________________________________________    
#
#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------| EXIT |---------------------------------------------------------------------
    elif asd == 'exit':
        break
#   _____________________________________________________________________________________________________       
#   _____________________________________________________________________________________________________        
#   eXCEPTION
    else:
        print('''\n Invalid operation----------
------------Please check your input and try again.\n''')
        #def plot_graph(x,y):  # Function to plot_graph...
    
    
    
