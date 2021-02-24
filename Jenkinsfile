pipeline {
	agent any
	stages {
		stage('Git Checkout') {
			steps {
				script {
					properties([pipelineTriggers([pollSCM('* * * * *')])])
				}
				git 'https://github.com/udisco/DevopsExperts.git'
			}
		}
		stage('start_web_app') {
			steps {
				script {
					sh 'python web_app.py'
				}
			}
		}
		stage('start rest_app') {
			steps {
				script {
					sh 'python rest_app.py'
				}
			}
		}
		stage('Run Backend Testing') {
			steps {
				script {
					sh 'python backend_testing.py'
				}
			}
		}
		stage('Run Front End Testing') {
			steps {
				script {
					sh 'python frontend_testing.py'
				}
			}
		}
		stage('Run Combined Testing') {
			steps {
				script {
					sh 'python combined_testing.py'
				}
			}
		}
		stage('Run Clean Environment') {
			steps {
				script {
					sh 'python clean_environment.py'
				}
			}
		}
	}
}
