precision highp float;

#ifdef ENABLE_WHITE_NOISE
uniform float uNoiseOffset;
uniform float uNoiseScale;
uniform float uNoiseSeed;

float rand(in vec2 uv) {
 return fract(sin(mod(dot(uv, vec2(12.9898, 78.233)), 3.14159)) * 43758.5453);
}

void applyNoise(in vec2 texCrd) {
  vec4 color = gl_FragColor;
  vec4 noise = vec4(rand(texCrd + uNoiseSeed));
  float maxColor = max(max(color.r, color.g), color.b);
  float amount = uNoiseScale * smoothstep(0.0, 0.1, maxColor);
  amount *= smoothstep(0.0, 0.1, 1.0 - maxColor);
  color += (noise.r - uNoiseOffset) * amount;
  gl_FragColor.rgb = color.rgb;
}
#else
void applyNoise(in vec2 texCrd) {}
#endif
