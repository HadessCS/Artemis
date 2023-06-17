precision mediump float;

uniform float uOpacity;

varying vec4 vColor;

void main() {
   gl_FragColor = vec4(vColor.xyz, vColor.a * uOpacity);
}
