uniform float uBrightness;
uniform float uOpacity;

varying vec2 vTextureCoords;
varying vec2 vClipCoords;

void main() {
    vec4 textureTemp = getColor(vTextureCoords);
    gl_FragColor = vec4(textureTemp.xyz * uBrightness, textureTemp.w * uOpacity);
    applyNoise(vClipCoords);
}
