float X1 = 50;
float X2 = 50;
float X3 = 50;
float X4 = 50;
float X5 = 50;
float X6 = 50;
float X7 = 50;
float X8 = 50;
float X9 = 50;
float X10 = 50;
float X11 = 50;
float X12 = 50;
float X13 = 50;
float X14 = 50;
float X15 = 50;
float X16 = 50;

float Y1 = 50;
float Y2 = 50;
float Y3 = 50;
float Y4 = 50;
float Y5 = 50;
float Y6 = 50;
float Y7 = 50;
float Y8 = 50;
float Y9 = 50;
float Y10 = 50;
float Y11 = 50;
float Y12 = 50;
float Y13 = 50;
float Y14 = 50;
float Y15 = 50;
float Y16 = 50;

void setup(){
size (500,500);
}

void draw(){
background(0,0,0);


noFill();
strokeWeight(12);
stroke(255,255,255);
rect(50,50,405,405);

strokeWeight(1);
quad1();
quad2();
quad3();
quad4();
quad5();
quad6();
quad7();
quad8();
quad9();
quad10();
quad11();
quad12();
quad13();
quad14();
quad15();

/*
delay(50);
line(50,50,X15,Y15);
line(450,50,X15+25,Y15);
line(50,450,X15,Y15+25);
line(450,450,X15+25,Y15+25);
*/

}
void quad1(){
if (X1<75){
if (Y15 == 50){
X1 = X1 + 1;
} 
}

if (X15 == 426){
if (Y1<76){ //<>//
Y1 = Y1 + 1;
}
}

if (Y15 == 426){
if (X1>50){
X1 = X1 - 1;
}
}

if (X15 == 50){
if (Y1 > 50){
Y1 = Y1 - 1;
}
}

noFill();
stroke(255,255,255);
rect(X1,Y1,375,375);
}

void quad2(){
if (X2<100){
if (Y15 == 50){
X2 = X2 + 1.5;
} 
}

if (X15 == 426){
if (Y2<101){
Y2 = Y2 + 1.5;
}
}

if (Y15 == 426){
if (X2>50){
X2 = X2 - 1.5;
}
}

if (X15 == 50){
if (Y2 > 50){
Y2 = Y2 - 1.5;
}
}

noFill();
stroke(255,255,255);
rect(X2,Y2,350,350);
}

void quad3(){
if (X3<125){
if (Y15 == 50){
X3 = X3 + 2;
}
}

if (X15 == 426){
if (Y3<126){
Y3 = Y3 + 2;
}
}

if (Y15 == 426){
if (X3>50){
X3 = X3 - 2;
}
}

if (X15 == 50){
if (Y3 > 50){
Y3 = Y3 - 2;
}
}

noFill();
stroke(255,255,255);
rect(X3,Y3,325,325);
}


void quad4(){
if (X4<150){
if (Y15 == 50){
X4 = X4 + 2.5;
}
}

if (X15 == 426){
if (Y4<151){
Y4 = Y4 + 2.5;
}
}

if (Y15 == 426){
if (X4>50){
X4 = X4 - 2.5;
}
}

if (X15 == 50){
if (Y4 > 50){
Y4 = Y4 - 2.5;
}
}


noFill();
stroke(255,255,255);
rect(X4,Y4,300,300);
}

void quad5(){
if (X5<175){
if (Y15 == 50){
X5 = X5 + 3;
}
}

if (X15 == 426){
if (Y5<176){
Y5 = Y5 + 3;
}
}

if (Y15 == 426){
if (X5>50){
X5 = X5 - 3;
}
}

if (X15 == 50){
if (Y5 > 50){
Y5 = Y5 - 3;
}
}

noFill();
stroke(255,255,255);
rect(X5,Y5,275,275);
}

void quad6(){
if (X6<200){
if (Y15 == 50){
X6 = X6 + 3.5;
}
}

if (X15 == 426){
if (Y6<201){
Y6 = Y6 + 3.5;
}
}

if (Y15 == 426){
if (X6>50){
X6 = X6 - 3.5;
}
}

if (X15 == 50){
if (Y6 > 50){
Y6 = Y6 - 3.5;
}
}

noFill();
stroke(255,255,255);
rect(X6,Y6,250,250);
}

