#include "FastLED.h"

// How many leds are in the strip?
#define NUM_LEDS 50
//LED brightness
#define BRIGHTNESS          80
// Data pin that led data will be written out over
#define DATA_PIN 3
#define COLOR_ORDER RGB
#define FRAMES_PER_SECOND  120


// This is an array of leds.  One item for each led in your strip.
CRGB leds[NUM_LEDS];

const uint8_t header[4] = { 0xDE, 0xAD, 0xBE, 0xEF };
uint8_t gHue = 0; // rotating "base color" used by many of the patterns


int led_values[NUM_LEDS*3];
int on_switch = 0;
String message = "";

int delayRainbow = 20;

boolean rainbow_flag = false;
boolean color_flag = false;
boolean bouncing_ball_flag = false;
boolean satisfaction_flag = false;

int bouncing_ball_i = 0;

void resetAllFlags(){
 rainbow_flag = false;
  color_flag = false;
 bouncing_ball_flag = false; 
  satisfaction_flag = false; 

}


void setup() {
  // put your setup code here, to run once:
FastLED.addLeds<WS2811, DATA_PIN, RGB>(leds, NUM_LEDS);
FastLED.setBrightness(BRIGHTNESS);
//FastLED.showColor(CRGB::Black);

// send the 'leds' array out to the actual LED strip
FastLED.show();  
// insert a delay to keep the framerate modest
FastLED.delay(1000/FRAMES_PER_SECOND);

fill_rainbow( leds, NUM_LEDS, gHue, 7);


Serial.begin(9600);
Serial.println("LED Control");
}

void convertLEDCommands(){  
  int index = 0;
  String index_str = "";
  String current_str = "";
  boolean index_found = false;
  
  int header_end = message.indexOf(',',0);
  String header_str = message.substring(0,header_end);
  
  int first_colon = 0;
  int second_colon = 0;
  int third_colon = 0;
  int fourth_colon = 0;
  int fifth_colon = 0;
  
  int next_comma = 0;
  String first_R = "";
  String first_G = "";
  String first_B = "";
  
  String second_R = "";
  String second_G = "";
  String second_B = "";
  
  int i = 0;
  

 while (i < message.length()) {
   
   current_str = message.substring(i,i+1);
 
   if (header_str=="rainbow"){
     resetAllFlags();
     rainbow_flag = true;
   }
   
   else if (header_str=="ball"){
     resetAllFlags();
      for(int n=0; n < NUM_LEDS; n++) { 
      leds[n] = CRGB::Black;
   }
     bouncing_ball_flag = true;
     bouncing_ball_i = 0;
     
   }else if (header_str="satisfy"){
      resetAllFlags();
     satisfaction_flag = true;
   }
	

   if (header_str=="0"){
    Serial.println("got header 0");
    // FastLED's built-in rainbow generator
    fill_rainbow( leds, NUM_LEDS, gHue, 7);
   }
   
   if(current_str=="q"){
          index = i;

   }else{
     
     int second_comma = message.indexOf(',',header_end+1);
  int third_comma = message.indexOf(',',second_comma);
  
  String time_1 = message.substring(second_comma,third_comma);

     first_colon = message.indexOf(':',header_end+1);
     second_colon = message.indexOf(':',first_colon+1);
     next_comma = message.indexOf(',',second_colon);
          
     first_R = message.substring(header_end+1,first_colon);
     first_G = message.substring(first_colon+1,second_colon);
     first_B = message.substring(second_colon+1,next_comma);
     
     index_str = "0";
     
     Serial.print("red value: ");
     Serial.println(first_R );
     Serial.print("blue value: ");
     Serial.println(first_G);
     Serial.print("green value: ");
     Serial.println(first_G);
     Serial.print("time value 1: ");
     Serial.println(time_1);
     
     //led_values[(index_str.toInt())*3] = firstValue.toInt();
     //led_values[(index_str.toInt())*3+1] = secondValue.toInt();
     //led_values[(index_str.toInt())*3+2] = thirdValue.toInt();
     
     int n=0;
     
     int r1 = first_R.toInt();
     int g1 = first_G.toInt();
     int b1 = first_B.toInt();
     
     int r2 = 255;
     int g2 = 0;
     int b2 = 102;

    leds[n].r = r1;
    leds[n].g = g1; 
    leds[n].b = b1;

     i = next_comma;
     index = i;
     i = message.length();
     
        //colorProgression(r1,g1,b1,r2,g2,b2,time_1.toInt());
     
	colorHighlight(r1,g1,b1,r2,g2,b2,time_1.toInt());
     
   }
   
   
        
  }
  
  /*
  Serial.println("led_values:");
  for(int n=0;n<(NUM_LEDS*3);n++){
    Serial.print(led_values[n]);
    Serial.print("-");
  }
  */
}

void colorHighlight(int r1,int g1,int b1,int r2,int g2,int b2,int time){

for(int n=0; n < NUM_LEDS; n++) { 
    leds[n].r = r1;
    leds[n].g = g1; 
    leds[n].b = b1;
   }
    FastLED.show();

for(int n=0; n < NUM_LEDS; n++) { 
    leds[n].r = r2;
    leds[n].g = g2; 
    leds[n].b = b2;
   //leds[n-1].r = r1;
    //leds[n-1].g = g1; 
    //leds[n-1].b = b1;
    FastLED.show();
    delay(time);
   }



}

