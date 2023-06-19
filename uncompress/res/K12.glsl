const mat4 cLeftColorTransform = mat4(
  0.456, -0.04,  -0.015, 0.0,
  0.5,   -0.038, -0.021, 0.0,
  0.176, -0.016, -0.005, 0.0,
  0.0,    0.0,    0.0,   1.0
);
const mat4 cRightColorTransform = mat4(
 -0.043, 0.378, -0.072, 0.0,
 -0.088, 0.734, -0.113, 0.0,
  0.0,  -0.018,  1.226, 0.0,
  0.0,   0.0,    0.0,   1.0
);

varying vec2 vTexCrd;
varying float vMidpoint;

void anaglyph(float x, float y) {
  x *= vMidpoint;
  vec4 leftColor = getColor(vec2(x, y));
  vec4 rightColor = getColor(vec2(vMidpoint + x, y));
  gl_FragColor = cLeftColorTransform * leftColor + cRightColorTransform * rightColor;
}

void main() {
  anaglyph(vTexCrd.x, vTexCrd.y);
  applyNoise(vTexCrd);
}