void quad7(){
if (X7<225){
if (Y15 == 50){
X7 = X7 + 4;
}
}

if (X15 == 426){
if (Y7<226){
Y7 = Y7 + 4;
}
}

if (Y15 == 426){
if (X7>50){
X7 = X7 - 4;
}
}

if (X15 == 50){
if (Y7 > 50){
Y7 = Y7 - 4;
}
}

noFill();
stroke(255,255,255);
rect(X7,Y7,225,225);
}

void quad8(){
if (X8<250){
if (Y15 == 50){
X8 = X8 + 4.5;
}
}

if (X15 == 426){
if (Y8<251){
Y8 = Y8 + 4.5;
}
}

if (Y15 == 426){
if (X8>50){
X8 = X8 - 4.5;
}
}

if (X15 == 50){
if (Y8 > 50){
Y8 = Y8 - 4.5;
}
}

noFill();
stroke(255,255,255);
rect(X8,Y8,200,200);
}

void quad9(){
if (X9<275){
if (Y15 == 50){
X9 = X9 + 5;
}
}

if (X15 == 426){
if (Y9<276){
Y9 = Y9 + 5;
}
}

if (Y15 == 426){
if (X9>50){
X9 = X9 - 5;
}
}

if (X15 == 50){
if (Y9 > 50){
Y9 = Y9 - 5;
}
}

noFill();
stroke(255,255,255);
rect(X9,Y9,175,175);
}

void quad10(){
if (X10<300){
if (Y15 == 50){
X10 = X10 + 5.5;
}
}

if (X15 == 426){
if (Y10<301){
Y10 = Y10 + 5.5;
}
}

if (Y15 == 426){
if (X10>50){
X10 = X10 - 5.5;
}
}

if (X15 == 50){
if (Y10 > 50){
Y10 = Y10 - 5.5;
}
}

noFill();
stroke(255,255,255);
rect(X10,Y10,150,150);
}

void quad11(){
if (X11<325){
if (Y15 == 50){
X11 = X11 + 6;
} 
}

if (X15 == 426){
if (Y11<326){
Y11 = Y11 + 6;
}
}

if (Y15 == 426){
if (X11>50){
X11 = X11 - 6;
}
}

if (X15 == 50){
if (Y11 > 50){
Y11 = Y11 - 6;
}
}

noFill();
stroke(255,255,255);
rect(X11,Y11,125,125);
}

void quad12(){
if (X12<350){
if (Y15 == 50){
X12 = X12 + 6.5;
}
}

if (X15 == 426){
if (Y12<351){
Y12 = Y12 + 6.5;
}
}

if (Y15 == 426){
if (X12>50){
X12 = X12 - 6.5;
}
}

if (X15 == 50){
if (Y12 > 50){
Y12 = Y12 - 6.5;
}
}

noFill();
stroke(255,255,255);
rect(X12,Y12,100,100);
}

void quad13(){
if (X13<375){
if (Y15 == 50){    
X13 = X13 + 7;
} 
}

if (X15 == 426){
if (Y13<376){
Y13 = Y13 + 7;
}
}

if (Y15 == 426){
if (X13>50){
X13 = X13 - 7;
}
}

if (X15 == 50){
if (Y13 > 50){
Y13 = Y13 - 7;
}
}

noFill();
stroke(255,255,255);
rect(X13,Y13,75,75);
}

void quad14(){
if (X14<400){
if (Y15 == 50){
X14 = X14 + 7.5;
} 
}

if (X15 == 426){
if (Y14<401){
Y14 = Y14 + 7.5;
}
}

if (Y15 == 426){
if (X14>50){
X14 = X14 - 7.5;
}
}

if (X15 == 50){
if (Y14 > 50){
Y14 = Y14 - 7.5;
}
}

noFill();
stroke(255,255,255);
rect(X14,Y14,50,50);
}

void quad15(){
if (X15<425){
if (Y15 == 50){
X15 = X15 + 8;
}
}

if (X15 == 426){
if (Y15<425){
Y15 = Y15 + 8;
}
}

if (Y15 == 426){
if (X15>50){
X15 = X15 - 8;
}
}

if (X15 == 50){
if (Y15 > 50){
Y15 = Y15 - 8;
}
}
}
