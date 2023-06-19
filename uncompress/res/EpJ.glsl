#extension GL_OES_EGL_image_external : require

precision mediump float;

uniform samplerExternalOES uTexture;
uniform float uBrightness;
uniform float uOpacity;

varying vec2 vTextureCoords;

void main() {
    vec4 textureTemp = texture2D(uTexture, vTextureCoords);
    gl_FragColor = vec4(textureTemp.xyz * uBrightness, textureTemp.w * uOpacity);
}
