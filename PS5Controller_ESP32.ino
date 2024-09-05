#include <ps5Controller.h>
#include <ArduinoJson.h>

int CLOCK_VAL = 200;                       // refresh rate

void setup() {
  Serial.begin(115200);
  ps5.begin("4C:B9:9B:54:00:CB");           // ps5 controler bluetooth ID thing
  Serial.println("Ready.");
}

void loop() {

  while (ps5.isConnected() == true) {

    JsonDocument controller_data;

    controller_data["Right"] = ps5.Right();
    controller_data["Down"] = ps5.Down();
    controller_data["Up"] = ps5.Up();
    controller_data["Left"] = ps5.Left();

    controller_data["Square"] = ps5.Square(); 
    controller_data["Cross"] = ps5.Cross();
    controller_data["Circle"] = ps5.Circle();
    controller_data["Triangle"] = ps5.Triangle();

    // controller_data["UpRight"] = ps5.UpRight();
    // controller_data["DownRight"] = ps5.DownRight();
    // controller_data["UpLeft"] = ps5.UpLeft();
    // controller_data["DownLeft"] = ps5.DownLeft();

    controller_data["L1"] = ps5.L1();
    controller_data["R1"] = ps5.R1();
    controller_data["L3"] = ps5.L3();
    controller_data["R3"] = ps5.R3();

    controller_data["ShareButton"] = ps5.Share();
    controller_data["OptionsButton"] = ps5.Options();

    controller_data["PSButton"] = ps5.PSButton();
    controller_data["TouchPad"] = ps5.Touchpad();

    if (ps5.L2()) {
      controller_data["L2"] = ps5.L2Value();
    }
    else {
      controller_data["L2"] = 0;
    }

    if (ps5.R2()) {
      controller_data["R2"] = ps5.R2Value();
    }
    else {
      controller_data["R2"] = 0;
    }

    if (ps5.LStickX()) {
      controller_data["LStickPos"][0] = ps5.LStickX();
    }
    else {
      controller_data["LStickPos"][0] = 0;
    }

    if (ps5.LStickY()) {
      controller_data["LStickPos"][1] = ps5.LStickY();
    }
    else {
      controller_data["LStickPos"][1] = 0;
    }

    if (ps5.RStickX()) {
      controller_data["RStickPos"][0] = ps5.RStickX();
    }
    else {
      controller_data["RStickPos"][0] = 0;
    }

    if (ps5.RStickY()) {
      controller_data["RStickPos"][1] = ps5.RStickY();
    }
    else {
      controller_data["RStickPos"][1] = 0;
    }

    serializeJson(controller_data, Serial);
    Serial.println();
    delay(CLOCK_VAL);
  }

  // while(!ps5.isConnected()) {
  //   Serial.println("Controller not detected..");
  //   delay(CLOCK_VAL);
  // }
}