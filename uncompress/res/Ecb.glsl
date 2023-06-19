precision mediump float;

uniform sampler2D uTexture;
uniform float uBrightness;
uniform float uOpacity;

varying vec2 vTextureCoords;

void main() {
    vec4 texture = texture2D(uTexture, vTextureCoords);
    gl_FragColor = vec4(texture.xyz * uBrightness, texture.a * uOpacity);
}
