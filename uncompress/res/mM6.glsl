uniform mat4 uMVP;
uniform vec2 uTexMultiplier;
uniform vec2 uTexOffset;

attribute vec4 aPosition;
attribute vec2 aTextureCoords;

varying vec2 vTextureCoords;

void main() {
  vTextureCoords = aTextureCoords;
  vTextureCoords.x = vTextureCoords.x * uTexMultiplier.x + uTexOffset.x;
  vTextureCoords.y = vTextureCoords.y * uTexMultiplier.y + uTexOffset.y;
  gl_Position = uMVP * aPosition;
}
