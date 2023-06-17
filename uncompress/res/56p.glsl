uniform mat4 uMVP;

attribute vec4 aPosition;
attribute vec4 aColor;

varying vec4 vColor;

void main() {
  vColor = aColor;
  gl_Position = uMVP * aPosition;
}
