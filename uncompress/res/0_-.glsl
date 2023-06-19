uniform mat4 uMVP;

attribute vec4 aPosition;
attribute vec2 aTextureCoords;

varying vec2 vTextureCoords;

void main() {
   vTextureCoords = aTextureCoords;
   gl_Position = uMVP * aPosition;
}
