module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('node_modules/grunt/package.json'),
    concat: {
      app: {
        src: ['wavesApp/static/js/app/**/*.js'],
        dest: 'wavesApp/static/static/js/app.js'
      },
      vendor: {
        src: ['wavesApp/static/js/vendor/**/*.js'],
        dest: 'wavesApp/static/static/js/lib.js'
      }
    },
    sass: {
      dev: {
        options: {
          includePaths: ['bower_components/foundation/scss']
        },
        files: {
          'wavesApp/static/css/main.css': 'wavesApp/static/scss/main.scss'
        }
      },
      deploy: {
        options: {
          includePaths: ['bower_components/foundation/scss'],
          outputStyle: 'compressed'
        },
        files: {
          'build/static/css/screen.min.css': 'wavesApp/static/scss/screen.scss'
        }
      }
    },
    watch: {
          options: {livereload: true},
          javascript: {
              files: ['wavesApp/static/js/app/**/*.js'],
              tasks: ['concat']
          },
          sass: {
              files: 'wavesApp/static/scss/**/*.scss',
              tasks: ['sass:dev']
          }
      }

    // Task configuration goes here.

  });

  // Load plugins here.
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-sass');
  grunt.loadNpmTasks('grunt-contrib-less');
  grunt.loadNpmTasks('grunt-contrib-watch');

  // Register tasks here.
  grunt.registerTask('default', []);

};