import processing.video.*;

int width = 1920;
int height = 1080;
float initOpacity = 0;

void setup() {

  size(960, 540);
  fill(0);
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

  if (initOpacity < 50) {
    initOpacity = initOpacity + .25;
  }

  int granularity = 40;
  int blockWidth = width / granularity;
  int blockHeight = height / granularity;
  
  int granularity2 = 80;
  int blockWidth2 = width / granularity2;
  int blockHeight2 = height / granularity2;
  int[][] Matrix = new int[blockWidth][blockHeight];
  int[][] Matrix2 = new int[blockWidth2][blockHeight2];
  noStroke();
  for (int i = 0; i < Matrix.length; i++) {
    for (int j = 0; j < Matrix[i].length; j++ ) {
      int[] rColor = randomColor();
      fill(rColor[0], rColor[1], rColor[2], 50);
      rect(i*blockWidth, j*blockHeight, blockWidth, blockHeight);
    }
  }
  for (int i = 0; i < Matrix2.length; i++) {
    for (int j = 0; j < Matrix2[i].length; j++ ) {
      int[] rColor = randomColor();
      fill(rColor[0], rColor[1], rColor[2], 50);
      rect(j*blockWidth2, i*blockHeight2, blockWidth2, blockHeight2);
    }
  }
  //float size = randy(width);
  //rect(randy(width), randy(height), size, size);
}