uniform mat4 uMVP;
// The multiplier and offset are used to adjust the video for stereo or mono content.
uniform vec2 uTexMultiplier;
uniform vec2 uTexOffset;
// Transformation matrix from the SurfaceTexture for the texture coordinates.
uniform mat4 uTextureMatrix;

attribute vec4 aPosition;
attribute vec2 aTextureCoords;

varying vec2 vTextureCoords;
varying vec2 vClipCoords;

void main() {
  vTextureCoords.x = aTextureCoords.x * uTexMultiplier.x + uTexOffset.x;
  vTextureCoords.y = aTextureCoords.y * uTexMultiplier.y + uTexOffset.y;
  vTextureCoords.x *= uCropRight;
  vTextureCoords = (uTextureMatrix * vec4(vTextureCoords, 0, 1)).xy;
  vec4 position = uMVP * aPosition;
  vClipCoords = position.xy;
  gl_Position = position;
}
