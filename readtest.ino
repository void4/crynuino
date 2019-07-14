#include <SPI.h>
#include <Wire.h>

char imagebuffer[1024];

void setup() {
    Serial.begin(115200);
}

void loop() {
    // May have to set Serial.setTimeout() to higher value
    int read = Serial.readBytes(imagebuffer, 1024);
    Serial.println(read);

}
