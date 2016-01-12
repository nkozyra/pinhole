import processing.video.*;

int width = 960;
int height = 540;
float initOpacity = 0;

void setup() {
  size(960, 540);
  fill(155);
  rect(0, 0, 960, 540);
}

float randy(int num) {
  return random(num);
}

int[] randomColor() {
  int[] colora = new int[3];
  int max = (int) random(initOpacity);
  colora[0] = (int) random(max);
  colora[1] = (int) random(max);
  colora[2] = (int) random(max);
  return colora;
}


void draw() {

  if (initOpacity < 90) {
    initOpacity = initOpacity + .35;
  }

  int granularity = 50;
  float blockWidth = (float) width / granularity ;
  float blockHeight = (float) height / granularity ;
  
  int granularity2 = 100;
  float blockWidth2 = (float) width / granularity2;
  float blockHeight2 = (float) height / granularity2;
  int[][] Matrix = new int[granularity][granularity];
  int[][] Matrix2 = new int[granularity2][granularity2];
  noStroke();
  for (int i = 0; i < granularity; i++) {
    for (int j = 0; j < granularity; j++ ) {
      int[] rColor = randomColor();
      fill(rColor[0], rColor[1], rColor[2], 50);
      rect(j*blockWidth, i*blockHeight, blockWidth, blockHeight);
    }
  }

  for (int i = 0; i < granularity2; i++) {
    for (int j = 0; j < granularity2; j++ ) {
      int[] rColor = randomColor();
      fill(rColor[0], rColor[1], rColor[2], 50);
      rect(j*blockWidth2, i*blockHeight2, blockWidth2, blockHeight2);
    }
  }
  //float size = randy(width);
  //rect(randy(width), randy(height), size, size);
}