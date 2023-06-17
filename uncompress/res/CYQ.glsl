#line 101
#ifndef ENABLE_YUV
#extension GL_OES_EGL_image_external : require

// Note: lowp is required here for certain Adreno 3XX devices running SDK 17 and 18, otherwise
// shader compilation will fail.
uniform lowp samplerExternalOES uTexture;
#endif

precision highp float;

uniform mat3 uColorPrimaryTransform;
uniform vec3 uLuminanceTransform;
uniform sampler2D uInputLut;
uniform sampler2D uOutputLut;
uniform sampler2D uKneeLut;
uniform float uLutSize;

void applyHdrTonemap(inout vec3 rgb) {
  rgb = clamp(rgb, 0.0, 1.0);
  // The input lut converts the color to linear RGB.
  // Reduce the range by 1 pixel so we can look up centre to centre.
  rgb *= (uLutSize - 1.0) / uLutSize;
  // We add half pixel to the lookups so the RGB range rests in the centre of
  // the pixels at the edge.
  float halfPixel = 0.5 / uLutSize;
  rgb += halfPixel;

  vec2 lookup;
  lookup = texture2D(uInputLut, vec2(0.5, rgb.r)).ra;
  rgb.r = lookup.x + lookup.y / 255.0;
  lookup = texture2D(uInputLut, vec2(0.5, rgb.g)).ra;
  rgb.g = lookup.x + lookup.y / 255.0;
  lookup = texture2D(uInputLut, vec2(0.5, rgb.b)).ra;
  rgb.b = lookup.x + lookup.y / 255.0;


  // Apply Knee Curve.
  float luminance = max(0.0, dot(rgb, uLuminanceTransform)) + halfPixel;
  lookup = texture2D(uKneeLut, vec2(0.5, luminance)).ra;
  float scale = (lookup.x + lookup.y / 255.0) / luminance;
  rgb *= scale;
  // Convert to output color primaries.
  rgb = uColorPrimaryTransform * rgb + halfPixel;

  // Apply output scale and gamma.
  lookup = texture2D(uOutputLut, vec2(0.5, rgb.r)).ra;
  rgb.r = lookup.x + lookup.y / 255.0;
  lookup = texture2D(uOutputLut, vec2(0.5, rgb.g)).ra;
  rgb.g = lookup.x + lookup.y / 255.0;
  lookup = texture2D(uOutputLut, vec2(0.5, rgb.b)).ra;
  rgb.b = lookup.x + lookup.y / 255.0;
}

#ifdef ENABLE_YUV
uniform sampler2D uTextureY;
uniform sampler2D uTextureU;
uniform sampler2D uTextureV;
uniform mat3 uColorConversion;

vec4 getColor(in vec2 texCrd) {
  vec3 yuv;
  yuv.x = texture2D(uTextureY, texCrd).r - 0.0625;
  yuv.y = texture2D(uTextureU, texCrd).r - 0.5;
  yuv.z = texture2D(uTextureV, texCrd).r - 0.5;
  vec3 rgb = uColorConversion * yuv;
  if (uLutSize > 0.0)
  {
    applyHdrTonemap(rgb);
  }
  return vec4(rgb, 1.0);
}
#else

vec4 getColor(in vec2 texCrd) {
  vec4 rgbColor = texture2D(uTexture, texCrd);
  if (uLutSize > 0.0)
  {
    applyHdrTonemap(rgbColor.rgb);
  }
  return rgbColor;
}
#endif
