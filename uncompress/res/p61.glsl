precision mediump float;
uniform sampler2D u_Texture0;
uniform float u_Grayscale;
uniform float u_Darken;
varying vec2 v_TextureCoord;

void main() {
  vec3 color = texture2D(u_Texture0, v_TextureCoord).rgb;
  // Converting to grayscale using the BT.601 standard for determining luminance.
  // Then reducing the contrast.
  vec3 gray = vec3(0.2 + 0.5 * dot(color, vec3(0.299, 0.587, 0.114)));
  // Take either the color or gray vec (u_Grayscale is treated as boolean).
  vec3 mixed = mix(color, gray, u_Grayscale);
  // Darken the result by a slope and offset specified by u_Darken (1.0 for completely darkened).
  mixed = (mixed - 0.4 * u_Darken) * (1.0 - u_Darken);
  gl_FragColor = vec4(pow(mixed, vec3(0.8)), 1);
}
