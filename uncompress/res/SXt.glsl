varying vec2 vTexCrd;

void main() {
  gl_FragColor = getColor(vTexCrd);
  applyNoise(vTexCrd);
}
