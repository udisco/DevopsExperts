pipeline {
  agent any
  stages {
    stage ('Git Checkout') {
        steps {
            script {
            properties([pipelineTriggers([pollSCM('H/30 * * * *')])])
            }
            git 'https://github.com/udisco/DevopsExperts.git'
        }
    }
    stage('start_web_app') {
        steps {
            sh 'python web_app.py'
          }
        }

    stage('start rest_app') {
        steps {
            sh 'python rest_app.py'
          }
        }

    stage('Run Backend Testing') {
        steps {
            sh 'python backend_testing.py'
          }
        }

    stage('Run Front End Testing') {
        steps {
            sh 'python frontend_testing.py'
          }
        }
    stage('Run Combined Testing') {
        steps {
            sh 'python combined_testing.py'
          }
        }
    stage('Run Clean Environment') {
        steps {
            sh 'python clean_environment.py'
          }
        }
      }
    }
}