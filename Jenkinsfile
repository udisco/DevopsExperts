pipeline {
	agent any
	options {
        disableConcurrentBuilds()
        buildDiscarder logRotator(daysToKeepStr: '5', numToKeepStr: '20')
          }
	stages {
		stage('Git Checkout') {
			steps {
				script {
					properties([pipelineTriggers([pollSCM('* * * * *')])])
				}
				git 'https://github.com/udisco/DevopsExperts.git'
			}
		}
		stage('install dependencies') {
   			steps {
      				script {
            				sh 'pip3 install Flask flask pymysql requests -t ./'
				}
			}
		}
		stage('start_frontend_server') {
			steps {
				script {
					sh 'nohup python3 web_app.py &'
				}
			}
		}
		stage('start backend_server') {
			steps {
				script {
					sh 'nohup python3 rest_app.py &'
				}
			}
		}
		stage('Run Backend Testing') {
			steps {
				script {
					sh 'python3 backend_tesing.py'
				}
			}
		}
		stage('Run Front End Testing') {
			steps {
				script {
					sh 'python3 frontend_testing.py'
				}
			}
		}
		stage('Run Combined Testing') {
			steps {
				script {
					sh 'python3 combined_testing.py'
				}
			}
		}
		stage('Run Clean Environment') {
			steps {
				script {
					sh 'python3 clean_environment.py'
				}
			}
		}
	}
}