void randomColorProgression(){
  
  int r1=0;
  int g1 = 0;
  int b1 = 0;
  int time =0;
    while(true){
    
    r1 = random(0, 255);
    g1 = random(0, 255);
    b1 = random(0, 255);
    time = random(10,400);
    
    for(int n=0; n < NUM_LEDS; n++) { 
    leds[n].r = r1;
    leds[n].g = g1; 
    leds[n].b = b1;
    FastLED.show();
    delay(time);
   }
  }
  
}


void colorProgression(int r1,int g1,int b1,int r2,int g2,int b2,int time){
  
  
  
   for(int n=0; n < NUM_LEDS; n++) { 
    leds[n].r = r1;
    leds[n].g = g1; 
    leds[n].b = b1;
    FastLED.show();
    delay(500);
   }
   for(int n=0; n < NUM_LEDS; n++) { 
    leds[n].r = r2;
    leds[n].g = g2; 
    leds[n].b = b2;
    FastLED.show();
    delay(100);
   }
   
   
  while(true){
    
    r1 = random(0, 255);
    g1 = random(0, 255);
    b1 = random(0, 255);
    time = random(10,400);
    
    for(int n=0; n < NUM_LEDS; n++) { 
    leds[n].r = r1;
    leds[n].g = g1; 
    leds[n].b = b1;
    FastLED.show();
    delay(time);
   }
  }
  
  
}


void loop() {
  FastLED.show();

  if(rainbow_flag){
    
  fill_rainbow( leds, NUM_LEDS, gHue, 7);

  EVERY_N_MILLISECONDS(delayRainbow) { 
    if (delayRainbow>20){
      gHue++;
    }
    else{
      gHue--;
    } } // slowly cycle the "base color" through the rainbow

  EVERY_N_SECONDS( 5 ) { delayRainbow = random(1,40); } // change patterns periodically
  }
  
  else if(bouncing_ball_flag){
    
    leds[bouncing_ball_i].b = 200;
    
    FastLED.show();
    
    leds[bouncing_ball_i] = CRGB::Black;
    
    bouncing_ball_i++;
    
    if(bouncing_ball_i>=NUM_LEDS){
     bouncing_ball_i = 0; 
    }
    
    
    delay(100); 
  }
  
  else if(satisfaction_flag){
     resetAllFlags();

      for(int n=0; n < NUM_LEDS; n++) { 
      leds[n] = CRGB::Black;
   }

      FastLED.show();
      delay(5000);
      
      leds[0] = CRGB::Red;

       FastLED.show();
      delay(5000);
      
      leds[1].r = 255;
      leds[1].g = 100;
      leds[1].b = 0;
      FastLED.show();
      delay(1000);
      leds[2].r = 255;
      leds[2].g = 100;
      leds[2].b = 0;

      FastLED.show();
      delay(5000);
      
      leds[3] = CRGB::White;
      FastLED.show();
      delay(1000);
      leds[4] = CRGB::White;

      FastLED.show();
      delay(2000);
      
      for(int n=5; n < 26; n++) { 
      leds[n] = CRGB::Yellow;
      FastLED.show();
      delay(100);
   }

   FastLED.show();
      delay(2000);
   for(int n=26; n < 50; n++) { 
      leds[n] = CRGB::Green;
      FastLED.show();
      delay(100);
   }

  FastLED.show();
      delay(2000);
     satisfaction_flag = true;
  }
  
  if (Serial.available() > 0) {
    //on_switch=Serial.parseInt();
    message = Serial.readString();
    Serial.println(message);
    convertLEDCommands();
    //Serial.println(on_switch);
  }
  
  /*
  if (on_switch==1){
    
    FastLED.showColor(CRGB::Green);
    for(int redLed = 0; redLed < NUM_LEDS; redLed = redLed + 1) 
    {
      // Turn our current led on to white, then show the leds
      leds[redLed] = CRGB::Red;

      // Show the leds (only one of which is set to white, from above)
      FastLED.show();

      // Wait a little bit
      delay(1000);

      // Turn our current led back to black for the next loop around
      leds[redLed] = CRGB::Green;
    }
    
    for (int i=0; i<255; i=i+1){
      FastLED.setBrightness(i);
      delay(100);
    }
    
    delay(1000);
  }
  if (on_switch==0){
    FastLED.showColor(CRGB::Black);
    
  }
  */

  /*
  if(Serial.available()>0){

   // we're going to read led data directly from serial, after we get our header
  uint8_t b = Serial.read(); 
  Serial.println(b);
  bool looksLikeHeader = false;
  if(b == header[0]) { 
      looksLikeHeader = true;
      for(int i=1; looksLikeHeader && (i < sizeof(header)); i++) { 
        b = Serial.read(); 
        Serial.println(b); 
        if(b != header[i]) { 
          // whoops, not a match, this no longer looks like a header.  
          looksLikeHeader = false;
        }
      }
    }

    if(looksLikeHeader) { 
      // hey, we read all the header bytes!  Yay!  Now read the frame data 
        Serial.readBytes((char*)leds, 3*NUM_LEDS);
        Serial.println(String(leds[0]));
               
      }
    
  

  // now show the led data 
  FastLED.show(); 

  }

  // finally, flush out any data in the serial buffer, as it may have been interrupted oddly by writing out led data:
  while(Serial.available() > 0) { Serial.read(); } 

  */
}


