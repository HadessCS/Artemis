attribute vec4 aVertPos;

varying vec2 vTexCrd;

void main() {
  gl_Position = aVertPos;
  vTexCrd = vec2(aVertPos.x + 1.0, 1.0 - aVertPos.y) * 0.5;
  vTexCrd.x *= uCropRight;
}
