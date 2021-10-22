module.exports = {
  future: {
    removeDeprecatedGapUtilities: true,
    purgeLayersByDefault: true,
  },
  purge: {
    enabled: false, //true for production build
    content: [
      '../**/templates/*.html',
      '../**/templates/**/*.html'
    ]
  },
  theme: {
    extend: {
      colors: {
        "veryblue": "#1DE5E2",
        "verypink": "#B588F7",
        "veryyellow": "#fed330",
      }
    },
    fontFamily: {
      raleway: ['Raleway', 'sans-serif'],
      lora: ['Lora', 'serif'],
      play: ['Play', 'sans-serif']
    },
    container: {
      center: true,
      padding: '1rem',
      screens: {
        lg: '1124px',
        xl: "1124px",
        "2xl": '1124px'
      },
    },
  },
  variants: {},
  plugins: [],
}