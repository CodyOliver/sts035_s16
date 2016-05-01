#include "FastLED.h"

// How many leds are in the strip?
#define NUM_LEDS 50

// Data pin that led data will be written out over
#define DATA_PIN 3

// This is an array of leds.  One item for each led in your strip.
CRGB leds[NUM_LEDS];

const uint8_t header[4] = { 0xDE, 0xAD, 0xBE, 0xEF };


int led_values[NUM_LEDS*3];
int on_switch = 0;
String message = "";

void setup() {
  // put your setup code here, to run once:
FastLED.addLeds<WS2811, DATA_PIN, RGB>(leds, NUM_LEDS);
Serial.begin(9600);
FastLED.showColor(CRGB::Black);
Serial.println("LED Control");
}
/*
void convertLEDCommands(){  
  int index = 0;
  String index_str = "";
  String current_str = "";
  boolean index_found = false;
  
  int first_colon = 0;
  int second_colon = 0;
  int third_colon = 0;
  
  int next_comma = 0;
  String firstValue = "";
  String secondValue = "";
  String thirdValue = "";
  
  int i = 0;

 while (i < message.length()) {
   
   current_str = message.substring(i,i+1);
   
   if(current_str=='q'){
          index = i;

   }else{

     first_colon = message.indexOf(':',index+1);
     second_colon = message.indexOf(':',first_colon+1);
     third_colon = message.indexOf(':',second_colon+1);
     next_comma = message.indexOf(',',third_colon);
          
     index_str = message.substring(index+1,first_colon);
     firstValue = message.substring(first_colon+1,second_colon);
     secondValue = message.substring(second_colon+1,third_colon);
     thirdValue = message.substring(third_colon+1,next_comma);
     
     Serial.print("index:");
     Serial.println(index_str);
     
     Serial.print("red value: ");
     Serial.println(firstValue);
     Serial.print("blue value: ");
     Serial.println(secondValue);
     Serial.print("green value: ");
     Serial.println(thirdValue);
     
     led_values[(index_str.toInt())*3] = firstValue.toInt();
     led_values[(index_str.toInt())*3+1] = secondValue.toInt();
     led_values[(index_str.toInt())*3+2] = thirdValue.toInt();

     i = next_comma;
     index = i;
   }
   
   
   //Serial.println(message[i]);
      
  }
  
  
  Serial.println("led_values:");
  for(int n=0;n<(NUM_LEDS*3);n++){
    Serial.print(led_values[n]);
    Serial.print("-");
  }
}
*/
void loop() {
  
  
  /*

  if (Serial.available() > 0) {
    //on_switch=Serial.parseInt();
    Serial.setTimeout(5000);
    message = Serial.readString();
    Serial.println(message);
    convertLEDCommands();
    //Serial.println(on_switch);
  }
  */
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

  
}


