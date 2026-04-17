pipeline {
    agent any

    options {
        timeout(time: 20, unit: 'MINUTES')
    }

    environment {
        APLIKACJA = 'Kalkulator'
        WERSJA    = '1.0.0'
    }

    parameters {
        choice(
            name: 'SRODOWISKO',
            choices: ['dev', 'staging', 'prod'],
            description: 'Srodowisko docelowe'
        )
    }

    stages {
        stage('Info') {
            steps {
                echo "${env.APLIKACJA} v${env.WERSJA}"
                echo "Build: ${env.BUILD_NUMBER}"
                echo "Galaz: ${env.GIT_BRANCH}"
                echo "Srodowisko: ${params.SRODOWISKO}"
            }
        }
        stage('Testy') {
            when {
                expression { env.GIT_BRANCH != 'origin/main' }
            }
            steps {
                sh 'python3 test_app.py'
            }
        }
        stage('Analiza jakosci') {
            parallel {
                stage('Sprawdzenie plikow') {
                    steps {
                        sh 'test -f app.py && test -f test_app.py'
                        echo 'Wymagane pliki istnieja.'
                    }
                }
                stage('Skanowanie zaleznosci') {
                    steps {
                        echo 'Skanowanie zaleznosci...'
                        sh 'echo "Brak zewnetrznych zaleznosci — OK"'
                    }
                }
            }
        }
        stage('Wdrozenie DEV') {
            when {
                expression { params.SRODOWISKO == 'dev' }
            }
            steps {
                echo "Wdrazam ${env.APLIKACJA} v${env.WERSJA} na DEV..."
                echo 'Wdrozenie DEV zakonczone.'
            }
        }
        stage('Zatwierdzenie') {
            when {
                expression { params.SRODOWISKO == 'prod' }
            }
            options {
                timeout(time: 5, unit: 'MINUTES')
            }
            steps {
                input message: "Wdrozyc ${env.APLIKACJA} v${env.WERSJA} na PRODUKCJE?",
                      ok: 'Tak, wdrazaj!'
            }
        }
        stage('Wdrozenie PROD') {
            when {
                expression { params.SRODOWISKO == 'prod' }
            }
            steps {
                echo "Wdrazam ${env.APLIKACJA} v${env.WERSJA} na PRODUKCJE!"
                echo 'Wdrozenie PROD zakonczone.'
            }
        }
    }

    post {
        success {
            echo "Build ${env.BUILD_NUMBER}: ${env.APLIKACJA} wdrozony na ${params.SRODOWISKO}."
        }
        failure {
            echo "BLAD w buildzie ${env.BUILD_NUMBER} — sprawdz logi."
        }
        always {
            echo "Pipeline zakonczona (build ${env.BUILD_NUMBER})."
        }
    }
}
